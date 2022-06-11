import unittest
import WriterComponent
from unittest.mock import patch
from unittest.mock import MagicMock

conn = MagicMock()
conn.root = MagicMock()
conn.root.send_to_replicator = MagicMock()

class MyTestOKCase(unittest.TestCase):
    def test_ok_send_data(self):
        idCounter = 1
        currentWaterCounsuption = 20.2
        month = "January"

        dict = {
            "idMeter" : 1,
            "consumption" : 20.2,
            "month" : "January"
        }
        WriterComponent.send_data(conn, idCounter, currentWaterCounsuption, month)
        conn.root.send_to_replicator.assert_called_with(dict)


class MyTestNotOkCase(unittest.TestCase):
    def test_wrong_idMeter_send_data(self):
        dict = {
            "idMeter": 1,
            "consumption": 20.2,
            "month": "January"
        }

        idCounter = "mile"
        currentWaterCounsuption = 20.2
        month = "January"

        WriterComponent.send_data(conn, idCounter, currentWaterCounsuption, month)
        conn.root.send_to_replicator.assert_not_called()

    def test_wrong_consumption_send_data(self):
        dict = {
            "idMeter": 1,
            "consumption": 20.2,
            "month": "January"
        }

        idCounter = 1
        currentWaterCounsuption = "mile"
        month = "January"

        WriterComponent.send_data(conn, idCounter, currentWaterCounsuption, month)
        conn.root.send_to_replicator.assert_not_called()



if __name__ == '__main__':
    unittest.main()
