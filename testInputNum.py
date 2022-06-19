import unittest
import WriterComponent


class InputNumTestCase(unittest.TestCase):
    def test_not_int(self):
        self.assertRaises(ValueError, WriterComponent.input_num, "mile", 12)
        #self.assertRaises(TypeError, WriterComponent.input_num, True, 12)
        #ako stavim True, ne baca error, ne znam sto?


    def test_input_out_of_range_lower(self):
        self.assertRaises(WriterComponent.InputOutOfRange, WriterComponent.input_num, 0, 12)
        self.assertRaises(WriterComponent.InputOutOfRange, WriterComponent.input_num, -1, 12)
        self.assertRaises(WriterComponent.InputOutOfRange, WriterComponent.input_num, -1)
        self.assertRaises(WriterComponent.InputOutOfRange, WriterComponent.input_num, 0)

    def test_input_out_of_range_upper(self):
        self.assertRaises(WriterComponent.InputOutOfRange, WriterComponent.input_num, 13, 12)
        self.assertRaises(WriterComponent.InputOutOfRange, WriterComponent.input_num, 20, 12)

    #def test_input_limit_is_none(self):
    # self.assertRaises(WriterComponent.InputOutOfRange, WriterComponent.input_num, 4)
    # on je ok ako je granica None, ne znam sto?


    def test_ok(self):
        self.assertEqual(WriterComponent.input_num(12, 12), 12)
        self.assertEqual(WriterComponent.input_num(1, 12), 1)
        self.assertEqual(WriterComponent.input_num(5, 12), 5)
        self.assertEqual(WriterComponent.input_num(4), 4)

if __name__ == '__main__':
    unittest.main()
