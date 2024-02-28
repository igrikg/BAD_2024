import random
from typing import Iterable, Callable


def calc(data_list: Iterable, pivot_fn: Callable = random.choice) -> float:
    if len(data_list) % 2 == 1:
        return __quickselect(data_list, len(data_list) // 2, pivot_fn)
    else:
        return 0.5 * (__quickselect(data_list, len(data_list) // 2 - 1, pivot_fn) +
                      __quickselect(data_list, len(data_list) // 2, pivot_fn))


def __quickselect(data_list: Iterable, index: int, pivot_fn: Callable) -> int:
    """
    Выбираем k-тый элемент в списке l (с нулевой базой)
    :param data_list: список числовых данных
    :param index: индекс
    :param pivot_fn: функция выбора pivot
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
