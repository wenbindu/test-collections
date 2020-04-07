import time
from functools import wraps
import cProfile
import time
from functools import wraps
import random
import yappi
import pstats

from line_profiler import LineProfiler

PATH = '/var/log'

def yappi_wrap(func):
    @wraps(func)
    def decorator(*args, **kwargs):
        filename = '{}/callgrind.{}.prof'.format(PATH, int(time.time() * 1000))
        yappi.set_clock_type('cpu')
        yappi.start(builtins=True)

        result = func(*args, **kwargs)
        stats = yappi.get_func_stats()
        stats.save(filename, type='callgrind')

        return result

    return decorator


def cprofile_wrap(func):
    @wraps(func)
    def decorator(*args, **kwargs):
        filename = '{}/cprofile.{}.prof'.format(PATH, int(time.time() * 1000))
        pr = cProfile.Profile()
        pr.enable()
        # func
        result = func(*args, **kwargs)
        pr.disable()
        pr.dump_stats(filename)
        return result

    return decorator


def line_proflie_wrap(func):
    @wraps(func)
    def decorator(*args, **kwargs):
        lp = LineProfiler()
        lp_wrapper = lp(func)
        result =lp_wrapper(*args, **kwargs)
        lp.print_stats()
        return result
    return decorator


def do_line_profile_wrap(func):
    @wraps(func)
    def decorator(*args, **kwargs):
        # line-profiler==3.0.2
        profiler = LineProfiler()
        try:
            profiler.add_function(func)
            profiler.enable_by_count()
            return func(*args, **kwargs)
        finally:
            profiler.dump_stats('/var/log/{}.lprof'.format(time.time()))
    return decorator