import unittest
import ReaderComponent
from unittest.mock import MagicMock
from unittest.mock import patch
from unittest.mock import call

conn = MagicMock()
cursor = MagicMock()
conn.cursor.return_value = cursor

class TestWriteToDatabase(unittest.TestCase):
    @patch("ReaderComponent.connect_to_database", return_value=conn)
    def test_regular_list_of_tuples(self, connectPatch):
        data = [(1, 1.0, "January"),
                ( 2, 2.0, "Februar"),
                ( 3, 3.0, "March")]
        calls = [call("INSERT INTO WATER_CONSUMPTION (idMeter, consumption, month) VALUES (:idMeter, :consumption, :month);",
                           {'idMeter': data[0][0], 'consumption': data[0][1], 'month': data[0][2]}),
                 call("INSERT INTO WATER_CONSUMPTION (idMeter, consumption, month) VALUES (:idMeter, :consumption, :month);",
                           {'idMeter': data[1][0], 'consumption': data[1][1], 'month': data[1][2]}),
                 call("INSERT INTO WATER_CONSUMPTION (idMeter, consumption, month) VALUES (:idMeter, :consumption, :month);",
                           {'idMeter': data[2][0], 'consumption': data[2][1], 'month': data[2][2]})]
        ReaderComponent.write_to_database(data[0])
        ReaderComponent.write_to_database(data[1])
        ReaderComponent.write_to_database(data[2])

        cursor.execute.assert_has_calls(calls)

    @patch("ReaderComponent.connect_to_database", return_value=conn)
    def test_empty_list_of_dictionaries(self, connectPatch):
        data = []
        ReaderComponent.write_to_database(data)
        cursor.execute.assert_not_called()


if __name__ == '__main__':
    unittest.main()
