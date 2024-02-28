import time
from typing import Callable


def work_with_none_decorator(func: Callable) -> Callable:
    """Decorator for make possibility to run function like min,max,sum, with None arguments.
    These arguments not include to calculation."""
    def wrapper(*args):
        without_none = list(filter(lambda x: x is not None, args))
        if not without_none:
            return None
        return func(without_none)

    return wrapper


def time_display_decorator(func: Callable) -> Callable:
    """Decorator show function execution time"""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        print("Operations execution time: ", round(time.time() - start_time, 2),'s')
        return result
    return wrapper

