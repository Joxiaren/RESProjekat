import unittest
import ReaderComponent
from unittest.mock import MagicMock
from unittest.mock import patch
from unittest.mock import call

conn = MagicMock()
cursor = MagicMock()
conn.cursor.return_value = cursor

class TestWriteToDatabase(unittest.TestCase):
    @patch("ReaderComponent.connectToDatabase", return_value=conn)
    def test_regular_list_of_dictionaries(self, connectPatch):
        data = [{"idMeter": 1, "consumption": 1.0, "month": "January"},
                {"idMeter": 2, "consumption": 2.0, "month": "February"},
                {"idMeter": 3, "consumption": 3.0, "month": "March"}]
        calls = [call("INSERT INTO WATER_CONSUMPTION (idMeter, consumption, month) VALUES (:idMeter, :consumption, :month);",
                           {'idMeter': data[0]["idMeter"], 'consumption': data[0]["consumption"], 'month': data[0]["month"]}),
                 call("INSERT INTO WATER_CONSUMPTION (idMeter, consumption, month) VALUES (:idMeter, :consumption, :month);",
                           {'idMeter': data[1]["idMeter"], 'consumption': data[1]["consumption"], 'month': data[1]["month"]}),
                 call("INSERT INTO WATER_CONSUMPTION (idMeter, consumption, month) VALUES (:idMeter, :consumption, :month);",
                           {'idMeter': data[2]["idMeter"], 'consumption': data[2]["consumption"], 'month': data[2]["month"]})]
        ReaderComponent.writeToDatabase(data)

        cursor.execute.assert_has_calls(calls)

    @patch("ReaderComponent.connectToDatabase", return_value=conn)
    def test_empty_list_of_dictionaries(self, connectPatch):
        data = []
        ReaderComponent.writeToDatabase(data)
        cursor.execute.assert_not_called()


if __name__ == '__main__':
    unittest.main()
