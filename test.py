import copy
import time
import unittest
from parameterized import parameterized
from statistic import ResultData, array_info, array_info_by_numpy
from utils import time_display_decorator, work_with_none_decorator


class TestSimpleTask(unittest.TestCase):
    cases_list = [
        ["clean_array", [], ResultData(), (None, None)],
        ["tuple", (1, 2), ResultData(min=1, median=1.5, max=2, mean=1.5), (2, 1)],
        ["odd_length", [1, 4, 7, 9, 0, 2, 5], ResultData(min=0, median=4, max=9, mean=4.0), (4, 2)],
        ["even_length", [1, 4, 7, 9, 5, 0], ResultData(min=0, median=4.5, max=9, mean=26 / 6), (4, 3)],
        ["repeating_in_sentence", [1, 4, 7, 9, 9, 5, 0], ResultData(min=0, median=5, max=9, mean=5.0), (4, 3)],
        ["check_sentence_go_up", [1, 4, 7, 9, 5, 3, 0, 2, 3, 4, 5, 6, 10],
         ResultData(min=0, median=4.0, max=10, mean=59 / 13), (7, 4)],
        ["check_sentence_go_down", [1, 4, 7, 9, 5, 0, 10, 7, 3, 1, 4, 6, 5, 4, 3, 2, 1, -1, -2, -4, -5, -6],
         ResultData(min=-6, median=3.0, max=10, mean=54 / 22), (4, 11)],
        ["one_element", [1], ResultData(min=1, median=1, max=1, mean=1.0), (1, 1)],
        ["test_file", 'testfile.txt', ResultData(min=-49776703, median=6822118.5, max=49819201, mean=4937594.895833333),
         (4, 3)]
    ]

    @parameterized.expand(cases_list)
    def test_array_info_numpy(self, name, input_data, result_data, sentences_len):
        self.assertEqual(array_info_by_numpy(input_data), result_data)

    @parameterized.expand(cases_list)
    def test_array_info(self, name, input_data, result_data, sentences_len):
        result_data = copy.deepcopy(result_data)
        result_data.len_sequence_go_up, result_data.len_sequence_go_down = sentences_len
        self.assertEqual(array_info(input_data), result_data)

    def test_time_display_decorator(self):
        self.assertEqual(time_display_decorator(time.sleep)(1), None)

    @parameterized.expand([
        ["clean_array1", [], None, max],
        ["one_is_none", [1, None], 1, min],
        ["sum_two_elem", [1, 2], 3, sum],
    ])
    def test_work_with_none_decorator(self, name, input_data, result_data, function):
        self.assertEqual(work_with_none_decorator(function)(*input_data), result_data)

    def test_datares_output(self):
        result = (f'Minimum: None\nMaximum: None\nMedian: None\nMean: None\n'
                f'Length of increasing sequence: None\n'
                f'Length of decreasing sequence: None')
        self.assertEqual(str(ResultData()), result)


if __name__ == '__main__':
    unittest.main()
