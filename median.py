import random
from typing import Iterable, Callable


def calc(data_list: Iterable) -> float:
    """
    Median calculation in the array. Algorithm from https://habr.com/ru/articles/346930/
    :param data_list: array with data
    :return:
        median value (float)
    """
    if len(data_list) % 2 == 1:
        return __quickselect(data_list, len(data_list) // 2)
    else:
        return 0.5 * (__quickselect(data_list, len(data_list) // 2 - 1) +
                      __quickselect(data_list, len(data_list) // 2))


def __quickselect(data_list: Iterable, index: int, pivot_fn: Callable = random.choice) -> int:
    """
    Recursive function for finding median in the array

    :param data_list: array with data
    :param index: index of finding elements median in our case
    :param pivot_fn: function of choosing element (default: random.choice)
    :return: k-тый элемент l
    """

    if len(data_list) == 1:
        assert index == 0
        return data_list[0]

    pivot = pivot_fn(data_list)

    lows = [el for el in data_list if el < pivot]
    highs = [el for el in data_list if el > pivot]
    pivots = [el for el in data_list if el == pivot]

    if index < len(lows):
        return __quickselect(lows, index, pivot_fn)
    elif index < len(lows) + len(pivots):
        return pivots[0]
    else:
        return __quickselect(highs, index - len(lows) - len(pivots), pivot_fn)
