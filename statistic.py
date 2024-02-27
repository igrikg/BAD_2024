from dataclasses import dataclass
from utils import time_display_decorator, work_with_none_decorator
import median


@dataclass
class ResultData:
    min: int = None
    max: int = None
    median: int = None
    mean: float = None

    def __str__(self):
        return f'Minimum:{self.min}\nMaximum: {self.max}\nMedian: {self.median}\nMean: {self.mean}\n'


@time_display_decorator
def get_parameter_by_numpy(file_name: str = '10m.txt'):
    try:
        import numpy as np
    except ImportError:
        print("Module numpy is not installed")
        return

    result = ResultData()
    data_array = np.loadtxt(file_name, dtype=int)
    result.mean = data_array.mean()
    result.max = data_array.max()
    result.min = data_array.min()
    result.median = np.median(data_array)
    print(result)
    return result


@time_display_decorator
def get_parameters_fromfile(file_name: str = '10m.txt') -> ResultData:
    result = ResultData()
    data_array = []
    number_line = 0
    min_none, max_none, sum_none = map(work_with_none_decorator, [min, max, sum])
    with open(file_name) as f:
        f.seek(0)
        for line in f:
            number = int(line)
            result.min = min_none(result.min, number)
            result.max = max_none(result.max, number)
            result.mean = sum_none(result.mean, number)
            number_line += 1
            data_array.append(number)
    result.mean /= number_line
    result.median = median.quickselect_median(data_array)
    print(result)
