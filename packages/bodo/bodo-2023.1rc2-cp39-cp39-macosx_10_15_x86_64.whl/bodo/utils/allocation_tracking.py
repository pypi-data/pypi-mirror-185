import llvmlite.binding as ll
import numba
from numba.core import types
from bodo.io import arrow_cpp
from bodo.libs import array_ext, decimal_ext, hstr_ext, quantile_alg
ll.add_symbol('get_stats_alloc_arr', array_ext.get_stats_alloc)
ll.add_symbol('get_stats_free_arr', array_ext.get_stats_free)
ll.add_symbol('get_stats_mi_alloc_arr', array_ext.get_stats_mi_alloc)
ll.add_symbol('get_stats_mi_free_arr', array_ext.get_stats_mi_free)
ll.add_symbol('get_stats_alloc_dec', decimal_ext.get_stats_alloc)
ll.add_symbol('get_stats_free_dec', decimal_ext.get_stats_free)
ll.add_symbol('get_stats_mi_alloc_dec', decimal_ext.get_stats_mi_alloc)
ll.add_symbol('get_stats_mi_free_dec', decimal_ext.get_stats_mi_free)
ll.add_symbol('get_stats_alloc_qa', quantile_alg.get_stats_alloc)
ll.add_symbol('get_stats_free_qa', quantile_alg.get_stats_free)
ll.add_symbol('get_stats_alloc_pq', arrow_cpp.get_stats_alloc)
ll.add_symbol('get_stats_free_pq', arrow_cpp.get_stats_free)
ll.add_symbol('get_stats_mi_alloc_pq', arrow_cpp.get_stats_mi_alloc)
ll.add_symbol('get_stats_mi_free_pq', arrow_cpp.get_stats_mi_free)
ll.add_symbol('get_stats_mi_alloc_qa', quantile_alg.get_stats_mi_alloc)
ll.add_symbol('get_stats_mi_free_qa', quantile_alg.get_stats_mi_free)
ll.add_symbol('get_stats_alloc_hstr', hstr_ext.get_stats_alloc)
ll.add_symbol('get_stats_free_hstr', hstr_ext.get_stats_free)
ll.add_symbol('get_stats_mi_alloc_hstr', hstr_ext.get_stats_mi_alloc)
ll.add_symbol('get_stats_mi_free_hstr', hstr_ext.get_stats_mi_free)
get_stats_alloc_arr = types.ExternalFunction('get_stats_alloc_arr', types.
    uint64())
get_stats_free_arr = types.ExternalFunction('get_stats_free_arr', types.
    uint64())
get_stats_mi_alloc_arr = types.ExternalFunction('get_stats_mi_alloc_arr',
    types.uint64())
get_stats_mi_free_arr = types.ExternalFunction('get_stats_mi_free_arr',
    types.uint64())
get_stats_alloc_dec = types.ExternalFunction('get_stats_alloc_dec', types.
    uint64())
get_stats_free_dec = types.ExternalFunction('get_stats_free_dec', types.
    uint64())
get_stats_mi_alloc_dec = types.ExternalFunction('get_stats_mi_alloc_dec',
    types.uint64())
get_stats_mi_free_dec = types.ExternalFunction('get_stats_mi_free_dec',
    types.uint64())
get_stats_alloc_pq = types.ExternalFunction('get_stats_alloc_pq', types.
    uint64())
get_stats_free_pq = types.ExternalFunction('get_stats_free_pq', types.uint64())
get_stats_mi_alloc_pq = types.ExternalFunction('get_stats_mi_alloc_pq',
    types.uint64())
get_stats_mi_free_pq = types.ExternalFunction('get_stats_mi_free_pq', types
    .uint64())
get_stats_alloc_qa = types.ExternalFunction('get_stats_alloc_qa', types.
    uint64())
get_stats_free_qa = types.ExternalFunction('get_stats_free_qa', types.uint64())
get_stats_mi_alloc_qa = types.ExternalFunction('get_stats_mi_alloc_qa',
    types.uint64())
get_stats_mi_free_qa = types.ExternalFunction('get_stats_mi_free_qa', types
    .uint64())
get_stats_alloc_hstr = types.ExternalFunction('get_stats_alloc_hstr', types
    .uint64())
get_stats_free_hstr = types.ExternalFunction('get_stats_free_hstr', types.
    uint64())
get_stats_mi_alloc_hstr = types.ExternalFunction('get_stats_mi_alloc_hstr',
    types.uint64())
get_stats_mi_free_hstr = types.ExternalFunction('get_stats_mi_free_hstr',
    types.uint64())


@numba.njit
def get_allocation_stats():
    wczg__mym = get_allocation_stats_arr(), get_allocation_stats_dec(
        ), get_allocation_stats_pq(), get_allocation_stats_qa(
        ), get_allocation_stats_hstr()
    jzfh__yad, fxk__eaa, jevqq__xfp, evklb__rqp = 0, 0, 0, 0
    for haarl__hryvd in wczg__mym:
        jzfh__yad += haarl__hryvd[0]
        fxk__eaa += haarl__hryvd[1]
        jevqq__xfp += haarl__hryvd[2]
        evklb__rqp += haarl__hryvd[3]
    return jzfh__yad, fxk__eaa, jevqq__xfp, evklb__rqp


@numba.njit
def get_allocation_stats_arr():
    return get_stats_alloc_arr(), get_stats_free_arr(), get_stats_mi_alloc_arr(
        ), get_stats_mi_free_arr()


@numba.njit
def get_allocation_stats_dec():
    return get_stats_alloc_dec(), get_stats_free_dec(), get_stats_mi_alloc_dec(
        ), get_stats_mi_free_dec()


@numba.njit
def get_allocation_stats_pq():
    return get_stats_alloc_pq(), get_stats_free_pq(), get_stats_mi_alloc_pq(
        ), get_stats_mi_free_pq()


@numba.njit
def get_allocation_stats_qa():
    return get_stats_alloc_qa(), get_stats_free_qa(), get_stats_mi_alloc_qa(
        ), get_stats_mi_free_qa()


@numba.njit
def get_allocation_stats_hstr():
    return get_stats_alloc_hstr(), get_stats_free_hstr(
        ), get_stats_mi_alloc_hstr(), get_stats_mi_free_hstr()
