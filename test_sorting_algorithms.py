from sorting_algorithms import *
import unittest

############################################################
##                                                        ##
##  UNIT TESTING OF PYTHON IMPLEMENTED SEARCH ALGORITHMS  ##
##                                                        ##
############################################################

class main(unittest.TestCase):


    def test_pass_int_through(self):
        self.assertEqual(convert_list([-36, -1, 0, 1, 35]), [-36, -1, 0, 1, 35])

    def test_pass_float_through(self):
        self.assertEqual(convert_list([234.64, 235.62, 2.2346, 0.1234]), [234.64, 235.62, 2.2346, 0.1234])

    def test_ignore_strings_with_characters(self):
            self.assertEqual(convert_list(['foo', 'bar', 'foo7bar']), [])

    def test_convert_num_strings_into_nums(self):
            self.assertEqual(convert_list(['235.34', '0.3521', '12', '48']), [235.34, 0.3521, 12.0, 48.0])

    def test_convert_mixed_list(self):
            self.assertEqual(convert_list(['235.34', 'marsh', 'snowflake' '0.3521', '12', '48', 12, 13, 56783, 0.2364, 0.43, 9863.0]),[235.34, 12.0, 48.0, 12, 13, 56783, 0.2364, 0.43, 9863.0])

    def test_bubble_sort_empty(self):
        self.assertEqual(bubble_sort([]), [])

    def test_selection_sort_empty(self):
        self.assertEqual(selection_sort([]), [])

    def test_quick_sort_empty(self):
        self.assertEqual(quick_sort([]), [])

    def test_bubble_sort_mixed(self):
        mixed_list = ['13556', 'hello', 12.532, 2678, 0, '0', '56bar', 'f00', '325.542', 0.123]
        mixed_list_sorted = [0, 0.0, 0.123, 12.532, 325.542, 2678, 13556.0]
        self.assertEqual(bubble_sort(mixed_list), [0, 0.0, 0.123, 12.532, 325.542, 2678, 13556.0])

    def test_quick_sort_mixed(self):
        mixed_list = ['13556', 'hello', 12.532, 2678, 0, '0', '56bar', 'f00', '325.542', 0.123]
        mixed_list_sorted = [0, 0.0, 0.123, 12.532, 325.542, 2678, 13556.0]
        self.assertEqual(quick_sort(mixed_list), [0, 0.0, 0.123, 12.532, 325.542, 2678, 13556.0])

    def test_selection_sort_mixed(self):
        mixed_list = ['13556', 'hello', 12.532, 2678, 0, '0', '56bar', 'f00', '325.542', 0.123]
        mixed_list_sorted = [0, 0.0, 0.123, 12.532, 325.542, 2678, 13556.0]
        self.assertEqual(selection_sort(mixed_list), [0, 0.0, 0.123, 12.532, 325.542, 2678, 13556.0])

if __name__ == '__main__':
    unittest.main()
