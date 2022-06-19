from asyncio import DatagramProtocol
import unittest
from unittest.mock import MagicMock, patch
from unittest.mock import ANY
import ReplicatorReceiver



class TestDataService(unittest.TestCase):
    @patch("ReplicatorReceiver.data_list")
    def test_forward_data_ok(self,empty_list):
        data = (1,1,1)
        data_service = ReplicatorReceiver.DataService()
        data_service.exposed_forward_data(data)
        empty_list.append.assert_called_once()

    @patch("ReplicatorReceiver.data_list")
    @patch("time.time")
    def test_try_send_data_not_called(self,empty_data_list,current_time):
        to_send=[]
        sent_items=[]
        empty_data_list=[]
        data = ReplicatorReceiver.Data((1,1,1),0)
        empty_data_list.append(data)
        current_time = 15

        replicator_receiver = ReplicatorReceiver.ReplicatorReceiver()
        replicator_conn = MagicMock()

        ReplicatorReceiver.try_send_data(to_send,sent_items,replicator_receiver,replicator_conn)

        self.assertEqual(to_send,[])
        self.assertEqual(sent_items,[])


if __name__=='__main__':
    unittest.main()