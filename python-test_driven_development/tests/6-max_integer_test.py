#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInt(unittest.TestCase):
    def test_empty_list(self):
        self.assertIsNone(max_integer())

    def test_single_element(self):
        self.assertEqual(max_integer([5]), 5)

    def test_many_elements(self):
        self.assertEqual(max_integer([1, 5, 43, 78]), 78)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-9, -6, -78, -7]), -6)

    def test_dupes(self):
        self.assertEqual(max_integer([2, 2, 2]), 2)

    def test_mixed_elements(self):
        with self.assertRaises(TypeError):
            max_integer([73, '89', 32])


if __name__ == '__main__':
    unittest.main()
