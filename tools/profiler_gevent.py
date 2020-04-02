import time
from functools import wraps

import GreenletProfiler


def do_line_profile_wrap(func):
    @wraps(func)
    def decorator(*args, **kwargs):

        filename = '/var/log/slots/callgrind.{}_{}.prof'.format(func.__name__, int(time.time() * 1000))
        GreenletProfiler.set_clock_type('cpu')

        try:
            GreenletProfiler.start()
            return func(*args, **kwargs)
        finally:
            GreenletProfiler.stop()
            stats = GreenletProfiler.get_func_stats()
            stats.print_all()
            stats.save(filename, type='callgrind')

    return decorator
