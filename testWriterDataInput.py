import unittest
import WriterComponent


class TestWriterDataInput(unittest.TestCase):
    def test_id_notInt(self):
        self.assertRaises(TypeError,WriterComponent.check_input_data,2.5,3000)
        self.assertRaises(TypeError,WriterComponent.check_input_data,'a',3000)
        self.assertRaises(TypeError,WriterComponent.check_input_data,True,3000)
    def test_wc_not_number(self):
        self.assertRaises(TypeError,WriterComponent.check_input_data,50,"3000")
        self.assertRaises(TypeError,WriterComponent.check_input_data,50,True)
    
if __name__ == '__main__':
    unittest.main()
