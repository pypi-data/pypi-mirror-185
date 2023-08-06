"""Array implementation for map values.
Corresponds to Spark's MapType: https://spark.apache.org/docs/latest/sql-reference.html
Corresponds to Arrow's Map arrays: https://github.com/apache/arrow/blob/master/format/Schema.fbs

The implementation uses an array(struct) array underneath similar to Spark and Arrow.
For example: [{1: 2.1, 3: 1.1}, {5: -1.0}]
[[{"key": 1, "value" 2.1}, {"key": 3, "value": 1.1}], [{"key": 5, "value": -1.0}]]
"""
import operator
import llvmlite.binding as ll
import numba
import numpy as np
from llvmlite import ir as lir
from numba.core import cgutils, types
from numba.extending import NativeValue, box, intrinsic, make_attribute_wrapper, models, overload, overload_attribute, overload_method, register_model, unbox
from numba.parfors.array_analysis import ArrayAnalysis
import bodo
from bodo.hiframes.datetime_date_ext import datetime_date_type
from bodo.libs.array_item_arr_ext import ArrayItemArrayType, _get_array_item_arr_payload, offset_type
from bodo.libs.struct_arr_ext import StructArrayType, _get_struct_arr_payload
from bodo.utils.cg_helpers import dict_keys, dict_merge_from_seq2, dict_values, gen_allocate_array, get_array_elem_counts, get_bitmap_bit, is_na_value, pyarray_setitem, seq_getitem, set_bitmap_bit
from bodo.utils.typing import BodoError
from bodo.libs import array_ext, hdist
ll.add_symbol('count_total_elems_list_array', array_ext.
    count_total_elems_list_array)
ll.add_symbol('map_array_from_sequence', array_ext.map_array_from_sequence)
ll.add_symbol('np_array_from_map_array', array_ext.np_array_from_map_array)


class MapArrayType(types.ArrayCompatible):

    def __init__(self, key_arr_type, value_arr_type):
        self.key_arr_type = key_arr_type
        self.value_arr_type = value_arr_type
        super(MapArrayType, self).__init__(name='MapArrayType({}, {})'.
            format(key_arr_type, value_arr_type))

    @property
    def as_array(self):
        return types.Array(types.undefined, 1, 'C')

    @property
    def dtype(self):
        return types.DictType(self.key_arr_type.dtype, self.value_arr_type.
            dtype)

    def copy(self):
        return MapArrayType(self.key_arr_type, self.value_arr_type)

    @property
    def mangling_args(self):
        return self.__class__.__name__, (self._code,)


def _get_map_arr_data_type(map_type):
    thof__oqdw = StructArrayType((map_type.key_arr_type, map_type.
        value_arr_type), ('key', 'value'))
    return ArrayItemArrayType(thof__oqdw)


@register_model(MapArrayType)
class MapArrayModel(models.StructModel):

    def __init__(self, dmm, fe_type):
        qhep__xgi = _get_map_arr_data_type(fe_type)
        rgc__tjp = [('data', qhep__xgi)]
        models.StructModel.__init__(self, dmm, fe_type, rgc__tjp)


make_attribute_wrapper(MapArrayType, 'data', '_data')


@unbox(MapArrayType)
def unbox_map_array(typ, val, c):
    n_maps = bodo.utils.utils.object_length(c, val)
    nufc__bpj = all(isinstance(eaun__glo, types.Array) and eaun__glo.dtype in
        (types.int64, types.float64, types.bool_, datetime_date_type) for
        eaun__glo in (typ.key_arr_type, typ.value_arr_type))
    if nufc__bpj:
        opzm__sjj = lir.FunctionType(lir.IntType(64), [lir.IntType(8).
            as_pointer()])
        vwwy__cyvs = cgutils.get_or_insert_function(c.builder.module,
            opzm__sjj, name='count_total_elems_list_array')
        rjysj__wdb = cgutils.pack_array(c.builder, [n_maps, c.builder.call(
            vwwy__cyvs, [val])])
    else:
        rjysj__wdb = get_array_elem_counts(c, c.builder, c.context, val, typ)
    qhep__xgi = _get_map_arr_data_type(typ)
    data_arr = gen_allocate_array(c.context, c.builder, qhep__xgi,
        rjysj__wdb, c)
    dmvbd__llfpk = _get_array_item_arr_payload(c.context, c.builder,
        qhep__xgi, data_arr)
    null_bitmap_ptr = c.context.make_array(types.Array(types.uint8, 1, 'C'))(c
        .context, c.builder, dmvbd__llfpk.null_bitmap).data
    offsets_ptr = c.context.make_array(types.Array(offset_type, 1, 'C'))(c.
        context, c.builder, dmvbd__llfpk.offsets).data
    iki__esbq = _get_struct_arr_payload(c.context, c.builder, qhep__xgi.
        dtype, dmvbd__llfpk.data)
    key_arr = c.builder.extract_value(iki__esbq.data, 0)
    value_arr = c.builder.extract_value(iki__esbq.data, 1)
    sig = types.none(types.Array(types.uint8, 1, 'C'))
    zlu__pda, hrjxr__vaoc = c.pyapi.call_jit_code(lambda A: A.fill(255),
        sig, [iki__esbq.null_bitmap])
    if nufc__bpj:
        pdrn__mryt = c.context.make_array(qhep__xgi.dtype.data[0])(c.
            context, c.builder, key_arr).data
        wyecj__jfsn = c.context.make_array(qhep__xgi.dtype.data[1])(c.
            context, c.builder, value_arr).data
        opzm__sjj = lir.FunctionType(lir.VoidType(), [lir.IntType(8).
            as_pointer(), lir.IntType(8).as_pointer(), lir.IntType(8).
            as_pointer(), lir.IntType(offset_type.bitwidth).as_pointer(),
            lir.IntType(8).as_pointer(), lir.IntType(32), lir.IntType(32)])
        nzz__fenfl = cgutils.get_or_insert_function(c.builder.module,
            opzm__sjj, name='map_array_from_sequence')
        xeicq__ygsdq = bodo.utils.utils.numba_to_c_type(typ.key_arr_type.dtype)
        qgawy__oifv = bodo.utils.utils.numba_to_c_type(typ.value_arr_type.dtype
            )
        c.builder.call(nzz__fenfl, [val, c.builder.bitcast(pdrn__mryt, lir.
            IntType(8).as_pointer()), c.builder.bitcast(wyecj__jfsn, lir.
            IntType(8).as_pointer()), offsets_ptr, null_bitmap_ptr, lir.
            Constant(lir.IntType(32), xeicq__ygsdq), lir.Constant(lir.
            IntType(32), qgawy__oifv)])
    else:
        _unbox_map_array_generic(typ, val, c, n_maps, key_arr, value_arr,
            offsets_ptr, null_bitmap_ptr)
    jhq__lga = c.context.make_helper(c.builder, typ)
    jhq__lga.data = data_arr
    epsbo__lcowb = cgutils.is_not_null(c.builder, c.pyapi.err_occurred())
    return NativeValue(jhq__lga._getvalue(), is_error=epsbo__lcowb)


def _unbox_map_array_generic(typ, val, c, n_maps, key_arr, value_arr,
    offsets_ptr, null_bitmap_ptr):
    from bodo.libs.array_item_arr_ext import _unbox_array_item_array_copy_data
    context = c.context
    builder = c.builder
    hbith__hhye = context.insert_const_string(builder.module, 'pandas')
    sxeyw__wtwq = c.pyapi.import_module_noblock(hbith__hhye)
    hhqi__gtqf = c.pyapi.object_getattr_string(sxeyw__wtwq, 'NA')
    vrde__wipcd = c.context.get_constant(offset_type, 0)
    builder.store(vrde__wipcd, offsets_ptr)
    rqnn__injv = cgutils.alloca_once_value(builder, context.get_constant(
        types.int64, 0))
    with cgutils.for_range(builder, n_maps) as xpphd__gjs:
        ztx__pmr = xpphd__gjs.index
        item_ind = builder.load(rqnn__injv)
        builder.store(builder.trunc(item_ind, lir.IntType(offset_type.
            bitwidth)), builder.gep(offsets_ptr, [ztx__pmr]))
        uqr__gjz = seq_getitem(builder, context, val, ztx__pmr)
        set_bitmap_bit(builder, null_bitmap_ptr, ztx__pmr, 0)
        qmbqu__crir = is_na_value(builder, context, uqr__gjz, hhqi__gtqf)
        ertwe__cqqq = builder.icmp_unsigned('!=', qmbqu__crir, lir.Constant
            (qmbqu__crir.type, 1))
        with builder.if_then(ertwe__cqqq):
            set_bitmap_bit(builder, null_bitmap_ptr, ztx__pmr, 1)
            dlpb__lobms = dict_keys(builder, context, uqr__gjz)
            kmb__mbe = dict_values(builder, context, uqr__gjz)
            n_items = bodo.utils.utils.object_length(c, dlpb__lobms)
            _unbox_array_item_array_copy_data(typ.key_arr_type, dlpb__lobms,
                c, key_arr, item_ind, n_items)
            _unbox_array_item_array_copy_data(typ.value_arr_type, kmb__mbe,
                c, value_arr, item_ind, n_items)
            builder.store(builder.add(item_ind, n_items), rqnn__injv)
            c.pyapi.decref(dlpb__lobms)
            c.pyapi.decref(kmb__mbe)
        c.pyapi.decref(uqr__gjz)
    builder.store(builder.trunc(builder.load(rqnn__injv), lir.IntType(
        offset_type.bitwidth)), builder.gep(offsets_ptr, [n_maps]))
    c.pyapi.decref(sxeyw__wtwq)
    c.pyapi.decref(hhqi__gtqf)


@box(MapArrayType)
def box_map_arr(typ, val, c):
    jhq__lga = c.context.make_helper(c.builder, typ, val)
    data_arr = jhq__lga.data
    qhep__xgi = _get_map_arr_data_type(typ)
    dmvbd__llfpk = _get_array_item_arr_payload(c.context, c.builder,
        qhep__xgi, data_arr)
    null_bitmap_ptr = c.context.make_array(types.Array(types.uint8, 1, 'C'))(c
        .context, c.builder, dmvbd__llfpk.null_bitmap).data
    offsets_ptr = c.context.make_array(types.Array(offset_type, 1, 'C'))(c.
        context, c.builder, dmvbd__llfpk.offsets).data
    iki__esbq = _get_struct_arr_payload(c.context, c.builder, qhep__xgi.
        dtype, dmvbd__llfpk.data)
    key_arr = c.builder.extract_value(iki__esbq.data, 0)
    value_arr = c.builder.extract_value(iki__esbq.data, 1)
    if all(isinstance(eaun__glo, types.Array) and eaun__glo.dtype in (types
        .int64, types.float64, types.bool_, datetime_date_type) for
        eaun__glo in (typ.key_arr_type, typ.value_arr_type)):
        pdrn__mryt = c.context.make_array(qhep__xgi.dtype.data[0])(c.
            context, c.builder, key_arr).data
        wyecj__jfsn = c.context.make_array(qhep__xgi.dtype.data[1])(c.
            context, c.builder, value_arr).data
        opzm__sjj = lir.FunctionType(c.context.get_argument_type(types.
            pyobject), [lir.IntType(64), lir.IntType(8).as_pointer(), lir.
            IntType(8).as_pointer(), lir.IntType(offset_type.bitwidth).
            as_pointer(), lir.IntType(8).as_pointer(), lir.IntType(32), lir
            .IntType(32)])
        sho__xdmyj = cgutils.get_or_insert_function(c.builder.module,
            opzm__sjj, name='np_array_from_map_array')
        xeicq__ygsdq = bodo.utils.utils.numba_to_c_type(typ.key_arr_type.dtype)
        qgawy__oifv = bodo.utils.utils.numba_to_c_type(typ.value_arr_type.dtype
            )
        arr = c.builder.call(sho__xdmyj, [dmvbd__llfpk.n_arrays, c.builder.
            bitcast(pdrn__mryt, lir.IntType(8).as_pointer()), c.builder.
            bitcast(wyecj__jfsn, lir.IntType(8).as_pointer()), offsets_ptr,
            null_bitmap_ptr, lir.Constant(lir.IntType(32), xeicq__ygsdq),
            lir.Constant(lir.IntType(32), qgawy__oifv)])
    else:
        arr = _box_map_array_generic(typ, c, dmvbd__llfpk.n_arrays, key_arr,
            value_arr, offsets_ptr, null_bitmap_ptr)
    c.context.nrt.decref(c.builder, typ, val)
    return arr


def _box_map_array_generic(typ, c, n_maps, key_arr, value_arr, offsets_ptr,
    null_bitmap_ptr):
    context = c.context
    builder = c.builder
    hbith__hhye = context.insert_const_string(builder.module, 'numpy')
    pvmp__dlfm = c.pyapi.import_module_noblock(hbith__hhye)
    krfht__krhs = c.pyapi.object_getattr_string(pvmp__dlfm, 'object_')
    gqy__yos = c.pyapi.long_from_longlong(n_maps)
    rxj__eoq = c.pyapi.call_method(pvmp__dlfm, 'ndarray', (gqy__yos,
        krfht__krhs))
    bdx__ohfss = c.pyapi.object_getattr_string(pvmp__dlfm, 'nan')
    dbw__lvris = c.pyapi.unserialize(c.pyapi.serialize_object(zip))
    rqnn__injv = cgutils.alloca_once_value(builder, lir.Constant(lir.
        IntType(64), 0))
    with cgutils.for_range(builder, n_maps) as xpphd__gjs:
        ernl__jvr = xpphd__gjs.index
        pyarray_setitem(builder, context, rxj__eoq, ernl__jvr, bdx__ohfss)
        fozpj__djp = get_bitmap_bit(builder, null_bitmap_ptr, ernl__jvr)
        esbqi__vrmso = builder.icmp_unsigned('!=', fozpj__djp, lir.Constant
            (lir.IntType(8), 0))
        with builder.if_then(esbqi__vrmso):
            n_items = builder.sext(builder.sub(builder.load(builder.gep(
                offsets_ptr, [builder.add(ernl__jvr, lir.Constant(ernl__jvr
                .type, 1))])), builder.load(builder.gep(offsets_ptr, [
                ernl__jvr]))), lir.IntType(64))
            item_ind = builder.load(rqnn__injv)
            uqr__gjz = c.pyapi.dict_new()
            ghk__shx = lambda data_arr, item_ind, n_items: data_arr[item_ind
                :item_ind + n_items]
            zlu__pda, fgfg__abza = c.pyapi.call_jit_code(ghk__shx, typ.
                key_arr_type(typ.key_arr_type, types.int64, types.int64), [
                key_arr, item_ind, n_items])
            zlu__pda, gnww__idnw = c.pyapi.call_jit_code(ghk__shx, typ.
                value_arr_type(typ.value_arr_type, types.int64, types.int64
                ), [value_arr, item_ind, n_items])
            liqay__mfbxl = c.pyapi.from_native_value(typ.key_arr_type,
                fgfg__abza, c.env_manager)
            wvgch__tpaf = c.pyapi.from_native_value(typ.value_arr_type,
                gnww__idnw, c.env_manager)
            labf__vqbm = c.pyapi.call_function_objargs(dbw__lvris, (
                liqay__mfbxl, wvgch__tpaf))
            dict_merge_from_seq2(builder, context, uqr__gjz, labf__vqbm)
            builder.store(builder.add(item_ind, n_items), rqnn__injv)
            pyarray_setitem(builder, context, rxj__eoq, ernl__jvr, uqr__gjz)
            c.pyapi.decref(labf__vqbm)
            c.pyapi.decref(liqay__mfbxl)
            c.pyapi.decref(wvgch__tpaf)
            c.pyapi.decref(uqr__gjz)
    c.pyapi.decref(dbw__lvris)
    c.pyapi.decref(pvmp__dlfm)
    c.pyapi.decref(krfht__krhs)
    c.pyapi.decref(gqy__yos)
    c.pyapi.decref(bdx__ohfss)
    return rxj__eoq


def init_map_arr_codegen(context, builder, sig, args):
    data_arr, = args
    jhq__lga = context.make_helper(builder, sig.return_type)
    jhq__lga.data = data_arr
    context.nrt.incref(builder, sig.args[0], data_arr)
    return jhq__lga._getvalue()


@intrinsic
def init_map_arr(typingctx, data_typ=None):
    assert isinstance(data_typ, ArrayItemArrayType) and isinstance(data_typ
        .dtype, StructArrayType)
    fwnc__mplp = MapArrayType(data_typ.dtype.data[0], data_typ.dtype.data[1])
    return fwnc__mplp(data_typ), init_map_arr_codegen


def alias_ext_init_map_arr(lhs_name, args, alias_map, arg_aliases):
    assert len(args) == 1
    numba.core.ir_utils._add_alias(lhs_name, args[0].name, alias_map,
        arg_aliases)


numba.core.ir_utils.alias_func_extensions['init_map_arr',
    'bodo.libs.map_arr_ext'] = alias_ext_init_map_arr


@numba.njit
def pre_alloc_map_array(num_maps, nested_counts, struct_typ):
    qhbiw__bph = bodo.libs.array_item_arr_ext.pre_alloc_array_item_array(
        num_maps, nested_counts, struct_typ)
    return init_map_arr(qhbiw__bph)


def pre_alloc_map_array_equiv(self, scope, equiv_set, loc, args, kws):
    assert len(args) == 3 and not kws
    return ArrayAnalysis.AnalyzeResult(shape=args[0], pre=[])


(ArrayAnalysis._analyze_op_call_bodo_libs_map_arr_ext_pre_alloc_map_array
    ) = pre_alloc_map_array_equiv


@overload(len, no_unliteral=True)
def overload_map_arr_len(A):
    if isinstance(A, MapArrayType):
        return lambda A: len(A._data)


@overload_attribute(MapArrayType, 'shape')
def overload_map_arr_shape(A):
    return lambda A: (len(A._data),)


@overload_attribute(MapArrayType, 'dtype')
def overload_map_arr_dtype(A):
    return lambda A: np.object_


@overload_attribute(MapArrayType, 'ndim')
def overload_map_arr_ndim(A):
    return lambda A: 1


@overload_attribute(MapArrayType, 'nbytes')
def overload_map_arr_nbytes(A):
    return lambda A: A._data.nbytes


@overload_method(MapArrayType, 'copy')
def overload_map_arr_copy(A):
    return lambda A: init_map_arr(A._data.copy())


@overload(operator.setitem, no_unliteral=True)
def map_arr_setitem(arr, ind, val):
    if not isinstance(arr, MapArrayType):
        return
    vdp__bzzv = arr.key_arr_type, arr.value_arr_type
    if isinstance(ind, types.Integer):

        def map_arr_setitem_impl(arr, ind, val):
            scwfs__dowdw = val.keys()
            lqg__upzfr = bodo.libs.struct_arr_ext.pre_alloc_struct_array(len
                (val), (-1,), vdp__bzzv, ('key', 'value'))
            for zjv__akpl, qfs__ahyyg in enumerate(scwfs__dowdw):
                lqg__upzfr[zjv__akpl] = bodo.libs.struct_arr_ext.init_struct((
                    qfs__ahyyg, val[qfs__ahyyg]), ('key', 'value'))
            arr._data[ind] = lqg__upzfr
        return map_arr_setitem_impl
    raise BodoError(
        'operator.setitem with MapArrays is only supported with an integer index.'
        )


@overload(operator.getitem, no_unliteral=True)
def map_arr_getitem(arr, ind):
    if not isinstance(arr, MapArrayType):
        return
    if isinstance(ind, types.Integer):

        def map_arr_getitem_impl(arr, ind):
            if ind < 0:
                ind += len(arr)
            dqc__tam = dict()
            fuxai__fmlgl = bodo.libs.array_item_arr_ext.get_offsets(arr._data)
            lqg__upzfr = bodo.libs.array_item_arr_ext.get_data(arr._data)
            dkxaj__ddlnd, rmbd__fiq = bodo.libs.struct_arr_ext.get_data(
                lqg__upzfr)
            ygena__bhz = fuxai__fmlgl[ind]
            xet__fyt = fuxai__fmlgl[ind + 1]
            for zjv__akpl in range(ygena__bhz, xet__fyt):
                dqc__tam[dkxaj__ddlnd[zjv__akpl]] = rmbd__fiq[zjv__akpl]
            return dqc__tam
        return map_arr_getitem_impl
    raise BodoError(
        'operator.getitem with MapArrays is only supported with an integer index.'
        )
