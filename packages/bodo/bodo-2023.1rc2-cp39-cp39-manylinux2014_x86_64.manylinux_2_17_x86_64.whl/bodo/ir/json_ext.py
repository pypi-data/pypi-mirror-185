import numba
import numpy as np
import pandas as pd
from llvmlite import ir as lir
from numba.core import cgutils, ir, ir_utils, typeinfer, types
from numba.core.ir_utils import compile_to_numba_ir, replace_arg_nodes
from numba.extending import intrinsic
import bodo
import bodo.ir.connector
from bodo import objmode
from bodo.io.fs_io import get_storage_options_pyobject, storage_options_dict_type
from bodo.libs.str_ext import string_type
from bodo.transforms import distributed_analysis, distributed_pass
from bodo.utils.utils import check_and_propagate_cpp_exception, check_java_installation, sanitize_varname


class JsonReader(ir.Stmt):

    def __init__(self, df_out, loc, out_vars, out_types, file_name,
        df_colnames, orient, convert_dates, precise_float, lines,
        compression, storage_options):
        self.connector_typ = 'json'
        self.df_out = df_out
        self.loc = loc
        self.out_vars = out_vars
        self.out_types = out_types
        self.file_name = file_name
        self.df_colnames = df_colnames
        self.orient = orient
        self.convert_dates = convert_dates
        self.precise_float = precise_float
        self.lines = lines
        self.compression = compression
        self.storage_options = storage_options

    def __repr__(self):
        return ('{} = ReadJson(file={}, col_names={}, types={}, vars={})'.
            format(self.df_out, self.file_name, self.df_colnames, self.
            out_types, self.out_vars))


import llvmlite.binding as ll
from bodo.io import json_cpp
ll.add_symbol('json_file_chunk_reader', json_cpp.json_file_chunk_reader)


@intrinsic
def json_file_chunk_reader(typingctx, fname_t, lines_t, is_parallel_t,
    nrows_t, compression_t, bucket_region_t, storage_options_t):
    assert storage_options_t == storage_options_dict_type, "Storage options don't match expected type"

    def codegen(context, builder, sig, args):
        ttsll__xjrq = lir.FunctionType(lir.IntType(8).as_pointer(), [lir.
            IntType(8).as_pointer(), lir.IntType(1), lir.IntType(1), lir.
            IntType(64), lir.IntType(8).as_pointer(), lir.IntType(8).
            as_pointer(), lir.IntType(8).as_pointer()])
        lbi__ulm = cgutils.get_or_insert_function(builder.module,
            ttsll__xjrq, name='json_file_chunk_reader')
        sbyww__viot = builder.call(lbi__ulm, args)
        context.compile_internal(builder, lambda :
            check_and_propagate_cpp_exception(), types.none(), [])
        wvfow__wmu = cgutils.create_struct_proxy(types.stream_reader_type)(
            context, builder)
        mesq__vpbyh = context.get_python_api(builder)
        wvfow__wmu.meminfo = mesq__vpbyh.nrt_meminfo_new_from_pyobject(context
            .get_constant_null(types.voidptr), sbyww__viot)
        wvfow__wmu.pyobj = sbyww__viot
        mesq__vpbyh.decref(sbyww__viot)
        return wvfow__wmu._getvalue()
    return types.stream_reader_type(types.voidptr, types.bool_, types.bool_,
        types.int64, types.voidptr, types.voidptr, storage_options_dict_type
        ), codegen


def remove_dead_json(json_node, lives_no_aliases, lives, arg_aliases,
    alias_map, func_ir, typemap):
    bcg__unr = []
    cubnm__uzdmv = []
    xdaw__msih = []
    for xxp__qgws, sox__mnjjr in enumerate(json_node.out_vars):
        if sox__mnjjr.name in lives:
            bcg__unr.append(json_node.df_colnames[xxp__qgws])
            cubnm__uzdmv.append(json_node.out_vars[xxp__qgws])
            xdaw__msih.append(json_node.out_types[xxp__qgws])
    json_node.df_colnames = bcg__unr
    json_node.out_vars = cubnm__uzdmv
    json_node.out_types = xdaw__msih
    if len(json_node.out_vars) == 0:
        return None
    return json_node


def json_distributed_run(json_node, array_dists, typemap, calltypes,
    typingctx, targetctx):
    if bodo.user_logging.get_verbose_level() >= 1:
        ffb__gok = (
            'Finish column pruning on read_json node:\n%s\nColumns loaded %s\n'
            )
        epsia__vhqf = json_node.loc.strformat()
        ttq__ditlm = json_node.df_colnames
        bodo.user_logging.log_message('Column Pruning', ffb__gok,
            epsia__vhqf, ttq__ditlm)
        abs__mvjef = [pzeeq__irga for xxp__qgws, pzeeq__irga in enumerate(
            json_node.df_colnames) if isinstance(json_node.out_types[
            xxp__qgws], bodo.libs.dict_arr_ext.DictionaryArrayType)]
        if abs__mvjef:
            qidd__vxxca = """Finished optimized encoding on read_json node:
%s
Columns %s using dictionary encoding to reduce memory usage.
"""
            bodo.user_logging.log_message('Dictionary Encoding',
                qidd__vxxca, epsia__vhqf, abs__mvjef)
    parallel = False
    if array_dists is not None:
        parallel = True
        for ltshr__fho in json_node.out_vars:
            if array_dists[ltshr__fho.name
                ] != distributed_pass.Distribution.OneD and array_dists[
                ltshr__fho.name] != distributed_pass.Distribution.OneD_Var:
                parallel = False
    fviwc__utp = len(json_node.out_vars)
    cqy__zwu = ', '.join('arr' + str(xxp__qgws) for xxp__qgws in range(
        fviwc__utp))
    qzt__ddbc = 'def json_impl(fname):\n'
    qzt__ddbc += '    ({},) = _json_reader_py(fname)\n'.format(cqy__zwu)
    qnyoj__okfy = {}
    exec(qzt__ddbc, {}, qnyoj__okfy)
    rtj__bcnta = qnyoj__okfy['json_impl']
    ciqfe__mvlms = _gen_json_reader_py(json_node.df_colnames, json_node.
        out_types, typingctx, targetctx, parallel, json_node.orient,
        json_node.convert_dates, json_node.precise_float, json_node.lines,
        json_node.compression, json_node.storage_options)
    wsbis__rzl = compile_to_numba_ir(rtj__bcnta, {'_json_reader_py':
        ciqfe__mvlms}, typingctx=typingctx, targetctx=targetctx, arg_typs=(
        string_type,), typemap=typemap, calltypes=calltypes).blocks.popitem()[1
        ]
    replace_arg_nodes(wsbis__rzl, [json_node.file_name])
    cbw__hzk = wsbis__rzl.body[:-3]
    for xxp__qgws in range(len(json_node.out_vars)):
        cbw__hzk[-len(json_node.out_vars) + xxp__qgws
            ].target = json_node.out_vars[xxp__qgws]
    return cbw__hzk


numba.parfors.array_analysis.array_analysis_extensions[JsonReader
    ] = bodo.ir.connector.connector_array_analysis
distributed_analysis.distributed_analysis_extensions[JsonReader
    ] = bodo.ir.connector.connector_distributed_analysis
typeinfer.typeinfer_extensions[JsonReader
    ] = bodo.ir.connector.connector_typeinfer
ir_utils.visit_vars_extensions[JsonReader
    ] = bodo.ir.connector.visit_vars_connector
ir_utils.remove_dead_extensions[JsonReader] = remove_dead_json
numba.core.analysis.ir_extension_usedefs[JsonReader
    ] = bodo.ir.connector.connector_usedefs
ir_utils.copy_propagate_extensions[JsonReader
    ] = bodo.ir.connector.get_copies_connector
ir_utils.apply_copy_propagate_extensions[JsonReader
    ] = bodo.ir.connector.apply_copies_connector
ir_utils.build_defs_extensions[JsonReader
    ] = bodo.ir.connector.build_connector_definitions
distributed_pass.distributed_run_extensions[JsonReader] = json_distributed_run
compiled_funcs = []


def _gen_json_reader_py(col_names, col_typs, typingctx, targetctx, parallel,
    orient, convert_dates, precise_float, lines, compression, storage_options):
    duid__zunwl = [sanitize_varname(pzeeq__irga) for pzeeq__irga in col_names]
    hbb__lbqf = ', '.join(str(xxp__qgws) for xxp__qgws, fdsx__oltwf in
        enumerate(col_typs) if fdsx__oltwf.dtype == types.NPDatetime('ns'))
    zsgck__oaqvj = ', '.join(["{}='{}'".format(nvaoc__efq, bodo.ir.csv_ext.
        _get_dtype_str(fdsx__oltwf)) for nvaoc__efq, fdsx__oltwf in zip(
        duid__zunwl, col_typs)])
    qsh__edpx = ', '.join(["'{}':{}".format(hwif__hdn, bodo.ir.csv_ext.
        _get_pd_dtype_str(fdsx__oltwf)) for hwif__hdn, fdsx__oltwf in zip(
        col_names, col_typs)])
    if compression is None:
        compression = 'uncompressed'
    qzt__ddbc = 'def json_reader_py(fname):\n'
    qzt__ddbc += '  df_typeref_2 = df_typeref\n'
    qzt__ddbc += '  check_java_installation(fname)\n'
    qzt__ddbc += f"""  bucket_region = bodo.io.fs_io.get_s3_bucket_region_njit(fname, parallel={parallel})
"""
    if storage_options is None:
        storage_options = {}
    storage_options['bodo_dummy'] = 'dummy'
    qzt__ddbc += (
        f'  storage_options_py = get_storage_options_pyobject({str(storage_options)})\n'
        )
    qzt__ddbc += (
        '  f_reader = bodo.ir.json_ext.json_file_chunk_reader(bodo.libs.str_ext.unicode_to_utf8(fname), '
        )
    qzt__ddbc += (
        """    {}, {}, -1, bodo.libs.str_ext.unicode_to_utf8('{}'), bodo.libs.str_ext.unicode_to_utf8(bucket_region), storage_options_py )
"""
        .format(lines, parallel, compression))
    qzt__ddbc += '  if bodo.utils.utils.is_null_pointer(f_reader._pyobj):\n'
    qzt__ddbc += "      raise FileNotFoundError('File does not exist')\n"
    qzt__ddbc += f'  with objmode({zsgck__oaqvj}):\n'
    qzt__ddbc += f"    df = pd.read_json(f_reader, orient='{orient}',\n"
    qzt__ddbc += f'       convert_dates = {convert_dates}, \n'
    qzt__ddbc += f'       precise_float={precise_float}, \n'
    qzt__ddbc += f'       lines={lines}, \n'
    qzt__ddbc += '       dtype={{{}}},\n'.format(qsh__edpx)
    qzt__ddbc += '       )\n'
    qzt__ddbc += (
        '    bodo.ir.connector.cast_float_to_nullable(df, df_typeref_2)\n')
    for nvaoc__efq, hwif__hdn in zip(duid__zunwl, col_names):
        qzt__ddbc += '    if len(df) > 0:\n'
        qzt__ddbc += "        {} = df['{}'].values\n".format(nvaoc__efq,
            hwif__hdn)
        qzt__ddbc += '    else:\n'
        qzt__ddbc += '        {} = np.array([])\n'.format(nvaoc__efq)
    qzt__ddbc += '  return ({},)\n'.format(', '.join(mdlri__bzprh for
        mdlri__bzprh in duid__zunwl))
    fdgmn__rove = globals()
    fdgmn__rove.update({'bodo': bodo, 'pd': pd, 'np': np, 'objmode':
        objmode, 'check_java_installation': check_java_installation,
        'df_typeref': bodo.DataFrameType(tuple(col_typs), bodo.
        RangeIndexType(None), tuple(col_names)),
        'get_storage_options_pyobject': get_storage_options_pyobject})
    qnyoj__okfy = {}
    exec(qzt__ddbc, fdgmn__rove, qnyoj__okfy)
    ciqfe__mvlms = qnyoj__okfy['json_reader_py']
    szdnx__tifhi = numba.njit(ciqfe__mvlms)
    compiled_funcs.append(szdnx__tifhi)
    return szdnx__tifhi
