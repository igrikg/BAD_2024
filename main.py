import time
import numpy as np

from dataclasses import dataclass


@dataclass
class ResultData:
    min: int = None
    max: int = None
    median: int = None
    mean: float = None


start = time.time()
a = np.loadtxt('10m.txt', dtype=int)
print("Min: ", a.min())
print("Max: ", a.max())
# print("Median: ", np.median(a))
print("Avg: ", a.mean())

print("Time: ", round(time.time() - start, 2))


# start = time.time()
# with open('10m.txt') as f:
#      f.seek(0)
#      for line in f:
#          b=line
# print("Time: ", round(time.time()-start, 2))

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


@time_display_decorator
def get_parameters_fromfile(file_name: str = '10m.txt') -> ResultData:
    result = ResultData()
    number = 0
    min_none, max_none, sum_none = map(work_with_none_decorator, [min, max, sum])



    with open(file_name) as f:
        f.seek(0)
        for line in f:
            number = int(line)
            result.min = min_none(result.min, number)
            result.max = max_none(result.max, number)
            result.mean = sum_none(result.mean, number)
            number += 1
    result.mean /= number
    print(result)



get_parameters_fromfile()
