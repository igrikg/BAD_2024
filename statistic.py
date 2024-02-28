from dataclasses import dataclass
from typing import Iterable

from utils import time_display_decorator, work_with_none_decorator
import median

__min_none, __max_none, __sum_none = map(work_with_none_decorator, [min, max, sum])


@dataclass
class ResultData:
    """Dataclass for  calculation result
    Args:
        min: int - the minimum value in the array
        max: int - the maximum value in the array
        median: int - the median of the array
        mean: float = the mean value of the array
        len_sequence_go_up: int  - the maximum length of the increasing sequence in the array
        len_sequence_go_down: int - the maximum length of the descending sequence in the array

    """
    min: int = None
    max: int = None
    median: float = None
    mean: float = None
    len_sequence_go_up: int = None
    len_sequence_go_down: int = None

    def __str__(self):
        return (f'Minimum: {self.min}\nMaximum: {self.max}\nMedian: {self.median}\nMean: {self.mean}\n'
                f'Length of increasing sequence: {self.len_sequence_go_up}\n'
                f'Length of decreasing sequence: {self.len_sequence_go_down}')

@time_display_decorator
def array_info_by_numpy(data: str | Iterable = '10m.txt') -> ResultData:
    """
    Calculate min, max, mean, median from file or array by using numpy library

    :param data: name or path to txt file with array
                 or
                 iterable object like list or tuple with array
    :return:
        ResultData - dataclass with all parameters
        len_sequence_go_up, len_sequence_go_down are not calculate (default values are None)
    """
    try:
        import numpy as np
    except ImportError:
        print("Module numpy is not installed")
        return

    result = ResultData()
    if isinstance(data, str):
        data_array = np.loadtxt(data, dtype=int)
    else:
        data_array = np.array(data, dtype=int)
    if not len(data_array) > 0:
        return result
    result.mean = data_array.mean()
    result.max = data_array.max()
    result.min = data_array.min()
    result.median = np.median(data_array)
    return result


def __calc_sequence(previous_numer: int, current_number: int, counter: int, result: int, go_up: bool = True) -> tuple[int]:
    """Function for counting of sentence elements"""
    if previous_numer is not None and (
            (go_up and (previous_numer < current_number)) or (not go_up and (previous_numer > current_number))):
        counter += 1
    else:
        return __max_none(result, counter), 1
    return __max_none(result, counter), counter


def __calc_info__array(numbers_list: Iterable):
    """
        Calculate min, max, mean, median of array

        :param iterable object like list or tuple with array
        :return:
            ResultData - dataclass with all parameters
    """
    result = ResultData()
    data_array = []
    number_line = 0
    current_go_up, current_go_down = 1, 1
    prev_number = None

    for line in numbers_list:
        number = int(line)
        result.min = __min_none(result.min, number)
        result.max = __max_none(result.max, number)
        result.mean = __sum_none(result.mean, number)
        number_line += 1
        # sequence calc
        result.len_sequence_go_up, current_go_up = __calc_sequence(prev_number, number, current_go_up,
                                                                   result.len_sequence_go_up)
        result.len_sequence_go_down, current_go_down = __calc_sequence(prev_number, number, current_go_down,
                                                                       result.len_sequence_go_down, False)
        prev_number = number
        data_array.append(number)
    if not len(data_array) > 0:
        return result
    result.mean /= number_line
    result.median = median.calc(data_array)
    return result


@time_display_decorator
def array_info(data: str | Iterable = '10m.txt') -> ResultData:
    """
        Calculate min, max, mean, median, maximum length of increasing and decreasing sequences from file or array

        :param data: name or path to txt file with array
                     or
                     iterable object like list or tuple with array
        :return:
            ResultData - dataclass with all parameters

    """
    if isinstance(data, str):
        with open(data) as file:
            file.seek(0)
            result = __calc_info__array(file)
    else:
        result = __calc_info__array(data)
    return result
