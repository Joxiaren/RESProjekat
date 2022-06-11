import unittest
import unittest.mock
import ReportsComponent


class TestCaseInputNum(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(ReportsComponent.input_num("5", 10), 5)
        self.assertEqual(ReportsComponent.input_num("5"), 5)
        self.assertEqual(ReportsComponent.input_num("12", 20), 12)
        self.assertEqual(ReportsComponent.input_num(768, 1000), 768)
        self.assertEqual(ReportsComponent.input_num(13), 13)

    def test_over_limit(self):
        with self.assertRaises(ReportsComponent.InputOutOfRange):
            ReportsComponent.input_num(3, 2)
        with self.assertRaises(ReportsComponent.InputOutOfRange):
            ReportsComponent.input_num("17", 2)
        with self.assertRaises(ReportsComponent.InputOutOfRange):
            ReportsComponent.input_num(10, -5)

    def test_under_limit(self):
        with self.assertRaises(ReportsComponent.InputOutOfRange):
            ReportsComponent.input_num(-2, 2)
        with self.assertRaises(ReportsComponent.InputOutOfRange):
            ReportsComponent.input_num("-9", 2)
        with self.assertRaises(ReportsComponent.InputOutOfRange):
            ReportsComponent.input_num(3, 2)
        with self.assertRaises(ReportsComponent.InputOutOfRange):
            ReportsComponent.input_num(3, 2)

    def test_NAN(self):
        with self.assertRaises(Exception):
            ReportsComponent.input_num("pet", 2)
        with self.assertRaises(Exception):
            ReportsComponent.input_num("5e", 10)
        with self.assertRaises(Exception):
            ReportsComponent.input_num([1, 2])
        with self.assertRaises(Exception):
            ReportsComponent.input_num([], 2)
        with self.assertRaises(Exception):
            ReportsComponent.input_num({})
    # possible to add test for double input


if __name__ == '__main__':
    unittest.main()
