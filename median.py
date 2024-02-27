import random


def nlogn_median(data_list):
    data_list = sorted(data_list)
    if len(data_list) % 2 == 1:
        return data_list[len(data_list) // 2]
    else:
        return 0.5 * (data_list[len(data_list) // 2 - 1] + data_list[len(data_list) // 2])


def quickselect_median(data_list, pivot_fn=random.choice):
    if len(data_list) % 2 == 1:
        return __quickselect(data_list, len(data_list) // 2, pivot_fn)
    else:
        return 0.5 * (__quickselect(data_list, len(data_list) // 2 - 1, pivot_fn) +
                      __quickselect(data_list, len(data_list) // 2, pivot_fn))


def __quickselect(data_list, index, pivot_fn):
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
