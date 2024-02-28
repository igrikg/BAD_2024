from dataclasses import dataclass
from typing import Iterable

from utils import time_display_decorator, work_with_none_decorator
import median


@dataclass
class ResultData:
    min: int = None
    max: int = None
    median: int = None
    mean: float = None
    len_sequence_go_up: int = None
    len_sequence_go_down: int = None

    def __str__(self):
        return (f'Minimum:{self.min}\nMaximum: {self.max}\nMedian: {self.median}\nMean: {self.mean}\n'
                f'Length of increasing sequence:{self.len_sequence_go_up}\n'
                f'Length of decreasing sequence:{self.len_sequence_go_down}')


@time_display_decorator
def array_info_by_numpy(file_name: str = '10m.txt'):
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
    return result


@time_display_decorator
def array_info(file_name: str = '10m.txt') -> ResultData:
    result = ResultData()
    data_array = []
    number_line = 0
    current_go_up = 1
    current_go_down = 1
    prev_number = None
    min_none, max_none, sum_none = map(work_with_none_decorator, [min, max, sum])
    with open(file_name) as f:
        f.seek(0)
        for line in f:
            number = int(line)

            result.min = min_none(result.min, number)
            result.max = max_none(result.max, number)
            result.mean = sum_none(result.mean, number)
            number_line += 1
            # sequence
            if prev_number is not None and prev_number < number:
                current_go_up += 1
            else:
                result.len_sequence_go_up = max_none(result.len_sequence_go_up, current_go_up)
            if prev_number is not None and prev_number > number:
                current_go_down += 1
            else:
                result.len_sequence_go_down = max_none(result.len_sequence_go_down, current_go_down)
            prev_number = number
            data_array.append(number)
    result.mean /= number_line
    result.median = median.quickselect_median(data_array)
    return result

