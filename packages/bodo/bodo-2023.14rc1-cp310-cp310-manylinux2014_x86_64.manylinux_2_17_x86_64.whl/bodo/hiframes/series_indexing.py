"""
Indexing support for Series objects, including loc/iloc/at/iat types.
"""
import operator
import numpy as np
from numba.core import cgutils, types
from numba.extending import intrinsic, lower_cast, make_attribute_wrapper, models, overload, overload_attribute, register_model
import bodo
from bodo.hiframes.datetime_timedelta_ext import datetime_timedelta_type, pd_timedelta_type
from bodo.hiframes.pd_index_ext import HeterogeneousIndexType, NumericIndexType, RangeIndexType
from bodo.hiframes.pd_series_ext import HeterogeneousSeriesType, SeriesType
from bodo.hiframes.pd_timestamp_ext import convert_datetime64_to_timestamp, convert_numpy_timedelta64_to_pd_timedelta, integer_to_dt64, pd_timestamp_tz_naive_type
from bodo.utils.typing import BodoError, get_literal_value, get_overload_const_tuple, is_immutable_array, is_list_like_index_type, is_literal_type, is_overload_constant_str, is_overload_constant_tuple, is_scalar_type, raise_bodo_error


class SeriesIatType(types.Type):

    def __init__(self, stype):
        self.stype = stype
        fvf__lzxo = 'SeriesIatType({})'.format(stype)
        super(SeriesIatType, self).__init__(fvf__lzxo)

    @property
    def mangling_args(self):
        return self.__class__.__name__, (self._code,)
    ndim = 1


@register_model(SeriesIatType)
class SeriesIatModel(models.StructModel):

    def __init__(self, dmm, fe_type):
        zfw__pjgz = [('obj', fe_type.stype)]
        super(SeriesIatModel, self).__init__(dmm, fe_type, zfw__pjgz)


make_attribute_wrapper(SeriesIatType, 'obj', '_obj')


@intrinsic
def init_series_iat(typingctx, obj=None):

    def codegen(context, builder, signature, args):
        fqqpt__ywfef, = args
        ejqtm__lsyxe = signature.return_type
        zfwy__lpr = cgutils.create_struct_proxy(ejqtm__lsyxe)(context, builder)
        zfwy__lpr.obj = fqqpt__ywfef
        context.nrt.incref(builder, signature.args[0], fqqpt__ywfef)
        return zfwy__lpr._getvalue()
    return SeriesIatType(obj)(obj), codegen


@overload_attribute(SeriesType, 'iat')
def overload_series_iat(s):
    return lambda s: bodo.hiframes.series_indexing.init_series_iat(s)


@overload(operator.getitem, no_unliteral=True)
def overload_series_iat_getitem(I, idx):
    if isinstance(I, SeriesIatType):
        if not isinstance(types.unliteral(idx), types.Integer):
            raise BodoError('iAt based indexing can only have integer indexers'
                )
        if I.stype.dtype == types.NPDatetime('ns'):
            return lambda I, idx: convert_datetime64_to_timestamp(np.int64(
                bodo.hiframes.pd_series_ext.get_series_data(I._obj)[idx]))
        if I.stype.dtype == types.NPTimedelta('ns'):
            return lambda I, idx: convert_numpy_timedelta64_to_pd_timedelta(
                bodo.hiframes.pd_series_ext.get_series_data(I._obj)[idx])
        return lambda I, idx: bodo.hiframes.pd_series_ext.get_series_data(I
            ._obj)[idx]


@overload(operator.setitem, no_unliteral=True)
def overload_series_iat_setitem(I, idx, val):
    if isinstance(I, SeriesIatType):
        if not isinstance(idx, types.Integer):
            raise BodoError('iAt based indexing can only have integer indexers'
                )
        if I.stype.dtype == bodo.string_type and val is not types.none:
            raise BodoError('Series string setitem not supported yet')
        if I.stype.dtype == bodo.bytes_type and val is not types.none:
            raise BodoError('Series binary setitem not supported yet')
        if is_immutable_array(I.stype.data):
            raise BodoError(
                f'Series setitem not supported for Series with immutable array type {I.stype.data}'
                )
        if I.stype.dtype == types.NPDatetime('ns'
            ) and val == pd_timestamp_tz_naive_type:

            def impl_dt(I, idx, val):
                s = integer_to_dt64(val.value)
                bodo.hiframes.pd_series_ext.get_series_data(I._obj)[idx] = s
            return impl_dt
        if I.stype.dtype == types.NPDatetime('ns'
            ) and val == bodo.datetime_datetime_type:

            def impl_dt(I, idx, val):
                s = bodo.hiframes.pd_timestamp_ext.datetime_datetime_to_dt64(
                    val)
                bodo.hiframes.pd_series_ext.get_series_data(I._obj)[idx] = s
            return impl_dt
        if I.stype.dtype == types.NPTimedelta('ns'
            ) and val == datetime_timedelta_type:

            def impl_dt(I, idx, val):
                phq__arsvb = (bodo.hiframes.datetime_timedelta_ext.
                    _to_nanoseconds(val))
                s = bodo.hiframes.pd_timestamp_ext.integer_to_timedelta64(
                    phq__arsvb)
                bodo.hiframes.pd_series_ext.get_series_data(I._obj)[idx] = s
            return impl_dt
        if I.stype.dtype == types.NPTimedelta('ns'
            ) and val == pd_timedelta_type:

            def impl_dt(I, idx, val):
                phq__arsvb = val.value
                s = bodo.hiframes.pd_timestamp_ext.integer_to_timedelta64(
                    phq__arsvb)
                bodo.hiframes.pd_series_ext.get_series_data(I._obj)[idx] = s
            return impl_dt

        def impl(I, idx, val):
            bodo.hiframes.pd_series_ext.get_series_data(I._obj)[idx] = val
        return impl


class SeriesIlocType(types.Type):

    def __init__(self, stype):
        self.stype = stype
        fvf__lzxo = 'SeriesIlocType({})'.format(stype)
        super(SeriesIlocType, self).__init__(fvf__lzxo)

    @property
    def mangling_args(self):
        return self.__class__.__name__, (self._code,)
    ndim = 1


@register_model(SeriesIlocType)
class SeriesIlocModel(models.StructModel):

    def __init__(self, dmm, fe_type):
        zfw__pjgz = [('obj', fe_type.stype)]
        super(SeriesIlocModel, self).__init__(dmm, fe_type, zfw__pjgz)


make_attribute_wrapper(SeriesIlocType, 'obj', '_obj')


@intrinsic
def init_series_iloc(typingctx, obj=None):

    def codegen(context, builder, signature, args):
        fqqpt__ywfef, = args
        ffrfb__rig = signature.return_type
        vdlu__akcrw = cgutils.create_struct_proxy(ffrfb__rig)(context, builder)
        vdlu__akcrw.obj = fqqpt__ywfef
        context.nrt.incref(builder, signature.args[0], fqqpt__ywfef)
        return vdlu__akcrw._getvalue()
    return SeriesIlocType(obj)(obj), codegen


@overload_attribute(SeriesType, 'iloc')
def overload_series_iloc(s):
    return lambda s: bodo.hiframes.series_indexing.init_series_iloc(s)


@overload(operator.getitem, no_unliteral=True)
def overload_series_iloc_getitem(I, idx):
    if isinstance(I, SeriesIlocType):
        if I.stype.dtype == types.NPTimedelta('ns') and isinstance(idx,
            types.Integer):
            return lambda I, idx: convert_numpy_timedelta64_to_pd_timedelta(
                bodo.hiframes.pd_series_ext.get_series_data(I._obj)[idx])
        if isinstance(idx, types.Integer):
            return lambda I, idx: bodo.utils.conversion.box_if_dt64(bodo.
                hiframes.pd_series_ext.get_series_data(I._obj)[idx])
        if is_list_like_index_type(idx) and isinstance(idx.dtype, (types.
            Integer, types.Boolean)):

            def impl(I, idx):
                S = I._obj
                wtfis__drqis = bodo.utils.conversion.coerce_to_array(idx)
                lsqiu__xmi = bodo.hiframes.pd_series_ext.get_series_data(S)[
                    wtfis__drqis]
                omrkx__novxq = bodo.hiframes.pd_series_ext.get_series_index(S)[
                    wtfis__drqis]
                fvf__lzxo = bodo.hiframes.pd_series_ext.get_series_name(S)
                return bodo.hiframes.pd_series_ext.init_series(lsqiu__xmi,
                    omrkx__novxq, fvf__lzxo)
            return impl
        if isinstance(idx, types.SliceType):

            def impl_slice(I, idx):
                S = I._obj
                lsqiu__xmi = bodo.hiframes.pd_series_ext.get_series_data(S)[idx
                    ]
                omrkx__novxq = bodo.hiframes.pd_series_ext.get_series_index(S)[
                    idx]
                fvf__lzxo = bodo.hiframes.pd_series_ext.get_series_name(S)
                return bodo.hiframes.pd_series_ext.init_series(lsqiu__xmi,
                    omrkx__novxq, fvf__lzxo)
            return impl_slice
        raise BodoError('Series.iloc[] getitem using {} not supported'.
            format(idx))


@overload(operator.setitem, no_unliteral=True)
def overload_series_iloc_setitem(I, idx, val):
    if isinstance(I, SeriesIlocType):
        if I.stype.dtype == bodo.string_type and val is not types.none:
            raise BodoError('Series string setitem not supported yet')
        if I.stype.dtype == bodo.bytes_type and val is not types.none:
            raise BodoError('Series binary setitem not supported yet')
        if is_immutable_array(I.stype.data):
            raise BodoError(
                f'Series setitem not supported for Series with immutable array type {I.stype.data}'
                )
        if isinstance(idx, types.Integer) or isinstance(idx, types.SliceType
            ) and is_scalar_type(val):
            if I.stype.dtype == types.NPDatetime('ns'
                ) and val == pd_timestamp_tz_naive_type:

                def impl_dt(I, idx, val):
                    s = integer_to_dt64(val.value)
                    bodo.hiframes.pd_series_ext.get_series_data(I._obj)[idx
                        ] = s
                return impl_dt
            if I.stype.dtype == types.NPDatetime('ns'
                ) and val == bodo.datetime_datetime_type:

                def impl_dt(I, idx, val):
                    s = (bodo.hiframes.pd_timestamp_ext.
                        datetime_datetime_to_dt64(val))
                    bodo.hiframes.pd_series_ext.get_series_data(I._obj)[idx
                        ] = s
                return impl_dt
            if I.stype.dtype == types.NPTimedelta('ns'
                ) and val == datetime_timedelta_type:

                def impl_dt(I, idx, val):
                    phq__arsvb = (bodo.hiframes.datetime_timedelta_ext.
                        _to_nanoseconds(val))
                    s = bodo.hiframes.pd_timestamp_ext.integer_to_timedelta64(
                        phq__arsvb)
                    bodo.hiframes.pd_series_ext.get_series_data(I._obj)[idx
                        ] = s
                return impl_dt
            if I.stype.dtype == types.NPTimedelta('ns'
                ) and val == pd_timedelta_type:

                def impl_dt(I, idx, val):
                    phq__arsvb = val.value
                    s = bodo.hiframes.pd_timestamp_ext.integer_to_timedelta64(
                        phq__arsvb)
                    bodo.hiframes.pd_series_ext.get_series_data(I._obj)[idx
                        ] = s
                return impl_dt

            def impl(I, idx, val):
                bodo.hiframes.pd_series_ext.get_series_data(I._obj)[idx] = val
            return impl
        if isinstance(idx, types.SliceType):

            def impl_slice(I, idx, val):
                bodo.hiframes.pd_series_ext.get_series_data(I._obj)[idx
                    ] = bodo.utils.conversion.coerce_to_array(val, False)
            return impl_slice
        if is_list_like_index_type(idx) and isinstance(idx.dtype, (types.
            Integer, types.Boolean)):
            if is_scalar_type(val):
                if I.stype.dtype == types.NPDatetime('ns'
                    ) and val == pd_timestamp_tz_naive_type:

                    def impl_dt(I, idx, val):
                        s = integer_to_dt64(val.value)
                        wtfis__drqis = bodo.utils.conversion.coerce_to_array(
                            idx)
                        bodo.hiframes.pd_series_ext.get_series_data(I._obj)[
                            wtfis__drqis] = s
                    return impl_dt
                if I.stype.dtype == types.NPDatetime('ns'
                    ) and val == bodo.datetime_datetime_type:

                    def impl_dt(I, idx, val):
                        s = (bodo.hiframes.pd_timestamp_ext.
                            datetime_datetime_to_dt64(val))
                        wtfis__drqis = bodo.utils.conversion.coerce_to_array(
                            idx)
                        bodo.hiframes.pd_series_ext.get_series_data(I._obj)[
                            wtfis__drqis] = s
                    return impl_dt
                if I.stype.dtype == types.NPTimedelta('ns'
                    ) and val == datetime_timedelta_type:

                    def impl_dt(I, idx, val):
                        phq__arsvb = (bodo.hiframes.datetime_timedelta_ext.
                            _to_nanoseconds(val))
                        s = (bodo.hiframes.pd_timestamp_ext.
                            integer_to_timedelta64(phq__arsvb))
                        wtfis__drqis = bodo.utils.conversion.coerce_to_array(
                            idx)
                        bodo.hiframes.pd_series_ext.get_series_data(I._obj)[
                            wtfis__drqis] = s
                    return impl_dt
                if I.stype.dtype == types.NPTimedelta('ns'
                    ) and val == pd_timedelta_type:

                    def impl_dt(I, idx, val):
                        phq__arsvb = val.value
                        s = (bodo.hiframes.pd_timestamp_ext.
                            integer_to_timedelta64(phq__arsvb))
                        wtfis__drqis = bodo.utils.conversion.coerce_to_array(
                            idx)
                        bodo.hiframes.pd_series_ext.get_series_data(I._obj)[
                            wtfis__drqis] = s
                    return impl_dt

                def impl(I, idx, val):
                    wtfis__drqis = bodo.utils.conversion.coerce_to_array(idx)
                    bodo.hiframes.pd_series_ext.get_series_data(I._obj)[
                        wtfis__drqis] = val
                return impl

            def impl_arr(I, idx, val):
                wtfis__drqis = bodo.utils.conversion.coerce_to_array(idx)
                bodo.hiframes.pd_series_ext.get_series_data(I._obj)[
                    wtfis__drqis] = bodo.utils.conversion.coerce_to_array(val,
                    False)
            return impl_arr
        raise BodoError('Series.iloc[] setitem using {} not supported'.
            format(idx))


class SeriesLocType(types.Type):

    def __init__(self, stype):
        self.stype = stype
        fvf__lzxo = 'SeriesLocType({})'.format(stype)
        super(SeriesLocType, self).__init__(fvf__lzxo)

    @property
    def mangling_args(self):
        return self.__class__.__name__, (self._code,)
    ndim = 1


@register_model(SeriesLocType)
class SeriesLocModel(models.StructModel):

    def __init__(self, dmm, fe_type):
        zfw__pjgz = [('obj', fe_type.stype)]
        super(SeriesLocModel, self).__init__(dmm, fe_type, zfw__pjgz)


make_attribute_wrapper(SeriesLocType, 'obj', '_obj')


@intrinsic
def init_series_loc(typingctx, obj=None):

    def codegen(context, builder, signature, args):
        fqqpt__ywfef, = args
        knwjp__nfa = signature.return_type
        fgar__hfta = cgutils.create_struct_proxy(knwjp__nfa)(context, builder)
        fgar__hfta.obj = fqqpt__ywfef
        context.nrt.incref(builder, signature.args[0], fqqpt__ywfef)
        return fgar__hfta._getvalue()
    return SeriesLocType(obj)(obj), codegen


@overload_attribute(SeriesType, 'loc')
def overload_series_loc(s):
    return lambda s: bodo.hiframes.series_indexing.init_series_loc(s)


@overload(operator.getitem)
def overload_series_loc_getitem(I, idx):
    if not isinstance(I, SeriesLocType):
        return
    if is_list_like_index_type(idx) and idx.dtype == types.bool_:

        def impl(I, idx):
            S = I._obj
            wtfis__drqis = bodo.utils.conversion.coerce_to_array(idx)
            lsqiu__xmi = bodo.hiframes.pd_series_ext.get_series_data(S)[
                wtfis__drqis]
            omrkx__novxq = bodo.hiframes.pd_series_ext.get_series_index(S)[
                wtfis__drqis]
            fvf__lzxo = bodo.hiframes.pd_series_ext.get_series_name(S)
            return bodo.hiframes.pd_series_ext.init_series(lsqiu__xmi,
                omrkx__novxq, fvf__lzxo)
        return impl
    if isinstance(idx, types.Integer) and isinstance(I.stype.index,
        RangeIndexType):

        def impl_range_index_int(I, idx):
            S = I._obj
            lsqiu__xmi = bodo.hiframes.pd_series_ext.get_series_data(S)
            omrkx__novxq = bodo.hiframes.pd_series_ext.get_series_index(S)
            zdf__siw = (idx - omrkx__novxq._start) // omrkx__novxq._step
            return lsqiu__xmi[zdf__siw]
        return impl_range_index_int
    raise BodoError(
        f'Series.loc[] getitem (location-based indexing) using {idx} not supported yet'
        )


@overload(operator.setitem)
def overload_series_loc_setitem(I, idx, val):
    if not isinstance(I, SeriesLocType):
        return
    if is_immutable_array(I.stype.data):
        raise BodoError(
            f'Series setitem not supported for Series with immutable array type {I.stype.data}'
            )
    if is_list_like_index_type(idx) and idx.dtype == types.bool_:

        def impl(I, idx, val):
            S = I._obj
            S[idx] = val
        return impl
    raise BodoError(
        f'Series.loc[] setitem (location-based indexing) using {idx} not supported yet'
        )


@overload(operator.getitem)
def overload_series_getitem(S, idx):
    if isinstance(S, SeriesType) and not (isinstance(S.index,
        HeterogeneousIndexType) and is_overload_constant_tuple(S.index.data)):
        if isinstance(idx, types.Integer):
            if isinstance(S.index, NumericIndexType) and isinstance(S.index
                .dtype, types.Integer):
                raise BodoError(
                    'Indexing Series with Integer index using [] (which is label-based) not supported yet'
                    )
            if isinstance(S.index, RangeIndexType):

                def impl(S, idx):
                    lsqiu__xmi = bodo.hiframes.pd_series_ext.get_series_data(S)
                    I = bodo.hiframes.pd_series_ext.get_series_index(S)
                    wtfis__drqis = idx * I._step + I._start
                    return bodo.utils.conversion.box_if_dt64(lsqiu__xmi[
                        wtfis__drqis])
                return impl
            return lambda S, idx: bodo.utils.conversion.box_if_dt64(bodo.
                hiframes.pd_series_ext.get_series_data(S)[idx])
        if is_list_like_index_type(idx) and isinstance(idx.dtype, (types.
            Integer, types.Boolean)):
            if isinstance(S.index, NumericIndexType) and isinstance(S.index
                .dtype, types.Integer) and isinstance(idx.dtype, types.Integer
                ):
                raise BodoError(
                    'Indexing Series with Integer index using [] (which is label-based) not supported yet'
                    )

            def impl_arr(S, idx):
                wtfis__drqis = bodo.utils.conversion.coerce_to_array(idx)
                lsqiu__xmi = bodo.hiframes.pd_series_ext.get_series_data(S)[
                    wtfis__drqis]
                omrkx__novxq = bodo.hiframes.pd_series_ext.get_series_index(S)[
                    wtfis__drqis]
                fvf__lzxo = bodo.hiframes.pd_series_ext.get_series_name(S)
                return bodo.hiframes.pd_series_ext.init_series(lsqiu__xmi,
                    omrkx__novxq, fvf__lzxo)
            return impl_arr
        if isinstance(idx, types.SliceType):

            def impl_slice(S, idx):
                lsqiu__xmi = bodo.hiframes.pd_series_ext.get_series_data(S)[idx
                    ]
                omrkx__novxq = bodo.hiframes.pd_series_ext.get_series_index(S)[
                    idx]
                fvf__lzxo = bodo.hiframes.pd_series_ext.get_series_name(S)
                return bodo.hiframes.pd_series_ext.init_series(lsqiu__xmi,
                    omrkx__novxq, fvf__lzxo)
            return impl_slice
        if idx == bodo.string_type or is_overload_constant_str(idx):
            if isinstance(S.index, bodo.hiframes.pd_index_ext.StringIndexType):

                def impl_str_getitem(S, idx):
                    vqa__lenxc = bodo.hiframes.pd_series_ext.get_series_index(S
                        )
                    wbv__idr = vqa__lenxc.get_loc(idx)
                    if wbv__idr is None:
                        raise IndexError
                    else:
                        val = bodo.hiframes.pd_series_ext.get_series_data(S)[
                            bodo.utils.indexing.unoptional(wbv__idr)]
                    return val
                return impl_str_getitem
            else:
                raise BodoError(
                    f'Cannot get Series value using a string, unless the index type is also string'
                    )
        raise BodoError(f'getting Series value using {idx} not supported yet')
    elif bodo.utils.utils.is_array_typ(S) and isinstance(idx, SeriesType):
        return lambda S, idx: S[bodo.hiframes.pd_series_ext.get_series_data
            (idx)]


@overload(operator.setitem, no_unliteral=True)
def overload_series_setitem(S, idx, val):
    if isinstance(S, SeriesType):
        if S.dtype == bodo.string_type and val is not types.none and not (
            is_list_like_index_type(idx) and idx.dtype == types.bool_):
            raise BodoError('Series string setitem not supported yet')
        elif S.dtype == bodo.bytes_type:
            raise BodoError('Series binary setitem not supported yet')
        if isinstance(idx, types.Integer):
            if isinstance(S.index, NumericIndexType) and isinstance(S.index
                .dtype, types.Integer):
                raise BodoError(
                    'Indexing Series with Integer index using [] (which is label-based) not supported yet'
                    )
            if S.dtype == types.NPDatetime('ns'
                ) and val == pd_timestamp_tz_naive_type:

                def impl_dt(S, idx, val):
                    s = integer_to_dt64(val.value)
                    bodo.hiframes.pd_series_ext.get_series_data(S)[idx] = s
                return impl_dt
            if S.dtype == types.NPTimedelta('ns'
                ) and val == datetime_timedelta_type:

                def impl_dt(S, idx, val):
                    phq__arsvb = (bodo.hiframes.datetime_timedelta_ext.
                        _to_nanoseconds(val))
                    s = bodo.hiframes.pd_timestamp_ext.integer_to_timedelta64(
                        phq__arsvb)
                    bodo.hiframes.pd_series_ext.get_series_data(S)[idx] = s
                return impl_dt
            if S.dtype == types.NPTimedelta('ns') and val == pd_timedelta_type:

                def impl_dt(S, idx, val):
                    phq__arsvb = val.value
                    s = bodo.hiframes.pd_timestamp_ext.integer_to_timedelta64(
                        phq__arsvb)
                    bodo.hiframes.pd_series_ext.get_series_data(S)[idx] = s
                return impl_dt

            def impl(S, idx, val):
                bodo.hiframes.pd_series_ext.get_series_data(S)[idx] = val
            return impl
        if isinstance(idx, types.SliceType):

            def impl_slice(S, idx, val):
                bodo.hiframes.pd_series_ext.get_series_data(S)[idx
                    ] = bodo.utils.conversion.coerce_to_array(val, False)
            return impl_slice
        if is_list_like_index_type(idx) and isinstance(idx.dtype, (types.
            Integer, types.Boolean)):
            if isinstance(S.index, NumericIndexType) and isinstance(S.index
                .dtype, types.Integer) and isinstance(idx.dtype, types.Integer
                ):
                raise BodoError(
                    'Indexing Series with Integer index using [] (which is label-based) not supported yet'
                    )

            def impl_arr(S, idx, val):
                wtfis__drqis = bodo.utils.conversion.coerce_to_array(idx)
                bodo.hiframes.pd_series_ext.get_series_data(S)[wtfis__drqis
                    ] = bodo.utils.conversion.coerce_to_array(val, False)
            return impl_arr
        raise BodoError(f'Series [] setitem using {idx} not supported yet')


@overload(operator.setitem, no_unliteral=True)
def overload_array_list_setitem(A, idx, val):
    if isinstance(A, types.Array) and isinstance(idx, (types.List, SeriesType)
        ):

        def impl(A, idx, val):
            A[bodo.utils.conversion.coerce_to_array(idx)] = val
        return impl


@overload(operator.getitem, no_unliteral=True)
def overload_const_index_series_getitem(S, idx):
    if isinstance(S, (SeriesType, HeterogeneousSeriesType)) and isinstance(S
        .index, HeterogeneousIndexType) and is_overload_constant_tuple(S.
        index.data):
        xevkb__cbpk = get_overload_const_tuple(S.index.data)
        if isinstance(idx, types.Integer) and not any(isinstance(mda__oakug,
            int) for mda__oakug in xevkb__cbpk):
            return lambda S, idx: bodo.hiframes.pd_series_ext.get_series_data(S
                )[idx]
        if is_literal_type(idx):
            jkwyk__ioy = get_literal_value(idx)
            if jkwyk__ioy not in xevkb__cbpk:
                raise_bodo_error(
                    f"Series label-based getitem: '{jkwyk__ioy}' not in {xevkb__cbpk}"
                    )
            arr_ind = xevkb__cbpk.index(jkwyk__ioy)
            return lambda S, idx: bodo.hiframes.pd_series_ext.get_series_data(S
                )[arr_ind]


@lower_cast(SeriesIatType, SeriesIatType)
@lower_cast(SeriesIlocType, SeriesIlocType)
@lower_cast(SeriesLocType, SeriesLocType)
def cast_series_iat(context, builder, fromty, toty, val):
    zfwy__lpr = cgutils.create_struct_proxy(fromty)(context, builder, val)
    zlhgr__trfrj = context.cast(builder, zfwy__lpr.obj, fromty.stype, toty.
        stype)
    avikk__fjc = cgutils.create_struct_proxy(toty)(context, builder)
    avikk__fjc.obj = zlhgr__trfrj
    return avikk__fjc._getvalue()
