import time


def work_with_none_decorator(func):
    def wrapper(*args):
        without_none = list(filter(lambda x: x is not None, args))
        if not without_none:
            return None
        return func(without_none)

    return wrapper


def time_display_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        print("Time: ", round(time.time() - start_time, 2))
        return result
    return wrapper

