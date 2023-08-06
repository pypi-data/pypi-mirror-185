"""
Implement pd.Series typing and data model handling.
"""
import operator
import llvmlite.binding as ll
import numba
import numpy as np
import pandas as pd
from llvmlite import ir as lir
from numba.core import cgutils, types
from numba.core.imputils import impl_ret_borrowed, lower_constant
from numba.core.typing.templates import bound_function, signature
from numba.extending import infer_getattr, intrinsic, lower_builtin, lower_cast, models, overload, overload_attribute, overload_method, register_model
from numba.parfors.array_analysis import ArrayAnalysis
import bodo
from bodo.hiframes.datetime_date_ext import datetime_date_type
from bodo.hiframes.datetime_timedelta_ext import pd_timedelta_type
from bodo.hiframes.pd_timestamp_ext import pd_timestamp_tz_naive_type
from bodo.io import csv_cpp
from bodo.libs.float_arr_ext import FloatDtype
from bodo.libs.int_arr_ext import IntDtype
from bodo.libs.pd_datetime_arr_ext import PandasDatetimeTZDtype
from bodo.libs.str_ext import string_type, unicode_to_utf8
from bodo.utils.templates import OverloadedKeyAttributeTemplate
from bodo.utils.transform import get_const_func_output_type
from bodo.utils.typing import BodoError, check_unsupported_args, create_unsupported_overload, dtype_to_array_type, get_overload_const_str, get_overload_const_tuple, get_udf_error_msg, get_udf_out_arr_type, is_heterogeneous_tuple_type, is_overload_constant_str, is_overload_constant_tuple, is_overload_false, is_overload_int, is_overload_none, raise_bodo_error, to_nullable_type
_csv_output_is_dir = types.ExternalFunction('csv_output_is_dir', types.int8
    (types.voidptr))
ll.add_symbol('csv_output_is_dir', csv_cpp.csv_output_is_dir)


class SeriesType(types.IterableType, types.ArrayCompatible):
    ndim = 1

    def __init__(self, dtype, data=None, index=None, name_typ=None, dist=None):
        from bodo.hiframes.pd_index_ext import RangeIndexType
        from bodo.transforms.distributed_analysis import Distribution
        data = dtype_to_array_type(dtype) if data is None else data
        dtype = dtype.dtype if isinstance(dtype, IntDtype) else dtype
        dtype = dtype.dtype if isinstance(dtype, FloatDtype) else dtype
        self.dtype = dtype
        self.data = data
        name_typ = types.none if name_typ is None else name_typ
        index = RangeIndexType(types.none) if index is None else index
        self.index = index
        self.name_typ = name_typ
        dist = Distribution.OneD_Var if dist is None else dist
        self.dist = dist
        super(SeriesType, self).__init__(name=
            f'series({dtype}, {data}, {index}, {name_typ}, {dist})')

    @property
    def as_array(self):
        return types.Array(types.undefined, 1, 'C')

    def copy(self, dtype=None, index=None, dist=None):
        if index is None:
            index = self.index
        if dist is None:
            dist = self.dist
        if dtype is None:
            dtype = self.dtype
            data = self.data
        else:
            data = dtype_to_array_type(dtype)
        return SeriesType(dtype, data, index, self.name_typ, dist)

    @property
    def key(self):
        return self.dtype, self.data, self.index, self.name_typ, self.dist

    def unify(self, typingctx, other):
        from bodo.transforms.distributed_analysis import Distribution
        if isinstance(other, SeriesType):
            pucjr__enq = (self.index if self.index == other.index else self
                .index.unify(typingctx, other.index))
            dist = Distribution(min(self.dist.value, other.dist.value))
            if other.dtype == self.dtype or not other.dtype.is_precise():
                return SeriesType(self.dtype, self.data.unify(typingctx,
                    other.data), pucjr__enq, dist=dist)
        return super(SeriesType, self).unify(typingctx, other)

    def can_convert_to(self, typingctx, other):
        from numba.core.typeconv import Conversion
        if (isinstance(other, SeriesType) and self.dtype == other.dtype and
            self.data == other.data and self.index == other.index and self.
            name_typ == other.name_typ and self.dist != other.dist):
            return Conversion.safe

    def is_precise(self):
        return self.dtype.is_precise()

    @property
    def iterator_type(self):
        return self.data.iterator_type

    @property
    def mangling_args(self):
        return self.__class__.__name__, (self._code,)


class HeterogeneousSeriesType(types.Type):
    ndim = 1

    def __init__(self, data=None, index=None, name_typ=None):
        from bodo.hiframes.pd_index_ext import RangeIndexType
        from bodo.transforms.distributed_analysis import Distribution
        self.data = data
        name_typ = types.none if name_typ is None else name_typ
        index = RangeIndexType(types.none) if index is None else index
        self.index = index
        self.name_typ = name_typ
        self.dist = Distribution.REP
        super(HeterogeneousSeriesType, self).__init__(name=
            f'heter_series({data}, {index}, {name_typ})')

    def copy(self, index=None, dist=None):
        from bodo.transforms.distributed_analysis import Distribution
        assert dist == Distribution.REP, 'invalid distribution for HeterogeneousSeriesType'
        if index is None:
            index = self.index.copy()
        return HeterogeneousSeriesType(self.data, index, self.name_typ)

    @property
    def key(self):
        return self.data, self.index, self.name_typ

    @property
    def mangling_args(self):
        return self.__class__.__name__, (self._code,)


@lower_builtin('getiter', SeriesType)
def series_getiter(context, builder, sig, args):
    lsueu__bkyj = get_series_payload(context, builder, sig.args[0], args[0])
    impl = context.get_function('getiter', sig.return_type(sig.args[0].data))
    return impl(builder, (lsueu__bkyj.data,))


@infer_getattr
class HeterSeriesAttribute(OverloadedKeyAttributeTemplate):
    key = HeterogeneousSeriesType

    def generic_resolve(self, S, attr):
        from bodo.hiframes.pd_index_ext import HeterogeneousIndexType
        if self._is_existing_attr(attr):
            return
        if isinstance(S.index, HeterogeneousIndexType
            ) and is_overload_constant_tuple(S.index.data):
            wjzb__qzbxe = get_overload_const_tuple(S.index.data)
            if attr in wjzb__qzbxe:
                fvikz__afn = wjzb__qzbxe.index(attr)
                return S.data[fvikz__afn]


def is_str_series_typ(t):
    return isinstance(t, SeriesType) and t.dtype == string_type


def is_dt64_series_typ(t):
    return isinstance(t, SeriesType) and (t.dtype == types.NPDatetime('ns') or
        isinstance(t.dtype, PandasDatetimeTZDtype))


def is_timedelta64_series_typ(t):
    return isinstance(t, SeriesType) and t.dtype == types.NPTimedelta('ns')


def is_datetime_date_series_typ(t):
    return isinstance(t, SeriesType) and t.dtype == datetime_date_type


class SeriesPayloadType(types.Type):

    def __init__(self, series_type):
        self.series_type = series_type
        super(SeriesPayloadType, self).__init__(name=
            f'SeriesPayloadType({series_type})')

    @property
    def mangling_args(self):
        return self.__class__.__name__, (self._code,)


@register_model(SeriesPayloadType)
class SeriesPayloadModel(models.StructModel):

    def __init__(self, dmm, fe_type):
        gtkiv__ifnk = [('data', fe_type.series_type.data), ('index',
            fe_type.series_type.index), ('name', fe_type.series_type.name_typ)]
        super(SeriesPayloadModel, self).__init__(dmm, fe_type, gtkiv__ifnk)


@register_model(HeterogeneousSeriesType)
@register_model(SeriesType)
class SeriesModel(models.StructModel):

    def __init__(self, dmm, fe_type):
        payload_type = SeriesPayloadType(fe_type)
        gtkiv__ifnk = [('meminfo', types.MemInfoPointer(payload_type)), (
            'parent', types.pyobject)]
        super(SeriesModel, self).__init__(dmm, fe_type, gtkiv__ifnk)


def define_series_dtor(context, builder, series_type, payload_type):
    lee__csfb = builder.module
    ftm__sovub = lir.FunctionType(lir.VoidType(), [cgutils.voidptr_t])
    ivp__tmz = cgutils.get_or_insert_function(lee__csfb, ftm__sovub, name=
        '.dtor.series.{}'.format(series_type))
    if not ivp__tmz.is_declaration:
        return ivp__tmz
    ivp__tmz.linkage = 'linkonce_odr'
    builder = lir.IRBuilder(ivp__tmz.append_basic_block())
    jeczl__opu = ivp__tmz.args[0]
    drn__ipv = context.get_value_type(payload_type).as_pointer()
    ewgsl__ktd = builder.bitcast(jeczl__opu, drn__ipv)
    uetk__ahdmi = context.make_helper(builder, payload_type, ref=ewgsl__ktd)
    context.nrt.decref(builder, series_type.data, uetk__ahdmi.data)
    context.nrt.decref(builder, series_type.index, uetk__ahdmi.index)
    context.nrt.decref(builder, series_type.name_typ, uetk__ahdmi.name)
    builder.ret_void()
    return ivp__tmz


def construct_series(context, builder, series_type, data_val, index_val,
    name_val):
    payload_type = SeriesPayloadType(series_type)
    lsueu__bkyj = cgutils.create_struct_proxy(payload_type)(context, builder)
    lsueu__bkyj.data = data_val
    lsueu__bkyj.index = index_val
    lsueu__bkyj.name = name_val
    yain__key = context.get_value_type(payload_type)
    pdz__nkopf = context.get_abi_sizeof(yain__key)
    vuw__key = define_series_dtor(context, builder, series_type, payload_type)
    pjds__ddv = context.nrt.meminfo_alloc_dtor(builder, context.
        get_constant(types.uintp, pdz__nkopf), vuw__key)
    wsmf__bdtm = context.nrt.meminfo_data(builder, pjds__ddv)
    rrs__mlh = builder.bitcast(wsmf__bdtm, yain__key.as_pointer())
    builder.store(lsueu__bkyj._getvalue(), rrs__mlh)
    series = cgutils.create_struct_proxy(series_type)(context, builder)
    series.meminfo = pjds__ddv
    series.parent = cgutils.get_null_value(series.parent.type)
    return series._getvalue()


@intrinsic
def init_series(typingctx, data, index, name=None):
    from bodo.hiframes.pd_index_ext import is_pd_index_type
    from bodo.hiframes.pd_multi_index_ext import MultiIndexType
    assert is_pd_index_type(index) or isinstance(index, MultiIndexType)
    name = types.none if name is None else name

    def codegen(context, builder, signature, args):
        data_val, index_val, name_val = args
        series_type = signature.return_type
        edo__ruj = construct_series(context, builder, series_type, data_val,
            index_val, name_val)
        context.nrt.incref(builder, signature.args[0], data_val)
        context.nrt.incref(builder, signature.args[1], index_val)
        context.nrt.incref(builder, signature.args[2], name_val)
        return edo__ruj
    if is_heterogeneous_tuple_type(data):
        ldt__mfm = HeterogeneousSeriesType(data, index, name)
    else:
        dtype = data.dtype
        data = if_series_to_array_type(data)
        ldt__mfm = SeriesType(dtype, data, index, name)
    sig = signature(ldt__mfm, data, index, name)
    return sig, codegen


def init_series_equiv(self, scope, equiv_set, loc, args, kws):
    from bodo.hiframes.pd_index_ext import HeterogeneousIndexType
    assert len(args) >= 2 and not kws
    data = args[0]
    index = args[1]
    eus__hrb = self.typemap[data.name]
    if is_heterogeneous_tuple_type(eus__hrb) or isinstance(eus__hrb, types.
        BaseTuple):
        return None
    mudwn__vdv = self.typemap[index.name]
    if not isinstance(mudwn__vdv, HeterogeneousIndexType
        ) and equiv_set.has_shape(data) and equiv_set.has_shape(index):
        equiv_set.insert_equiv(data, index)
    if equiv_set.has_shape(data):
        return ArrayAnalysis.AnalyzeResult(shape=data, pre=[])
    return None


ArrayAnalysis._analyze_op_call_bodo_hiframes_pd_series_ext_init_series = (
    init_series_equiv)


def get_series_payload(context, builder, series_type, value):
    pjds__ddv = cgutils.create_struct_proxy(series_type)(context, builder,
        value).meminfo
    payload_type = SeriesPayloadType(series_type)
    uetk__ahdmi = context.nrt.meminfo_data(builder, pjds__ddv)
    drn__ipv = context.get_value_type(payload_type).as_pointer()
    uetk__ahdmi = builder.bitcast(uetk__ahdmi, drn__ipv)
    return context.make_helper(builder, payload_type, ref=uetk__ahdmi)


@intrinsic
def get_series_data(typingctx, series_typ=None):

    def codegen(context, builder, signature, args):
        lsueu__bkyj = get_series_payload(context, builder, signature.args[0
            ], args[0])
        return impl_ret_borrowed(context, builder, series_typ.data,
            lsueu__bkyj.data)
    ldt__mfm = series_typ.data
    sig = signature(ldt__mfm, series_typ)
    return sig, codegen


@intrinsic
def get_series_index(typingctx, series_typ=None):

    def codegen(context, builder, signature, args):
        lsueu__bkyj = get_series_payload(context, builder, signature.args[0
            ], args[0])
        return impl_ret_borrowed(context, builder, series_typ.index,
            lsueu__bkyj.index)
    ldt__mfm = series_typ.index
    sig = signature(ldt__mfm, series_typ)
    return sig, codegen


@intrinsic
def get_series_name(typingctx, series_typ=None):

    def codegen(context, builder, signature, args):
        lsueu__bkyj = get_series_payload(context, builder, signature.args[0
            ], args[0])
        return impl_ret_borrowed(context, builder, signature.return_type,
            lsueu__bkyj.name)
    sig = signature(series_typ.name_typ, series_typ)
    return sig, codegen


def get_series_data_equiv(self, scope, equiv_set, loc, args, kws):
    assert len(args) == 1 and not kws
    jmjzz__nhc = args[0]
    eus__hrb = self.typemap[jmjzz__nhc.name].data
    if is_heterogeneous_tuple_type(eus__hrb) or isinstance(eus__hrb, types.
        BaseTuple):
        return None
    if equiv_set.has_shape(jmjzz__nhc):
        return ArrayAnalysis.AnalyzeResult(shape=jmjzz__nhc, pre=[])
    return None


(ArrayAnalysis._analyze_op_call_bodo_hiframes_pd_series_ext_get_series_data
    ) = get_series_data_equiv


def get_series_index_equiv(self, scope, equiv_set, loc, args, kws):
    from bodo.hiframes.pd_index_ext import HeterogeneousIndexType
    assert len(args) == 1 and not kws
    jmjzz__nhc = args[0]
    mudwn__vdv = self.typemap[jmjzz__nhc.name].index
    if isinstance(mudwn__vdv, HeterogeneousIndexType):
        return None
    if equiv_set.has_shape(jmjzz__nhc):
        return ArrayAnalysis.AnalyzeResult(shape=jmjzz__nhc, pre=[])
    return None


(ArrayAnalysis._analyze_op_call_bodo_hiframes_pd_series_ext_get_series_index
    ) = get_series_index_equiv


def alias_ext_init_series(lhs_name, args, alias_map, arg_aliases):
    assert len(args) >= 1
    numba.core.ir_utils._add_alias(lhs_name, args[0].name, alias_map,
        arg_aliases)
    if len(args) > 1:
        numba.core.ir_utils._add_alias(lhs_name, args[1].name, alias_map,
            arg_aliases)


numba.core.ir_utils.alias_func_extensions['init_series',
    'bodo.hiframes.pd_series_ext'] = alias_ext_init_series


def alias_ext_dummy_func(lhs_name, args, alias_map, arg_aliases):
    assert len(args) >= 1
    numba.core.ir_utils._add_alias(lhs_name, args[0].name, alias_map,
        arg_aliases)


numba.core.ir_utils.alias_func_extensions['get_series_data',
    'bodo.hiframes.pd_series_ext'] = alias_ext_dummy_func
numba.core.ir_utils.alias_func_extensions['get_series_index',
    'bodo.hiframes.pd_series_ext'] = alias_ext_dummy_func


def is_series_type(typ):
    return isinstance(typ, SeriesType)


def if_series_to_array_type(typ):
    if isinstance(typ, SeriesType):
        return typ.data
    return typ


@lower_cast(SeriesType, SeriesType)
def cast_series(context, builder, fromty, toty, val):
    if fromty.copy(index=toty.index) == toty and isinstance(fromty.index,
        bodo.hiframes.pd_index_ext.RangeIndexType) and isinstance(toty.
        index, bodo.hiframes.pd_index_ext.NumericIndexType):
        lsueu__bkyj = get_series_payload(context, builder, fromty, val)
        pucjr__enq = context.cast(builder, lsueu__bkyj.index, fromty.index,
            toty.index)
        context.nrt.incref(builder, fromty.data, lsueu__bkyj.data)
        context.nrt.incref(builder, fromty.name_typ, lsueu__bkyj.name)
        return construct_series(context, builder, toty, lsueu__bkyj.data,
            pucjr__enq, lsueu__bkyj.name)
    if (fromty.dtype == toty.dtype and fromty.data == toty.data and fromty.
        index == toty.index and fromty.name_typ == toty.name_typ and fromty
        .dist != toty.dist):
        return val
    return val


@infer_getattr
class SeriesAttribute(OverloadedKeyAttributeTemplate):
    key = SeriesType

    @bound_function('series.head')
    def resolve_head(self, ary, args, kws):
        ynrmx__pxg = 'Series.head'
        dyzo__rpw = 'n',
        evzyv__wfyi = {'n': 5}
        pysig, avvt__zjr = bodo.utils.typing.fold_typing_args(ynrmx__pxg,
            args, kws, dyzo__rpw, evzyv__wfyi)
        akncg__tgedo = avvt__zjr[0]
        if not is_overload_int(akncg__tgedo):
            raise BodoError(f"{ynrmx__pxg}(): 'n' must be an Integer")
        jxwio__gjs = ary
        return jxwio__gjs(*avvt__zjr).replace(pysig=pysig)

    def _resolve_map_func(self, ary, func, pysig, fname, f_args=None, kws=None
        ):
        dtype = ary.dtype
        bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(ary,
            'Series.map()')
        if dtype == types.NPDatetime('ns'):
            dtype = pd_timestamp_tz_naive_type
        if dtype == types.NPTimedelta('ns'):
            dtype = pd_timedelta_type
        bjwah__ywhtc = dtype,
        if f_args is not None:
            bjwah__ywhtc += tuple(f_args.types)
        if kws is None:
            kws = {}
        lcp__kes = False
        grx__rfs = True
        if fname == 'map' and isinstance(func, types.DictType):
            uemy__ghop = func.value_type
            lcp__kes = True
        else:
            try:
                if types.unliteral(func) == types.unicode_type:
                    if not is_overload_constant_str(func):
                        raise BodoError(
                            f'Series.apply(): string argument (for builtins) must be a compile time constant'
                            )
                    uemy__ghop = bodo.utils.transform.get_udf_str_return_type(
                        ary, get_overload_const_str(func), self.context,
                        'Series.apply')
                    grx__rfs = False
                elif bodo.utils.typing.is_numpy_ufunc(func):
                    uemy__ghop = func.get_call_type(self.context, (ary,), {}
                        ).return_type
                    grx__rfs = False
                else:
                    uemy__ghop = get_const_func_output_type(func,
                        bjwah__ywhtc, kws, self.context, numba.core.
                        registry.cpu_target.target_context)
            except Exception as czn__novbm:
                raise BodoError(get_udf_error_msg(f'Series.{fname}()',
                    czn__novbm))
        if grx__rfs:
            if isinstance(uemy__ghop, (SeriesType, HeterogeneousSeriesType)
                ) and uemy__ghop.const_info is None:
                raise BodoError(
                    'Invalid Series output in UDF (Series with constant length and constant Index value expected)'
                    )
            if isinstance(uemy__ghop, HeterogeneousSeriesType):
                amdcp__jyqc, qus__xerr = uemy__ghop.const_info
                if isinstance(uemy__ghop.data, bodo.libs.nullable_tuple_ext
                    .NullableTupleType):
                    mqaoy__rsno = uemy__ghop.data.tuple_typ.types
                elif isinstance(uemy__ghop.data, types.Tuple):
                    mqaoy__rsno = uemy__ghop.data.types
                iqkkm__bgm = tuple(to_nullable_type(dtype_to_array_type(t)) for
                    t in mqaoy__rsno)
                jcfg__eloxe = bodo.DataFrameType(iqkkm__bgm, ary.index,
                    qus__xerr)
            elif isinstance(uemy__ghop, SeriesType):
                vcfp__rgb, qus__xerr = uemy__ghop.const_info
                iqkkm__bgm = tuple(to_nullable_type(dtype_to_array_type(
                    uemy__ghop.dtype)) for amdcp__jyqc in range(vcfp__rgb))
                jcfg__eloxe = bodo.DataFrameType(iqkkm__bgm, ary.index,
                    qus__xerr)
            else:
                kpu__apl = get_udf_out_arr_type(uemy__ghop, lcp__kes)
                jcfg__eloxe = SeriesType(kpu__apl.dtype, kpu__apl, ary.
                    index, ary.name_typ)
        else:
            jcfg__eloxe = uemy__ghop
        return signature(jcfg__eloxe, (func,)).replace(pysig=pysig)

    @bound_function('series.map', no_unliteral=True)
    def resolve_map(self, ary, args, kws):
        kws = dict(kws)
        func = args[0] if len(args) > 0 else kws['arg']
        kws.pop('arg', None)
        na_action = args[1] if len(args) > 1 else kws.pop('na_action',
            types.none)
        aolv__cgdcz = dict(na_action=na_action)
        misi__tmdgl = dict(na_action=None)
        check_unsupported_args('Series.map', aolv__cgdcz, misi__tmdgl,
            package_name='pandas', module_name='Series')

        def map_stub(arg, na_action=None):
            pass
        pysig = numba.core.utils.pysignature(map_stub)
        return self._resolve_map_func(ary, func, pysig, 'map')

    @bound_function('series.apply', no_unliteral=True)
    def resolve_apply(self, ary, args, kws):
        kws = dict(kws)
        func = args[0] if len(args) > 0 else kws['func']
        kws.pop('func', None)
        iuuu__lcb = args[1] if len(args) > 1 else kws.pop('convert_dtype',
            types.literal(True))
        f_args = args[2] if len(args) > 2 else kws.pop('args', None)
        aolv__cgdcz = dict(convert_dtype=iuuu__lcb)
        wkho__wfflo = dict(convert_dtype=True)
        check_unsupported_args('Series.apply', aolv__cgdcz, wkho__wfflo,
            package_name='pandas', module_name='Series')
        szd__iejo = ', '.join("{} = ''".format(bmgk__wtqsg) for bmgk__wtqsg in
            kws.keys())
        eceei__cxgg = (
            f'def apply_stub(func, convert_dtype=True, args=(), {szd__iejo}):\n'
            )
        eceei__cxgg += '    pass\n'
        fxo__zgg = {}
        exec(eceei__cxgg, {}, fxo__zgg)
        qwphs__btc = fxo__zgg['apply_stub']
        pysig = numba.core.utils.pysignature(qwphs__btc)
        return self._resolve_map_func(ary, func, pysig, 'apply', f_args, kws)

    def _resolve_combine_func(self, ary, args, kws):
        kwargs = dict(kws)
        other = args[0] if len(args) > 0 else types.unliteral(kwargs['other'])
        func = args[1] if len(args) > 1 else kwargs['func']
        fill_value = args[2] if len(args) > 2 else types.unliteral(kwargs.
            get('fill_value', types.none))

        def combine_stub(other, func, fill_value=None):
            pass
        pysig = numba.core.utils.pysignature(combine_stub)
        pww__alvqp = ary.dtype
        bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(ary,
            'Series.combine()')
        bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(other,
            'Series.combine()')
        if pww__alvqp == types.NPDatetime('ns'):
            pww__alvqp = pd_timestamp_tz_naive_type
        wkm__mcc = other.dtype
        if wkm__mcc == types.NPDatetime('ns'):
            wkm__mcc = pd_timestamp_tz_naive_type
        uemy__ghop = get_const_func_output_type(func, (pww__alvqp, wkm__mcc
            ), {}, self.context, numba.core.registry.cpu_target.target_context)
        sig = signature(SeriesType(uemy__ghop, index=ary.index, name_typ=
            types.none), (other, func, fill_value))
        return sig.replace(pysig=pysig)

    @bound_function('series.combine', no_unliteral=True)
    def resolve_combine(self, ary, args, kws):
        return self._resolve_combine_func(ary, args, kws)

    @bound_function('series.pipe', no_unliteral=True)
    def resolve_pipe(self, ary, args, kws):
        bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(ary,
            'Series.pipe()')
        return bodo.hiframes.pd_groupby_ext.resolve_obj_pipe(self, ary,
            args, kws, 'Series')

    def generic_resolve(self, S, attr):
        from bodo.hiframes.pd_index_ext import HeterogeneousIndexType
        if self._is_existing_attr(attr):
            return
        if isinstance(S.index, HeterogeneousIndexType
            ) and is_overload_constant_tuple(S.index.data):
            wjzb__qzbxe = get_overload_const_tuple(S.index.data)
            if attr in wjzb__qzbxe:
                fvikz__afn = wjzb__qzbxe.index(attr)
                return S.data[fvikz__afn]


series_binary_ops = tuple(op for op in numba.core.typing.npydecl.
    NumpyRulesArrayOperator._op_map.keys() if op not in (operator.lshift,
    operator.rshift))
series_inplace_binary_ops = tuple(op for op in numba.core.typing.npydecl.
    NumpyRulesInplaceArrayOperator._op_map.keys() if op not in (operator.
    ilshift, operator.irshift, operator.itruediv))
inplace_binop_to_imm = {operator.iadd: operator.add, operator.isub:
    operator.sub, operator.imul: operator.mul, operator.ifloordiv: operator
    .floordiv, operator.imod: operator.mod, operator.ipow: operator.pow,
    operator.iand: operator.and_, operator.ior: operator.or_, operator.ixor:
    operator.xor}
series_unary_ops = operator.neg, operator.invert, operator.pos
str2str_methods = ('capitalize', 'lower', 'lstrip', 'rstrip', 'strip',
    'swapcase', 'title', 'upper')
str2bool_methods = ('isalnum', 'isalpha', 'isdigit', 'isspace', 'islower',
    'isupper', 'istitle', 'isnumeric', 'isdecimal')


@overload(pd.Series, no_unliteral=True)
def pd_series_overload(data=None, index=None, dtype=None, name=None, copy=
    False, fastpath=False):
    if not is_overload_false(fastpath):
        raise BodoError("pd.Series(): 'fastpath' argument not supported.")
    sgl__nztgk = is_overload_none(data)
    wsfok__ukkjn = is_overload_none(index)
    yjo__eeu = is_overload_none(dtype)
    if sgl__nztgk and wsfok__ukkjn and yjo__eeu:
        raise BodoError(
            'pd.Series() requires at least 1 of data, index, and dtype to not be none'
            )
    if is_series_type(data) and not wsfok__ukkjn:
        raise BodoError(
            'pd.Series() does not support index value when input data is a Series'
            )
    if isinstance(data, types.DictType):
        raise_bodo_error(
            'pd.Series(): When intializing series with a dictionary, it is required that the dict has constant keys'
            )
    if is_heterogeneous_tuple_type(data) and is_overload_none(dtype):
        qzr__tmh = tuple(len(data) * [False])

        def impl_heter(data=None, index=None, dtype=None, name=None, copy=
            False, fastpath=False):
            amfhe__sfhi = bodo.utils.conversion.extract_index_if_none(data,
                index)
            ipio__felu = bodo.utils.conversion.to_tuple(data)
            data_val = bodo.libs.nullable_tuple_ext.build_nullable_tuple(
                ipio__felu, qzr__tmh)
            return bodo.hiframes.pd_series_ext.init_series(data_val, bodo.
                utils.conversion.convert_to_index(amfhe__sfhi), name)
        return impl_heter
    if sgl__nztgk:
        if yjo__eeu:

            def impl(data=None, index=None, dtype=None, name=None, copy=
                False, fastpath=False):
                idni__ijrz = bodo.utils.conversion.extract_name_if_none(data,
                    name)
                amfhe__sfhi = bodo.utils.conversion.extract_index_if_none(data,
                    index)
                numba.parfors.parfor.init_prange()
                aleg__zco = len(amfhe__sfhi)
                ipio__felu = np.empty(aleg__zco, np.float64)
                for dlgg__mne in numba.parfors.parfor.internal_prange(aleg__zco
                    ):
                    bodo.libs.array_kernels.setna(ipio__felu, dlgg__mne)
                return bodo.hiframes.pd_series_ext.init_series(ipio__felu,
                    bodo.utils.conversion.convert_to_index(amfhe__sfhi),
                    idni__ijrz)
            return impl
        if bodo.utils.conversion._is_str_dtype(dtype):
            swsfs__gdxf = bodo.string_array_type
        else:
            kbiha__qdom = bodo.utils.typing.parse_dtype(dtype, 'pandas.Series')
            if isinstance(kbiha__qdom, bodo.libs.int_arr_ext.IntDtype):
                swsfs__gdxf = bodo.IntegerArrayType(kbiha__qdom.dtype)
            elif isinstance(kbiha__qdom, bodo.libs.float_arr_ext.FloatDtype):
                swsfs__gdxf = bodo.FloatingArrayType(kbiha__qdom.dtype)
            elif kbiha__qdom == bodo.libs.bool_arr_ext.boolean_dtype:
                swsfs__gdxf = bodo.boolean_array
            elif isinstance(kbiha__qdom, types.Number) or kbiha__qdom in [bodo
                .datetime64ns, bodo.timedelta64ns]:
                swsfs__gdxf = types.Array(kbiha__qdom, 1, 'C')
            else:
                raise BodoError(
                    'pd.Series with dtype: {dtype} not currently supported')
        if wsfok__ukkjn:

            def impl(data=None, index=None, dtype=None, name=None, copy=
                False, fastpath=False):
                idni__ijrz = bodo.utils.conversion.extract_name_if_none(data,
                    name)
                amfhe__sfhi = bodo.hiframes.pd_index_ext.init_range_index(0,
                    0, 1, None)
                numba.parfors.parfor.init_prange()
                aleg__zco = len(amfhe__sfhi)
                ipio__felu = bodo.utils.utils.alloc_type(aleg__zco,
                    swsfs__gdxf, (-1,))
                return bodo.hiframes.pd_series_ext.init_series(ipio__felu,
                    amfhe__sfhi, idni__ijrz)
            return impl
        else:

            def impl(data=None, index=None, dtype=None, name=None, copy=
                False, fastpath=False):
                idni__ijrz = bodo.utils.conversion.extract_name_if_none(data,
                    name)
                amfhe__sfhi = bodo.utils.conversion.extract_index_if_none(data,
                    index)
                numba.parfors.parfor.init_prange()
                aleg__zco = len(amfhe__sfhi)
                ipio__felu = bodo.utils.utils.alloc_type(aleg__zco,
                    swsfs__gdxf, (-1,))
                for dlgg__mne in numba.parfors.parfor.internal_prange(aleg__zco
                    ):
                    bodo.libs.array_kernels.setna(ipio__felu, dlgg__mne)
                return bodo.hiframes.pd_series_ext.init_series(ipio__felu,
                    bodo.utils.conversion.convert_to_index(amfhe__sfhi),
                    idni__ijrz)
            return impl

    def impl(data=None, index=None, dtype=None, name=None, copy=False,
        fastpath=False):
        idni__ijrz = bodo.utils.conversion.extract_name_if_none(data, name)
        amfhe__sfhi = bodo.utils.conversion.extract_index_if_none(data, index)
        tgf__nfpf = bodo.utils.conversion.coerce_to_array(data, True,
            scalar_to_arr_len=len(amfhe__sfhi))
        bcuqc__rta = bodo.utils.conversion.fix_arr_dtype(tgf__nfpf, dtype,
            None, False)
        return bodo.hiframes.pd_series_ext.init_series(bcuqc__rta, bodo.
            utils.conversion.convert_to_index(amfhe__sfhi), idni__ijrz)
    return impl


@overload_method(SeriesType, 'to_csv', no_unliteral=True)
def to_csv_overload(series, path_or_buf=None, sep=',', na_rep='',
    float_format=None, columns=None, header=True, index=True, index_label=
    None, mode='w', encoding=None, compression='infer', quoting=None,
    quotechar='"', line_terminator=None, chunksize=None, date_format=None,
    doublequote=True, escapechar=None, decimal='.', errors='strict',
    _bodo_file_prefix='part-', _is_parallel=False):
    if not (is_overload_none(path_or_buf) or is_overload_constant_str(
        path_or_buf) or path_or_buf == string_type):
        raise BodoError(
            "Series.to_csv(): 'path_or_buf' argument should be None or string")
    if is_overload_none(path_or_buf):

        def _impl(series, path_or_buf=None, sep=',', na_rep='',
            float_format=None, columns=None, header=True, index=True,
            index_label=None, mode='w', encoding=None, compression='infer',
            quoting=None, quotechar='"', line_terminator=None, chunksize=
            None, date_format=None, doublequote=True, escapechar=None,
            decimal='.', errors='strict', _bodo_file_prefix='part-',
            _is_parallel=False):
            with numba.objmode(D='unicode_type'):
                D = series.to_csv(None, sep, na_rep, float_format, columns,
                    header, index, index_label, mode, encoding, compression,
                    quoting, quotechar, line_terminator, chunksize,
                    date_format, doublequote, escapechar, decimal, errors)
            return D
        return _impl

    def _impl(series, path_or_buf=None, sep=',', na_rep='', float_format=
        None, columns=None, header=True, index=True, index_label=None, mode
        ='w', encoding=None, compression='infer', quoting=None, quotechar=
        '"', line_terminator=None, chunksize=None, date_format=None,
        doublequote=True, escapechar=None, decimal='.', errors='strict',
        _bodo_file_prefix='part-', _is_parallel=False):
        if _is_parallel:
            header &= (bodo.libs.distributed_api.get_rank() == 0
                ) | _csv_output_is_dir(unicode_to_utf8(path_or_buf))
        with numba.objmode(D='unicode_type'):
            D = series.to_csv(None, sep, na_rep, float_format, columns,
                header, index, index_label, mode, encoding, compression,
                quoting, quotechar, line_terminator, chunksize, date_format,
                doublequote, escapechar, decimal, errors)
        bodo.io.fs_io.csv_write(path_or_buf, D, _bodo_file_prefix, _is_parallel
            )
    return _impl


@lower_constant(SeriesType)
def lower_constant_series(context, builder, series_type, pyval):
    if isinstance(series_type.data, bodo.DatetimeArrayType):
        myeq__duq = pyval.array
    else:
        myeq__duq = pyval.values
    data_val = context.get_constant_generic(builder, series_type.data,
        myeq__duq)
    index_val = context.get_constant_generic(builder, series_type.index,
        pyval.index)
    name_val = context.get_constant_generic(builder, series_type.name_typ,
        pyval.name)
    uetk__ahdmi = lir.Constant.literal_struct([data_val, index_val, name_val])
    uetk__ahdmi = cgutils.global_constant(builder, '.const.payload',
        uetk__ahdmi).bitcast(cgutils.voidptr_t)
    luaq__rftdx = context.get_constant(types.int64, -1)
    rbzi__ixgz = context.get_constant_null(types.voidptr)
    pjds__ddv = lir.Constant.literal_struct([luaq__rftdx, rbzi__ixgz,
        rbzi__ixgz, uetk__ahdmi, luaq__rftdx])
    pjds__ddv = cgutils.global_constant(builder, '.const.meminfo', pjds__ddv
        ).bitcast(cgutils.voidptr_t)
    edo__ruj = lir.Constant.literal_struct([pjds__ddv, rbzi__ixgz])
    return edo__ruj


series_unsupported_attrs = {'axes', 'array', 'flags', 'at', 'is_unique',
    'sparse', 'attrs'}
series_unsupported_methods = ('set_flags', 'convert_dtypes', 'bool',
    'to_period', 'to_timestamp', '__array__', 'get', 'at', '__iter__',
    'items', 'iteritems', 'pop', 'item', 'xs', 'combine_first', 'agg',
    'aggregate', 'transform', 'expanding', 'ewm', 'clip', 'factorize',
    'mode', 'align', 'drop', 'droplevel', 'reindex', 'reindex_like',
    'sample', 'set_axis', 'truncate', 'add_prefix', 'add_suffix', 'filter',
    'interpolate', 'argmin', 'argmax', 'reorder_levels', 'swaplevel',
    'unstack', 'searchsorted', 'ravel', 'squeeze', 'view', 'compare',
    'update', 'asfreq', 'asof', 'resample', 'tz_convert', 'tz_localize',
    'at_time', 'between_time', 'tshift', 'slice_shift', 'plot', 'hist',
    'to_pickle', 'to_excel', 'to_xarray', 'to_hdf', 'to_sql', 'to_json',
    'to_string', 'to_clipboard', 'to_latex', 'to_markdown')


def _install_series_unsupported():
    for stpi__muwzo in series_unsupported_attrs:
        pjgxc__crwli = 'Series.' + stpi__muwzo
        overload_attribute(SeriesType, stpi__muwzo)(create_unsupported_overload
            (pjgxc__crwli))
    for fname in series_unsupported_methods:
        pjgxc__crwli = 'Series.' + fname
        overload_method(SeriesType, fname, no_unliteral=True)(
            create_unsupported_overload(pjgxc__crwli))


_install_series_unsupported()
heter_series_unsupported_attrs = {'axes', 'array', 'dtype', 'nbytes',
    'memory_usage', 'hasnans', 'dtypes', 'flags', 'at', 'is_unique',
    'is_monotonic', 'is_monotonic_increasing', 'is_monotonic_decreasing',
    'dt', 'str', 'cat', 'sparse', 'attrs'}
heter_series_unsupported_methods = {'set_flags', 'convert_dtypes',
    'infer_objects', 'copy', 'bool', 'to_numpy', 'to_period',
    'to_timestamp', 'to_list', 'tolist', '__array__', 'get', 'at', 'iat',
    'iloc', 'loc', '__iter__', 'items', 'iteritems', 'keys', 'pop', 'item',
    'xs', 'add', 'sub', 'mul', 'div', 'truediv', 'floordiv', 'mod', 'pow',
    'radd', 'rsub', 'rmul', 'rdiv', 'rtruediv', 'rfloordiv', 'rmod', 'rpow',
    'combine', 'combine_first', 'round', 'lt', 'gt', 'le', 'ge', 'ne', 'eq',
    'product', 'dot', 'apply', 'agg', 'aggregate', 'transform', 'map',
    'groupby', 'rolling', 'expanding', 'ewm', 'pipe', 'abs', 'all', 'any',
    'autocorr', 'between', 'clip', 'corr', 'count', 'cov', 'cummax',
    'cummin', 'cumprod', 'cumsum', 'describe', 'diff', 'factorize', 'kurt',
    'mad', 'max', 'mean', 'median', 'min', 'mode', 'nlargest', 'nsmallest',
    'pct_change', 'prod', 'quantile', 'rank', 'sem', 'skew', 'std', 'sum',
    'var', 'kurtosis', 'unique', 'nunique', 'value_counts', 'align', 'drop',
    'droplevel', 'drop_duplicates', 'duplicated', 'equals', 'first', 'head',
    'idxmax', 'idxmin', 'isin', 'last', 'reindex', 'reindex_like', 'rename',
    'rename_axis', 'reset_index', 'sample', 'set_axis', 'take', 'tail',
    'truncate', 'where', 'mask', 'add_prefix', 'add_suffix', 'filter',
    'backfill', 'bfill', 'dropna', 'ffill', 'fillna', 'interpolate', 'isna',
    'isnull', 'notna', 'notnull', 'pad', 'replace', 'argsort', 'argmin',
    'argmax', 'reorder_levels', 'sort_values', 'sort_index', 'swaplevel',
    'unstack', 'explode', 'searchsorted', 'ravel', 'repeat', 'squeeze',
    'view', 'append', 'compare', 'update', 'asfreq', 'asof', 'shift',
    'first_valid_index', 'last_valid_index', 'resample', 'tz_convert',
    'tz_localize', 'at_time', 'between_time', 'tshift', 'slice_shift',
    'plot', 'hist', 'to_pickle', 'to_csv', 'to_dict', 'to_excel',
    'to_frame', 'to_xarray', 'to_hdf', 'to_sql', 'to_json', 'to_string',
    'to_clipboard', 'to_latex', 'to_markdown'}


def _install_heter_series_unsupported():
    for stpi__muwzo in heter_series_unsupported_attrs:
        pjgxc__crwli = 'HeterogeneousSeries.' + stpi__muwzo
        overload_attribute(HeterogeneousSeriesType, stpi__muwzo)(
            create_unsupported_overload(pjgxc__crwli))
    for fname in heter_series_unsupported_methods:
        pjgxc__crwli = 'HeterogeneousSeries.' + fname
        overload_method(HeterogeneousSeriesType, fname, no_unliteral=True)(
            create_unsupported_overload(pjgxc__crwli))


_install_heter_series_unsupported()
