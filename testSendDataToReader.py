import unittest
import ReplicatorReceiver
from unittest.mock import patch

@patch('ReaderService.send_to_reader')
class MyTestCase(unittest.TestCase):
    def test_send(self, mocked_send_to_reader):
        dictinary_list = [{"idMeter": 1, "consumption": 1.0, "month": "January"},
                          {"idMeter": 2, "consumption": 2.0, "month": "February"},
                          {"idMeter": 3, "consumption": 3.0, "month": "March"}]
        ReplicatorReceiver.send_data(dictinary_list)
        mocked_send_to_reader.assert_called_once_with(dictinary_list) # add assertion here


if __name__ == '__main__':
    unittest.main()
