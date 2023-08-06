"""
Implementation of DataFrame attributes and methods using overload.
"""
import operator
import re
import warnings
from collections import namedtuple
from typing import Tuple
import numba
import numpy as np
import pandas as pd
from numba.core import cgutils, ir, types
from numba.core.imputils import RefType, impl_ret_borrowed, impl_ret_new_ref, iternext_impl, lower_builtin
from numba.core.ir_utils import mk_unique_var, next_label
from numba.core.typing import signature
from numba.core.typing.templates import AbstractTemplate, infer_global
from numba.extending import lower_getattr, models, overload, overload_attribute, overload_method, register_model, type_callable
import bodo
from bodo.hiframes.datetime_date_ext import datetime_date_array_type
from bodo.hiframes.datetime_timedelta_ext import _no_input, datetime_timedelta_array_type
from bodo.hiframes.pd_categorical_ext import CategoricalArrayType
from bodo.hiframes.pd_dataframe_ext import DataFrameType, check_runtime_cols_unsupported, handle_inplace_df_type_change
from bodo.hiframes.pd_index_ext import DatetimeIndexType, RangeIndexType, StringIndexType, is_pd_index_type
from bodo.hiframes.pd_multi_index_ext import MultiIndexType
from bodo.hiframes.pd_series_ext import SeriesType, if_series_to_array_type
from bodo.hiframes.pd_timestamp_ext import pd_timestamp_tz_naive_type
from bodo.hiframes.rolling import is_supported_shift_array_type
from bodo.hiframes.split_impl import string_array_split_view_type
from bodo.hiframes.time_ext import TimeArrayType
from bodo.libs.array_item_arr_ext import ArrayItemArrayType
from bodo.libs.binary_arr_ext import binary_array_type
from bodo.libs.bool_arr_ext import BooleanArrayType, boolean_array
from bodo.libs.decimal_arr_ext import DecimalArrayType
from bodo.libs.dict_arr_ext import dict_str_arr_type
from bodo.libs.float_arr_ext import FloatingArrayType
from bodo.libs.int_arr_ext import IntegerArrayType
from bodo.libs.interval_arr_ext import IntervalArrayType
from bodo.libs.map_arr_ext import MapArrayType
from bodo.libs.str_arr_ext import string_array_type
from bodo.libs.str_ext import string_type
from bodo.libs.struct_arr_ext import StructArrayType
from bodo.utils import tracing
from bodo.utils.transform import bodo_types_with_params, gen_const_tup, no_side_effect_call_tuples
from bodo.utils.typing import BodoError, BodoWarning, ColNamesMetaType, check_unsupported_args, dtype_to_array_type, ensure_constant_arg, ensure_constant_values, get_castable_arr_dtype, get_index_data_arr_types, get_index_names, get_literal_value, get_nullable_and_non_nullable_types, get_overload_const_bool, get_overload_const_int, get_overload_const_list, get_overload_const_str, get_overload_const_tuple, get_overload_constant_dict, get_overload_constant_series, is_common_scalar_dtype, is_literal_type, is_overload_bool, is_overload_bool_list, is_overload_constant_bool, is_overload_constant_dict, is_overload_constant_int, is_overload_constant_list, is_overload_constant_series, is_overload_constant_str, is_overload_constant_tuple, is_overload_false, is_overload_int, is_overload_none, is_overload_true, is_overload_zero, is_scalar_type, parse_dtype, raise_bodo_error, unliteral_val
from bodo.utils.utils import is_array_typ


@overload_attribute(DataFrameType, 'index', inline='always')
def overload_dataframe_index(df):
    return lambda df: bodo.hiframes.pd_dataframe_ext.get_dataframe_index(df)


def generate_col_to_index_func_text(col_names: Tuple):
    if all(isinstance(a, str) for a in col_names) or all(isinstance(a,
        bytes) for a in col_names):
        artza__jtett = f'bodo.utils.conversion.coerce_to_array({col_names})'
        return (
            f'bodo.hiframes.pd_index_ext.init_binary_str_index({artza__jtett})\n'
            )
    elif all(isinstance(a, (int, float)) for a in col_names):
        arr = f'bodo.utils.conversion.coerce_to_array({col_names})'
        return f'bodo.hiframes.pd_index_ext.init_numeric_index({arr})\n'
    else:
        return f'bodo.hiframes.pd_index_ext.init_heter_index({col_names})\n'


@overload_attribute(DataFrameType, 'columns', inline='always')
def overload_dataframe_columns(df):
    ilzk__soby = 'def impl(df):\n'
    if df.has_runtime_cols:
        ilzk__soby += (
            '  return bodo.hiframes.pd_dataframe_ext.get_dataframe_column_names(df)\n'
            )
    else:
        lnjos__ktsgc = (bodo.hiframes.dataframe_impl.
            generate_col_to_index_func_text(df.columns))
        ilzk__soby += f'  return {lnjos__ktsgc}'
    lxd__swvja = {}
    exec(ilzk__soby, {'bodo': bodo}, lxd__swvja)
    impl = lxd__swvja['impl']
    return impl


@overload_attribute(DataFrameType, 'values')
def overload_dataframe_values(df):
    check_runtime_cols_unsupported(df, 'DataFrame.values')
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(df,
        'DataFrame.values')
    if not is_df_values_numpy_supported_dftyp(df):
        raise_bodo_error(
            'DataFrame.values: only supported for dataframes containing numeric values'
            )
    vzoky__jjk = len(df.columns)
    lccqi__ivgj = set(i for i in range(vzoky__jjk) if isinstance(df.data[i],
        IntegerArrayType))
    data_args = ', '.join(
        'bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {}){}'.
        format(i, '.astype(float)' if i in lccqi__ivgj else '') for i in
        range(vzoky__jjk))
    ilzk__soby = 'def f(df):\n'.format()
    ilzk__soby += '    return np.stack(({},), 1)\n'.format(data_args)
    lxd__swvja = {}
    exec(ilzk__soby, {'bodo': bodo, 'np': np}, lxd__swvja)
    eksj__hjlk = lxd__swvja['f']
    return eksj__hjlk


@overload_method(DataFrameType, 'to_numpy', inline='always', no_unliteral=True)
def overload_dataframe_to_numpy(df, dtype=None, copy=False, na_value=_no_input
    ):
    check_runtime_cols_unsupported(df, 'DataFrame.to_numpy()')
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(df,
        'DataFrame.to_numpy()')
    if not is_df_values_numpy_supported_dftyp(df):
        raise_bodo_error(
            'DataFrame.to_numpy(): only supported for dataframes containing numeric values'
            )
    wdxk__vydem = {'dtype': dtype, 'na_value': na_value}
    jyskm__yjr = {'dtype': None, 'na_value': _no_input}
    check_unsupported_args('DataFrame.to_numpy', wdxk__vydem, jyskm__yjr,
        package_name='pandas', module_name='DataFrame')

    def impl(df, dtype=None, copy=False, na_value=_no_input):
        return df.values
    return impl


@overload_attribute(DataFrameType, 'ndim', inline='always')
def overload_dataframe_ndim(df):
    return lambda df: 2


@overload_attribute(DataFrameType, 'size')
def overload_dataframe_size(df):
    if df.has_runtime_cols:

        def impl(df):
            t = bodo.hiframes.pd_dataframe_ext.get_dataframe_table(df)
            jkh__dtx = bodo.hiframes.table.compute_num_runtime_columns(t)
            return jkh__dtx * len(t)
        return impl
    ncols = len(df.columns)
    return lambda df: ncols * len(df)


@lower_getattr(DataFrameType, 'shape')
def lower_dataframe_shape(context, builder, typ, val):
    impl = overload_dataframe_shape(typ)
    return context.compile_internal(builder, impl, types.Tuple([types.int64,
        types.int64])(typ), (val,))


def overload_dataframe_shape(df):
    if df.has_runtime_cols:

        def impl(df):
            t = bodo.hiframes.pd_dataframe_ext.get_dataframe_table(df)
            jkh__dtx = bodo.hiframes.table.compute_num_runtime_columns(t)
            return len(t), jkh__dtx
        return impl
    ncols = len(df.columns)
    return lambda df: (len(df), ncols)


@overload_attribute(DataFrameType, 'dtypes')
def overload_dataframe_dtypes(df):
    check_runtime_cols_unsupported(df, 'DataFrame.dtypes')
    ilzk__soby = 'def impl(df):\n'
    data = ', '.join(
        f'bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {i}).dtype\n'
         for i in range(len(df.columns)))
    qtbw__rqvma = ',' if len(df.columns) == 1 else ''
    index = f'bodo.hiframes.pd_index_ext.init_heter_index({df.columns})'
    ilzk__soby += f"""  return bodo.hiframes.pd_series_ext.init_series(({data}{qtbw__rqvma}), {index}, None)
"""
    lxd__swvja = {}
    exec(ilzk__soby, {'bodo': bodo}, lxd__swvja)
    impl = lxd__swvja['impl']
    return impl


@overload_attribute(DataFrameType, 'empty')
def overload_dataframe_empty(df):
    check_runtime_cols_unsupported(df, 'DataFrame.empty')
    if len(df.columns) == 0:
        return lambda df: True
    return lambda df: len(df) == 0


@overload_method(DataFrameType, 'assign', no_unliteral=True)
def overload_dataframe_assign(df, **kwargs):
    check_runtime_cols_unsupported(df, 'DataFrame.assign()')
    raise_bodo_error('Invalid df.assign() call')


@overload_method(DataFrameType, 'insert', no_unliteral=True)
def overload_dataframe_insert(df, loc, column, value, allow_duplicates=False):
    check_runtime_cols_unsupported(df, 'DataFrame.insert()')
    raise_bodo_error('Invalid df.insert() call')


def _get_dtype_str(dtype):
    if isinstance(dtype, types.Function):
        if dtype.key[0] == str:
            return "'str'"
        elif dtype.key[0] == float:
            return 'float'
        elif dtype.key[0] == int:
            return 'int'
        elif dtype.key[0] == bool:
            return 'bool'
        else:
            raise BodoError(f'invalid dtype: {dtype}')
    if type(dtype) in bodo.libs.int_arr_ext.pd_int_dtype_classes:
        return dtype.name
    if isinstance(dtype, types.DTypeSpec):
        dtype = dtype.dtype
    if isinstance(dtype, types.functions.NumberClass):
        return f"'{dtype.key}'"
    if isinstance(dtype, types.PyObject) or dtype in (object, 'object'):
        return "'object'"
    if dtype in (bodo.libs.str_arr_ext.string_dtype, pd.StringDtype()):
        return 'str'
    return f"'{dtype}'"


@overload_method(DataFrameType, 'astype', inline='always', no_unliteral=True)
def overload_dataframe_astype(df, dtype, copy=True, errors='raise',
    _bodo_nan_to_str=True, _bodo_object_typeref=None):
    check_runtime_cols_unsupported(df, 'DataFrame.astype()')
    wdxk__vydem = {'errors': errors}
    jyskm__yjr = {'errors': 'raise'}
    check_unsupported_args('df.astype', wdxk__vydem, jyskm__yjr,
        package_name='pandas', module_name='DataFrame')
    if dtype == types.unicode_type:
        raise_bodo_error(
            "DataFrame.astype(): 'dtype' when passed as string must be a constant value"
            )
    if not is_overload_bool(copy):
        raise BodoError("DataFrame.astype(): 'copy' must be a boolean value")
    extra_globals = None
    header = """def impl(df, dtype, copy=True, errors='raise', _bodo_nan_to_str=True, _bodo_object_typeref=None):
"""
    if df.is_table_format:
        extra_globals = {}
        header += (
            '  table = bodo.hiframes.pd_dataframe_ext.get_dataframe_table(df)\n'
            )
        hindk__prc = []
    if _bodo_object_typeref is not None:
        assert isinstance(_bodo_object_typeref, types.TypeRef
            ), 'Bodo schema used in DataFrame.astype should be a TypeRef'
        bzv__wjhu = _bodo_object_typeref.instance_type
        assert isinstance(bzv__wjhu, DataFrameType
            ), 'Bodo schema used in DataFrame.astype is only supported for DataFrame schemas'
        if df.is_table_format:
            for i, name in enumerate(df.columns):
                if name in bzv__wjhu.column_index:
                    idx = bzv__wjhu.column_index[name]
                    arr_typ = bzv__wjhu.data[idx]
                else:
                    arr_typ = df.data[i]
                hindk__prc.append(arr_typ)
        else:
            extra_globals = {}
            uihvz__vxi = {}
            for i, name in enumerate(bzv__wjhu.columns):
                arr_typ = bzv__wjhu.data[i]
                extra_globals[f'_bodo_schema{i}'] = get_castable_arr_dtype(
                    arr_typ)
                uihvz__vxi[name] = f'_bodo_schema{i}'
            data_args = ', '.join(
                f'bodo.utils.conversion.fix_arr_dtype(bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {i}), {uihvz__vxi[kxm__lejo]}, copy, nan_to_str=_bodo_nan_to_str, from_series=True)'
                 if kxm__lejo in uihvz__vxi else
                f'bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {i})'
                 for i, kxm__lejo in enumerate(df.columns))
    elif is_overload_constant_dict(dtype) or is_overload_constant_series(dtype
        ):
        fud__wrrz = get_overload_constant_dict(dtype
            ) if is_overload_constant_dict(dtype) else dict(
            get_overload_constant_series(dtype))
        if df.is_table_format:
            fud__wrrz = {name: dtype_to_array_type(parse_dtype(dtype)) for 
                name, dtype in fud__wrrz.items()}
            for i, name in enumerate(df.columns):
                if name in fud__wrrz:
                    arr_typ = fud__wrrz[name]
                else:
                    arr_typ = df.data[i]
                hindk__prc.append(arr_typ)
        else:
            data_args = ', '.join(
                f'bodo.utils.conversion.fix_arr_dtype(bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {i}), {_get_dtype_str(fud__wrrz[kxm__lejo])}, copy, nan_to_str=_bodo_nan_to_str, from_series=True)'
                 if kxm__lejo in fud__wrrz else
                f'bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {i})'
                 for i, kxm__lejo in enumerate(df.columns))
    elif df.is_table_format:
        arr_typ = dtype_to_array_type(parse_dtype(dtype))
        hindk__prc = [arr_typ] * len(df.columns)
    else:
        data_args = ', '.join(
            f'bodo.utils.conversion.fix_arr_dtype(bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {i}), dtype, copy, nan_to_str=_bodo_nan_to_str, from_series=True)'
             for i in range(len(df.columns)))
    if df.is_table_format:
        iboag__twheu = bodo.TableType(tuple(hindk__prc))
        extra_globals['out_table_typ'] = iboag__twheu
        data_args = (
            'bodo.utils.table_utils.table_astype(table, out_table_typ, copy, _bodo_nan_to_str)'
            )
    return _gen_init_df(header, df.columns, data_args, extra_globals=
        extra_globals)


@overload_method(DataFrameType, 'copy', inline='always', no_unliteral=True)
def overload_dataframe_copy(df, deep=True):
    check_runtime_cols_unsupported(df, 'DataFrame.copy()')
    header = 'def impl(df, deep=True):\n'
    extra_globals = None
    if df.is_table_format:
        header += (
            '  table = bodo.hiframes.pd_dataframe_ext.get_dataframe_table(df)\n'
            )
        jdcz__mjxw = types.none
        extra_globals = {'output_arr_typ': jdcz__mjxw}
        if is_overload_false(deep):
            data_args = (
                'bodo.utils.table_utils.generate_mappable_table_func(' +
                'table, ' + 'None, ' + 'output_arr_typ, ' + 'True)')
        elif is_overload_true(deep):
            data_args = (
                'bodo.utils.table_utils.generate_mappable_table_func(' +
                'table, ' + "'copy', " + 'output_arr_typ, ' + 'True)')
        else:
            data_args = (
                'bodo.utils.table_utils.generate_mappable_table_func(' +
                'table, ' + "'copy', " + 'output_arr_typ, ' +
                'True) if deep else bodo.utils.table_utils.generate_mappable_table_func('
                 + 'table, ' + 'None, ' + 'output_arr_typ, ' + 'True)')
    else:
        qdw__gjrdj = []
        for i in range(len(df.columns)):
            arr = f'bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {i})'
            if is_overload_true(deep):
                qdw__gjrdj.append(arr + '.copy()')
            elif is_overload_false(deep):
                qdw__gjrdj.append(arr)
            else:
                qdw__gjrdj.append(f'{arr}.copy() if deep else {arr}')
        data_args = ', '.join(qdw__gjrdj)
    return _gen_init_df(header, df.columns, data_args, extra_globals=
        extra_globals)


@overload_method(DataFrameType, 'rename', inline='always', no_unliteral=True)
def overload_dataframe_rename(df, mapper=None, index=None, columns=None,
    axis=None, copy=True, inplace=False, level=None, errors='ignore',
    _bodo_transformed=False):
    check_runtime_cols_unsupported(df, 'DataFrame.rename()')
    handle_inplace_df_type_change(inplace, _bodo_transformed, 'rename')
    wdxk__vydem = {'index': index, 'level': level, 'errors': errors}
    jyskm__yjr = {'index': None, 'level': None, 'errors': 'ignore'}
    check_unsupported_args('DataFrame.rename', wdxk__vydem, jyskm__yjr,
        package_name='pandas', module_name='DataFrame')
    if not is_overload_constant_bool(inplace):
        raise BodoError(
            "DataFrame.rename(): 'inplace' keyword only supports boolean constant assignment"
            )
    if not is_overload_none(mapper):
        if not is_overload_none(columns):
            raise BodoError(
                "DataFrame.rename(): Cannot specify both 'mapper' and 'columns'"
                )
        if not (is_overload_constant_int(axis) and get_overload_const_int(
            axis) == 1):
            raise BodoError(
                "DataFrame.rename(): 'mapper' only supported with axis=1")
        if not is_overload_constant_dict(mapper):
            raise_bodo_error(
                "'mapper' argument to DataFrame.rename() should be a constant dictionary"
                )
        cvdjg__zik = get_overload_constant_dict(mapper)
    elif not is_overload_none(columns):
        if not is_overload_none(axis):
            raise BodoError(
                "DataFrame.rename(): Cannot specify both 'axis' and 'columns'")
        if not is_overload_constant_dict(columns):
            raise_bodo_error(
                "'columns' argument to DataFrame.rename() should be a constant dictionary"
                )
        cvdjg__zik = get_overload_constant_dict(columns)
    else:
        raise_bodo_error(
            "DataFrame.rename(): must pass columns either via 'mapper' and 'axis'=1 or 'columns'"
            )
    etku__hunb = tuple([cvdjg__zik.get(df.columns[i], df.columns[i]) for i in
        range(len(df.columns))])
    header = """def impl(df, mapper=None, index=None, columns=None, axis=None, copy=True, inplace=False, level=None, errors='ignore', _bodo_transformed=False):
"""
    extra_globals = None
    ipy__unq = None
    if df.is_table_format:
        header += (
            '  table = bodo.hiframes.pd_dataframe_ext.get_dataframe_table(df)\n'
            )
        ipy__unq = df.copy(columns=etku__hunb)
        jdcz__mjxw = types.none
        extra_globals = {'output_arr_typ': jdcz__mjxw}
        if is_overload_false(copy):
            data_args = (
                'bodo.utils.table_utils.generate_mappable_table_func(' +
                'table, ' + 'None, ' + 'output_arr_typ, ' + 'True)')
        elif is_overload_true(copy):
            data_args = (
                'bodo.utils.table_utils.generate_mappable_table_func(' +
                'table, ' + "'copy', " + 'output_arr_typ, ' + 'True)')
        else:
            data_args = (
                'bodo.utils.table_utils.generate_mappable_table_func(' +
                'table, ' + "'copy', " + 'output_arr_typ, ' +
                'True) if copy else bodo.utils.table_utils.generate_mappable_table_func('
                 + 'table, ' + 'None, ' + 'output_arr_typ, ' + 'True)')
    else:
        qdw__gjrdj = []
        for i in range(len(df.columns)):
            arr = f'bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {i})'
            if is_overload_true(copy):
                qdw__gjrdj.append(arr + '.copy()')
            elif is_overload_false(copy):
                qdw__gjrdj.append(arr)
            else:
                qdw__gjrdj.append(f'{arr}.copy() if copy else {arr}')
        data_args = ', '.join(qdw__gjrdj)
    return _gen_init_df(header, etku__hunb, data_args, extra_globals=
        extra_globals)


@overload_method(DataFrameType, 'filter', no_unliteral=True)
def overload_dataframe_filter(df, items=None, like=None, regex=None, axis=None
    ):
    check_runtime_cols_unsupported(df, 'DataFrame.filter()')
    rzhhj__jhnb = not is_overload_none(items)
    bycc__wejh = not is_overload_none(like)
    blsp__cjlqi = not is_overload_none(regex)
    fmkqt__dgtxi = rzhhj__jhnb ^ bycc__wejh ^ blsp__cjlqi
    bedu__kep = not (rzhhj__jhnb or bycc__wejh or blsp__cjlqi)
    if bedu__kep:
        raise BodoError(
            'DataFrame.filter(): one of keyword arguments `items`, `like`, and `regex` must be supplied'
            )
    if not fmkqt__dgtxi:
        raise BodoError(
            'DataFrame.filter(): keyword arguments `items`, `like`, and `regex` are mutually exclusive'
            )
    if is_overload_none(axis):
        axis = 'columns'
    if is_overload_constant_str(axis):
        axis = get_overload_const_str(axis)
        if axis not in {'index', 'columns'}:
            raise_bodo_error(
                'DataFrame.filter(): keyword arguments `axis` must be either "index" or "columns" if string'
                )
        odbux__smu = 0 if axis == 'index' else 1
    elif is_overload_constant_int(axis):
        axis = get_overload_const_int(axis)
        if axis not in {0, 1}:
            raise_bodo_error(
                'DataFrame.filter(): keyword arguments `axis` must be either 0 or 1 if integer'
                )
        odbux__smu = axis
    else:
        raise_bodo_error(
            'DataFrame.filter(): keyword arguments `axis` must be constant string or integer'
            )
    assert odbux__smu in {0, 1}
    ilzk__soby = (
        'def impl(df, items=None, like=None, regex=None, axis=None):\n')
    if odbux__smu == 0:
        raise BodoError(
            'DataFrame.filter(): filtering based on index is not supported.')
    if odbux__smu == 1:
        mbo__yyy = []
        sgn__nsott = []
        lhkdh__hsy = []
        if rzhhj__jhnb:
            if is_overload_constant_list(items):
                runcu__pbib = get_overload_const_list(items)
            else:
                raise BodoError(
                    "Dataframe.filter(): argument 'items' must be a list of constant strings."
                    )
        if bycc__wejh:
            if is_overload_constant_str(like):
                nrbrn__lop = get_overload_const_str(like)
            else:
                raise BodoError(
                    "Dataframe.filter(): argument 'like' must be a constant string."
                    )
        if blsp__cjlqi:
            if is_overload_constant_str(regex):
                gqklh__dgh = get_overload_const_str(regex)
                sbi__qrkv = re.compile(gqklh__dgh)
            else:
                raise BodoError(
                    "Dataframe.filter(): argument 'regex' must be a constant string."
                    )
        for i, kxm__lejo in enumerate(df.columns):
            if not is_overload_none(items
                ) and kxm__lejo in runcu__pbib or not is_overload_none(like
                ) and nrbrn__lop in str(kxm__lejo) or not is_overload_none(
                regex) and sbi__qrkv.search(str(kxm__lejo)):
                sgn__nsott.append(kxm__lejo)
                lhkdh__hsy.append(i)
        for i in lhkdh__hsy:
            var_name = f'data_{i}'
            mbo__yyy.append(var_name)
            ilzk__soby += f"""  {var_name} = bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {i})
"""
        data_args = ', '.join(mbo__yyy)
        return _gen_init_df(ilzk__soby, sgn__nsott, data_args)


@overload_method(DataFrameType, 'isna', inline='always', no_unliteral=True)
@overload_method(DataFrameType, 'isnull', inline='always', no_unliteral=True)
def overload_dataframe_isna(df):
    check_runtime_cols_unsupported(df, 'DataFrame.isna()')
    header = 'def impl(df):\n'
    extra_globals = None
    ipy__unq = None
    if df.is_table_format:
        jdcz__mjxw = types.Array(types.bool_, 1, 'C')
        ipy__unq = DataFrameType(tuple([jdcz__mjxw] * len(df.data)), df.
            index, df.columns, df.dist, is_table_format=True)
        extra_globals = {'output_arr_typ': jdcz__mjxw}
        data_args = ('bodo.utils.table_utils.generate_mappable_table_func(' +
            'bodo.hiframes.pd_dataframe_ext.get_dataframe_table(df), ' +
            "'bodo.libs.array_ops.array_op_isna', " + 'output_arr_typ, ' +
            'False)')
    else:
        data_args = ', '.join(
            f'bodo.libs.array_ops.array_op_isna(bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {i}))'
             for i in range(len(df.columns)))
    return _gen_init_df(header, df.columns, data_args, extra_globals=
        extra_globals)


@overload_method(DataFrameType, 'select_dtypes', inline='always',
    no_unliteral=True)
def overload_dataframe_select_dtypes(df, include=None, exclude=None):
    check_runtime_cols_unsupported(df, 'DataFrame.select_dtypes')
    qakvs__mar = is_overload_none(include)
    czfc__jzk = is_overload_none(exclude)
    mlk__dakt = 'DataFrame.select_dtypes'
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(df,
        'DataFrame.select_dtypes()')
    if qakvs__mar and czfc__jzk:
        raise_bodo_error(
            'DataFrame.select_dtypes() At least one of include or exclude must not be none'
            )

    def is_legal_input(elem):
        return is_overload_constant_str(elem) or isinstance(elem, types.
            DTypeSpec) or isinstance(elem, types.Function)
    if not qakvs__mar:
        if is_overload_constant_list(include):
            include = get_overload_const_list(include)
            ohfbj__gad = [dtype_to_array_type(parse_dtype(elem, mlk__dakt)) for
                elem in include]
        elif is_legal_input(include):
            ohfbj__gad = [dtype_to_array_type(parse_dtype(include, mlk__dakt))]
        else:
            raise_bodo_error(
                'DataFrame.select_dtypes() only supports constant strings or types as arguments'
                )
        ohfbj__gad = get_nullable_and_non_nullable_types(ohfbj__gad)
        dpee__mlln = tuple(kxm__lejo for i, kxm__lejo in enumerate(df.
            columns) if df.data[i] in ohfbj__gad)
    else:
        dpee__mlln = df.columns
    if not czfc__jzk:
        if is_overload_constant_list(exclude):
            exclude = get_overload_const_list(exclude)
            lepup__cgqr = [dtype_to_array_type(parse_dtype(elem, mlk__dakt)
                ) for elem in exclude]
        elif is_legal_input(exclude):
            lepup__cgqr = [dtype_to_array_type(parse_dtype(exclude, mlk__dakt))
                ]
        else:
            raise_bodo_error(
                'DataFrame.select_dtypes() only supports constant strings or types as arguments'
                )
        lepup__cgqr = get_nullable_and_non_nullable_types(lepup__cgqr)
        dpee__mlln = tuple(kxm__lejo for kxm__lejo in dpee__mlln if df.data
            [df.column_index[kxm__lejo]] not in lepup__cgqr)
    data_args = ', '.join(
        f'bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {df.column_index[kxm__lejo]})'
         for kxm__lejo in dpee__mlln)
    header = 'def impl(df, include=None, exclude=None):\n'
    return _gen_init_df(header, dpee__mlln, data_args)


@overload_method(DataFrameType, 'notna', inline='always', no_unliteral=True)
@overload_method(DataFrameType, 'notnull', inline='always', no_unliteral=True)
def overload_dataframe_notna(df):
    check_runtime_cols_unsupported(df, 'DataFrame.notna()')
    header = 'def impl(df):\n'
    extra_globals = None
    ipy__unq = None
    if df.is_table_format:
        jdcz__mjxw = types.Array(types.bool_, 1, 'C')
        ipy__unq = DataFrameType(tuple([jdcz__mjxw] * len(df.data)), df.
            index, df.columns, df.dist, is_table_format=True)
        extra_globals = {'output_arr_typ': jdcz__mjxw}
        data_args = ('bodo.utils.table_utils.generate_mappable_table_func(' +
            'bodo.hiframes.pd_dataframe_ext.get_dataframe_table(df), ' +
            "'~bodo.libs.array_ops.array_op_isna', " + 'output_arr_typ, ' +
            'False)')
    else:
        data_args = ', '.join(
            f'bodo.libs.array_ops.array_op_isna(bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {i})) == False'
             for i in range(len(df.columns)))
    return _gen_init_df(header, df.columns, data_args, extra_globals=
        extra_globals)


def overload_dataframe_head(df, n=5):
    if df.is_table_format:
        data_args = (
            'bodo.hiframes.pd_dataframe_ext.get_dataframe_table(df)[:n]')
    else:
        data_args = ', '.join(
            f'bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {i})[:n]'
             for i in range(len(df.columns)))
    header = 'def impl(df, n=5):\n'
    index = 'bodo.hiframes.pd_dataframe_ext.get_dataframe_index(df)[:n]'
    return _gen_init_df(header, df.columns, data_args, index)


@lower_builtin('df.head', DataFrameType, types.Integer)
@lower_builtin('df.head', DataFrameType, types.Omitted)
def dataframe_head_lower(context, builder, sig, args):
    impl = overload_dataframe_head(*sig.args)
    return context.compile_internal(builder, impl, sig, args)


@overload_method(DataFrameType, 'tail', inline='always', no_unliteral=True)
def overload_dataframe_tail(df, n=5):
    check_runtime_cols_unsupported(df, 'DataFrame.tail()')
    if not is_overload_int(n):
        raise BodoError("Dataframe.tail(): 'n' must be an Integer")
    if df.is_table_format:
        data_args = (
            'bodo.hiframes.pd_dataframe_ext.get_dataframe_table(df)[m:]')
    else:
        data_args = ', '.join(
            f'bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {i})[m:]'
             for i in range(len(df.columns)))
    header = 'def impl(df, n=5):\n'
    header += '  m = bodo.hiframes.series_impl.tail_slice(len(df), n)\n'
    index = 'bodo.hiframes.pd_dataframe_ext.get_dataframe_index(df)[m:]'
    return _gen_init_df(header, df.columns, data_args, index)


@overload_method(DataFrameType, 'first', inline='always', no_unliteral=True)
def overload_dataframe_first(df, offset):
    check_runtime_cols_unsupported(df, 'DataFrame.first()')
    dkz__tfdp = (types.unicode_type, bodo.month_begin_type, bodo.
        month_end_type, bodo.week_type, bodo.date_offset_type)
    if not isinstance(df.index, DatetimeIndexType):
        raise BodoError(
            'DataFrame.first(): only supports a DatetimeIndex index')
    if types.unliteral(offset) not in dkz__tfdp:
        raise BodoError(
            "DataFrame.first(): 'offset' must be an string or DateOffset")
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(df,
        'DataFrame.first()')
    index = (
        'bodo.hiframes.pd_dataframe_ext.get_dataframe_index(df)[:valid_entries]'
        )
    data_args = ', '.join(
        f'bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {i})[:valid_entries]'
         for i in range(len(df.columns)))
    header = 'def impl(df, offset):\n'
    header += (
        '  df_index = bodo.hiframes.pd_dataframe_ext.get_dataframe_index(df)\n'
        )
    header += '  if len(df_index):\n'
    header += '    start_date = df_index[0]\n'
    header += """    valid_entries = bodo.libs.array_kernels.get_valid_entries_from_date_offset(df_index, offset, start_date, False)
"""
    header += '  else:\n'
    header += '    valid_entries = 0\n'
    return _gen_init_df(header, df.columns, data_args, index)


@overload_method(DataFrameType, 'last', inline='always', no_unliteral=True)
def overload_dataframe_last(df, offset):
    check_runtime_cols_unsupported(df, 'DataFrame.last()')
    dkz__tfdp = (types.unicode_type, bodo.month_begin_type, bodo.
        month_end_type, bodo.week_type, bodo.date_offset_type)
    if not isinstance(df.index, DatetimeIndexType):
        raise BodoError('DataFrame.last(): only supports a DatetimeIndex index'
            )
    if types.unliteral(offset) not in dkz__tfdp:
        raise BodoError(
            "DataFrame.last(): 'offset' must be an string or DateOffset")
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(df,
        'DataFrame.last()')
    index = (
        'bodo.hiframes.pd_dataframe_ext.get_dataframe_index(df)[len(df)-valid_entries:]'
        )
    data_args = ', '.join(
        f'bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {i})[len(df)-valid_entries:]'
         for i in range(len(df.columns)))
    header = 'def impl(df, offset):\n'
    header += (
        '  df_index = bodo.hiframes.pd_dataframe_ext.get_dataframe_index(df)\n'
        )
    header += '  if len(df_index):\n'
    header += '    final_date = df_index[-1]\n'
    header += """    valid_entries = bodo.libs.array_kernels.get_valid_entries_from_date_offset(df_index, offset, final_date, True)
"""
    header += '  else:\n'
    header += '    valid_entries = 0\n'
    return _gen_init_df(header, df.columns, data_args, index)


@overload_method(DataFrameType, 'to_string', no_unliteral=True)
def to_string_overload(df, buf=None, columns=None, col_space=None, header=
    True, index=True, na_rep='NaN', formatters=None, float_format=None,
    sparsify=None, index_names=True, justify=None, max_rows=None, min_rows=
    None, max_cols=None, show_dimensions=False, decimal='.', line_width=
    None, max_colwidth=None, encoding=None):
    check_runtime_cols_unsupported(df, 'DataFrame.to_string()')

    def impl(df, buf=None, columns=None, col_space=None, header=True, index
        =True, na_rep='NaN', formatters=None, float_format=None, sparsify=
        None, index_names=True, justify=None, max_rows=None, min_rows=None,
        max_cols=None, show_dimensions=False, decimal='.', line_width=None,
        max_colwidth=None, encoding=None):
        with numba.objmode(res='string'):
            res = df.to_string(buf=buf, columns=columns, col_space=
                col_space, header=header, index=index, na_rep=na_rep,
                formatters=formatters, float_format=float_format, sparsify=
                sparsify, index_names=index_names, justify=justify,
                max_rows=max_rows, min_rows=min_rows, max_cols=max_cols,
                show_dimensions=show_dimensions, decimal=decimal,
                line_width=line_width, max_colwidth=max_colwidth, encoding=
                encoding)
        return res
    return impl


@overload_method(DataFrameType, 'isin', inline='always', no_unliteral=True)
def overload_dataframe_isin(df, values):
    check_runtime_cols_unsupported(df, 'DataFrame.isin()')
    from bodo.utils.typing import is_iterable_type
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(df,
        'DataFrame.isin()')
    ilzk__soby = 'def impl(df, values):\n'
    ltxbx__kvvh = {}
    rwqj__laj = False
    if isinstance(values, DataFrameType):
        rwqj__laj = True
        for i, kxm__lejo in enumerate(df.columns):
            if kxm__lejo in values.column_index:
                rwnf__ryzp = 'val{}'.format(i)
                ilzk__soby += f"""  {rwnf__ryzp} = bodo.hiframes.pd_dataframe_ext.get_dataframe_data(values, {values.column_index[kxm__lejo]})
"""
                ltxbx__kvvh[kxm__lejo] = rwnf__ryzp
    elif is_iterable_type(values) and not isinstance(values, SeriesType):
        ltxbx__kvvh = {kxm__lejo: 'values' for kxm__lejo in df.columns}
    else:
        raise_bodo_error(f'pd.isin(): not supported for type {values}')
    data = []
    for i in range(len(df.columns)):
        rwnf__ryzp = 'data{}'.format(i)
        ilzk__soby += (
            '  {} = bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {})\n'
            .format(rwnf__ryzp, i))
        data.append(rwnf__ryzp)
    aemod__tfid = ['out{}'.format(i) for i in range(len(df.columns))]
    rmb__sno = """
  numba.parfors.parfor.init_prange()
  n = len({0})
  m = len({1})
  {2} = np.empty(n, np.bool_)
  for i in numba.parfors.parfor.internal_prange(n):
    {2}[i] = {0}[i] == {1}[i] if i < m else False
"""
    hbqqr__zet = """
  numba.parfors.parfor.init_prange()
  n = len({0})
  {2} = np.empty(n, np.bool_)
  for i in numba.parfors.parfor.internal_prange(n):
    {2}[i] = {0}[i] in {1}
"""
    spuw__vsuoz = '  {} = np.zeros(len(df), np.bool_)\n'
    for i, (cname, qql__meu) in enumerate(zip(df.columns, data)):
        if cname in ltxbx__kvvh:
            ntgcg__qmbk = ltxbx__kvvh[cname]
            if rwqj__laj:
                ilzk__soby += rmb__sno.format(qql__meu, ntgcg__qmbk,
                    aemod__tfid[i])
            else:
                ilzk__soby += hbqqr__zet.format(qql__meu, ntgcg__qmbk,
                    aemod__tfid[i])
        else:
            ilzk__soby += spuw__vsuoz.format(aemod__tfid[i])
    return _gen_init_df(ilzk__soby, df.columns, ','.join(aemod__tfid))


@overload_method(DataFrameType, 'abs', inline='always', no_unliteral=True)
def overload_dataframe_abs(df):
    check_runtime_cols_unsupported(df, 'DataFrame.abs()')
    for arr_typ in df.data:
        if not (isinstance(arr_typ.dtype, types.Number) or arr_typ.dtype ==
            bodo.timedelta64ns):
            raise_bodo_error(
                f'DataFrame.abs(): Only supported for numeric and Timedelta. Encountered array with dtype {arr_typ.dtype}'
                )
    vzoky__jjk = len(df.columns)
    data_args = ', '.join(
        'np.abs(bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {}))'
        .format(i) for i in range(vzoky__jjk))
    header = 'def impl(df):\n'
    return _gen_init_df(header, df.columns, data_args)


def overload_dataframe_corr(df, method='pearson', min_periods=1):
    hxjsy__jzaz = [kxm__lejo for kxm__lejo, vvpnu__xjesd in zip(df.columns,
        df.data) if bodo.utils.typing._is_pandas_numeric_dtype(vvpnu__xjesd
        .dtype)]
    assert len(hxjsy__jzaz) != 0
    nmm__oyjd = ''
    if not any(vvpnu__xjesd == types.float64 for vvpnu__xjesd in df.data):
        nmm__oyjd = '.astype(np.float64)'
    uky__kfkrg = ', '.join(
        'bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {}){}'.
        format(df.column_index[kxm__lejo], '.astype(np.float64)' if 
        isinstance(df.data[df.column_index[kxm__lejo]], IntegerArrayType) or
        df.data[df.column_index[kxm__lejo]] == boolean_array else '') for
        kxm__lejo in hxjsy__jzaz)
    bphl__aaz = 'np.stack(({},), 1){}'.format(uky__kfkrg, nmm__oyjd)
    data_args = ', '.join('res[:,{}]'.format(i) for i in range(len(
        hxjsy__jzaz)))
    index = f'{generate_col_to_index_func_text(hxjsy__jzaz)}\n'
    header = "def impl(df, method='pearson', min_periods=1):\n"
    header += '  mat = {}\n'.format(bphl__aaz)
    header += '  res = bodo.libs.array_kernels.nancorr(mat, 0, min_periods)\n'
    return _gen_init_df(header, hxjsy__jzaz, data_args, index)


@lower_builtin('df.corr', DataFrameType, types.VarArg(types.Any))
def dataframe_corr_lower(context, builder, sig, args):
    impl = overload_dataframe_corr(*sig.args)
    return context.compile_internal(builder, impl, sig, args)


@overload_method(DataFrameType, 'cov', inline='always', no_unliteral=True)
def overload_dataframe_cov(df, min_periods=None, ddof=1):
    check_runtime_cols_unsupported(df, 'DataFrame.cov()')
    tyy__szp = dict(ddof=ddof)
    vtdv__ntf = dict(ddof=1)
    check_unsupported_args('DataFrame.cov', tyy__szp, vtdv__ntf,
        package_name='pandas', module_name='DataFrame')
    sxt__lcsf = '1' if is_overload_none(min_periods) else 'min_periods'
    hxjsy__jzaz = [kxm__lejo for kxm__lejo, vvpnu__xjesd in zip(df.columns,
        df.data) if bodo.utils.typing._is_pandas_numeric_dtype(vvpnu__xjesd
        .dtype)]
    if len(hxjsy__jzaz) == 0:
        raise_bodo_error('DataFrame.cov(): requires non-empty dataframe')
    nmm__oyjd = ''
    if not any(vvpnu__xjesd == types.float64 for vvpnu__xjesd in df.data):
        nmm__oyjd = '.astype(np.float64)'
    uky__kfkrg = ', '.join(
        'bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {}){}'.
        format(df.column_index[kxm__lejo], '.astype(np.float64)' if 
        isinstance(df.data[df.column_index[kxm__lejo]], IntegerArrayType) or
        df.data[df.column_index[kxm__lejo]] == boolean_array else '') for
        kxm__lejo in hxjsy__jzaz)
    bphl__aaz = 'np.stack(({},), 1){}'.format(uky__kfkrg, nmm__oyjd)
    data_args = ', '.join('res[:,{}]'.format(i) for i in range(len(
        hxjsy__jzaz)))
    index = f'pd.Index({hxjsy__jzaz})\n'
    header = 'def impl(df, min_periods=None, ddof=1):\n'
    header += '  mat = {}\n'.format(bphl__aaz)
    header += '  res = bodo.libs.array_kernels.nancorr(mat, 1, {})\n'.format(
        sxt__lcsf)
    return _gen_init_df(header, hxjsy__jzaz, data_args, index)


@overload_method(DataFrameType, 'count', inline='always', no_unliteral=True)
def overload_dataframe_count(df, axis=0, level=None, numeric_only=False):
    check_runtime_cols_unsupported(df, 'DataFrame.count()')
    tyy__szp = dict(axis=axis, level=level, numeric_only=numeric_only)
    vtdv__ntf = dict(axis=0, level=None, numeric_only=False)
    check_unsupported_args('DataFrame.count', tyy__szp, vtdv__ntf,
        package_name='pandas', module_name='DataFrame')
    data_args = ', '.join(
        f'bodo.libs.array_ops.array_op_count(bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {i}))'
         for i in range(len(df.columns)))
    ilzk__soby = 'def impl(df, axis=0, level=None, numeric_only=False):\n'
    ilzk__soby += '  data = np.array([{}])\n'.format(data_args)
    lnjos__ktsgc = (bodo.hiframes.dataframe_impl.
        generate_col_to_index_func_text(df.columns))
    ilzk__soby += (
        f'  return bodo.hiframes.pd_series_ext.init_series(data, {lnjos__ktsgc})\n'
        )
    lxd__swvja = {}
    exec(ilzk__soby, {'bodo': bodo, 'np': np}, lxd__swvja)
    impl = lxd__swvja['impl']
    return impl


@overload_method(DataFrameType, 'nunique', inline='always', no_unliteral=True)
def overload_dataframe_nunique(df, axis=0, dropna=True):
    check_runtime_cols_unsupported(df, 'DataFrame.unique()')
    tyy__szp = dict(axis=axis)
    vtdv__ntf = dict(axis=0)
    if not is_overload_bool(dropna):
        raise BodoError('DataFrame.nunique: dropna must be a boolean value')
    check_unsupported_args('DataFrame.nunique', tyy__szp, vtdv__ntf,
        package_name='pandas', module_name='DataFrame')
    data_args = ', '.join(
        f'bodo.libs.array_kernels.nunique(bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {i}), dropna)'
         for i in range(len(df.columns)))
    ilzk__soby = 'def impl(df, axis=0, dropna=True):\n'
    ilzk__soby += '  data = np.asarray(({},))\n'.format(data_args)
    lnjos__ktsgc = (bodo.hiframes.dataframe_impl.
        generate_col_to_index_func_text(df.columns))
    ilzk__soby += (
        f'  return bodo.hiframes.pd_series_ext.init_series(data, {lnjos__ktsgc})\n'
        )
    lxd__swvja = {}
    exec(ilzk__soby, {'bodo': bodo, 'np': np}, lxd__swvja)
    impl = lxd__swvja['impl']
    return impl


@overload_method(DataFrameType, 'prod', inline='always', no_unliteral=True)
@overload_method(DataFrameType, 'product', inline='always', no_unliteral=True)
def overload_dataframe_prod(df, axis=None, skipna=None, level=None,
    numeric_only=None, min_count=0):
    check_runtime_cols_unsupported(df, 'DataFrame.prod()')
    tyy__szp = dict(skipna=skipna, level=level, numeric_only=numeric_only,
        min_count=min_count)
    vtdv__ntf = dict(skipna=None, level=None, numeric_only=None, min_count=0)
    check_unsupported_args('DataFrame.prod', tyy__szp, vtdv__ntf,
        package_name='pandas', module_name='DataFrame')
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(df,
        'DataFrame.product()')
    return _gen_reduce_impl(df, 'prod', axis=axis)


@overload_method(DataFrameType, 'sum', inline='always', no_unliteral=True)
def overload_dataframe_sum(df, axis=None, skipna=None, level=None,
    numeric_only=None, min_count=0):
    check_runtime_cols_unsupported(df, 'DataFrame.sum()')
    tyy__szp = dict(skipna=skipna, level=level, numeric_only=numeric_only,
        min_count=min_count)
    vtdv__ntf = dict(skipna=None, level=None, numeric_only=None, min_count=0)
    check_unsupported_args('DataFrame.sum', tyy__szp, vtdv__ntf,
        package_name='pandas', module_name='DataFrame')
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(df,
        'DataFrame.sum()')
    return _gen_reduce_impl(df, 'sum', axis=axis)


@overload_method(DataFrameType, 'max', inline='always', no_unliteral=True)
def overload_dataframe_max(df, axis=None, skipna=None, level=None,
    numeric_only=None):
    check_runtime_cols_unsupported(df, 'DataFrame.max()')
    tyy__szp = dict(skipna=skipna, level=level, numeric_only=numeric_only)
    vtdv__ntf = dict(skipna=None, level=None, numeric_only=None)
    check_unsupported_args('DataFrame.max', tyy__szp, vtdv__ntf,
        package_name='pandas', module_name='DataFrame')
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(df,
        'DataFrame.max()')
    return _gen_reduce_impl(df, 'max', axis=axis)


@overload_method(DataFrameType, 'min', inline='always', no_unliteral=True)
def overload_dataframe_min(df, axis=None, skipna=None, level=None,
    numeric_only=None):
    check_runtime_cols_unsupported(df, 'DataFrame.min()')
    tyy__szp = dict(skipna=skipna, level=level, numeric_only=numeric_only)
    vtdv__ntf = dict(skipna=None, level=None, numeric_only=None)
    check_unsupported_args('DataFrame.min', tyy__szp, vtdv__ntf,
        package_name='pandas', module_name='DataFrame')
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(df,
        'DataFrame.min()')
    return _gen_reduce_impl(df, 'min', axis=axis)


@overload_method(DataFrameType, 'mean', inline='always', no_unliteral=True)
def overload_dataframe_mean(df, axis=None, skipna=None, level=None,
    numeric_only=None):
    check_runtime_cols_unsupported(df, 'DataFrame.mean()')
    tyy__szp = dict(skipna=skipna, level=level, numeric_only=numeric_only)
    vtdv__ntf = dict(skipna=None, level=None, numeric_only=None)
    check_unsupported_args('DataFrame.mean', tyy__szp, vtdv__ntf,
        package_name='pandas', module_name='DataFrame')
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(df,
        'DataFrame.mean()')
    return _gen_reduce_impl(df, 'mean', axis=axis)


@overload_method(DataFrameType, 'var', inline='always', no_unliteral=True)
def overload_dataframe_var(df, axis=None, skipna=None, level=None, ddof=1,
    numeric_only=None):
    check_runtime_cols_unsupported(df, 'DataFrame.var()')
    tyy__szp = dict(skipna=skipna, level=level, ddof=ddof, numeric_only=
        numeric_only)
    vtdv__ntf = dict(skipna=None, level=None, ddof=1, numeric_only=None)
    check_unsupported_args('DataFrame.var', tyy__szp, vtdv__ntf,
        package_name='pandas', module_name='DataFrame')
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(df,
        'DataFrame.var()')
    return _gen_reduce_impl(df, 'var', axis=axis)


@overload_method(DataFrameType, 'std', inline='always', no_unliteral=True)
def overload_dataframe_std(df, axis=None, skipna=None, level=None, ddof=1,
    numeric_only=None):
    check_runtime_cols_unsupported(df, 'DataFrame.std()')
    tyy__szp = dict(skipna=skipna, level=level, ddof=ddof, numeric_only=
        numeric_only)
    vtdv__ntf = dict(skipna=None, level=None, ddof=1, numeric_only=None)
    check_unsupported_args('DataFrame.std', tyy__szp, vtdv__ntf,
        package_name='pandas', module_name='DataFrame')
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(df,
        'DataFrame.std()')
    return _gen_reduce_impl(df, 'std', axis=axis)


@overload_method(DataFrameType, 'median', inline='always', no_unliteral=True)
def overload_dataframe_median(df, axis=None, skipna=None, level=None,
    numeric_only=None):
    check_runtime_cols_unsupported(df, 'DataFrame.median()')
    tyy__szp = dict(skipna=skipna, level=level, numeric_only=numeric_only)
    vtdv__ntf = dict(skipna=None, level=None, numeric_only=None)
    check_unsupported_args('DataFrame.median', tyy__szp, vtdv__ntf,
        package_name='pandas', module_name='DataFrame')
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(df,
        'DataFrame.median()')
    return _gen_reduce_impl(df, 'median', axis=axis)


@overload_method(DataFrameType, 'quantile', inline='always', no_unliteral=True)
def overload_dataframe_quantile(df, q=0.5, axis=0, numeric_only=True,
    interpolation='linear'):
    check_runtime_cols_unsupported(df, 'DataFrame.quantile()')
    tyy__szp = dict(numeric_only=numeric_only, interpolation=interpolation)
    vtdv__ntf = dict(numeric_only=True, interpolation='linear')
    check_unsupported_args('DataFrame.quantile', tyy__szp, vtdv__ntf,
        package_name='pandas', module_name='DataFrame')
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(df,
        'DataFrame.quantile()')
    return _gen_reduce_impl(df, 'quantile', 'q', axis=axis)


@overload_method(DataFrameType, 'idxmax', inline='always', no_unliteral=True)
def overload_dataframe_idxmax(df, axis=0, skipna=True):
    check_runtime_cols_unsupported(df, 'DataFrame.idxmax()')
    tyy__szp = dict(axis=axis, skipna=skipna)
    vtdv__ntf = dict(axis=0, skipna=True)
    check_unsupported_args('DataFrame.idxmax', tyy__szp, vtdv__ntf,
        package_name='pandas', module_name='DataFrame')
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(df,
        'DataFrame.idxmax()')
    for ajxe__pqz in df.data:
        if not (bodo.utils.utils.is_np_array_typ(ajxe__pqz) and (ajxe__pqz.
            dtype in [bodo.datetime64ns, bodo.timedelta64ns] or isinstance(
            ajxe__pqz.dtype, (types.Number, types.Boolean))) or isinstance(
            ajxe__pqz, (bodo.IntegerArrayType, bodo.FloatingArrayType, bodo
            .CategoricalArrayType)) or ajxe__pqz in [bodo.boolean_array,
            bodo.datetime_date_array_type]):
            raise BodoError(
                f'DataFrame.idxmax() only supported for numeric column types. Column type: {ajxe__pqz} not supported.'
                )
        if isinstance(ajxe__pqz, bodo.CategoricalArrayType
            ) and not ajxe__pqz.dtype.ordered:
            raise BodoError(
                'DataFrame.idxmax(): categorical columns must be ordered')
    return _gen_reduce_impl(df, 'idxmax', axis=axis)


@overload_method(DataFrameType, 'idxmin', inline='always', no_unliteral=True)
def overload_dataframe_idxmin(df, axis=0, skipna=True):
    check_runtime_cols_unsupported(df, 'DataFrame.idxmin()')
    tyy__szp = dict(axis=axis, skipna=skipna)
    vtdv__ntf = dict(axis=0, skipna=True)
    check_unsupported_args('DataFrame.idxmin', tyy__szp, vtdv__ntf,
        package_name='pandas', module_name='DataFrame')
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(df,
        'DataFrame.idxmin()')
    for ajxe__pqz in df.data:
        if not (bodo.utils.utils.is_np_array_typ(ajxe__pqz) and (ajxe__pqz.
            dtype in [bodo.datetime64ns, bodo.timedelta64ns] or isinstance(
            ajxe__pqz.dtype, (types.Number, types.Boolean))) or isinstance(
            ajxe__pqz, (bodo.IntegerArrayType, bodo.FloatingArrayType, bodo
            .CategoricalArrayType)) or ajxe__pqz in [bodo.boolean_array,
            bodo.datetime_date_array_type]):
            raise BodoError(
                f'DataFrame.idxmin() only supported for numeric column types. Column type: {ajxe__pqz} not supported.'
                )
        if isinstance(ajxe__pqz, bodo.CategoricalArrayType
            ) and not ajxe__pqz.dtype.ordered:
            raise BodoError(
                'DataFrame.idxmin(): categorical columns must be ordered')
    return _gen_reduce_impl(df, 'idxmin', axis=axis)


@overload_method(DataFrameType, 'infer_objects', inline='always')
def overload_dataframe_infer_objects(df):
    check_runtime_cols_unsupported(df, 'DataFrame.infer_objects()')
    return lambda df: df.copy()


def _gen_reduce_impl(df, func_name, args=None, axis=None):
    args = '' if is_overload_none(args) else args
    if is_overload_none(axis):
        axis = 0
    elif is_overload_constant_int(axis):
        axis = get_overload_const_int(axis)
    else:
        raise_bodo_error(
            f'DataFrame.{func_name}: axis must be a constant Integer')
    assert axis in (0, 1), f'invalid axis argument for DataFrame.{func_name}'
    if func_name in ('idxmax', 'idxmin'):
        out_colnames = df.columns
    else:
        hxjsy__jzaz = tuple(kxm__lejo for kxm__lejo, vvpnu__xjesd in zip(df
            .columns, df.data) if bodo.utils.typing.
            _is_pandas_numeric_dtype(vvpnu__xjesd.dtype))
        out_colnames = hxjsy__jzaz
    assert len(out_colnames) != 0
    try:
        if func_name in ('idxmax', 'idxmin') and axis == 0:
            comm_dtype = None
        else:
            zyah__amgk = [numba.np.numpy_support.as_dtype(df.data[df.
                column_index[kxm__lejo]].dtype) for kxm__lejo in out_colnames]
            comm_dtype = numba.np.numpy_support.from_dtype(np.
                find_common_type(zyah__amgk, []))
    except NotImplementedError as kfza__jie:
        raise BodoError(
            f'Dataframe.{func_name}() with column types: {df.data} could not be merged to a common type.'
            )
    nbtgs__bcw = ''
    if func_name in ('sum', 'prod'):
        nbtgs__bcw = ', min_count=0'
    ddof = ''
    if func_name in ('var', 'std'):
        ddof = 'ddof=1, '
    ilzk__soby = (
        'def impl(df, axis=None, skipna=None, level=None,{} numeric_only=None{}):\n'
        .format(ddof, nbtgs__bcw))
    if func_name == 'quantile':
        ilzk__soby = (
            "def impl(df, q=0.5, axis=0, numeric_only=True, interpolation='linear'):\n"
            )
    if func_name in ('idxmax', 'idxmin'):
        ilzk__soby = 'def impl(df, axis=0, skipna=True):\n'
    if axis == 0:
        ilzk__soby += _gen_reduce_impl_axis0(df, func_name, out_colnames,
            comm_dtype, args)
    else:
        ilzk__soby += _gen_reduce_impl_axis1(func_name, out_colnames,
            comm_dtype, df)
    lxd__swvja = {}
    exec(ilzk__soby, {'bodo': bodo, 'np': np, 'pd': pd, 'numba': numba},
        lxd__swvja)
    impl = lxd__swvja['impl']
    return impl


def _gen_reduce_impl_axis0(df, func_name, out_colnames, comm_dtype, args):
    rxi__gswn = ''
    if func_name in ('min', 'max'):
        rxi__gswn = ', dtype=np.{}'.format(comm_dtype)
    if comm_dtype == types.float32 and func_name in ('sum', 'prod', 'mean',
        'var', 'std', 'median'):
        rxi__gswn = ', dtype=np.float32'
    hmyu__ydywj = f'bodo.libs.array_ops.array_op_{func_name}'
    lut__sein = ''
    if func_name in ['sum', 'prod']:
        lut__sein = 'True, min_count'
    elif func_name in ['idxmax', 'idxmin']:
        lut__sein = 'index'
    elif func_name == 'quantile':
        lut__sein = 'q'
    elif func_name in ['std', 'var']:
        lut__sein = 'True, ddof'
    elif func_name == 'median':
        lut__sein = 'True'
    data_args = ', '.join(
        f'{hmyu__ydywj}(bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {df.column_index[kxm__lejo]}), {lut__sein})'
         for kxm__lejo in out_colnames)
    ilzk__soby = ''
    if func_name in ('idxmax', 'idxmin'):
        ilzk__soby += (
            '  index = bodo.hiframes.pd_dataframe_ext.get_dataframe_index(df)\n'
            )
        ilzk__soby += (
            '  data = bodo.utils.conversion.coerce_to_array(({},))\n'.
            format(data_args))
    else:
        ilzk__soby += '  data = np.asarray(({},){})\n'.format(data_args,
            rxi__gswn)
    ilzk__soby += f"""  return bodo.hiframes.pd_series_ext.init_series(data, pd.Index({out_colnames}))
"""
    return ilzk__soby


def _gen_reduce_impl_axis1(func_name, out_colnames, comm_dtype, df_type):
    ktjbe__zuafd = [df_type.column_index[kxm__lejo] for kxm__lejo in
        out_colnames]
    index = 'bodo.hiframes.pd_dataframe_ext.get_dataframe_index(df)'
    data_args = '\n    '.join(
        'arr_{0} = bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {0})'
        .format(i) for i in ktjbe__zuafd)
    nslsw__ngaj = '\n        '.join(f'row[{i}] = arr_{ktjbe__zuafd[i]}[i]' for
        i in range(len(out_colnames)))
    assert len(data_args) > 0, f'empty dataframe in DataFrame.{func_name}()'
    lxf__oblwg = f'len(arr_{ktjbe__zuafd[0]})'
    ijug__kui = {'max': 'np.nanmax', 'min': 'np.nanmin', 'sum': 'np.nansum',
        'prod': 'np.nanprod', 'mean': 'np.nanmean', 'median':
        'np.nanmedian', 'var': 'bodo.utils.utils.nanvar_ddof1', 'std':
        'bodo.utils.utils.nanstd_ddof1'}
    if func_name in ijug__kui:
        jtqv__fke = ijug__kui[func_name]
        zbntm__ioyl = 'float64' if func_name in ['mean', 'median', 'std', 'var'
            ] else comm_dtype
        ilzk__soby = f"""
    {data_args}
    numba.parfors.parfor.init_prange()
    n = {lxf__oblwg}
    row = np.empty({len(out_colnames)}, np.{comm_dtype})
    A = np.empty(n, np.{zbntm__ioyl})
    for i in numba.parfors.parfor.internal_prange(n):
        {nslsw__ngaj}
        A[i] = {jtqv__fke}(row)
    return bodo.hiframes.pd_series_ext.init_series(A, {index})
"""
        return ilzk__soby
    else:
        raise BodoError(f'DataFrame.{func_name}(): Not supported for axis=1')


@overload_method(DataFrameType, 'pct_change', inline='always', no_unliteral
    =True)
def overload_dataframe_pct_change(df, periods=1, fill_method='pad', limit=
    None, freq=None):
    check_runtime_cols_unsupported(df, 'DataFrame.pct_change()')
    tyy__szp = dict(fill_method=fill_method, limit=limit, freq=freq)
    vtdv__ntf = dict(fill_method='pad', limit=None, freq=None)
    check_unsupported_args('DataFrame.pct_change', tyy__szp, vtdv__ntf,
        package_name='pandas', module_name='DataFrame')
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(df,
        'DataFrame.pct_change()')
    data_args = ', '.join(
        f'bodo.hiframes.rolling.pct_change(bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {i}), periods, False)'
         for i in range(len(df.columns)))
    header = (
        "def impl(df, periods=1, fill_method='pad', limit=None, freq=None):\n")
    return _gen_init_df(header, df.columns, data_args)


@overload_method(DataFrameType, 'cumprod', inline='always', no_unliteral=True)
def overload_dataframe_cumprod(df, axis=None, skipna=True):
    check_runtime_cols_unsupported(df, 'DataFrame.cumprod()')
    tyy__szp = dict(axis=axis, skipna=skipna)
    vtdv__ntf = dict(axis=None, skipna=True)
    check_unsupported_args('DataFrame.cumprod', tyy__szp, vtdv__ntf,
        package_name='pandas', module_name='DataFrame')
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(df,
        'DataFrame.cumprod()')
    data_args = ', '.join(
        f'bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {i}).cumprod()'
         for i in range(len(df.columns)))
    header = 'def impl(df, axis=None, skipna=True):\n'
    return _gen_init_df(header, df.columns, data_args)


@overload_method(DataFrameType, 'cumsum', inline='always', no_unliteral=True)
def overload_dataframe_cumsum(df, axis=None, skipna=True):
    check_runtime_cols_unsupported(df, 'DataFrame.cumsum()')
    tyy__szp = dict(skipna=skipna)
    vtdv__ntf = dict(skipna=True)
    check_unsupported_args('DataFrame.cumsum', tyy__szp, vtdv__ntf,
        package_name='pandas', module_name='DataFrame')
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(df,
        'DataFrame.cumsum()')
    data_args = ', '.join(
        f'bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {i}).cumsum()'
         for i in range(len(df.columns)))
    header = 'def impl(df, axis=None, skipna=True):\n'
    return _gen_init_df(header, df.columns, data_args)


def _is_describe_type(data):
    return isinstance(data, (IntegerArrayType, FloatingArrayType)
        ) or isinstance(data, types.Array) and isinstance(data.dtype, types
        .Number) or data.dtype == bodo.datetime64ns


@overload_method(DataFrameType, 'describe', inline='always', no_unliteral=True)
def overload_dataframe_describe(df, percentiles=None, include=None, exclude
    =None, datetime_is_numeric=True):
    check_runtime_cols_unsupported(df, 'DataFrame.describe()')
    tyy__szp = dict(percentiles=percentiles, include=include, exclude=
        exclude, datetime_is_numeric=datetime_is_numeric)
    vtdv__ntf = dict(percentiles=None, include=None, exclude=None,
        datetime_is_numeric=True)
    check_unsupported_args('DataFrame.describe', tyy__szp, vtdv__ntf,
        package_name='pandas', module_name='DataFrame')
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(df,
        'DataFrame.describe()')
    hxjsy__jzaz = [kxm__lejo for kxm__lejo, vvpnu__xjesd in zip(df.columns,
        df.data) if _is_describe_type(vvpnu__xjesd)]
    if len(hxjsy__jzaz) == 0:
        raise BodoError('df.describe() only supports numeric columns')
    qqt__rkpi = sum(df.data[df.column_index[kxm__lejo]].dtype == bodo.
        datetime64ns for kxm__lejo in hxjsy__jzaz)

    def _get_describe(col_ind):
        fnkef__euid = df.data[col_ind].dtype == bodo.datetime64ns
        if qqt__rkpi and qqt__rkpi != len(hxjsy__jzaz):
            if fnkef__euid:
                return f'des_{col_ind} + (np.nan,)'
            return (
                f'des_{col_ind}[:2] + des_{col_ind}[3:] + (des_{col_ind}[2],)')
        return f'des_{col_ind}'
    header = """def impl(df, percentiles=None, include=None, exclude=None, datetime_is_numeric=True):
"""
    for kxm__lejo in hxjsy__jzaz:
        col_ind = df.column_index[kxm__lejo]
        header += f"""  des_{col_ind} = bodo.libs.array_ops.array_op_describe(bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {col_ind}))
"""
    data_args = ', '.join(_get_describe(df.column_index[kxm__lejo]) for
        kxm__lejo in hxjsy__jzaz)
    gwilk__nui = "['count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max']"
    if qqt__rkpi == len(hxjsy__jzaz):
        gwilk__nui = "['count', 'mean', 'min', '25%', '50%', '75%', 'max']"
    elif qqt__rkpi:
        gwilk__nui = (
            "['count', 'mean', 'min', '25%', '50%', '75%', 'max', 'std']")
    index = f'bodo.utils.conversion.convert_to_index({gwilk__nui})'
    return _gen_init_df(header, hxjsy__jzaz, data_args, index)


@overload_method(DataFrameType, 'take', inline='always', no_unliteral=True)
def overload_dataframe_take(df, indices, axis=0, convert=None, is_copy=True):
    check_runtime_cols_unsupported(df, 'DataFrame.take()')
    tyy__szp = dict(axis=axis, convert=convert, is_copy=is_copy)
    vtdv__ntf = dict(axis=0, convert=None, is_copy=True)
    check_unsupported_args('DataFrame.take', tyy__szp, vtdv__ntf,
        package_name='pandas', module_name='DataFrame')
    data_args = ', '.join(
        'bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {})[indices_t]'
        .format(i) for i in range(len(df.columns)))
    header = 'def impl(df, indices, axis=0, convert=None, is_copy=True):\n'
    header += (
        '  indices_t = bodo.utils.conversion.coerce_to_ndarray(indices)\n')
    index = 'bodo.hiframes.pd_dataframe_ext.get_dataframe_index(df)[indices_t]'
    return _gen_init_df(header, df.columns, data_args, index)


@overload_method(DataFrameType, 'shift', inline='always', no_unliteral=True)
def overload_dataframe_shift(df, periods=1, freq=None, axis=0, fill_value=None
    ):
    check_runtime_cols_unsupported(df, 'DataFrame.shift()')
    tyy__szp = dict(freq=freq, axis=axis)
    vtdv__ntf = dict(freq=None, axis=0)
    check_unsupported_args('DataFrame.shift', tyy__szp, vtdv__ntf,
        package_name='pandas', module_name='DataFrame')
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(df,
        'DataFrame.shift()')
    for owb__mxwd in df.data:
        if not is_supported_shift_array_type(owb__mxwd):
            raise BodoError(
                f'Dataframe.shift() column input type {owb__mxwd.dtype} not supported yet.'
                )
    if not is_overload_int(periods):
        raise BodoError(
            "DataFrame.shift(): 'periods' input must be an integer.")
    data_args = ', '.join(
        f'bodo.hiframes.rolling.shift(bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {i}), periods, False, fill_value)'
         for i in range(len(df.columns)))
    header = 'def impl(df, periods=1, freq=None, axis=0, fill_value=None):\n'
    return _gen_init_df(header, df.columns, data_args)


@overload_method(DataFrameType, 'diff', inline='always', no_unliteral=True)
def overload_dataframe_diff(df, periods=1, axis=0):
    check_runtime_cols_unsupported(df, 'DataFrame.diff()')
    tyy__szp = dict(axis=axis)
    vtdv__ntf = dict(axis=0)
    check_unsupported_args('DataFrame.diff', tyy__szp, vtdv__ntf,
        package_name='pandas', module_name='DataFrame')
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(df,
        'DataFrame.diff()')
    for owb__mxwd in df.data:
        if not (isinstance(owb__mxwd, types.Array) and (isinstance(
            owb__mxwd.dtype, types.Number) or owb__mxwd.dtype == bodo.
            datetime64ns)):
            raise BodoError(
                f'DataFrame.diff() column input type {owb__mxwd.dtype} not supported.'
                )
    if not is_overload_int(periods):
        raise BodoError("DataFrame.diff(): 'periods' input must be an integer."
            )
    header = 'def impl(df, periods=1, axis= 0):\n'
    for i in range(len(df.columns)):
        header += (
            f'  data_{i} = bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {i})\n'
            )
    data_args = ', '.join(
        f'bodo.hiframes.series_impl.dt64_arr_sub(data_{i}, bodo.hiframes.rolling.shift(data_{i}, periods, False))'
         if df.data[i] == types.Array(bodo.datetime64ns, 1, 'C') else
        f'data_{i} - bodo.hiframes.rolling.shift(data_{i}, periods, False)' for
        i in range(len(df.columns)))
    return _gen_init_df(header, df.columns, data_args)


@overload_method(DataFrameType, 'explode', inline='always', no_unliteral=True)
def overload_dataframe_explode(df, column, ignore_index=False):
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(df,
        'DataFrame.explode()')
    jjgu__fnow = (
        "DataFrame.explode(): 'column' must a constant label or list of labels"
        )
    if not is_literal_type(column):
        raise_bodo_error(jjgu__fnow)
    if is_overload_constant_list(column) or is_overload_constant_tuple(column):
        wuqw__hrcc = get_overload_const_list(column)
    else:
        wuqw__hrcc = [get_literal_value(column)]
    mhhe__qltob = [df.column_index[kxm__lejo] for kxm__lejo in wuqw__hrcc]
    for i in mhhe__qltob:
        if not isinstance(df.data[i], ArrayItemArrayType) and df.data[i
            ].dtype != string_array_split_view_type:
            raise BodoError(
                f'DataFrame.explode(): columns must have array-like entries')
    n = len(df.columns)
    header = 'def impl(df, column, ignore_index=False):\n'
    header += (
        '  index = bodo.hiframes.pd_dataframe_ext.get_dataframe_index(df)\n')
    header += '  index_arr = bodo.utils.conversion.index_to_array(index)\n'
    for i in range(n):
        header += (
            f'  data{i} = bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {i})\n'
            )
    header += (
        f'  counts = bodo.libs.array_kernels.get_arr_lens(data{mhhe__qltob[0]})\n'
        )
    for i in range(n):
        if i in mhhe__qltob:
            header += (
                f'  out_data{i} = bodo.libs.array_kernels.explode_no_index(data{i}, counts)\n'
                )
        else:
            header += (
                f'  out_data{i} = bodo.libs.array_kernels.repeat_kernel(data{i}, counts)\n'
                )
    header += (
        '  new_index = bodo.libs.array_kernels.repeat_kernel(index_arr, counts)\n'
        )
    data_args = ', '.join(f'out_data{i}' for i in range(n))
    index = 'bodo.utils.conversion.convert_to_index(new_index)'
    return _gen_init_df(header, df.columns, data_args, index)


@overload_method(DataFrameType, 'set_index', inline='always', no_unliteral=True
    )
def overload_dataframe_set_index(df, keys, drop=True, append=False, inplace
    =False, verify_integrity=False):
    check_runtime_cols_unsupported(df, 'DataFrame.set_index()')
    wdxk__vydem = {'inplace': inplace, 'append': append, 'verify_integrity':
        verify_integrity}
    jyskm__yjr = {'inplace': False, 'append': False, 'verify_integrity': False}
    check_unsupported_args('DataFrame.set_index', wdxk__vydem, jyskm__yjr,
        package_name='pandas', module_name='DataFrame')
    if not is_overload_constant_str(keys):
        raise_bodo_error(
            "DataFrame.set_index(): 'keys' must be a constant string")
    col_name = get_overload_const_str(keys)
    col_ind = df.columns.index(col_name)
    header = """def impl(df, keys, drop=True, append=False, inplace=False, verify_integrity=False):
"""
    data_args = ', '.join(
        'bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {})'.format(
        i) for i in range(len(df.columns)) if i != col_ind)
    columns = tuple(kxm__lejo for kxm__lejo in df.columns if kxm__lejo !=
        col_name)
    index = (
        'bodo.utils.conversion.index_from_array(bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {}), {})'
        .format(col_ind, f"'{col_name}'" if isinstance(col_name, str) else
        col_name))
    return _gen_init_df(header, columns, data_args, index)


@overload_method(DataFrameType, 'query', no_unliteral=True)
def overload_dataframe_query(df, expr, inplace=False):
    check_runtime_cols_unsupported(df, 'DataFrame.query()')
    wdxk__vydem = {'inplace': inplace}
    jyskm__yjr = {'inplace': False}
    check_unsupported_args('query', wdxk__vydem, jyskm__yjr, package_name=
        'pandas', module_name='DataFrame')
    if not isinstance(expr, (types.StringLiteral, types.UnicodeType)):
        raise BodoError('query(): expr argument should be a string')

    def impl(df, expr, inplace=False):
        xnvfj__dtaoy = bodo.hiframes.pd_dataframe_ext.query_dummy(df, expr)
        return df[xnvfj__dtaoy]
    return impl


@overload_method(DataFrameType, 'duplicated', inline='always', no_unliteral
    =True)
def overload_dataframe_duplicated(df, subset=None, keep='first'):
    check_runtime_cols_unsupported(df, 'DataFrame.duplicated()')
    wdxk__vydem = {'subset': subset, 'keep': keep}
    jyskm__yjr = {'subset': None, 'keep': 'first'}
    check_unsupported_args('DataFrame.duplicated', wdxk__vydem, jyskm__yjr,
        package_name='pandas', module_name='DataFrame')
    vzoky__jjk = len(df.columns)
    ilzk__soby = "def impl(df, subset=None, keep='first'):\n"
    for i in range(vzoky__jjk):
        ilzk__soby += (
            '  data_{0} = bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {0})\n'
            .format(i))
    fgycr__zdp = ', '.join(f'data_{i}' for i in range(vzoky__jjk))
    fgycr__zdp += ',' if vzoky__jjk == 1 else ''
    ilzk__soby += (
        f'  duplicated = bodo.libs.array_kernels.duplicated(({fgycr__zdp}))\n')
    ilzk__soby += (
        '  index = bodo.hiframes.pd_dataframe_ext.get_dataframe_index(df)\n')
    ilzk__soby += (
        '  return bodo.hiframes.pd_series_ext.init_series(duplicated, index)\n'
        )
    lxd__swvja = {}
    exec(ilzk__soby, {'bodo': bodo}, lxd__swvja)
    impl = lxd__swvja['impl']
    return impl


@overload_method(DataFrameType, 'drop_duplicates', inline='always',
    no_unliteral=True)
def overload_dataframe_drop_duplicates(df, subset=None, keep='first',
    inplace=False, ignore_index=False):
    check_runtime_cols_unsupported(df, 'DataFrame.drop_duplicates()')
    wdxk__vydem = {'keep': keep, 'inplace': inplace, 'ignore_index':
        ignore_index}
    jyskm__yjr = {'keep': 'first', 'inplace': False, 'ignore_index': False}
    gajw__hish = []
    if is_overload_constant_list(subset):
        gajw__hish = get_overload_const_list(subset)
    elif is_overload_constant_str(subset):
        gajw__hish = [get_overload_const_str(subset)]
    elif is_overload_constant_int(subset):
        gajw__hish = [get_overload_const_int(subset)]
    elif not is_overload_none(subset):
        raise_bodo_error(
            'DataFrame.drop_duplicates(): subset must be a constant column name, constant list of column names or None'
            )
    cvyzi__qbfh = []
    for col_name in gajw__hish:
        if col_name not in df.column_index:
            raise BodoError(
                'DataFrame.drop_duplicates(): All subset columns must be found in the DataFrame.'
                 +
                f'Column {col_name} not found in DataFrame columns {df.columns}'
                )
        cvyzi__qbfh.append(df.column_index[col_name])
    check_unsupported_args('DataFrame.drop_duplicates', wdxk__vydem,
        jyskm__yjr, package_name='pandas', module_name='DataFrame')
    gypdm__zcv = []
    if cvyzi__qbfh:
        for eyz__puge in cvyzi__qbfh:
            if isinstance(df.data[eyz__puge], bodo.MapArrayType):
                gypdm__zcv.append(df.columns[eyz__puge])
    else:
        for i, col_name in enumerate(df.columns):
            if isinstance(df.data[i], bodo.MapArrayType):
                gypdm__zcv.append(col_name)
    if gypdm__zcv:
        raise BodoError(
            f'DataFrame.drop_duplicates(): Columns {gypdm__zcv} ' +
            f'have dictionary types which cannot be used to drop duplicates. '
             +
            "Please consider using the 'subset' argument to skip these columns."
            )
    vzoky__jjk = len(df.columns)
    esl__yrcv = ['data_{}'.format(i) for i in cvyzi__qbfh]
    zbvyq__smqrp = ['data_{}'.format(i) for i in range(vzoky__jjk) if i not in
        cvyzi__qbfh]
    if esl__yrcv:
        zergx__vvpir = len(esl__yrcv)
    else:
        zergx__vvpir = vzoky__jjk
    fgr__soth = ', '.join(esl__yrcv + zbvyq__smqrp)
    data_args = ', '.join('data_{}'.format(i) for i in range(vzoky__jjk))
    ilzk__soby = (
        "def impl(df, subset=None, keep='first', inplace=False, ignore_index=False):\n"
        )
    for i in range(vzoky__jjk):
        ilzk__soby += (
            '  data_{0} = bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {0})\n'
            .format(i))
    index = (
        'bodo.utils.conversion.index_to_array(bodo.hiframes.pd_dataframe_ext.get_dataframe_index(df))'
        )
    ilzk__soby += (
        """  ({0},), index_arr = bodo.libs.array_kernels.drop_duplicates(({0},), {1}, {2})
"""
        .format(fgr__soth, index, zergx__vvpir))
    ilzk__soby += (
        '  index = bodo.utils.conversion.index_from_array(index_arr)\n')
    return _gen_init_df(ilzk__soby, df.columns, data_args, 'index')


def create_dataframe_mask_where_overload(func_name):

    def overload_dataframe_mask_where(df, cond, other=np.nan, inplace=False,
        axis=None, level=None, errors='raise', try_cast=False):
        bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(df,
            f'DataFrame.{func_name}()')
        _validate_arguments_mask_where(f'DataFrame.{func_name}', df, cond,
            other, inplace, axis, level, errors, try_cast)
        header = """def impl(df, cond, other=np.nan, inplace=False, axis=None, level=None, errors='raise', try_cast=False):
"""
        if func_name == 'mask':
            header += '  cond = ~cond\n'
        gen_all_false = [False]
        if cond.ndim == 1:
            cond_str = lambda i, _: 'cond'
        elif cond.ndim == 2:
            if isinstance(cond, DataFrameType):

                def cond_str(i, gen_all_false):
                    if df.columns[i] in cond.column_index:
                        return (
                            f'bodo.hiframes.pd_dataframe_ext.get_dataframe_data(cond, {cond.column_index[df.columns[i]]})'
                            )
                    else:
                        gen_all_false[0] = True
                        return 'all_false'
            elif isinstance(cond, types.Array):
                cond_str = lambda i, _: f'cond[:,{i}]'
        if not hasattr(other, 'ndim') or other.ndim == 1:
            jzq__vxm = lambda i: 'other'
        elif other.ndim == 2:
            if isinstance(other, DataFrameType):
                jzq__vxm = (lambda i: 
                    f'bodo.hiframes.pd_dataframe_ext.get_dataframe_data(other, {other.column_index[df.columns[i]]})'
                     if df.columns[i] in other.column_index else 'None')
            elif isinstance(other, types.Array):
                jzq__vxm = lambda i: f'other[:,{i}]'
        vzoky__jjk = len(df.columns)
        data_args = ', '.join(
            f'bodo.hiframes.series_impl.where_impl({cond_str(i, gen_all_false)}, bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {i}), {jzq__vxm(i)})'
             for i in range(vzoky__jjk))
        if gen_all_false[0]:
            header += '  all_false = np.zeros(len(df), dtype=bool)\n'
        return _gen_init_df(header, df.columns, data_args)
    return overload_dataframe_mask_where


def _install_dataframe_mask_where_overload():
    for func_name in ('mask', 'where'):
        wwjmn__vhf = create_dataframe_mask_where_overload(func_name)
        overload_method(DataFrameType, func_name, no_unliteral=True)(wwjmn__vhf
            )


_install_dataframe_mask_where_overload()


def _validate_arguments_mask_where(func_name, df, cond, other, inplace,
    axis, level, errors, try_cast):
    tyy__szp = dict(inplace=inplace, level=level, errors=errors, try_cast=
        try_cast)
    vtdv__ntf = dict(inplace=False, level=None, errors='raise', try_cast=False)
    check_unsupported_args(f'{func_name}', tyy__szp, vtdv__ntf,
        package_name='pandas', module_name='DataFrame')
    if not (is_overload_none(axis) or is_overload_zero(axis)):
        raise_bodo_error(f'{func_name}(): axis argument not supported')
    if not (isinstance(cond, (SeriesType, types.Array, BooleanArrayType)) and
        (cond.ndim == 1 or cond.ndim == 2) and cond.dtype == types.bool_
        ) and not (isinstance(cond, DataFrameType) and cond.ndim == 2 and
        all(cond.data[i].dtype == types.bool_ for i in range(len(df.columns)))
        ):
        raise BodoError(
            f"{func_name}(): 'cond' argument must be a DataFrame, Series, 1- or 2-dimensional array of booleans"
            )
    vzoky__jjk = len(df.columns)
    if hasattr(other, 'ndim') and (other.ndim != 1 or other.ndim != 2):
        if other.ndim == 2:
            if not isinstance(other, (DataFrameType, types.Array)):
                raise BodoError(
                    f"{func_name}(): 'other', if 2-dimensional, must be a DataFrame or array."
                    )
        elif other.ndim != 1:
            raise BodoError(
                f"{func_name}(): 'other' must be either 1 or 2-dimensional")
    if isinstance(other, DataFrameType):
        for i in range(vzoky__jjk):
            if df.columns[i] in other.column_index:
                bodo.hiframes.series_impl._validate_self_other_mask_where(
                    func_name, 'Series', df.data[i], other.data[other.
                    column_index[df.columns[i]]])
            else:
                bodo.hiframes.series_impl._validate_self_other_mask_where(
                    func_name, 'Series', df.data[i], None, is_default=True)
    elif isinstance(other, SeriesType):
        for i in range(vzoky__jjk):
            bodo.hiframes.series_impl._validate_self_other_mask_where(func_name
                , 'Series', df.data[i], other.data)
    else:
        for i in range(vzoky__jjk):
            bodo.hiframes.series_impl._validate_self_other_mask_where(func_name
                , 'Series', df.data[i], other, max_ndim=2)


def _gen_init_df(header, columns, data_args, index=None, extra_globals=None):
    if index is None:
        index = 'bodo.hiframes.pd_dataframe_ext.get_dataframe_index(df)'
    if extra_globals is None:
        extra_globals = {}
    wlhd__ijpi = ColNamesMetaType(tuple(columns))
    data_args = '({}{})'.format(data_args, ',' if data_args else '')
    ilzk__soby = f"""{header}  return bodo.hiframes.pd_dataframe_ext.init_dataframe({data_args}, {index}, __col_name_meta_value_gen_init_df)
"""
    lxd__swvja = {}
    mgljd__oyxdb = {'bodo': bodo, 'np': np, 'pd': pd, 'numba': numba,
        '__col_name_meta_value_gen_init_df': wlhd__ijpi}
    mgljd__oyxdb.update(extra_globals)
    exec(ilzk__soby, mgljd__oyxdb, lxd__swvja)
    impl = lxd__swvja['impl']
    return impl


def _get_binop_columns(lhs, rhs, is_inplace=False):
    if lhs.columns != rhs.columns:
        utx__ren = pd.Index(lhs.columns)
        tuj__kvm = pd.Index(rhs.columns)
        tlzy__mjs, ukgy__devk, lom__jcc = utx__ren.join(tuj__kvm, how=
            'left' if is_inplace else 'outer', level=None, return_indexers=True
            )
        return tuple(tlzy__mjs), ukgy__devk, lom__jcc
    return lhs.columns, range(len(lhs.columns)), range(len(lhs.columns))


def create_binary_op_overload(op):

    def overload_dataframe_binary_op(lhs, rhs):
        cbej__jmalb = numba.core.utils.OPERATORS_TO_BUILTINS[op]
        oobt__nit = operator.eq, operator.ne
        check_runtime_cols_unsupported(lhs, cbej__jmalb)
        check_runtime_cols_unsupported(rhs, cbej__jmalb)
        if isinstance(lhs, DataFrameType):
            if isinstance(rhs, DataFrameType):
                tlzy__mjs, ukgy__devk, lom__jcc = _get_binop_columns(lhs, rhs)
                data_args = ', '.join(
                    f'bodo.hiframes.pd_dataframe_ext.get_dataframe_data(lhs, {ubyjw__wmfhq}) {cbej__jmalb}bodo.hiframes.pd_dataframe_ext.get_dataframe_data(rhs, {kst__qowz})'
                     if ubyjw__wmfhq != -1 and kst__qowz != -1 else
                    f'bodo.libs.array_kernels.gen_na_array(len(lhs), float64_arr_type)'
                     for ubyjw__wmfhq, kst__qowz in zip(ukgy__devk, lom__jcc))
                header = 'def impl(lhs, rhs):\n'
                index = (
                    'bodo.hiframes.pd_dataframe_ext.get_dataframe_index(lhs)')
                return _gen_init_df(header, tlzy__mjs, data_args, index,
                    extra_globals={'float64_arr_type': types.Array(types.
                    float64, 1, 'C')})
            elif isinstance(rhs, SeriesType):
                raise_bodo_error(
                    'Comparison operation between Dataframe and Series is not supported yet.'
                    )
            gza__mcsy = []
            xgi__yan = []
            if op in oobt__nit:
                for i, jlt__dtxm in enumerate(lhs.data):
                    if is_common_scalar_dtype([jlt__dtxm.dtype, rhs]):
                        gza__mcsy.append(
                            f'bodo.hiframes.pd_dataframe_ext.get_dataframe_data(lhs, {i}) {cbej__jmalb} rhs'
                            )
                    else:
                        lmb__tjmn = f'arr{i}'
                        xgi__yan.append(lmb__tjmn)
                        gza__mcsy.append(lmb__tjmn)
                data_args = ', '.join(gza__mcsy)
            else:
                data_args = ', '.join(
                    f'bodo.hiframes.pd_dataframe_ext.get_dataframe_data(lhs, {i}) {cbej__jmalb} rhs'
                     for i in range(len(lhs.columns)))
            header = 'def impl(lhs, rhs):\n'
            if len(xgi__yan) > 0:
                header += '  numba.parfors.parfor.init_prange()\n'
                header += '  n = len(lhs)\n'
                header += ''.join(
                    f'  {lmb__tjmn} = np.empty(n, dtype=np.bool_)\n' for
                    lmb__tjmn in xgi__yan)
                header += (
                    '  for i in numba.parfors.parfor.internal_prange(n):\n')
                header += ''.join('    {0}[i] = {1}\n'.format(lmb__tjmn, op ==
                    operator.ne) for lmb__tjmn in xgi__yan)
            index = 'bodo.hiframes.pd_dataframe_ext.get_dataframe_index(lhs)'
            return _gen_init_df(header, lhs.columns, data_args, index)
        if isinstance(rhs, DataFrameType):
            if isinstance(lhs, SeriesType):
                raise_bodo_error(
                    'Comparison operation between Dataframe and Series is not supported yet.'
                    )
            gza__mcsy = []
            xgi__yan = []
            if op in oobt__nit:
                for i, jlt__dtxm in enumerate(rhs.data):
                    if is_common_scalar_dtype([lhs, jlt__dtxm.dtype]):
                        gza__mcsy.append(
                            f'lhs {cbej__jmalb} bodo.hiframes.pd_dataframe_ext.get_dataframe_data(rhs, {i})'
                            )
                    else:
                        lmb__tjmn = f'arr{i}'
                        xgi__yan.append(lmb__tjmn)
                        gza__mcsy.append(lmb__tjmn)
                data_args = ', '.join(gza__mcsy)
            else:
                data_args = ', '.join(
                    'lhs {1} bodo.hiframes.pd_dataframe_ext.get_dataframe_data(rhs, {0})'
                    .format(i, cbej__jmalb) for i in range(len(rhs.columns)))
            header = 'def impl(lhs, rhs):\n'
            if len(xgi__yan) > 0:
                header += '  numba.parfors.parfor.init_prange()\n'
                header += '  n = len(rhs)\n'
                header += ''.join('  {0} = np.empty(n, dtype=np.bool_)\n'.
                    format(lmb__tjmn) for lmb__tjmn in xgi__yan)
                header += (
                    '  for i in numba.parfors.parfor.internal_prange(n):\n')
                header += ''.join('    {0}[i] = {1}\n'.format(lmb__tjmn, op ==
                    operator.ne) for lmb__tjmn in xgi__yan)
            index = 'bodo.hiframes.pd_dataframe_ext.get_dataframe_index(rhs)'
            return _gen_init_df(header, rhs.columns, data_args, index)
    return overload_dataframe_binary_op


skips = [operator.lt, operator.le, operator.eq, operator.ne, operator.gt,
    operator.ge, operator.add, operator.sub, operator.mul, operator.truediv,
    operator.floordiv, operator.pow, operator.mod]


def _install_binary_ops():
    for op in bodo.hiframes.pd_series_ext.series_binary_ops:
        if op in skips:
            continue
        wwjmn__vhf = create_binary_op_overload(op)
        overload(op)(wwjmn__vhf)


_install_binary_ops()


def create_inplace_binary_op_overload(op):

    def overload_dataframe_inplace_binary_op(left, right):
        cbej__jmalb = numba.core.utils.OPERATORS_TO_BUILTINS[op]
        check_runtime_cols_unsupported(left, cbej__jmalb)
        check_runtime_cols_unsupported(right, cbej__jmalb)
        if isinstance(left, DataFrameType):
            if isinstance(right, DataFrameType):
                tlzy__mjs, _, lom__jcc = _get_binop_columns(left, right, True)
                ilzk__soby = 'def impl(left, right):\n'
                for i, kst__qowz in enumerate(lom__jcc):
                    if kst__qowz == -1:
                        ilzk__soby += f"""  df_arr{i} = bodo.libs.array_kernels.gen_na_array(len(left), float64_arr_type)
"""
                        continue
                    ilzk__soby += f"""  df_arr{i} = bodo.hiframes.pd_dataframe_ext.get_dataframe_data(left, {i})
"""
                    ilzk__soby += f"""  df_arr{i} {cbej__jmalb} bodo.hiframes.pd_dataframe_ext.get_dataframe_data(right, {kst__qowz})
"""
                data_args = ', '.join(f'df_arr{i}' for i in range(len(
                    tlzy__mjs)))
                index = (
                    'bodo.hiframes.pd_dataframe_ext.get_dataframe_index(left)')
                return _gen_init_df(ilzk__soby, tlzy__mjs, data_args, index,
                    extra_globals={'float64_arr_type': types.Array(types.
                    float64, 1, 'C')})
            ilzk__soby = 'def impl(left, right):\n'
            for i in range(len(left.columns)):
                ilzk__soby += (
                    """  df_arr{0} = bodo.hiframes.pd_dataframe_ext.get_dataframe_data(left, {0})
"""
                    .format(i))
                ilzk__soby += '  df_arr{0} {1} right\n'.format(i, cbej__jmalb)
            data_args = ', '.join('df_arr{}'.format(i) for i in range(len(
                left.columns)))
            index = 'bodo.hiframes.pd_dataframe_ext.get_dataframe_index(left)'
            return _gen_init_df(ilzk__soby, left.columns, data_args, index)
    return overload_dataframe_inplace_binary_op


def _install_inplace_binary_ops():
    for op in bodo.hiframes.pd_series_ext.series_inplace_binary_ops:
        wwjmn__vhf = create_inplace_binary_op_overload(op)
        overload(op, no_unliteral=True)(wwjmn__vhf)


_install_inplace_binary_ops()


def create_unary_op_overload(op):

    def overload_dataframe_unary_op(df):
        if isinstance(df, DataFrameType):
            cbej__jmalb = numba.core.utils.OPERATORS_TO_BUILTINS[op]
            check_runtime_cols_unsupported(df, cbej__jmalb)
            data_args = ', '.join(
                '{1} bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {0})'
                .format(i, cbej__jmalb) for i in range(len(df.columns)))
            header = 'def impl(df):\n'
            return _gen_init_df(header, df.columns, data_args)
    return overload_dataframe_unary_op


def _install_unary_ops():
    for op in bodo.hiframes.pd_series_ext.series_unary_ops:
        wwjmn__vhf = create_unary_op_overload(op)
        overload(op, no_unliteral=True)(wwjmn__vhf)


_install_unary_ops()


def overload_isna(obj):
    check_runtime_cols_unsupported(obj, 'pd.isna()')
    if isinstance(obj, (DataFrameType, SeriesType)
        ) or bodo.hiframes.pd_index_ext.is_pd_index_type(obj):
        return lambda obj: obj.isna()
    if is_array_typ(obj):

        def impl(obj):
            numba.parfors.parfor.init_prange()
            n = len(obj)
            jom__srd = np.empty(n, np.bool_)
            for i in numba.parfors.parfor.internal_prange(n):
                jom__srd[i] = bodo.libs.array_kernels.isna(obj, i)
            return jom__srd
        return impl


overload(pd.isna, inline='always')(overload_isna)
overload(pd.isnull, inline='always')(overload_isna)


@overload(pd.isna)
@overload(pd.isnull)
def overload_isna_scalar(obj):
    if isinstance(obj, (DataFrameType, SeriesType)
        ) or bodo.hiframes.pd_index_ext.is_pd_index_type(obj) or is_array_typ(
        obj):
        return
    if isinstance(obj, (types.List, types.UniTuple)):

        def impl(obj):
            n = len(obj)
            jom__srd = np.empty(n, np.bool_)
            for i in range(n):
                jom__srd[i] = pd.isna(obj[i])
            return jom__srd
        return impl
    obj = types.unliteral(obj)
    if obj == bodo.string_type:
        return lambda obj: unliteral_val(False)
    if isinstance(obj, types.Integer):
        return lambda obj: unliteral_val(False)
    if isinstance(obj, types.Float):
        return lambda obj: np.isnan(obj)
    if isinstance(obj, (types.NPDatetime, types.NPTimedelta)):
        return lambda obj: np.isnat(obj)
    if obj == types.none:
        return lambda obj: unliteral_val(True)
    if isinstance(obj, bodo.hiframes.pd_timestamp_ext.PandasTimestampType):
        return lambda obj: np.isnat(bodo.hiframes.pd_timestamp_ext.
            integer_to_dt64(obj.value))
    if obj == bodo.hiframes.datetime_timedelta_ext.pd_timedelta_type:
        return lambda obj: np.isnat(bodo.hiframes.pd_timestamp_ext.
            integer_to_timedelta64(obj.value))
    if isinstance(obj, types.Optional):
        return lambda obj: obj is None
    return lambda obj: unliteral_val(False)


@overload(operator.setitem, no_unliteral=True)
def overload_setitem_arr_none(A, idx, val):
    if is_array_typ(A, False) and isinstance(idx, types.Integer
        ) and val == types.none:
        return lambda A, idx, val: bodo.libs.array_kernels.setna(A, idx)


def overload_notna(obj):
    check_runtime_cols_unsupported(obj, 'pd.notna()')
    if isinstance(obj, (DataFrameType, SeriesType)):
        return lambda obj: obj.notna()
    if isinstance(obj, (types.List, types.UniTuple)) or is_array_typ(obj,
        include_index_series=True):
        return lambda obj: ~pd.isna(obj)
    return lambda obj: not pd.isna(obj)


overload(pd.notna, inline='always', no_unliteral=True)(overload_notna)
overload(pd.notnull, inline='always', no_unliteral=True)(overload_notna)


def _get_pd_dtype_str(t):
    if t.dtype == types.NPDatetime('ns'):
        return "'datetime64[ns]'"
    return bodo.ir.csv_ext._get_pd_dtype_str(t)


@overload_method(DataFrameType, 'replace', inline='always', no_unliteral=True)
def overload_dataframe_replace(df, to_replace=None, value=None, inplace=
    False, limit=None, regex=False, method='pad'):
    check_runtime_cols_unsupported(df, 'DataFrame.replace()')
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(df,
        'DataFrame.replace()')
    if is_overload_none(to_replace):
        raise BodoError('replace(): to_replace value of None is not supported')
    wdxk__vydem = {'inplace': inplace, 'limit': limit, 'regex': regex,
        'method': method}
    jyskm__yjr = {'inplace': False, 'limit': None, 'regex': False, 'method':
        'pad'}
    check_unsupported_args('replace', wdxk__vydem, jyskm__yjr, package_name
        ='pandas', module_name='DataFrame')
    data_args = ', '.join(
        f'df.iloc[:, {i}].replace(to_replace, value).values' for i in range
        (len(df.columns)))
    header = """def impl(df, to_replace=None, value=None, inplace=False, limit=None, regex=False, method='pad'):
"""
    return _gen_init_df(header, df.columns, data_args)


def _is_col_access(expr_node):
    xaxhl__mgg = str(expr_node)
    return xaxhl__mgg.startswith('(left.') or xaxhl__mgg.startswith('(right.')


def _insert_NA_cond(expr_node, left_columns, left_data, right_columns,
    right_data):
    fly__nnnak = {'left': 0, 'right': 0, 'NOT_NA': 0}
    env = pd.core.computation.scope.ensure_scope(2, {}, {}, (fly__nnnak,))
    dmop__ahxm = pd.core.computation.parsing.clean_column_name

    def append_null_checks(expr_node, null_set):
        if not null_set:
            return expr_node
        dioea__ckqyt = ' & '.join([('NOT_NA.`' + x + '`') for x in null_set])
        anz__ummxx = {('NOT_NA', dmop__ahxm(jlt__dtxm)): jlt__dtxm for
            jlt__dtxm in null_set}
        lwv__cpw, _, _ = _parse_query_expr(dioea__ckqyt, env, [], [], None,
            join_cleaned_cols=anz__ummxx)
        yjni__ukicw = (pd.core.computation.ops.BinOp.
            _disallow_scalar_only_bool_ops)
        pd.core.computation.ops.BinOp._disallow_scalar_only_bool_ops = (lambda
            self: None)
        try:
            gikv__bgcni = pd.core.computation.ops.BinOp('&', lwv__cpw,
                expr_node)
        finally:
            (pd.core.computation.ops.BinOp._disallow_scalar_only_bool_ops
                ) = yjni__ukicw
        return gikv__bgcni

    def _insert_NA_cond_body(expr_node, null_set):
        if isinstance(expr_node, pd.core.computation.ops.BinOp):
            if expr_node.op == '|':
                kqza__lsqc = set()
                rejo__xcdry = set()
                qcxa__hayjg = _insert_NA_cond_body(expr_node.lhs, kqza__lsqc)
                zdcc__gcihe = _insert_NA_cond_body(expr_node.rhs, rejo__xcdry)
                pdkb__uhvra = kqza__lsqc.intersection(rejo__xcdry)
                kqza__lsqc.difference_update(pdkb__uhvra)
                rejo__xcdry.difference_update(pdkb__uhvra)
                null_set.update(pdkb__uhvra)
                expr_node.lhs = append_null_checks(qcxa__hayjg, kqza__lsqc)
                expr_node.rhs = append_null_checks(zdcc__gcihe, rejo__xcdry)
                expr_node.operands = expr_node.lhs, expr_node.rhs
            else:
                expr_node.lhs = _insert_NA_cond_body(expr_node.lhs, null_set)
                expr_node.rhs = _insert_NA_cond_body(expr_node.rhs, null_set)
        elif _is_col_access(expr_node):
            tzrfi__gdm = expr_node.name
            wbr__gfu, col_name = tzrfi__gdm.split('.')
            if wbr__gfu == 'left':
                zajf__ctngm = left_columns
                data = left_data
            else:
                zajf__ctngm = right_columns
                data = right_data
            nqbtj__frjgh = data[zajf__ctngm.index(col_name)]
            if bodo.utils.typing.is_nullable(nqbtj__frjgh):
                null_set.add(expr_node.name)
        return expr_node
    null_set = set()
    hxegc__yze = _insert_NA_cond_body(expr_node, null_set)
    return append_null_checks(expr_node, null_set)


def _extract_equal_conds(expr_node):
    if not hasattr(expr_node, 'op'):
        return [], [], expr_node
    if expr_node.op == '==' and _is_col_access(expr_node.lhs
        ) and _is_col_access(expr_node.rhs):
        arul__jkc = str(expr_node.lhs)
        xqv__cjue = str(expr_node.rhs)
        if arul__jkc.startswith('(left.') and xqv__cjue.startswith('(left.'
            ) or arul__jkc.startswith('(right.') and xqv__cjue.startswith(
            '(right.'):
            return [], [], expr_node
        left_on = [arul__jkc.split('.')[1][:-1]]
        right_on = [xqv__cjue.split('.')[1][:-1]]
        if arul__jkc.startswith('(right.'):
            return right_on, left_on, None
        return left_on, right_on, None
    if expr_node.op == '&':
        lgwoz__cugdh, dca__nkb, bzal__adkks = _extract_equal_conds(expr_node
            .lhs)
        hmzsj__ctab, xgedl__lvcz, ablpl__mzuc = _extract_equal_conds(expr_node
            .rhs)
        left_on = lgwoz__cugdh + hmzsj__ctab
        right_on = dca__nkb + xgedl__lvcz
        if bzal__adkks is None:
            return left_on, right_on, ablpl__mzuc
        if ablpl__mzuc is None:
            return left_on, right_on, bzal__adkks
        expr_node.lhs = bzal__adkks
        expr_node.rhs = ablpl__mzuc
        expr_node.operands = expr_node.lhs, expr_node.rhs
        return left_on, right_on, expr_node
    return [], [], expr_node


def _parse_merge_cond(on_str, left_columns, left_data, right_columns,
    right_data):
    fly__nnnak = {'left': 0, 'right': 0}
    env = pd.core.computation.scope.ensure_scope(2, {}, {}, (fly__nnnak,))
    cvdjg__zik = dict()
    dmop__ahxm = pd.core.computation.parsing.clean_column_name
    for name, wnayy__ctpb in (('left', left_columns), ('right', right_columns)
        ):
        for jlt__dtxm in wnayy__ctpb:
            ynheb__eyuf = dmop__ahxm(jlt__dtxm)
            qmubn__zbsyu = name, ynheb__eyuf
            if qmubn__zbsyu in cvdjg__zik:
                raise_bodo_error(
                    f"pd.merge(): {name} table contains two columns that are escaped to the same Python identifier '{jlt__dtxm}' and '{cvdjg__zik[ynheb__eyuf]}' Please rename one of these columns. To avoid this issue, please use names that are valid Python identifiers."
                    )
            cvdjg__zik[qmubn__zbsyu] = jlt__dtxm
    ccz__mgokc, _, _ = _parse_query_expr(on_str, env, [], [], None,
        join_cleaned_cols=cvdjg__zik)
    left_on, right_on, fgi__hqlgc = _extract_equal_conds(ccz__mgokc.terms)
    return left_on, right_on, _insert_NA_cond(fgi__hqlgc, left_columns,
        left_data, right_columns, right_data)


@overload_method(DataFrameType, 'merge', inline='always', no_unliteral=True)
@overload(pd.merge, inline='always', no_unliteral=True)
def overload_dataframe_merge(left, right, how='inner', on=None, left_on=
    None, right_on=None, left_index=False, right_index=False, sort=False,
    suffixes=('_x', '_y'), copy=True, indicator=False, validate=None,
    _bodo_na_equal=True):
    check_runtime_cols_unsupported(left, 'DataFrame.merge()')
    check_runtime_cols_unsupported(right, 'DataFrame.merge()')
    tyy__szp = dict(sort=sort, copy=copy, validate=validate)
    vtdv__ntf = dict(sort=False, copy=True, validate=None)
    check_unsupported_args('DataFrame.merge', tyy__szp, vtdv__ntf,
        package_name='pandas', module_name='DataFrame')
    validate_merge_spec(left, right, how, on, left_on, right_on, left_index,
        right_index, sort, suffixes, copy, indicator, validate)
    how = get_overload_const_str(how)
    kou__poly = tuple(sorted(set(left.columns) & set(right.columns), key=lambda
        k: str(k)))
    stu__tywq = ''
    if not is_overload_none(on):
        left_on = right_on = on
        if is_overload_constant_str(on):
            on_str = get_overload_const_str(on)
            if on_str not in kou__poly and ('left.' in on_str or 'right.' in
                on_str):
                left_on, right_on, rnv__qmaj = _parse_merge_cond(on_str,
                    left.columns, left.data, right.columns, right.data)
                if rnv__qmaj is None:
                    stu__tywq = ''
                else:
                    stu__tywq = str(rnv__qmaj)
    if is_overload_none(on) and is_overload_none(left_on) and is_overload_none(
        right_on) and is_overload_false(left_index) and is_overload_false(
        right_index):
        left_keys = kou__poly
        right_keys = kou__poly
    else:
        if is_overload_true(left_index):
            left_keys = ['$_bodo_index_']
        else:
            left_keys = get_overload_const_list(left_on)
            validate_keys(left_keys, left)
        if is_overload_true(right_index):
            right_keys = ['$_bodo_index_']
        else:
            right_keys = get_overload_const_list(right_on)
            validate_keys(right_keys, right)
    if not is_overload_bool(indicator):
        raise_bodo_error(
            'DataFrame.merge(): indicator must be a constant boolean')
    indicator_val = get_overload_const_bool(indicator)
    if not is_overload_bool(_bodo_na_equal):
        raise_bodo_error(
            'DataFrame.merge(): bodo extension _bodo_na_equal must be a constant boolean'
            )
    cxsgx__ovcf = get_overload_const_bool(_bodo_na_equal)
    validate_keys_length(left_index, right_index, left_keys, right_keys)
    validate_keys_dtypes(left, right, left_index, right_index, left_keys,
        right_keys)
    if is_overload_constant_tuple(suffixes):
        aky__euajp = get_overload_const_tuple(suffixes)
    if is_overload_constant_list(suffixes):
        aky__euajp = list(get_overload_const_list(suffixes))
    suffix_x = aky__euajp[0]
    suffix_y = aky__euajp[1]
    validate_unicity_output_column_names(suffix_x, suffix_y, left_keys,
        right_keys, left.columns, right.columns, indicator_val)
    left_keys = gen_const_tup(left_keys)
    right_keys = gen_const_tup(right_keys)
    ilzk__soby = "def _impl(left, right, how='inner', on=None, left_on=None,\n"
    ilzk__soby += (
        '    right_on=None, left_index=False, right_index=False, sort=False,\n'
        )
    ilzk__soby += """    suffixes=('_x', '_y'), copy=True, indicator=False, validate=None, _bodo_na_equal=True):
"""
    ilzk__soby += (
        """  return bodo.hiframes.pd_dataframe_ext.join_dummy(left, right, {}, {}, '{}', '{}', '{}', False, {}, {}, '{}')
"""
        .format(left_keys, right_keys, how, suffix_x, suffix_y,
        indicator_val, cxsgx__ovcf, stu__tywq))
    lxd__swvja = {}
    exec(ilzk__soby, {'bodo': bodo}, lxd__swvja)
    _impl = lxd__swvja['_impl']
    return _impl


def common_validate_merge_merge_asof_spec(name_func, left, right, on,
    left_on, right_on, left_index, right_index, suffixes):
    if not isinstance(left, DataFrameType) or not isinstance(right,
        DataFrameType):
        raise BodoError(name_func + '() requires dataframe inputs')
    valid_dataframe_column_types = (ArrayItemArrayType, MapArrayType,
        StructArrayType, CategoricalArrayType, types.Array,
        IntegerArrayType, FloatingArrayType, DecimalArrayType,
        IntervalArrayType, bodo.DatetimeArrayType, TimeArrayType)
    imph__ojrg = {string_array_type, dict_str_arr_type, binary_array_type,
        datetime_date_array_type, datetime_timedelta_array_type, boolean_array}
    uhf__hvwsb = {get_overload_const_str(mvo__oea) for mvo__oea in (left_on,
        right_on, on) if is_overload_constant_str(mvo__oea)}
    for df in (left, right):
        for i, jlt__dtxm in enumerate(df.data):
            if not isinstance(jlt__dtxm, valid_dataframe_column_types
                ) and jlt__dtxm not in imph__ojrg:
                raise BodoError(
                    f'{name_func}(): use of column with {type(jlt__dtxm)} in merge unsupported'
                    )
            if df.columns[i] in uhf__hvwsb and isinstance(jlt__dtxm,
                MapArrayType):
                raise BodoError(
                    f'{name_func}(): merge on MapArrayType unsupported')
    ensure_constant_arg(name_func, 'left_index', left_index, bool)
    ensure_constant_arg(name_func, 'right_index', right_index, bool)
    if not is_overload_constant_tuple(suffixes
        ) and not is_overload_constant_list(suffixes):
        raise_bodo_error(name_func +
            "(): suffixes parameters should be ['_left', '_right']")
    if is_overload_constant_tuple(suffixes):
        aky__euajp = get_overload_const_tuple(suffixes)
    if is_overload_constant_list(suffixes):
        aky__euajp = list(get_overload_const_list(suffixes))
    if len(aky__euajp) != 2:
        raise BodoError(name_func +
            '(): The number of suffixes should be exactly 2')
    kou__poly = tuple(set(left.columns) & set(right.columns))
    if not is_overload_none(on):
        kwf__rxmcy = False
        if is_overload_constant_str(on):
            on_str = get_overload_const_str(on)
            kwf__rxmcy = on_str not in kou__poly and ('left.' in on_str or 
                'right.' in on_str)
        if len(kou__poly) == 0 and not kwf__rxmcy:
            raise_bodo_error(name_func +
                '(): No common columns to perform merge on. Merge options: left_on={lon}, right_on={ron}, left_index={lidx}, right_index={ridx}'
                .format(lon=is_overload_true(left_on), ron=is_overload_true
                (right_on), lidx=is_overload_true(left_index), ridx=
                is_overload_true(right_index)))
        if not is_overload_none(left_on) or not is_overload_none(right_on):
            raise BodoError(name_func +
                '(): Can only pass argument "on" OR "left_on" and "right_on", not a combination of both.'
                )
    if (is_overload_true(left_index) or not is_overload_none(left_on)
        ) and is_overload_none(right_on) and not is_overload_true(right_index):
        raise BodoError(name_func +
            '(): Must pass right_on or right_index=True')
    if (is_overload_true(right_index) or not is_overload_none(right_on)
        ) and is_overload_none(left_on) and not is_overload_true(left_index):
        raise BodoError(name_func + '(): Must pass left_on or left_index=True')


def validate_merge_spec(left, right, how, on, left_on, right_on, left_index,
    right_index, sort, suffixes, copy, indicator, validate):
    common_validate_merge_merge_asof_spec('merge', left, right, on, left_on,
        right_on, left_index, right_index, suffixes)
    ensure_constant_values('merge', 'how', how, ('left', 'right', 'outer',
        'inner', 'cross'))


def validate_merge_asof_spec(left, right, on, left_on, right_on, left_index,
    right_index, by, left_by, right_by, suffixes, tolerance,
    allow_exact_matches, direction):
    common_validate_merge_merge_asof_spec('merge_asof', left, right, on,
        left_on, right_on, left_index, right_index, suffixes)
    if not is_overload_true(allow_exact_matches):
        raise BodoError(
            'merge_asof(): allow_exact_matches parameter only supports default value True'
            )
    if not is_overload_none(tolerance):
        raise BodoError(
            'merge_asof(): tolerance parameter only supports default value None'
            )
    if not is_overload_none(by):
        raise BodoError(
            'merge_asof(): by parameter only supports default value None')
    if not is_overload_none(left_by):
        raise BodoError(
            'merge_asof(): left_by parameter only supports default value None')
    if not is_overload_none(right_by):
        raise BodoError(
            'merge_asof(): right_by parameter only supports default value None'
            )
    if not is_overload_constant_str(direction):
        raise BodoError(
            'merge_asof(): direction parameter should be of type str')
    else:
        direction = get_overload_const_str(direction)
        if direction != 'backward':
            raise BodoError(
                "merge_asof(): direction parameter only supports default value 'backward'"
                )


def validate_merge_asof_keys_length(left_on, right_on, left_index,
    right_index, left_keys, right_keys):
    if not is_overload_true(left_index) and not is_overload_true(right_index):
        if len(right_keys) != len(left_keys):
            raise BodoError('merge(): len(right_on) must equal len(left_on)')
    if not is_overload_none(left_on) and is_overload_true(right_index):
        raise BodoError(
            'merge(): right_index = True and specifying left_on is not suppported yet.'
            )
    if not is_overload_none(right_on) and is_overload_true(left_index):
        raise BodoError(
            'merge(): left_index = True and specifying right_on is not suppported yet.'
            )


def validate_keys_length(left_index, right_index, left_keys, right_keys):
    if not is_overload_true(left_index) and not is_overload_true(right_index):
        if len(right_keys) != len(left_keys):
            raise BodoError('merge(): len(right_on) must equal len(left_on)')
    if is_overload_true(right_index):
        if len(left_keys) != 1:
            raise BodoError(
                'merge(): len(left_on) must equal the number of levels in the index of "right", which is 1'
                )
    if is_overload_true(left_index):
        if len(right_keys) != 1:
            raise BodoError(
                'merge(): len(right_on) must equal the number of levels in the index of "left", which is 1'
                )


def validate_keys_dtypes(left, right, left_index, right_index, left_keys,
    right_keys):
    egi__xnza = numba.core.registry.cpu_target.typing_context
    if is_overload_true(left_index) or is_overload_true(right_index):
        if is_overload_true(left_index) and is_overload_true(right_index):
            glg__mexdo = left.index
            inum__ozovo = isinstance(glg__mexdo, StringIndexType)
            chm__jrw = right.index
            yiv__gaxmp = isinstance(chm__jrw, StringIndexType)
        elif is_overload_true(left_index):
            glg__mexdo = left.index
            inum__ozovo = isinstance(glg__mexdo, StringIndexType)
            chm__jrw = right.data[right.columns.index(right_keys[0])]
            yiv__gaxmp = chm__jrw.dtype == string_type
        elif is_overload_true(right_index):
            glg__mexdo = left.data[left.columns.index(left_keys[0])]
            inum__ozovo = glg__mexdo.dtype == string_type
            chm__jrw = right.index
            yiv__gaxmp = isinstance(chm__jrw, StringIndexType)
        if inum__ozovo and yiv__gaxmp:
            return
        glg__mexdo = glg__mexdo.dtype
        chm__jrw = chm__jrw.dtype
        try:
            uffb__heqgn = egi__xnza.resolve_function_type(operator.eq, (
                glg__mexdo, chm__jrw), {})
        except:
            raise_bodo_error(
                'merge: You are trying to merge on {lk_dtype} and {rk_dtype} columns. If you wish to proceed you should use pd.concat'
                .format(lk_dtype=glg__mexdo, rk_dtype=chm__jrw))
    else:
        for uxdfs__vku, onh__bwmj in zip(left_keys, right_keys):
            glg__mexdo = left.data[left.columns.index(uxdfs__vku)].dtype
            sxk__qpt = left.data[left.columns.index(uxdfs__vku)]
            chm__jrw = right.data[right.columns.index(onh__bwmj)].dtype
            jydke__fon = right.data[right.columns.index(onh__bwmj)]
            if sxk__qpt == jydke__fon:
                continue
            emg__mkl = (
                'merge: You are trying to merge on column {lk} of {lk_dtype} and column {rk} of {rk_dtype}. If you wish to proceed you should use pd.concat'
                .format(lk=uxdfs__vku, lk_dtype=glg__mexdo, rk=onh__bwmj,
                rk_dtype=chm__jrw))
            wyy__gcv = glg__mexdo == string_type
            dduda__iang = chm__jrw == string_type
            if wyy__gcv ^ dduda__iang:
                raise_bodo_error(emg__mkl)
            try:
                uffb__heqgn = egi__xnza.resolve_function_type(operator.eq,
                    (glg__mexdo, chm__jrw), {})
            except:
                raise_bodo_error(emg__mkl)


def validate_keys(keys, df):
    amxtz__benis = set(keys).difference(set(df.columns))
    if len(amxtz__benis) > 0:
        if is_overload_constant_str(df.index.name_typ
            ) and get_overload_const_str(df.index.name_typ) in amxtz__benis:
            raise_bodo_error(
                f'merge(): use of index {df.index.name_typ} as key for on/left_on/right_on is unsupported'
                )
        raise_bodo_error(
            f"""merge(): invalid key {amxtz__benis} for on/left_on/right_on
merge supports only valid column names {df.columns}"""
            )


@overload_method(DataFrameType, 'join', inline='always', no_unliteral=True)
def overload_dataframe_join(left, other, on=None, how='left', lsuffix='',
    rsuffix='', sort=False):
    check_runtime_cols_unsupported(left, 'DataFrame.join()')
    check_runtime_cols_unsupported(other, 'DataFrame.join()')
    tyy__szp = dict(lsuffix=lsuffix, rsuffix=rsuffix)
    vtdv__ntf = dict(lsuffix='', rsuffix='')
    check_unsupported_args('DataFrame.join', tyy__szp, vtdv__ntf,
        package_name='pandas', module_name='DataFrame')
    validate_join_spec(left, other, on, how, lsuffix, rsuffix, sort)
    how = get_overload_const_str(how)
    if not is_overload_none(on):
        left_keys = get_overload_const_list(on)
    else:
        left_keys = ['$_bodo_index_']
    right_keys = ['$_bodo_index_']
    left_keys = gen_const_tup(left_keys)
    right_keys = gen_const_tup(right_keys)
    ilzk__soby = "def _impl(left, other, on=None, how='left',\n"
    ilzk__soby += "    lsuffix='', rsuffix='', sort=False):\n"
    ilzk__soby += (
        """  return bodo.hiframes.pd_dataframe_ext.join_dummy(left, other, {}, {}, '{}', '{}', '{}', True, False, True, '')
"""
        .format(left_keys, right_keys, how, lsuffix, rsuffix))
    lxd__swvja = {}
    exec(ilzk__soby, {'bodo': bodo}, lxd__swvja)
    _impl = lxd__swvja['_impl']
    return _impl


def validate_join_spec(left, other, on, how, lsuffix, rsuffix, sort):
    if not isinstance(other, DataFrameType):
        raise BodoError('join() requires dataframe inputs')
    ensure_constant_values('merge', 'how', how, ('left', 'right', 'outer',
        'inner'))
    if not is_overload_none(on) and len(get_overload_const_list(on)) != 1:
        raise BodoError('join(): len(on) must equals to 1 when specified.')
    if not is_overload_none(on):
        tsls__dqf = get_overload_const_list(on)
        validate_keys(tsls__dqf, left)
    if not is_overload_false(sort):
        raise BodoError(
            'join(): sort parameter only supports default value False')
    kou__poly = tuple(set(left.columns) & set(other.columns))
    if len(kou__poly) > 0:
        raise_bodo_error(
            'join(): not supporting joining on overlapping columns:{cols} Use DataFrame.merge() instead.'
            .format(cols=kou__poly))


def validate_unicity_output_column_names(suffix_x, suffix_y, left_keys,
    right_keys, left_columns, right_columns, indicator_val):
    xlzt__iprc = set(left_keys) & set(right_keys)
    vqpcp__komdo = set(left_columns) & set(right_columns)
    jjtm__ltaif = vqpcp__komdo - xlzt__iprc
    qfee__cswt = set(left_columns) - vqpcp__komdo
    zja__iyvoa = set(right_columns) - vqpcp__komdo
    zga__kscz = {}

    def insertOutColumn(col_name):
        if col_name in zga__kscz:
            raise_bodo_error(
                'join(): two columns happen to have the same name : {}'.
                format(col_name))
        zga__kscz[col_name] = 0
    for qeg__rvwx in xlzt__iprc:
        insertOutColumn(qeg__rvwx)
    for qeg__rvwx in jjtm__ltaif:
        bkio__ibgf = str(qeg__rvwx) + suffix_x
        syah__kid = str(qeg__rvwx) + suffix_y
        insertOutColumn(bkio__ibgf)
        insertOutColumn(syah__kid)
    for qeg__rvwx in qfee__cswt:
        insertOutColumn(qeg__rvwx)
    for qeg__rvwx in zja__iyvoa:
        insertOutColumn(qeg__rvwx)
    if indicator_val:
        insertOutColumn('_merge')


@overload(pd.merge_asof, inline='always', no_unliteral=True)
def overload_dataframe_merge_asof(left, right, on=None, left_on=None,
    right_on=None, left_index=False, right_index=False, by=None, left_by=
    None, right_by=None, suffixes=('_x', '_y'), tolerance=None,
    allow_exact_matches=True, direction='backward'):
    raise BodoError('pandas.merge_asof() not support yet')
    validate_merge_asof_spec(left, right, on, left_on, right_on, left_index,
        right_index, by, left_by, right_by, suffixes, tolerance,
        allow_exact_matches, direction)
    if not isinstance(left, DataFrameType) or not isinstance(right,
        DataFrameType):
        raise BodoError('merge_asof() requires dataframe inputs')
    kou__poly = tuple(sorted(set(left.columns) & set(right.columns), key=lambda
        k: str(k)))
    if not is_overload_none(on):
        left_on = right_on = on
    if is_overload_none(on) and is_overload_none(left_on) and is_overload_none(
        right_on) and is_overload_false(left_index) and is_overload_false(
        right_index):
        left_keys = kou__poly
        right_keys = kou__poly
    else:
        if is_overload_true(left_index):
            left_keys = ['$_bodo_index_']
        else:
            left_keys = get_overload_const_list(left_on)
            validate_keys(left_keys, left)
        if is_overload_true(right_index):
            right_keys = ['$_bodo_index_']
        else:
            right_keys = get_overload_const_list(right_on)
            validate_keys(right_keys, right)
    validate_merge_asof_keys_length(left_on, right_on, left_index,
        right_index, left_keys, right_keys)
    validate_keys_dtypes(left, right, left_index, right_index, left_keys,
        right_keys)
    left_keys = gen_const_tup(left_keys)
    right_keys = gen_const_tup(right_keys)
    if isinstance(suffixes, tuple):
        aky__euajp = suffixes
    if is_overload_constant_list(suffixes):
        aky__euajp = list(get_overload_const_list(suffixes))
    if isinstance(suffixes, types.Omitted):
        aky__euajp = suffixes.value
    suffix_x = aky__euajp[0]
    suffix_y = aky__euajp[1]
    ilzk__soby = (
        'def _impl(left, right, on=None, left_on=None, right_on=None,\n')
    ilzk__soby += (
        '    left_index=False, right_index=False, by=None, left_by=None,\n')
    ilzk__soby += "    right_by=None, suffixes=('_x', '_y'), tolerance=None,\n"
    ilzk__soby += "    allow_exact_matches=True, direction='backward'):\n"
    ilzk__soby += '  suffix_x = suffixes[0]\n'
    ilzk__soby += '  suffix_y = suffixes[1]\n'
    ilzk__soby += (
        """  return bodo.hiframes.pd_dataframe_ext.join_dummy(left, right, {}, {}, 'asof', '{}', '{}', False, False, True, '')
"""
        .format(left_keys, right_keys, suffix_x, suffix_y))
    lxd__swvja = {}
    exec(ilzk__soby, {'bodo': bodo}, lxd__swvja)
    _impl = lxd__swvja['_impl']
    return _impl


@overload_method(DataFrameType, 'groupby', inline='always', no_unliteral=True)
def overload_dataframe_groupby(df, by=None, axis=0, level=None, as_index=
    True, sort=False, group_keys=True, squeeze=False, observed=True, dropna
    =True, _bodo_num_shuffle_keys=-1):
    check_runtime_cols_unsupported(df, 'DataFrame.groupby()')
    validate_groupby_spec(df, by, axis, level, as_index, sort, group_keys,
        squeeze, observed, dropna, _bodo_num_shuffle_keys)

    def _impl(df, by=None, axis=0, level=None, as_index=True, sort=False,
        group_keys=True, squeeze=False, observed=True, dropna=True,
        _bodo_num_shuffle_keys=-1):
        return bodo.hiframes.pd_groupby_ext.init_groupby(df, by, as_index,
            dropna, _bodo_num_shuffle_keys)
    return _impl


def validate_groupby_spec(df, by, axis, level, as_index, sort, group_keys,
    squeeze, observed, dropna, _num_shuffle_keys):
    if is_overload_none(by):
        raise BodoError("groupby(): 'by' must be supplied.")
    if not is_overload_zero(axis):
        raise BodoError(
            "groupby(): 'axis' parameter only supports integer value 0.")
    if not is_overload_none(level):
        raise BodoError(
            "groupby(): 'level' is not supported since MultiIndex is not supported."
            )
    if not is_literal_type(by) and not is_overload_constant_list(by):
        raise_bodo_error(
            f"groupby(): 'by' parameter only supports a constant column label or column labels, not {by}."
            )
    if len(set(get_overload_const_list(by)).difference(set(df.columns))) > 0:
        raise_bodo_error(
            "groupby(): invalid key {} for 'by' (not available in columns {})."
            .format(get_overload_const_list(by), df.columns))
    if not is_overload_constant_bool(as_index):
        raise_bodo_error(
            "groupby(): 'as_index' parameter must be a constant bool, not {}."
            .format(as_index))
    if not is_overload_constant_bool(dropna):
        raise_bodo_error(
            "groupby(): 'dropna' parameter must be a constant bool, not {}."
            .format(dropna))
    if not is_overload_constant_int(_num_shuffle_keys):
        raise_bodo_error(
            f"groupby(): '_num_shuffle_keys' parameter must be a constant integer, not {_num_shuffle_keys}."
            )
    tyy__szp = dict(sort=sort, group_keys=group_keys, squeeze=squeeze,
        observed=observed)
    kiygq__jcqfn = dict(sort=False, group_keys=True, squeeze=False,
        observed=True)
    check_unsupported_args('Dataframe.groupby', tyy__szp, kiygq__jcqfn,
        package_name='pandas', module_name='GroupBy')


def pivot_error_checking(df, index, columns, values, func_name):
    uih__iunwn = func_name == 'DataFrame.pivot_table'
    if uih__iunwn:
        if is_overload_none(index) or not is_literal_type(index):
            raise_bodo_error(
                f"DataFrame.pivot_table(): 'index' argument is required and must be constant column labels"
                )
    elif not is_overload_none(index) and not is_literal_type(index):
        raise_bodo_error(
            f"{func_name}(): if 'index' argument is provided it must be constant column labels"
            )
    if is_overload_none(columns) or not is_literal_type(columns):
        raise_bodo_error(
            f"{func_name}(): 'columns' argument is required and must be a constant column label"
            )
    if not is_overload_none(values) and not is_literal_type(values):
        raise_bodo_error(
            f"{func_name}(): if 'values' argument is provided it must be constant column labels"
            )
    fnrcr__nqmp = get_literal_value(columns)
    if isinstance(fnrcr__nqmp, (list, tuple)):
        if len(fnrcr__nqmp) > 1:
            raise BodoError(
                f"{func_name}(): 'columns' argument must be a constant column label not a {fnrcr__nqmp}"
                )
        fnrcr__nqmp = fnrcr__nqmp[0]
    if fnrcr__nqmp not in df.columns:
        raise BodoError(
            f"{func_name}(): 'columns' column {fnrcr__nqmp} not found in DataFrame {df}."
            )
    qws__xzfzi = df.column_index[fnrcr__nqmp]
    if is_overload_none(index):
        rak__grb = []
        gdpza__kxe = []
    else:
        gdpza__kxe = get_literal_value(index)
        if not isinstance(gdpza__kxe, (list, tuple)):
            gdpza__kxe = [gdpza__kxe]
        rak__grb = []
        for index in gdpza__kxe:
            if index not in df.column_index:
                raise BodoError(
                    f"{func_name}(): 'index' column {index} not found in DataFrame {df}."
                    )
            rak__grb.append(df.column_index[index])
    if not (all(isinstance(kxm__lejo, int) for kxm__lejo in gdpza__kxe) or
        all(isinstance(kxm__lejo, str) for kxm__lejo in gdpza__kxe)):
        raise BodoError(
            f"{func_name}(): column names selected for 'index' must all share a common int or string type. Please convert your names to a common type using DataFrame.rename()"
            )
    if is_overload_none(values):
        uzmnd__zybgw = []
        ulkh__xdwwr = []
        gry__tvi = rak__grb + [qws__xzfzi]
        for i, kxm__lejo in enumerate(df.columns):
            if i not in gry__tvi:
                uzmnd__zybgw.append(i)
                ulkh__xdwwr.append(kxm__lejo)
    else:
        ulkh__xdwwr = get_literal_value(values)
        if not isinstance(ulkh__xdwwr, (list, tuple)):
            ulkh__xdwwr = [ulkh__xdwwr]
        uzmnd__zybgw = []
        for val in ulkh__xdwwr:
            if val not in df.column_index:
                raise BodoError(
                    f"{func_name}(): 'values' column {val} not found in DataFrame {df}."
                    )
            uzmnd__zybgw.append(df.column_index[val])
    zzu__iulk = set(uzmnd__zybgw) | set(rak__grb) | {qws__xzfzi}
    if len(zzu__iulk) != len(uzmnd__zybgw) + len(rak__grb) + 1:
        raise BodoError(
            f"{func_name}(): 'index', 'columns', and 'values' must all refer to different columns"
            )

    def check_valid_index_typ(index_column):
        if isinstance(index_column, (bodo.ArrayItemArrayType, bodo.
            MapArrayType, bodo.StructArrayType, bodo.TupleArrayType, bodo.
            IntervalArrayType)):
            raise BodoError(
                f"{func_name}(): 'index' DataFrame column must have scalar rows"
                )
        if isinstance(index_column, bodo.CategoricalArrayType):
            raise BodoError(
                f"{func_name}(): 'index' DataFrame column does not support categorical data"
                )
    if len(rak__grb) == 0:
        index = df.index
        if isinstance(index, MultiIndexType):
            raise BodoError(
                f"{func_name}(): 'index' cannot be None with a DataFrame with a multi-index"
                )
        if not isinstance(index, RangeIndexType):
            check_valid_index_typ(index.data)
        if not is_literal_type(df.index.name_typ):
            raise BodoError(
                f"{func_name}(): If 'index' is None, the name of the DataFrame's Index must be constant at compile-time"
                )
    else:
        for eiqa__mzvj in rak__grb:
            index_column = df.data[eiqa__mzvj]
            check_valid_index_typ(index_column)
    oqt__tvk = df.data[qws__xzfzi]
    if isinstance(oqt__tvk, (bodo.ArrayItemArrayType, bodo.MapArrayType,
        bodo.StructArrayType, bodo.TupleArrayType, bodo.IntervalArrayType)):
        raise BodoError(
            f"{func_name}(): 'columns' DataFrame column must have scalar rows")
    if isinstance(oqt__tvk, bodo.CategoricalArrayType):
        raise BodoError(
            f"{func_name}(): 'columns' DataFrame column does not support categorical data"
            )
    for vdzl__sho in uzmnd__zybgw:
        cow__buvbz = df.data[vdzl__sho]
        if isinstance(cow__buvbz, (bodo.ArrayItemArrayType, bodo.
            MapArrayType, bodo.StructArrayType, bodo.TupleArrayType)
            ) or cow__buvbz == bodo.binary_array_type:
            raise BodoError(
                f"{func_name}(): 'values' DataFrame column must have scalar rows"
                )
    return (gdpza__kxe, fnrcr__nqmp, ulkh__xdwwr, rak__grb, qws__xzfzi,
        uzmnd__zybgw)


@overload(pd.pivot, inline='always', no_unliteral=True)
@overload_method(DataFrameType, 'pivot', inline='always', no_unliteral=True)
def overload_dataframe_pivot(data, index=None, columns=None, values=None):
    check_runtime_cols_unsupported(data, 'DataFrame.pivot()')
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(data,
        'DataFrame.pivot()')
    if not isinstance(data, DataFrameType):
        raise BodoError("pandas.pivot(): 'data' argument must be a DataFrame")
    (gdpza__kxe, fnrcr__nqmp, ulkh__xdwwr, eiqa__mzvj, qws__xzfzi, vcvi__smwwy
        ) = (pivot_error_checking(data, index, columns, values,
        'DataFrame.pivot'))
    if len(gdpza__kxe) == 0:
        if is_overload_none(data.index.name_typ):
            ybct__vnreq = None,
        else:
            ybct__vnreq = get_literal_value(data.index.name_typ),
    else:
        ybct__vnreq = tuple(gdpza__kxe)
    gdpza__kxe = ColNamesMetaType(ybct__vnreq)
    ulkh__xdwwr = ColNamesMetaType(tuple(ulkh__xdwwr))
    fnrcr__nqmp = ColNamesMetaType((fnrcr__nqmp,))
    ilzk__soby = 'def impl(data, index=None, columns=None, values=None):\n'
    ilzk__soby += "    ev = tracing.Event('df.pivot')\n"
    ilzk__soby += f'    pivot_values = data.iloc[:, {qws__xzfzi}].unique()\n'
    ilzk__soby += '    result = bodo.hiframes.pd_dataframe_ext.pivot_impl(\n'
    if len(eiqa__mzvj) == 0:
        ilzk__soby += f"""        (bodo.utils.conversion.index_to_array(bodo.hiframes.pd_dataframe_ext.get_dataframe_index(data)),),
"""
    else:
        ilzk__soby += '        (\n'
        for gwkpa__cgui in eiqa__mzvj:
            ilzk__soby += f"""            bodo.hiframes.pd_dataframe_ext.get_dataframe_data(data, {gwkpa__cgui}),
"""
        ilzk__soby += '        ),\n'
    ilzk__soby += f"""        (bodo.hiframes.pd_dataframe_ext.get_dataframe_data(data, {qws__xzfzi}),),
"""
    ilzk__soby += '        (\n'
    for vdzl__sho in vcvi__smwwy:
        ilzk__soby += f"""            bodo.hiframes.pd_dataframe_ext.get_dataframe_data(data, {vdzl__sho}),
"""
    ilzk__soby += '        ),\n'
    ilzk__soby += '        pivot_values,\n'
    ilzk__soby += '        index_lit,\n'
    ilzk__soby += '        columns_lit,\n'
    ilzk__soby += '        values_lit,\n'
    ilzk__soby += '    )\n'
    ilzk__soby += '    ev.finalize()\n'
    ilzk__soby += '    return result\n'
    lxd__swvja = {}
    exec(ilzk__soby, {'bodo': bodo, 'index_lit': gdpza__kxe, 'columns_lit':
        fnrcr__nqmp, 'values_lit': ulkh__xdwwr, 'tracing': tracing}, lxd__swvja
        )
    impl = lxd__swvja['impl']
    return impl


@overload(pd.pivot_table, inline='always', no_unliteral=True)
@overload_method(DataFrameType, 'pivot_table', inline='always',
    no_unliteral=True)
def overload_dataframe_pivot_table(data, values=None, index=None, columns=
    None, aggfunc='mean', fill_value=None, margins=False, dropna=True,
    margins_name='All', observed=False, sort=True, _pivot_values=None):
    check_runtime_cols_unsupported(data, 'DataFrame.pivot_table()')
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(data,
        'DataFrame.pivot_table()')
    tyy__szp = dict(fill_value=fill_value, margins=margins, dropna=dropna,
        margins_name=margins_name, observed=observed, sort=sort)
    vtdv__ntf = dict(fill_value=None, margins=False, dropna=True,
        margins_name='All', observed=False, sort=True)
    check_unsupported_args('DataFrame.pivot_table', tyy__szp, vtdv__ntf,
        package_name='pandas', module_name='DataFrame')
    if not isinstance(data, DataFrameType):
        raise BodoError(
            "pandas.pivot_table(): 'data' argument must be a DataFrame")
    (gdpza__kxe, fnrcr__nqmp, ulkh__xdwwr, eiqa__mzvj, qws__xzfzi, vcvi__smwwy
        ) = (pivot_error_checking(data, index, columns, values,
        'DataFrame.pivot_table'))
    xdlhp__pzl = gdpza__kxe
    gdpza__kxe = ColNamesMetaType(tuple(gdpza__kxe))
    ulkh__xdwwr = ColNamesMetaType(tuple(ulkh__xdwwr))
    tzsl__vtir = fnrcr__nqmp
    fnrcr__nqmp = ColNamesMetaType((fnrcr__nqmp,))
    ilzk__soby = 'def impl(\n'
    ilzk__soby += '    data,\n'
    ilzk__soby += '    values=None,\n'
    ilzk__soby += '    index=None,\n'
    ilzk__soby += '    columns=None,\n'
    ilzk__soby += '    aggfunc="mean",\n'
    ilzk__soby += '    fill_value=None,\n'
    ilzk__soby += '    margins=False,\n'
    ilzk__soby += '    dropna=True,\n'
    ilzk__soby += '    margins_name="All",\n'
    ilzk__soby += '    observed=False,\n'
    ilzk__soby += '    sort=True,\n'
    ilzk__soby += '    _pivot_values=None,\n'
    ilzk__soby += '):\n'
    ilzk__soby += "    ev = tracing.Event('df.pivot_table')\n"
    umfww__buqs = eiqa__mzvj + [qws__xzfzi] + vcvi__smwwy
    ilzk__soby += f'    data = data.iloc[:, {umfww__buqs}]\n'
    lhfuk__gzu = xdlhp__pzl + [tzsl__vtir]
    if not is_overload_none(_pivot_values):
        lwfj__hhi = tuple(sorted(_pivot_values.meta))
        _pivot_values = ColNamesMetaType(lwfj__hhi)
        ilzk__soby += '    pivot_values = _pivot_values_arr\n'
        ilzk__soby += (
            f'    data = data[data.iloc[:, {len(eiqa__mzvj)}].isin(pivot_values)]\n'
            )
        if all(isinstance(kxm__lejo, str) for kxm__lejo in lwfj__hhi):
            nuz__zfwt = pd.array(lwfj__hhi, 'string')
        elif all(isinstance(kxm__lejo, int) for kxm__lejo in lwfj__hhi):
            nuz__zfwt = np.array(lwfj__hhi, 'int64')
        else:
            raise BodoError(
                f'pivot(): pivot values selcected via pivot JIT argument must all share a common int or string type.'
                )
    else:
        nuz__zfwt = None
    npyc__tlbq = is_overload_constant_str(aggfunc) and get_overload_const_str(
        aggfunc) == 'nunique'
    xdw__kaxid = len(lhfuk__gzu) if npyc__tlbq else len(xdlhp__pzl)
    ilzk__soby += f"""    data = data.groupby({lhfuk__gzu!r}, as_index=False, _bodo_num_shuffle_keys={xdw__kaxid}).agg(aggfunc)
"""
    if is_overload_none(_pivot_values):
        ilzk__soby += (
            f'    pivot_values = data.iloc[:, {len(eiqa__mzvj)}].unique()\n')
    ilzk__soby += '    result = bodo.hiframes.pd_dataframe_ext.pivot_impl(\n'
    ilzk__soby += '        (\n'
    for i in range(0, len(eiqa__mzvj)):
        ilzk__soby += (
            f'            bodo.hiframes.pd_dataframe_ext.get_dataframe_data(data, {i}),\n'
            )
    ilzk__soby += '        ),\n'
    ilzk__soby += f"""        (bodo.hiframes.pd_dataframe_ext.get_dataframe_data(data, {len(eiqa__mzvj)}),),
"""
    ilzk__soby += '        (\n'
    for i in range(len(eiqa__mzvj) + 1, len(vcvi__smwwy) + len(eiqa__mzvj) + 1
        ):
        ilzk__soby += (
            f'            bodo.hiframes.pd_dataframe_ext.get_dataframe_data(data, {i}),\n'
            )
    ilzk__soby += '        ),\n'
    ilzk__soby += '        pivot_values,\n'
    ilzk__soby += '        index_lit,\n'
    ilzk__soby += '        columns_lit,\n'
    ilzk__soby += '        values_lit,\n'
    ilzk__soby += '        check_duplicates=False,\n'
    ilzk__soby += f'        is_already_shuffled={not npyc__tlbq},\n'
    ilzk__soby += '        _constant_pivot_values=_constant_pivot_values,\n'
    ilzk__soby += '    )\n'
    ilzk__soby += '    ev.finalize()\n'
    ilzk__soby += '    return result\n'
    lxd__swvja = {}
    exec(ilzk__soby, {'bodo': bodo, 'numba': numba, 'index_lit': gdpza__kxe,
        'columns_lit': fnrcr__nqmp, 'values_lit': ulkh__xdwwr,
        '_pivot_values_arr': nuz__zfwt, '_constant_pivot_values':
        _pivot_values, 'tracing': tracing}, lxd__swvja)
    impl = lxd__swvja['impl']
    return impl


@overload(pd.melt, inline='always', no_unliteral=True)
@overload_method(DataFrameType, 'melt', inline='always', no_unliteral=True)
def overload_dataframe_melt(frame, id_vars=None, value_vars=None, var_name=
    None, value_name='value', col_level=None, ignore_index=True):
    tyy__szp = dict(col_level=col_level, ignore_index=ignore_index)
    vtdv__ntf = dict(col_level=None, ignore_index=True)
    check_unsupported_args('DataFrame.melt', tyy__szp, vtdv__ntf,
        package_name='pandas', module_name='DataFrame')
    if not isinstance(frame, DataFrameType):
        raise BodoError("pandas.melt(): 'frame' argument must be a DataFrame.")
    if not is_overload_none(id_vars) and not is_literal_type(id_vars):
        raise_bodo_error(
            "DataFrame.melt(): 'id_vars', if specified, must be a literal.")
    if not is_overload_none(value_vars) and not is_literal_type(value_vars):
        raise_bodo_error(
            "DataFrame.melt(): 'value_vars', if specified, must be a literal.")
    if not is_overload_none(var_name) and not (is_literal_type(var_name) and
        (is_scalar_type(var_name) or isinstance(value_name, types.Omitted))):
        raise_bodo_error(
            "DataFrame.melt(): 'var_name', if specified, must be a literal.")
    if value_name != 'value' and not (is_literal_type(value_name) and (
        is_scalar_type(value_name) or isinstance(value_name, types.Omitted))):
        raise_bodo_error(
            "DataFrame.melt(): 'value_name', if specified, must be a literal.")
    var_name = get_literal_value(var_name) if not is_overload_none(var_name
        ) else 'variable'
    value_name = get_literal_value(value_name
        ) if value_name != 'value' else 'value'
    tnx__mhfxq = get_literal_value(id_vars) if not is_overload_none(id_vars
        ) else []
    if not isinstance(tnx__mhfxq, (list, tuple)):
        tnx__mhfxq = [tnx__mhfxq]
    for kxm__lejo in tnx__mhfxq:
        if kxm__lejo not in frame.columns:
            raise BodoError(
                f"DataFrame.melt(): 'id_vars' column {kxm__lejo} not found in {frame}."
                )
    aqq__juai = [frame.column_index[i] for i in tnx__mhfxq]
    if is_overload_none(value_vars):
        ukwi__cmerp = []
        uym__lgi = []
        for i, kxm__lejo in enumerate(frame.columns):
            if i not in aqq__juai:
                ukwi__cmerp.append(i)
                uym__lgi.append(kxm__lejo)
    else:
        uym__lgi = get_literal_value(value_vars)
        if not isinstance(uym__lgi, (list, tuple)):
            uym__lgi = [uym__lgi]
        uym__lgi = [v for v in uym__lgi if v not in tnx__mhfxq]
        if not uym__lgi:
            raise BodoError(
                "DataFrame.melt(): currently empty 'value_vars' is unsupported."
                )
        ukwi__cmerp = []
        for val in uym__lgi:
            if val not in frame.column_index:
                raise BodoError(
                    f"DataFrame.melt(): 'value_vars' column {val} not found in DataFrame {frame}."
                    )
            ukwi__cmerp.append(frame.column_index[val])
    for kxm__lejo in uym__lgi:
        if kxm__lejo not in frame.columns:
            raise BodoError(
                f"DataFrame.melt(): 'value_vars' column {kxm__lejo} not found in {frame}."
                )
    if not (all(isinstance(kxm__lejo, int) for kxm__lejo in uym__lgi) or
        all(isinstance(kxm__lejo, str) for kxm__lejo in uym__lgi)):
        raise BodoError(
            f"DataFrame.melt(): column names selected for 'value_vars' must all share a common int or string type. Please convert your names to a common type using DataFrame.rename()"
            )
    tnsxw__cgf = frame.data[ukwi__cmerp[0]]
    zlyt__kqiue = [frame.data[i].dtype for i in ukwi__cmerp]
    ukwi__cmerp = np.array(ukwi__cmerp, dtype=np.int64)
    aqq__juai = np.array(aqq__juai, dtype=np.int64)
    _, ica__uegv = bodo.utils.typing.get_common_scalar_dtype(zlyt__kqiue)
    if not ica__uegv:
        raise BodoError(
            "DataFrame.melt(): columns selected in 'value_vars' must have a unifiable type."
            )
    extra_globals = {'np': np, 'value_lit': uym__lgi, 'val_type': tnsxw__cgf}
    header = 'def impl(\n'
    header += '  frame,\n'
    header += '  id_vars=None,\n'
    header += '  value_vars=None,\n'
    header += '  var_name=None,\n'
    header += "  value_name='value',\n"
    header += '  col_level=None,\n'
    header += '  ignore_index=True,\n'
    header += '):\n'
    header += (
        '  dummy_id = bodo.hiframes.pd_dataframe_ext.get_dataframe_data(frame, 0)\n'
        )
    if frame.is_table_format and all(v == tnsxw__cgf.dtype for v in zlyt__kqiue
        ):
        extra_globals['value_idxs'] = bodo.utils.typing.MetaType(tuple(
            ukwi__cmerp))
        header += (
            '  table = bodo.hiframes.pd_dataframe_ext.get_dataframe_table(frame)\n'
            )
        header += (
            '  val_col = bodo.utils.table_utils.table_concat(table, value_idxs, val_type)\n'
            )
    elif len(uym__lgi) == 1:
        header += f"""  val_col = bodo.hiframes.pd_dataframe_ext.get_dataframe_data(frame, {ukwi__cmerp[0]})
"""
    else:
        ybmde__fbg = ', '.join(
            f'bodo.hiframes.pd_dataframe_ext.get_dataframe_data(frame, {i})'
             for i in ukwi__cmerp)
        header += (
            f'  val_col = bodo.libs.array_kernels.concat(({ybmde__fbg},))\n')
    header += """  var_col = bodo.libs.array_kernels.repeat_like(bodo.utils.conversion.coerce_to_array(value_lit), dummy_id)
"""
    for i in aqq__juai:
        header += (
            f'  id{i} = bodo.hiframes.pd_dataframe_ext.get_dataframe_data(frame, {i})\n'
            )
        header += (
            f'  out_id{i} = bodo.libs.array_kernels.concat([id{i}] * {len(uym__lgi)})\n'
            )
    vqqj__keo = ', '.join(f'out_id{i}' for i in aqq__juai) + (', ' if len(
        aqq__juai) > 0 else '')
    data_args = vqqj__keo + 'var_col, val_col'
    columns = tuple(tnx__mhfxq + [var_name, value_name])
    index = (
        f'bodo.hiframes.pd_index_ext.init_range_index(0, len(frame) * {len(uym__lgi)}, 1, None)'
        )
    return _gen_init_df(header, columns, data_args, index, extra_globals)


@overload(pd.crosstab, inline='always', no_unliteral=True)
def crosstab_overload(index, columns, values=None, rownames=None, colnames=
    None, aggfunc=None, margins=False, margins_name='All', dropna=True,
    normalize=False, _pivot_values=None):
    raise BodoError(f'pandas.crosstab() not supported yet')
    tyy__szp = dict(values=values, rownames=rownames, colnames=colnames,
        aggfunc=aggfunc, margins=margins, margins_name=margins_name, dropna
        =dropna, normalize=normalize)
    vtdv__ntf = dict(values=None, rownames=None, colnames=None, aggfunc=
        None, margins=False, margins_name='All', dropna=True, normalize=False)
    check_unsupported_args('pandas.crosstab', tyy__szp, vtdv__ntf,
        package_name='pandas', module_name='DataFrame')
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(index,
        'pandas.crosstab()')
    if not isinstance(index, SeriesType):
        raise BodoError(
            f"pandas.crosstab(): 'index' argument only supported for Series types, found {index}"
            )
    if not isinstance(columns, SeriesType):
        raise BodoError(
            f"pandas.crosstab(): 'columns' argument only supported for Series types, found {columns}"
            )

    def _impl(index, columns, values=None, rownames=None, colnames=None,
        aggfunc=None, margins=False, margins_name='All', dropna=True,
        normalize=False, _pivot_values=None):
        return bodo.hiframes.pd_groupby_ext.crosstab_dummy(index, columns,
            _pivot_values)
    return _impl


@overload_method(DataFrameType, 'sort_values', inline='always',
    no_unliteral=True)
def overload_dataframe_sort_values(df, by, axis=0, ascending=True, inplace=
    False, kind='quicksort', na_position='last', ignore_index=False, key=
    None, _bodo_chunk_bounds=None, _bodo_transformed=False):
    check_runtime_cols_unsupported(df, 'DataFrame.sort_values()')
    tyy__szp = dict(ignore_index=ignore_index, key=key)
    vtdv__ntf = dict(ignore_index=False, key=None)
    check_unsupported_args('DataFrame.sort_values', tyy__szp, vtdv__ntf,
        package_name='pandas', module_name='DataFrame')
    handle_inplace_df_type_change(inplace, _bodo_transformed, 'sort_values')
    validate_sort_values_spec(df, by, axis, ascending, inplace, kind,
        na_position, _bodo_chunk_bounds)

    def _impl(df, by, axis=0, ascending=True, inplace=False, kind=
        'quicksort', na_position='last', ignore_index=False, key=None,
        _bodo_chunk_bounds=None, _bodo_transformed=False):
        return bodo.hiframes.pd_dataframe_ext.sort_values_dummy(df, by,
            ascending, inplace, na_position, _bodo_chunk_bounds)
    return _impl


def validate_sort_values_spec(df, by, axis, ascending, inplace, kind,
    na_position, _bodo_chunk_bounds):
    if is_overload_none(by) or not is_literal_type(by
        ) and not is_overload_constant_list(by):
        raise_bodo_error(
            "sort_values(): 'by' parameter only supports a constant column label or column labels. by={}"
            .format(by))
    ops__eqb = set(df.columns)
    if is_overload_constant_str(df.index.name_typ):
        ops__eqb.add(get_overload_const_str(df.index.name_typ))
    if is_overload_constant_tuple(by):
        yww__hsl = [get_overload_const_tuple(by)]
    else:
        yww__hsl = get_overload_const_list(by)
    yww__hsl = set((k, '') if (k, '') in ops__eqb else k for k in yww__hsl)
    if len(yww__hsl.difference(ops__eqb)) > 0:
        wngy__girmi = list(set(get_overload_const_list(by)).difference(
            ops__eqb))
        raise_bodo_error(f'sort_values(): invalid keys {wngy__girmi} for by.')
    if not is_overload_none(_bodo_chunk_bounds) and len(yww__hsl) != 1:
        raise_bodo_error(
            f'sort_values(): _bodo_chunk_bounds only supported when there is a single key.'
            )
    if not is_overload_zero(axis):
        raise_bodo_error(
            "sort_values(): 'axis' parameter only supports integer value 0.")
    if not is_overload_bool(ascending) and not is_overload_bool_list(ascending
        ):
        raise_bodo_error(
            "sort_values(): 'ascending' parameter must be of type bool or list of bool, not {}."
            .format(ascending))
    if not is_overload_bool(inplace):
        raise_bodo_error(
            "sort_values(): 'inplace' parameter must be of type bool, not {}."
            .format(inplace))
    if kind != 'quicksort' and not isinstance(kind, types.Omitted):
        warnings.warn(BodoWarning(
            'sort_values(): specifying sorting algorithm is not supported in Bodo. Bodo uses stable sort.'
            ))
    if is_overload_constant_str(na_position):
        na_position = get_overload_const_str(na_position)
        if na_position not in ('first', 'last'):
            raise BodoError(
                "sort_values(): na_position should either be 'first' or 'last'"
                )
    elif is_overload_constant_list(na_position):
        joe__wfxyg = get_overload_const_list(na_position)
        for na_position in joe__wfxyg:
            if na_position not in ('first', 'last'):
                raise BodoError(
                    "sort_values(): Every value in na_position should either be 'first' or 'last'"
                    )
    else:
        raise_bodo_error(
            f'sort_values(): na_position parameter must be a literal constant of type str or a constant list of str with 1 entry per key column, not {na_position}'
            )
    na_position = get_overload_const_str(na_position)
    if na_position not in ['first', 'last']:
        raise BodoError(
            "sort_values(): na_position should either be 'first' or 'last'")


@overload_method(DataFrameType, 'sort_index', inline='always', no_unliteral
    =True)
def overload_dataframe_sort_index(df, axis=0, level=None, ascending=True,
    inplace=False, kind='quicksort', na_position='last', sort_remaining=
    True, ignore_index=False, key=None):
    check_runtime_cols_unsupported(df, 'DataFrame.sort_index()')
    tyy__szp = dict(axis=axis, level=level, kind=kind, sort_remaining=
        sort_remaining, ignore_index=ignore_index, key=key)
    vtdv__ntf = dict(axis=0, level=None, kind='quicksort', sort_remaining=
        True, ignore_index=False, key=None)
    check_unsupported_args('DataFrame.sort_index', tyy__szp, vtdv__ntf,
        package_name='pandas', module_name='DataFrame')
    if not is_overload_bool(ascending):
        raise BodoError(
            "DataFrame.sort_index(): 'ascending' parameter must be of type bool"
            )
    if not is_overload_bool(inplace):
        raise BodoError(
            "DataFrame.sort_index(): 'inplace' parameter must be of type bool")
    if not is_overload_constant_str(na_position) or get_overload_const_str(
        na_position) not in ('first', 'last'):
        raise_bodo_error(
            "DataFrame.sort_index(): 'na_position' should either be 'first' or 'last'"
            )

    def _impl(df, axis=0, level=None, ascending=True, inplace=False, kind=
        'quicksort', na_position='last', sort_remaining=True, ignore_index=
        False, key=None):
        return bodo.hiframes.pd_dataframe_ext.sort_values_dummy(df,
            '$_bodo_index_', ascending, inplace, na_position, None)
    return _impl


@overload_method(DataFrameType, 'rank', inline='always', no_unliteral=True)
def overload_dataframe_rank(df, axis=0, method='average', numeric_only=None,
    na_option='keep', ascending=True, pct=False):
    ilzk__soby = """def impl(df, axis=0, method='average', numeric_only=None, na_option='keep', ascending=True, pct=False):
"""
    vzoky__jjk = len(df.columns)
    data_args = ', '.join(
        'bodo.libs.array_kernels.rank(data_{}, method=method, na_option=na_option, ascending=ascending, pct=pct)'
        .format(i) for i in range(vzoky__jjk))
    for i in range(vzoky__jjk):
        ilzk__soby += (
            '  data_{0} = bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {0})\n'
            .format(i))
    index = 'bodo.hiframes.pd_dataframe_ext.get_dataframe_index(df)'
    return _gen_init_df(ilzk__soby, df.columns, data_args, index)


@overload_method(DataFrameType, 'fillna', inline='always', no_unliteral=True)
def overload_dataframe_fillna(df, value=None, method=None, axis=None,
    inplace=False, limit=None, downcast=None):
    check_runtime_cols_unsupported(df, 'DataFrame.fillna()')
    tyy__szp = dict(limit=limit, downcast=downcast)
    vtdv__ntf = dict(limit=None, downcast=None)
    check_unsupported_args('DataFrame.fillna', tyy__szp, vtdv__ntf,
        package_name='pandas', module_name='DataFrame')
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(df,
        'DataFrame.fillna()')
    if not (is_overload_none(axis) or is_overload_zero(axis)):
        raise BodoError("DataFrame.fillna(): 'axis' argument not supported.")
    lsyry__ejb = not is_overload_none(value)
    lsnp__stmz = not is_overload_none(method)
    if lsyry__ejb and lsnp__stmz:
        raise BodoError(
            "DataFrame.fillna(): Cannot specify both 'value' and 'method'.")
    if not lsyry__ejb and not lsnp__stmz:
        raise BodoError(
            "DataFrame.fillna(): Must specify one of 'value' and 'method'.")
    if lsyry__ejb:
        apyb__ogyw = 'value=value'
    else:
        apyb__ogyw = 'method=method'
    data_args = [(
        f"df['{kxm__lejo}'].fillna({apyb__ogyw}, inplace=inplace)" if
        isinstance(kxm__lejo, str) else
        f'df[{kxm__lejo}].fillna({apyb__ogyw}, inplace=inplace)') for
        kxm__lejo in df.columns]
    ilzk__soby = """def impl(df, value=None, method=None, axis=None, inplace=False, limit=None, downcast=None):
"""
    if is_overload_true(inplace):
        ilzk__soby += '  ' + '  \n'.join(data_args) + '\n'
        lxd__swvja = {}
        exec(ilzk__soby, {}, lxd__swvja)
        impl = lxd__swvja['impl']
        return impl
    else:
        return _gen_init_df(ilzk__soby, df.columns, ', '.join(vvpnu__xjesd +
            '.values' for vvpnu__xjesd in data_args))


@overload_method(DataFrameType, 'reset_index', inline='always',
    no_unliteral=True)
def overload_dataframe_reset_index(df, level=None, drop=False, inplace=
    False, col_level=0, col_fill='', _bodo_transformed=False):
    check_runtime_cols_unsupported(df, 'DataFrame.reset_index()')
    tyy__szp = dict(col_level=col_level, col_fill=col_fill)
    vtdv__ntf = dict(col_level=0, col_fill='')
    check_unsupported_args('DataFrame.reset_index', tyy__szp, vtdv__ntf,
        package_name='pandas', module_name='DataFrame')
    handle_inplace_df_type_change(inplace, _bodo_transformed, 'reset_index')
    if not _is_all_levels(df, level):
        raise_bodo_error(
            'DataFrame.reset_index(): only dropping all index levels supported'
            )
    if not is_overload_constant_bool(drop):
        raise BodoError(
            "DataFrame.reset_index(): 'drop' parameter should be a constant boolean value"
            )
    if not is_overload_constant_bool(inplace):
        raise BodoError(
            "DataFrame.reset_index(): 'inplace' parameter should be a constant boolean value"
            )
    ilzk__soby = """def impl(df, level=None, drop=False, inplace=False, col_level=0, col_fill='', _bodo_transformed=False,):
"""
    ilzk__soby += (
        '  index = bodo.hiframes.pd_index_ext.init_range_index(0, len(df), 1, None)\n'
        )
    drop = is_overload_true(drop)
    inplace = is_overload_true(inplace)
    columns = df.columns
    data_args = [
        'bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {}){}\n'.
        format(i, '' if inplace else '.copy()') for i in range(len(df.columns))
        ]
    if not drop:
        neyyz__lqv = 'index' if 'index' not in columns else 'level_0'
        index_names = get_index_names(df.index, 'DataFrame.reset_index()',
            neyyz__lqv)
        columns = index_names + columns
        if isinstance(df.index, MultiIndexType):
            ilzk__soby += """  m_index = bodo.hiframes.pd_index_ext.get_index_data(bodo.hiframes.pd_dataframe_ext.get_dataframe_index(df))
"""
            buyy__rvapw = ['m_index[{}]'.format(i) for i in range(df.index.
                nlevels)]
            data_args = buyy__rvapw + data_args
        else:
            zaz__sgxkk = (
                'bodo.utils.conversion.index_to_array(bodo.hiframes.pd_dataframe_ext.get_dataframe_index(df))'
                )
            data_args = [zaz__sgxkk] + data_args
    return _gen_init_df(ilzk__soby, columns, ', '.join(data_args), 'index')


def _is_all_levels(df, level):
    fts__qzdsc = len(get_index_data_arr_types(df.index))
    return is_overload_none(level) or is_overload_constant_int(level
        ) and get_overload_const_int(level
        ) == 0 and fts__qzdsc == 1 or is_overload_constant_list(level
        ) and list(get_overload_const_list(level)) == list(range(fts__qzdsc))


@overload_method(DataFrameType, 'dropna', inline='always', no_unliteral=True)
def overload_dataframe_dropna(df, axis=0, how='any', thresh=None, subset=
    None, inplace=False):
    check_runtime_cols_unsupported(df, 'DataFrame.dropna()')
    if not is_overload_constant_bool(inplace) or is_overload_true(inplace):
        raise BodoError('DataFrame.dropna(): inplace=True is not supported')
    if not is_overload_zero(axis):
        raise_bodo_error(f'df.dropna(): only axis=0 supported')
    ensure_constant_values('dropna', 'how', how, ('any', 'all'))
    if is_overload_none(subset):
        dcg__qrbrj = list(range(len(df.columns)))
    elif not is_overload_constant_list(subset):
        raise_bodo_error(
            f'df.dropna(): subset argument should a constant list, not {subset}'
            )
    else:
        pss__xxvlx = get_overload_const_list(subset)
        dcg__qrbrj = []
        for pur__dhc in pss__xxvlx:
            if pur__dhc not in df.column_index:
                raise_bodo_error(
                    f"df.dropna(): column '{pur__dhc}' not in data frame columns {df}"
                    )
            dcg__qrbrj.append(df.column_index[pur__dhc])
    vzoky__jjk = len(df.columns)
    data_args = ', '.join('data_{}'.format(i) for i in range(vzoky__jjk))
    ilzk__soby = (
        "def impl(df, axis=0, how='any', thresh=None, subset=None, inplace=False):\n"
        )
    for i in range(vzoky__jjk):
        ilzk__soby += (
            '  data_{0} = bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {0})\n'
            .format(i))
    index = (
        'bodo.utils.conversion.index_to_array(bodo.hiframes.pd_dataframe_ext.get_dataframe_index(df))'
        )
    ilzk__soby += (
        """  ({0}, index_arr) = bodo.libs.array_kernels.dropna(({0}, {1}), how, thresh, ({2},))
"""
        .format(data_args, index, ', '.join(str(a) for a in dcg__qrbrj)))
    ilzk__soby += (
        '  index = bodo.utils.conversion.index_from_array(index_arr)\n')
    return _gen_init_df(ilzk__soby, df.columns, data_args, 'index')


@overload_method(DataFrameType, 'drop', inline='always', no_unliteral=True)
def overload_dataframe_drop(df, labels=None, axis=0, index=None, columns=
    None, level=None, inplace=False, errors='raise', _bodo_transformed=False):
    check_runtime_cols_unsupported(df, 'DataFrame.drop()')
    tyy__szp = dict(index=index, level=level, errors=errors)
    vtdv__ntf = dict(index=None, level=None, errors='raise')
    check_unsupported_args('DataFrame.drop', tyy__szp, vtdv__ntf,
        package_name='pandas', module_name='DataFrame')
    handle_inplace_df_type_change(inplace, _bodo_transformed, 'drop')
    if not is_overload_constant_bool(inplace):
        raise_bodo_error(
            "DataFrame.drop(): 'inplace' parameter should be a constant bool")
    if not is_overload_none(labels):
        if not is_overload_none(columns):
            raise BodoError(
                "Dataframe.drop(): Cannot specify both 'labels' and 'columns'")
        if not is_overload_constant_int(axis) or get_overload_const_int(axis
            ) != 1:
            raise_bodo_error('DataFrame.drop(): only axis=1 supported')
        if is_overload_constant_str(labels):
            dnko__dft = get_overload_const_str(labels),
        elif is_overload_constant_list(labels):
            dnko__dft = get_overload_const_list(labels)
        else:
            raise_bodo_error(
                'constant list of columns expected for labels in DataFrame.drop()'
                )
    else:
        if is_overload_none(columns):
            raise BodoError(
                "DataFrame.drop(): Need to specify at least one of 'labels' or 'columns'"
                )
        if is_overload_constant_str(columns):
            dnko__dft = get_overload_const_str(columns),
        elif is_overload_constant_list(columns):
            dnko__dft = get_overload_const_list(columns)
        else:
            raise_bodo_error(
                'constant list of columns expected for labels in DataFrame.drop()'
                )
    for kxm__lejo in dnko__dft:
        if kxm__lejo not in df.columns:
            raise_bodo_error(
                'DataFrame.drop(): column {} not in DataFrame columns {}'.
                format(kxm__lejo, df.columns))
    if len(set(dnko__dft)) == len(df.columns):
        raise BodoError('DataFrame.drop(): Dropping all columns not supported.'
            )
    inplace = is_overload_true(inplace)
    etku__hunb = tuple(kxm__lejo for kxm__lejo in df.columns if kxm__lejo
         not in dnko__dft)
    data_args = ', '.join(
        'bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {}){}'.
        format(df.column_index[kxm__lejo], '.copy()' if not inplace else ''
        ) for kxm__lejo in etku__hunb)
    ilzk__soby = (
        'def impl(df, labels=None, axis=0, index=None, columns=None,\n')
    ilzk__soby += (
        "     level=None, inplace=False, errors='raise', _bodo_transformed=False):\n"
        )
    index = 'bodo.hiframes.pd_dataframe_ext.get_dataframe_index(df)'
    return _gen_init_df(ilzk__soby, etku__hunb, data_args, index)


@overload_method(DataFrameType, 'append', inline='always', no_unliteral=True)
def overload_dataframe_append(df, other, ignore_index=False,
    verify_integrity=False, sort=None):
    check_runtime_cols_unsupported(df, 'DataFrame.append()')
    check_runtime_cols_unsupported(other, 'DataFrame.append()')
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(df,
        'DataFrame.append()')
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(other,
        'DataFrame.append()')
    if isinstance(other, DataFrameType):
        return (lambda df, other, ignore_index=False, verify_integrity=
            False, sort=None: pd.concat((df, other), ignore_index=
            ignore_index, verify_integrity=verify_integrity))
    if isinstance(other, types.BaseTuple):
        return (lambda df, other, ignore_index=False, verify_integrity=
            False, sort=None: pd.concat((df,) + other, ignore_index=
            ignore_index, verify_integrity=verify_integrity))
    if isinstance(other, types.List) and isinstance(other.dtype, DataFrameType
        ):
        return (lambda df, other, ignore_index=False, verify_integrity=
            False, sort=None: pd.concat([df] + other, ignore_index=
            ignore_index, verify_integrity=verify_integrity))
    raise BodoError(
        'invalid df.append() input. Only dataframe and list/tuple of dataframes supported'
        )


@overload_method(DataFrameType, 'sample', inline='always', no_unliteral=True)
def overload_dataframe_sample(df, n=None, frac=None, replace=False, weights
    =None, random_state=None, axis=None, ignore_index=False):
    check_runtime_cols_unsupported(df, 'DataFrame.sample()')
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(df,
        'DataFrame.sample()')
    tyy__szp = dict(random_state=random_state, weights=weights, axis=axis,
        ignore_index=ignore_index)
    iyazw__fbtwq = dict(random_state=None, weights=None, axis=None,
        ignore_index=False)
    check_unsupported_args('DataFrame.sample', tyy__szp, iyazw__fbtwq,
        package_name='pandas', module_name='DataFrame')
    if not is_overload_none(n) and not is_overload_none(frac):
        raise BodoError(
            'DataFrame.sample(): only one of n and frac option can be selected'
            )
    vzoky__jjk = len(df.columns)
    data_args = ', '.join('data_{}'.format(i) for i in range(vzoky__jjk))
    krpb__fpx = ', '.join('rhs_data_{}'.format(i) for i in range(vzoky__jjk))
    ilzk__soby = """def impl(df, n=None, frac=None, replace=False, weights=None, random_state=None, axis=None, ignore_index=False):
"""
    ilzk__soby += '  if (frac == 1 or n == len(df)) and not replace:\n'
    ilzk__soby += (
        '    return bodo.allgatherv(bodo.random_shuffle(df), False)\n')
    for i in range(vzoky__jjk):
        ilzk__soby += (
            """  rhs_data_{0} = bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {0})
"""
            .format(i))
    ilzk__soby += '  if frac is None:\n'
    ilzk__soby += '    frac_d = -1.0\n'
    ilzk__soby += '  else:\n'
    ilzk__soby += '    frac_d = frac\n'
    ilzk__soby += '  if n is None:\n'
    ilzk__soby += '    n_i = 0\n'
    ilzk__soby += '  else:\n'
    ilzk__soby += '    n_i = n\n'
    index = (
        'bodo.utils.conversion.index_to_array(bodo.hiframes.pd_dataframe_ext.get_dataframe_index(df))'
        )
    ilzk__soby += f"""  ({data_args},), index_arr = bodo.libs.array_kernels.sample_table_operation(({krpb__fpx},), {index}, n_i, frac_d, replace)
"""
    ilzk__soby += (
        '  index = bodo.utils.conversion.index_from_array(index_arr)\n')
    return bodo.hiframes.dataframe_impl._gen_init_df(ilzk__soby, df.columns,
        data_args, 'index')


@numba.njit
def _sizeof_fmt(num, size_qualifier=''):
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return f'{num:3.1f}{size_qualifier} {x}'
        num /= 1024.0
    return f'{num:3.1f}{size_qualifier} PB'


@overload_method(DataFrameType, 'info', no_unliteral=True)
def overload_dataframe_info(df, verbose=None, buf=None, max_cols=None,
    memory_usage=None, show_counts=None, null_counts=None):
    check_runtime_cols_unsupported(df, 'DataFrame.info()')
    wdxk__vydem = {'verbose': verbose, 'buf': buf, 'max_cols': max_cols,
        'memory_usage': memory_usage, 'show_counts': show_counts,
        'null_counts': null_counts}
    jyskm__yjr = {'verbose': None, 'buf': None, 'max_cols': None,
        'memory_usage': None, 'show_counts': None, 'null_counts': None}
    check_unsupported_args('DataFrame.info', wdxk__vydem, jyskm__yjr,
        package_name='pandas', module_name='DataFrame')
    yyj__xkav = f"<class '{str(type(df)).split('.')[-1]}"
    if len(df.columns) == 0:

        def _info_impl(df, verbose=None, buf=None, max_cols=None,
            memory_usage=None, show_counts=None, null_counts=None):
            wlgnb__kms = yyj__xkav + '\n'
            wlgnb__kms += 'Index: 0 entries\n'
            wlgnb__kms += 'Empty DataFrame'
            print(wlgnb__kms)
        return _info_impl
    else:
        ilzk__soby = """def _info_impl(df, verbose=None, buf=None, max_cols=None, memory_usage=None, show_counts=None, null_counts=None): #pragma: no cover
"""
        ilzk__soby += '    ncols = df.shape[1]\n'
        ilzk__soby += f'    lines = "{yyj__xkav}\\n"\n'
        ilzk__soby += f'    lines += "{df.index}: "\n'
        ilzk__soby += (
            '    index = bodo.hiframes.pd_dataframe_ext.get_dataframe_index(df)\n'
            )
        if isinstance(df.index, bodo.hiframes.pd_index_ext.RangeIndexType):
            ilzk__soby += """    lines += f"{len(index)} entries, {index.start} to {index.stop-1}\\n\"
"""
        elif isinstance(df.index, bodo.hiframes.pd_index_ext.StringIndexType):
            ilzk__soby += """    lines += f"{len(index)} entries, {index[0]} to {index[len(index)-1]}\\n\"
"""
        else:
            ilzk__soby += (
                '    lines += f"{len(index)} entries, {index[0]} to {index[-1]}\\n"\n'
                )
        ilzk__soby += (
            '    lines += f"Data columns (total {ncols} columns):\\n"\n')
        ilzk__soby += (
            f'    space = {max(len(str(k)) for k in df.columns) + 1}\n')
        ilzk__soby += '    column_width = max(space, 7)\n'
        ilzk__soby += '    column= "Column"\n'
        ilzk__soby += '    underl= "------"\n'
        ilzk__soby += (
            '    lines += f"#   {column:<{column_width}} Non-Null Count  Dtype\\n"\n'
            )
        ilzk__soby += (
            '    lines += f"--- {underl:<{column_width}} --------------  -----\\n"\n'
            )
        ilzk__soby += '    mem_size = 0\n'
        ilzk__soby += (
            '    col_name = bodo.libs.str_arr_ext.pre_alloc_string_array(ncols, -1)\n'
            )
        ilzk__soby += """    non_null_count = bodo.libs.str_arr_ext.pre_alloc_string_array(ncols, -1)
"""
        ilzk__soby += (
            '    col_dtype = bodo.libs.str_arr_ext.pre_alloc_string_array(ncols, -1)\n'
            )
        bef__jxmeq = dict()
        for i in range(len(df.columns)):
            ilzk__soby += f"""    non_null_count[{i}] = str(bodo.libs.array_ops.array_op_count(bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {i})))
"""
            ehn__dbtxj = f'{df.data[i].dtype}'
            if isinstance(df.data[i], bodo.CategoricalArrayType):
                ehn__dbtxj = 'category'
            elif isinstance(df.data[i], bodo.IntegerArrayType):
                lrlz__phrjv = bodo.libs.int_arr_ext.IntDtype(df.data[i].dtype
                    ).name
                ehn__dbtxj = f'{lrlz__phrjv[:-7]}'
            ilzk__soby += f'    col_dtype[{i}] = "{ehn__dbtxj}"\n'
            if ehn__dbtxj in bef__jxmeq:
                bef__jxmeq[ehn__dbtxj] += 1
            else:
                bef__jxmeq[ehn__dbtxj] = 1
            ilzk__soby += f'    col_name[{i}] = "{df.columns[i]}"\n'
            ilzk__soby += f"""    mem_size += bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {i}).nbytes
"""
        ilzk__soby += """    column_info = [f'{i:^3} {name:<{column_width}} {count} non-null      {dtype}' for i, (name, count, dtype) in enumerate(zip(col_name, non_null_count, col_dtype))]
"""
        ilzk__soby += '    for i in column_info:\n'
        ilzk__soby += "        lines += f'{i}\\n'\n"
        xtk__bjdrt = ', '.join(f'{k}({bef__jxmeq[k]})' for k in sorted(
            bef__jxmeq))
        ilzk__soby += f"    lines += 'dtypes: {xtk__bjdrt}\\n'\n"
        ilzk__soby += '    mem_size += df.index.nbytes\n'
        ilzk__soby += '    total_size = _sizeof_fmt(mem_size)\n'
        ilzk__soby += "    lines += f'memory usage: {total_size}'\n"
        ilzk__soby += '    print(lines)\n'
        lxd__swvja = {}
        exec(ilzk__soby, {'_sizeof_fmt': _sizeof_fmt, 'pd': pd, 'bodo':
            bodo, 'np': np}, lxd__swvja)
        _info_impl = lxd__swvja['_info_impl']
        return _info_impl


@overload_method(DataFrameType, 'memory_usage', inline='always',
    no_unliteral=True)
def overload_dataframe_memory_usage(df, index=True, deep=False):
    check_runtime_cols_unsupported(df, 'DataFrame.memory_usage()')
    ilzk__soby = 'def impl(df, index=True, deep=False):\n'
    eny__gfvy = 'bodo.hiframes.pd_dataframe_ext.get_dataframe_index(df).nbytes'
    mpcfv__kbnb = is_overload_true(index)
    columns = df.columns
    if mpcfv__kbnb:
        columns = ('Index',) + columns
    if len(columns) == 0:
        tuy__auehc = ()
    elif all(isinstance(kxm__lejo, int) for kxm__lejo in columns):
        tuy__auehc = np.array(columns, 'int64')
    elif all(isinstance(kxm__lejo, str) for kxm__lejo in columns):
        tuy__auehc = pd.array(columns, 'string')
    else:
        tuy__auehc = columns
    if df.is_table_format and len(df.columns) > 0:
        etia__uqs = int(mpcfv__kbnb)
        jkh__dtx = len(columns)
        ilzk__soby += f'  nbytes_arr = np.empty({jkh__dtx}, np.int64)\n'
        ilzk__soby += (
            '  table = bodo.hiframes.pd_dataframe_ext.get_dataframe_table(df)\n'
            )
        ilzk__soby += f"""  bodo.utils.table_utils.generate_table_nbytes(table, nbytes_arr, {etia__uqs})
"""
        if mpcfv__kbnb:
            ilzk__soby += f'  nbytes_arr[0] = {eny__gfvy}\n'
        ilzk__soby += f"""  return bodo.hiframes.pd_series_ext.init_series(nbytes_arr, pd.Index(column_vals), None)
"""
    else:
        data = ', '.join(
            f'bodo.libs.array_ops.array_op_nbytes(bodo.hiframes.pd_dataframe_ext.get_dataframe_data(df, {i}))'
             for i in range(len(df.columns)))
        if mpcfv__kbnb:
            data = f'{eny__gfvy},{data}'
        else:
            qtbw__rqvma = ',' if len(columns) == 1 else ''
            data = f'{data}{qtbw__rqvma}'
        ilzk__soby += f"""  return bodo.hiframes.pd_series_ext.init_series(({data}), pd.Index(column_vals), None)
"""
    lxd__swvja = {}
    exec(ilzk__soby, {'bodo': bodo, 'np': np, 'pd': pd, 'column_vals':
        tuy__auehc}, lxd__swvja)
    impl = lxd__swvja['impl']
    return impl


@overload(pd.read_excel, no_unliteral=True)
def overload_read_excel(io, sheet_name=0, header=0, names=None, index_col=
    None, usecols=None, squeeze=False, dtype=None, engine=None, converters=
    None, true_values=None, false_values=None, skiprows=None, nrows=None,
    na_values=None, keep_default_na=True, na_filter=True, verbose=False,
    parse_dates=False, date_parser=None, thousands=None, comment=None,
    skipfooter=0, convert_float=True, mangle_dupe_cols=True, _bodo_df_type=None
    ):
    df_type = _bodo_df_type.instance_type
    sqjk__julmb = 'read_excel_df{}'.format(next_label())
    setattr(types, sqjk__julmb, df_type)
    jyo__enuj = False
    if is_overload_constant_list(parse_dates):
        jyo__enuj = get_overload_const_list(parse_dates)
    bckzn__edn = ', '.join(["'{}':{}".format(cname, _get_pd_dtype_str(t)) for
        cname, t in zip(df_type.columns, df_type.data)])
    ilzk__soby = f"""
def impl(
    io,
    sheet_name=0,
    header=0,
    names=None,
    index_col=None,
    usecols=None,
    squeeze=False,
    dtype=None,
    engine=None,
    converters=None,
    true_values=None,
    false_values=None,
    skiprows=None,
    nrows=None,
    na_values=None,
    keep_default_na=True,
    na_filter=True,
    verbose=False,
    parse_dates=False,
    date_parser=None,
    thousands=None,
    comment=None,
    skipfooter=0,
    convert_float=True,
    mangle_dupe_cols=True,
    _bodo_df_type=None,
):
    with numba.objmode(df="{sqjk__julmb}"):
        df = pd.read_excel(
            io=io,
            sheet_name=sheet_name,
            header=header,
            names={list(df_type.columns)},
            index_col=index_col,
            usecols=usecols,
            squeeze=squeeze,
            dtype={{{bckzn__edn}}},
            engine=engine,
            converters=converters,
            true_values=true_values,
            false_values=false_values,
            skiprows=skiprows,
            nrows=nrows,
            na_values=na_values,
            keep_default_na=keep_default_na,
            na_filter=na_filter,
            verbose=verbose,
            parse_dates={jyo__enuj},
            date_parser=date_parser,
            thousands=thousands,
            comment=comment,
            skipfooter=skipfooter,
            convert_float=convert_float,
            mangle_dupe_cols=mangle_dupe_cols,
        )
    return df
"""
    lxd__swvja = {}
    exec(ilzk__soby, globals(), lxd__swvja)
    impl = lxd__swvja['impl']
    return impl


def overload_dataframe_plot(df, x=None, y=None, kind='line', figsize=None,
    xlabel=None, ylabel=None, title=None, legend=True, fontsize=None,
    xticks=None, yticks=None, ax=None):
    try:
        import matplotlib.pyplot as plt
    except ImportError as kfza__jie:
        raise BodoError('df.plot needs matplotllib which is not installed.')
    ilzk__soby = (
        "def impl(df, x=None, y=None, kind='line', figsize=None, xlabel=None, \n"
        )
    ilzk__soby += '    ylabel=None, title=None, legend=True, fontsize=None, \n'
    ilzk__soby += '    xticks=None, yticks=None, ax=None):\n'
    if is_overload_none(ax):
        ilzk__soby += '   fig, ax = plt.subplots()\n'
    else:
        ilzk__soby += '   fig = ax.get_figure()\n'
    if not is_overload_none(figsize):
        ilzk__soby += '   fig.set_figwidth(figsize[0])\n'
        ilzk__soby += '   fig.set_figheight(figsize[1])\n'
    if is_overload_none(xlabel):
        ilzk__soby += '   xlabel = x\n'
    ilzk__soby += '   ax.set_xlabel(xlabel)\n'
    if is_overload_none(ylabel):
        ilzk__soby += '   ylabel = y\n'
    else:
        ilzk__soby += '   ax.set_ylabel(ylabel)\n'
    if not is_overload_none(title):
        ilzk__soby += '   ax.set_title(title)\n'
    if not is_overload_none(fontsize):
        ilzk__soby += '   ax.tick_params(labelsize=fontsize)\n'
    kind = get_overload_const_str(kind)
    if kind == 'line':
        if is_overload_none(x) and is_overload_none(y):
            for i in range(len(df.columns)):
                if isinstance(df.data[i], (types.Array, IntegerArrayType)
                    ) and isinstance(df.data[i].dtype, (types.Integer,
                    types.Float)):
                    ilzk__soby += (
                        f'   ax.plot(df.iloc[:, {i}], label=df.columns[{i}])\n'
                        )
        elif is_overload_none(x):
            ilzk__soby += '   ax.plot(df[y], label=y)\n'
        elif is_overload_none(y):
            gdpn__pyszy = get_overload_const_str(x)
            cjky__top = df.columns.index(gdpn__pyszy)
            for i in range(len(df.columns)):
                if isinstance(df.data[i], (types.Array, IntegerArrayType)
                    ) and isinstance(df.data[i].dtype, (types.Integer,
                    types.Float)):
                    if cjky__top != i:
                        ilzk__soby += (
                            f'   ax.plot(df[x], df.iloc[:, {i}], label=df.columns[{i}])\n'
                            )
        else:
            ilzk__soby += '   ax.plot(df[x], df[y], label=y)\n'
    elif kind == 'scatter':
        legend = False
        ilzk__soby += '   ax.scatter(df[x], df[y], s=20)\n'
        ilzk__soby += '   ax.set_ylabel(ylabel)\n'
    if not is_overload_none(xticks):
        ilzk__soby += '   ax.set_xticks(xticks)\n'
    if not is_overload_none(yticks):
        ilzk__soby += '   ax.set_yticks(yticks)\n'
    if is_overload_true(legend):
        ilzk__soby += '   ax.legend()\n'
    ilzk__soby += '   return ax\n'
    lxd__swvja = {}
    exec(ilzk__soby, {'bodo': bodo, 'plt': plt}, lxd__swvja)
    impl = lxd__swvja['impl']
    return impl


@lower_builtin('df.plot', DataFrameType, types.VarArg(types.Any))
def dataframe_plot_low(context, builder, sig, args):
    impl = overload_dataframe_plot(*sig.args)
    return context.compile_internal(builder, impl, sig, args)


def is_df_values_numpy_supported_dftyp(df_typ):
    for fcows__mep in df_typ.data:
        if not (isinstance(fcows__mep, (IntegerArrayType, FloatingArrayType
            )) or isinstance(fcows__mep.dtype, types.Number) or fcows__mep.
            dtype in (bodo.datetime64ns, bodo.timedelta64ns)):
            return False
    return True


def typeref_to_type(v):
    if isinstance(v, types.BaseTuple):
        return types.BaseTuple.from_types(tuple(typeref_to_type(a) for a in v))
    return v.instance_type if isinstance(v, (types.TypeRef, types.NumberClass)
        ) else v


def _install_typer_for_type(type_name, typ):

    @type_callable(typ)
    def type_call_type(context):

        def typer(*args, **kws):
            args = tuple(typeref_to_type(v) for v in args)
            kws = {name: typeref_to_type(v) for name, v in kws.items()}
            return types.TypeRef(typ(*args, **kws))
        return typer
    no_side_effect_call_tuples.add((type_name, bodo))
    no_side_effect_call_tuples.add((typ,))


def _install_type_call_typers():
    for type_name in bodo_types_with_params:
        typ = getattr(bodo, type_name)
        _install_typer_for_type(type_name, typ)


_install_type_call_typers()


def set_df_col(df, cname, arr, inplace):
    df[cname] = arr


@infer_global(set_df_col)
class SetDfColInfer(AbstractTemplate):

    def generic(self, args, kws):
        from bodo.hiframes.pd_dataframe_ext import DataFrameType
        assert not kws
        assert len(args) == 4
        assert isinstance(args[1], types.Literal)
        sytvt__cdy = args[0]
        zrzou__ehddf = args[1].literal_value
        val = args[2]
        assert val != types.unknown
        gakc__fij = sytvt__cdy
        check_runtime_cols_unsupported(sytvt__cdy, 'set_df_col()')
        if isinstance(sytvt__cdy, DataFrameType):
            index = sytvt__cdy.index
            if len(sytvt__cdy.columns) == 0:
                index = bodo.hiframes.pd_index_ext.RangeIndexType(types.none)
            if isinstance(val, SeriesType):
                if len(sytvt__cdy.columns) == 0:
                    index = val.index
                val = val.data
            if is_pd_index_type(val):
                val = bodo.utils.typing.get_index_data_arr_types(val)[0]
            if isinstance(val, types.List):
                val = dtype_to_array_type(val.dtype)
            if is_overload_constant_str(val) or val == types.unicode_type:
                val = bodo.dict_str_arr_type
            elif not is_array_typ(val):
                val = dtype_to_array_type(val)
            if zrzou__ehddf in sytvt__cdy.columns:
                etku__hunb = sytvt__cdy.columns
                aqvns__pdge = sytvt__cdy.columns.index(zrzou__ehddf)
                jozc__mehl = list(sytvt__cdy.data)
                jozc__mehl[aqvns__pdge] = val
                jozc__mehl = tuple(jozc__mehl)
            else:
                etku__hunb = sytvt__cdy.columns + (zrzou__ehddf,)
                jozc__mehl = sytvt__cdy.data + (val,)
            gakc__fij = DataFrameType(jozc__mehl, index, etku__hunb,
                sytvt__cdy.dist, sytvt__cdy.is_table_format)
        return gakc__fij(*args)


SetDfColInfer.prefer_literal = True


def __bodosql_replace_columns_dummy(df, col_names_to_replace,
    cols_to_replace_with):
    for i in range(len(col_names_to_replace)):
        df[col_names_to_replace[i]] = cols_to_replace_with[i]


@infer_global(__bodosql_replace_columns_dummy)
class BodoSQLReplaceColsInfer(AbstractTemplate):

    def generic(self, args, kws):
        from bodo.hiframes.pd_dataframe_ext import DataFrameType
        assert not kws
        assert len(args) == 3
        assert is_overload_constant_tuple(args[1])
        assert isinstance(args[2], types.BaseTuple)
        nxagq__fmydm = args[0]
        assert isinstance(nxagq__fmydm, DataFrameType) and len(nxagq__fmydm
            .columns
            ) > 0, 'Error while typechecking __bodosql_replace_columns_dummy: we should only generate a call __bodosql_replace_columns_dummy if the input dataframe'
        col_names_to_replace = get_overload_const_tuple(args[1])
        mozvr__ypt = args[2]
        assert len(col_names_to_replace) == len(mozvr__ypt
            ), 'Error while typechecking __bodosql_replace_columns_dummy: the tuple of column indicies to replace should be equal to the number of columns to replace them with'
        assert len(col_names_to_replace) <= len(nxagq__fmydm.columns
            ), 'Error while typechecking __bodosql_replace_columns_dummy: The number of indicies provided should be less than or equal to the number of columns in the input dataframe'
        for col_name in col_names_to_replace:
            assert col_name in nxagq__fmydm.columns, 'Error while typechecking __bodosql_replace_columns_dummy: All columns specified to be replaced should already be present in input dataframe'
        check_runtime_cols_unsupported(nxagq__fmydm,
            '__bodosql_replace_columns_dummy()')
        index = nxagq__fmydm.index
        etku__hunb = nxagq__fmydm.columns
        jozc__mehl = list(nxagq__fmydm.data)
        for i in range(len(col_names_to_replace)):
            col_name = col_names_to_replace[i]
            iraro__hek = mozvr__ypt[i]
            assert isinstance(iraro__hek, SeriesType
                ), 'Error while typechecking __bodosql_replace_columns_dummy: the values to replace the columns with are expected to be series'
            if isinstance(iraro__hek, SeriesType):
                iraro__hek = iraro__hek.data
            eyz__puge = nxagq__fmydm.column_index[col_name]
            jozc__mehl[eyz__puge] = iraro__hek
        jozc__mehl = tuple(jozc__mehl)
        gakc__fij = DataFrameType(jozc__mehl, index, etku__hunb,
            nxagq__fmydm.dist, nxagq__fmydm.is_table_format)
        return gakc__fij(*args)


BodoSQLReplaceColsInfer.prefer_literal = True


def _parse_query_expr(expr, env, columns, cleaned_columns, index_name=None,
    join_cleaned_cols=()):
    uyl__acbh = {}

    def _rewrite_membership_op(self, node, left, right):
        dbdq__lntbo = node.op
        op = self.visit(dbdq__lntbo)
        return op, dbdq__lntbo, left, right

    def _maybe_evaluate_binop(self, op, op_class, lhs, rhs, eval_in_python=
        ('in', 'not in'), maybe_eval_in_python=('==', '!=', '<', '>', '<=',
        '>=')):
        res = op(lhs, rhs)
        return res
    jowtn__golq = []


    class NewFuncNode(pd.core.computation.ops.FuncNode):

        def __init__(self, name):
            if (name not in pd.core.computation.ops.MATHOPS or pd.core.
                computation.check._NUMEXPR_INSTALLED and pd.core.
                computation.check_NUMEXPR_VERSION < pd.core.computation.ops
                .LooseVersion('2.6.9') and name in ('floor', 'ceil')):
                if name not in jowtn__golq:
                    raise BodoError('"{0}" is not a supported function'.
                        format(name))
            self.name = name
            if name in jowtn__golq:
                self.func = name
            else:
                self.func = getattr(np, name)

        def __call__(self, *args):
            return pd.core.computation.ops.MathCall(self, args)

        def __repr__(self):
            return pd.io.formats.printing.pprint_thing('(' + self.name + ')')

    def visit_Attribute(self, node, **kwargs):
        omezz__xsbox = node.attr
        value = node.value
        vgt__rutqq = pd.core.computation.ops.LOCAL_TAG
        if omezz__xsbox in ('str', 'dt'):
            try:
                bln__xlk = str(self.visit(value))
            except pd.core.computation.ops.UndefinedVariableError as eexi__bcw:
                col_name = eexi__bcw.args[0].split("'")[1]
                raise BodoError(
                    'df.query(): column {} is not found in dataframe columns {}'
                    .format(col_name, columns))
        else:
            bln__xlk = str(self.visit(value))
        qmubn__zbsyu = bln__xlk, omezz__xsbox
        if qmubn__zbsyu in join_cleaned_cols:
            omezz__xsbox = join_cleaned_cols[qmubn__zbsyu]
        name = bln__xlk + '.' + omezz__xsbox
        if name.startswith(vgt__rutqq):
            name = name[len(vgt__rutqq):]
        if omezz__xsbox in ('str', 'dt'):
            ifz__quo = columns[cleaned_columns.index(bln__xlk)]
            uyl__acbh[ifz__quo] = bln__xlk
            self.env.scope[name] = 0
            return self.term_type(vgt__rutqq + name, self.env)
        jowtn__golq.append(name)
        return NewFuncNode(name)

    def __str__(self):
        if isinstance(self.value, list):
            return '{}'.format(self.value)
        if isinstance(self.value, str):
            return "'{}'".format(self.value)
        return pd.io.formats.printing.pprint_thing(self.name)

    def math__str__(self):
        if self.op in jowtn__golq:
            return pd.io.formats.printing.pprint_thing('{0}({1})'.format(
                self.op, ','.join(map(str, self.operands))))
        uxi__egqef = map(lambda a:
            'bodo.hiframes.pd_series_ext.get_series_data({})'.format(str(a)
            ), self.operands)
        op = 'np.{}'.format(self.op)
        zrzou__ehddf = (
            'bodo.hiframes.pd_index_ext.init_range_index(0, len({}), 1, None)'
            .format(str(self.operands[0])))
        return pd.io.formats.printing.pprint_thing(
            'bodo.hiframes.pd_series_ext.init_series({0}({1}), {2})'.format
            (op, ','.join(uxi__egqef), zrzou__ehddf))

    def op__str__(self):
        eebjp__myzrm = ('({0})'.format(pd.io.formats.printing.pprint_thing(
            gmw__quly)) for gmw__quly in self.operands)
        if self.op == 'in':
            return pd.io.formats.printing.pprint_thing(
                'bodo.hiframes.pd_dataframe_ext.val_isin_dummy({})'.format(
                ', '.join(eebjp__myzrm)))
        if self.op == 'not in':
            return pd.io.formats.printing.pprint_thing(
                'bodo.hiframes.pd_dataframe_ext.val_notin_dummy({})'.format
                (', '.join(eebjp__myzrm)))
        return pd.io.formats.printing.pprint_thing(' {0} '.format(self.op).
            join(eebjp__myzrm))
    isstr__ukku = (pd.core.computation.expr.BaseExprVisitor.
        _rewrite_membership_op)
    moj__qltrk = pd.core.computation.expr.BaseExprVisitor._maybe_evaluate_binop
    pqvar__opcny = pd.core.computation.expr.BaseExprVisitor.visit_Attribute
    fqvlk__vomvh = (pd.core.computation.expr.BaseExprVisitor.
        _maybe_downcast_constants)
    fcbzl__uwa = pd.core.computation.ops.Term.__str__
    qjbxh__prmff = pd.core.computation.ops.MathCall.__str__
    fef__giv = pd.core.computation.ops.Op.__str__
    yjni__ukicw = pd.core.computation.ops.BinOp._disallow_scalar_only_bool_ops
    try:
        pd.core.computation.expr.BaseExprVisitor._rewrite_membership_op = (
            _rewrite_membership_op)
        pd.core.computation.expr.BaseExprVisitor._maybe_evaluate_binop = (
            _maybe_evaluate_binop)
        pd.core.computation.expr.BaseExprVisitor.visit_Attribute = (
            visit_Attribute)
        (pd.core.computation.expr.BaseExprVisitor._maybe_downcast_constants
            ) = lambda self, left, right: (left, right)
        pd.core.computation.ops.Term.__str__ = __str__
        pd.core.computation.ops.MathCall.__str__ = math__str__
        pd.core.computation.ops.Op.__str__ = op__str__
        pd.core.computation.ops.BinOp._disallow_scalar_only_bool_ops = (lambda
            self: None)
        ccz__mgokc = pd.core.computation.expr.Expr(expr, env=env)
        ajxrr__olwkh = str(ccz__mgokc)
    except pd.core.computation.ops.UndefinedVariableError as eexi__bcw:
        if not is_overload_none(index_name) and get_overload_const_str(
            index_name) == eexi__bcw.args[0].split("'")[1]:
            raise BodoError(
                "df.query(): Refering to named index ('{}') by name is not supported"
                .format(get_overload_const_str(index_name)))
        else:
            raise BodoError(f'df.query(): undefined variable, {eexi__bcw}')
    finally:
        pd.core.computation.expr.BaseExprVisitor._rewrite_membership_op = (
            isstr__ukku)
        pd.core.computation.expr.BaseExprVisitor._maybe_evaluate_binop = (
            moj__qltrk)
        pd.core.computation.expr.BaseExprVisitor.visit_Attribute = pqvar__opcny
        (pd.core.computation.expr.BaseExprVisitor._maybe_downcast_constants
            ) = fqvlk__vomvh
        pd.core.computation.ops.Term.__str__ = fcbzl__uwa
        pd.core.computation.ops.MathCall.__str__ = qjbxh__prmff
        pd.core.computation.ops.Op.__str__ = fef__giv
        pd.core.computation.ops.BinOp._disallow_scalar_only_bool_ops = (
            yjni__ukicw)
    ywa__zjo = pd.core.computation.parsing.clean_column_name
    uyl__acbh.update({kxm__lejo: ywa__zjo(kxm__lejo) for kxm__lejo in
        columns if ywa__zjo(kxm__lejo) in ccz__mgokc.names})
    return ccz__mgokc, ajxrr__olwkh, uyl__acbh


class DataFrameTupleIterator(types.SimpleIteratorType):

    def __init__(self, col_names, arr_typs):
        self.array_types = arr_typs
        self.col_names = col_names
        timjc__wpk = ['{}={}'.format(col_names[i], arr_typs[i]) for i in
            range(len(col_names))]
        name = 'itertuples({})'.format(','.join(timjc__wpk))
        dyaa__umfre = namedtuple('Pandas', col_names)
        nxre__fgnlp = types.NamedTuple([_get_series_dtype(a) for a in
            arr_typs], dyaa__umfre)
        super(DataFrameTupleIterator, self).__init__(name, nxre__fgnlp)

    @property
    def mangling_args(self):
        return self.__class__.__name__, (self._code,)


def _get_series_dtype(arr_typ):
    if arr_typ == types.Array(types.NPDatetime('ns'), 1, 'C'):
        return pd_timestamp_tz_naive_type
    return arr_typ.dtype


def get_itertuples():
    pass


@infer_global(get_itertuples)
class TypeIterTuples(AbstractTemplate):

    def generic(self, args, kws):
        assert not kws
        assert len(args) % 2 == 0, 'name and column pairs expected'
        col_names = [a.literal_value for a in args[:len(args) // 2]]
        dlh__pnbxc = [if_series_to_array_type(a) for a in args[len(args) // 2:]
            ]
        assert 'Index' not in col_names[0]
        col_names = ['Index'] + col_names
        dlh__pnbxc = [types.Array(types.int64, 1, 'C')] + dlh__pnbxc
        dnhyb__rcfn = DataFrameTupleIterator(col_names, dlh__pnbxc)
        return dnhyb__rcfn(*args)


TypeIterTuples.prefer_literal = True


@register_model(DataFrameTupleIterator)
class DataFrameTupleIteratorModel(models.StructModel):

    def __init__(self, dmm, fe_type):
        eqbbu__omlo = [('index', types.EphemeralPointer(types.uintp))] + [(
            'array{}'.format(i), arr) for i, arr in enumerate(fe_type.
            array_types[1:])]
        super(DataFrameTupleIteratorModel, self).__init__(dmm, fe_type,
            eqbbu__omlo)

    def from_return(self, builder, value):
        return value


@lower_builtin(get_itertuples, types.VarArg(types.Any))
def get_itertuples_impl(context, builder, sig, args):
    qhko__gfei = args[len(args) // 2:]
    vkbwg__zcnm = sig.args[len(sig.args) // 2:]
    aoqkj__rfaor = context.make_helper(builder, sig.return_type)
    gjtso__itd = context.get_constant(types.intp, 0)
    zxbxl__aewtg = cgutils.alloca_once_value(builder, gjtso__itd)
    aoqkj__rfaor.index = zxbxl__aewtg
    for i, arr in enumerate(qhko__gfei):
        setattr(aoqkj__rfaor, 'array{}'.format(i), arr)
    for arr, arr_typ in zip(qhko__gfei, vkbwg__zcnm):
        context.nrt.incref(builder, arr_typ, arr)
    res = aoqkj__rfaor._getvalue()
    return impl_ret_new_ref(context, builder, sig.return_type, res)


@lower_builtin('getiter', DataFrameTupleIterator)
def getiter_itertuples(context, builder, sig, args):
    return impl_ret_borrowed(context, builder, sig.return_type, args[0])


@lower_builtin('iternext', DataFrameTupleIterator)
@iternext_impl(RefType.UNTRACKED)
def iternext_itertuples(context, builder, sig, args, result):
    abxil__fmjd, = sig.args
    pfhu__lvbc, = args
    aoqkj__rfaor = context.make_helper(builder, abxil__fmjd, value=pfhu__lvbc)
    wxm__okob = signature(types.intp, abxil__fmjd.array_types[1])
    zhvj__flff = context.compile_internal(builder, lambda a: len(a),
        wxm__okob, [aoqkj__rfaor.array0])
    index = builder.load(aoqkj__rfaor.index)
    akk__krxwg = builder.icmp_signed('<', index, zhvj__flff)
    result.set_valid(akk__krxwg)
    with builder.if_then(akk__krxwg):
        values = [index]
        for i, arr_typ in enumerate(abxil__fmjd.array_types[1:]):
            lai__tky = getattr(aoqkj__rfaor, 'array{}'.format(i))
            if arr_typ == types.Array(types.NPDatetime('ns'), 1, 'C'):
                otsn__gjldk = signature(pd_timestamp_tz_naive_type, arr_typ,
                    types.intp)
                val = context.compile_internal(builder, lambda a, i: bodo.
                    hiframes.pd_timestamp_ext.
                    convert_datetime64_to_timestamp(np.int64(a[i])),
                    otsn__gjldk, [lai__tky, index])
            else:
                otsn__gjldk = signature(arr_typ.dtype, arr_typ, types.intp)
                val = context.compile_internal(builder, lambda a, i: a[i],
                    otsn__gjldk, [lai__tky, index])
            values.append(val)
        value = context.make_tuple(builder, abxil__fmjd.yield_type, values)
        result.yield_(value)
        krtl__vgr = cgutils.increment_index(builder, index)
        builder.store(krtl__vgr, aoqkj__rfaor.index)


def _analyze_op_pair_first(self, scope, equiv_set, expr, lhs):
    typ = self.typemap[expr.value.name].first_type
    if not isinstance(typ, types.NamedTuple):
        return None
    lhs = ir.Var(scope, mk_unique_var('tuple_var'), expr.loc)
    self.typemap[lhs.name] = typ
    rhs = ir.Expr.pair_first(expr.value, expr.loc)
    fyuzg__zii = ir.Assign(rhs, lhs, expr.loc)
    gahx__nijrf = lhs
    wcssm__iyunw = []
    eguqo__vpqu = []
    oshv__hqkx = typ.count
    for i in range(oshv__hqkx):
        wet__kbsv = ir.Var(gahx__nijrf.scope, mk_unique_var('{}_size{}'.
            format(gahx__nijrf.name, i)), gahx__nijrf.loc)
        znjbf__lppo = ir.Expr.static_getitem(lhs, i, None, gahx__nijrf.loc)
        self.calltypes[znjbf__lppo] = None
        wcssm__iyunw.append(ir.Assign(znjbf__lppo, wet__kbsv, gahx__nijrf.loc))
        self._define(equiv_set, wet__kbsv, types.intp, znjbf__lppo)
        eguqo__vpqu.append(wet__kbsv)
    gyv__cswv = tuple(eguqo__vpqu)
    return numba.parfors.array_analysis.ArrayAnalysis.AnalyzeResult(shape=
        gyv__cswv, pre=[fyuzg__zii] + wcssm__iyunw)


numba.parfors.array_analysis.ArrayAnalysis._analyze_op_pair_first = (
    _analyze_op_pair_first)
