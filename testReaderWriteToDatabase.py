import unittest
import ReaderComponent
from unittest.mock import MagicMock


conn = MagicMock()
conn.cursor = MagicMock()
conn.cursor.execute = MagicMock()
ReaderComponent.connectToDatabase = MagicMock()
cursor = MagicMock()
cursor.execute = MagicMock()
conn.commit = MagicMock()
class MyTestCase(unittest.TestCase):
    def test_something(self):
        data = [{"idMeter": 1, "consumption": 1.0, "month": "January"},
                {"idMeter": 2, "consumption": 2.0, "month": "February"},
                {"idMeter": 3, "consumption": 3.0, "month": "March"}]
        ReaderComponent.writeToDatabase(data)
        #ReaderComponent.connectToDatabase.asser_called_once_with()
        #conn.cursor.assert_called_with()
        cursor.execute.assert_called_with("INSERT INTO WATER_CONSUMPTION (idMeter, consumption, month) VALUES (1, 1.0, January);")
        #cursor.execute.assert_called_with("INSERT INTO WATER_CONSUMPTION (idMeter, consumption, month) VALUES (2, 2.0, February);")
        #cursor.execute.assert_called_with("INSERT INTO WATER_CONSUMPTION (idMeter, consumption, month) VALUES (3, 3.0, March);")
        #conn.commit.assert_called_with()


if __name__ == '__main__':
    unittest.main()
