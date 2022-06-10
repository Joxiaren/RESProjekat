import unittest
from ReplicatorReceiver import ReplicatorReceiver as RR
from unittest.mock import MagicMock

conn = MagicMock()
conn.root = MagicMock()
conn.root.send_to_reader = MagicMock()

replicatorComponent = RR()

class MyTestCase(unittest.TestCase):
    def test_send_regular_data(self):
        data = [{"idMeter": 1, "consumption": 1.0, "month": "January"},
                {"idMeter": 2, "consumption": 2.0, "month": "February"},
                {"idMeter": 3, "consumption": 3.0, "month": "March"}]
        replicatorComponent.send_data(conn,data)
        conn.root.send_to_reader.assert_called_with(data)

    def test_send_empty_data(self):
        empty_data = []
        replicatorComponent.send_data(conn, empty_data)
        conn.root.send_to_reader.assert_called_with(empty_data)

    def test_send_without_conn_parameter(self):
        data = [{"idMeter": 1, "consumption": 1.0, "month": "January"},
                {"idMeter": 2, "consumption": 2.0, "month": "February"},
                {"idMeter": 3, "consumption": 3.0, "month": "March"}]
        self.assertRaises(TypeError, replicatorComponent.send_data, data)

    def test_send_without_data_parameter(self):
        self.assertRaises(TypeError, replicatorComponent.send_data, conn)



if __name__ == '__main__':
    unittest.main()
