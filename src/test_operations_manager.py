import sys
import unittest

from operations_manager import OperationsManager


class TestOperationsManage(unittest.TestCase):

    def test_positive_integer_division(self):
        operations_manager = OperationsManager(10, 5)
        self.assertEqual(operations_manager.perform_division(), 2)

    def test_negative_integer_division(self):
        operations_manager = OperationsManager(-10, 5)
        self.assertEqual(operations_manager.perform_division(), -2)

    def test_float_division(self):
        operations_manager = OperationsManager(10.0, 5.0)
        self.assertEqual(operations_manager.perform_division(), 2.0)

    def test_float_division_by_zero(self):
        operations_manager = OperationsManager(10.0, 0.0)
        self.assertEqual(operations_manager.perform_division(), float("nan"))

    def test_integer_division_by_zero(self):
        operations_manager = OperationsManager(10, 0)
        self.assertEqual(operations_manager.perform_division(), float("nan"))

    def test_overflow_division(self):
        operations_manager = OperationsManager(sys.float_info.max, sys.float_info.min)
        self.assertEqual(operations_manager.perform_division(), float('inf'))

    def test_string_division(self):
        operations_manager = OperationsManager("10", "5")
        self.assertRaises(TypeError, operations_manager.perform_division)


if __name__ == '__main__':
    unittest.main()
