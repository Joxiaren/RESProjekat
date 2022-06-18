import unittest
import WriterComponent

class TestCovertToMonthName(unittest.TestCase):
    def test_not_int(self):
        self.assertRaises(TypeError, WriterComponent.convert_to_month_name, True)
        self.assertRaises(TypeError, WriterComponent.convert_to_month_name, 2.44)
        self.assertRaises(TypeError, WriterComponent.convert_to_month_name, "mile")

    def test_ok(self):
        self.assertEqual(WriterComponent.convert_to_month_name(1), 'January')
        self.assertEqual(WriterComponent.convert_to_month_name(2), 'February')
        self.assertEqual(WriterComponent.convert_to_month_name(3), 'March')
        self.assertEqual(WriterComponent.convert_to_month_name(4), 'April')
        self.assertEqual(WriterComponent.convert_to_month_name(5), 'May')
        self.assertEqual(WriterComponent.convert_to_month_name(6), 'June')
        self.assertEqual(WriterComponent.convert_to_month_name(7), 'July')
        self.assertEqual(WriterComponent.convert_to_month_name(8), 'August')
        self.assertEqual(WriterComponent.convert_to_month_name(9), 'September')
        self.assertEqual(WriterComponent.convert_to_month_name(10), 'October')
        self.assertEqual(WriterComponent.convert_to_month_name(11), 'November')
        self.assertEqual(WriterComponent.convert_to_month_name(12), 'December')


if __name__ == '__main__':
    unittest.main()
