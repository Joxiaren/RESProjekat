import copy
import time
import rpyc
from rpyc.utils.server import ThreadedServer
from threading import Thread

data_list = []


class Data:
    def __init__(self, tup, timestamp):
        self.tup = tup
        self.timestamp = timestamp


class ReplicatorReceiver:
    def open_connection(self): # pragma: no cover
        # connecting to ReaderService
        conn = rpyc.connect("localhost", 32277)
        print("ReplicatorReceiver: Connected.")
        return conn

    def close_connection(self, conn): # pragma: no cover
        # disconnecting from ReaderService
        del conn
        print("ReplicatorReceiver: Disconnected.")

    def send_data(self, conn, data):
        for s in data:
            conn.root.send_to_reader(s)
        print("sent data")
        return


class DataService(rpyc.Service):
    def exposed_temporary_store_data(self, data):
        print("ReplicatorReceiver: Received data.")
        print(data)
        data_list.append(Data(data, time.time()))


def try_send_data(to_send,sent_items,replicator_receiver,replicator_conn):
    if len(data_list) > 0:
        for data in data_list:
            if time.time() - data.timestamp >= 10:  # see if time expired
                to_send.append(data.tup)
                # print("Data to the Reader is ready to send! [{}]".format(data.dictionary))
                sent_items.append(data)  # add sent items to the buffer
        if len(to_send) > 0:
            replicator_receiver.send_data(replicator_conn, to_send)
            print("ReplicatorReceiver: Data to the reader has been sent!")
            to_send.clear()

        if len(sent_items) > 0:  # buffer not empty?
            for sent_item in sent_items:  # iterate through the buffer and delete those items from the data_list
                data_list.remove(sent_item)  # and remove them
                print("ReplicatorReceiver: Removed [{}]".format(sent_item))
            sent_items.clear()  # zero the buffer

              
def main():  # pragma: no cover
    listener_server = ThreadedServer(DataService(), port=22278)
    thread_listener = Thread(target=lambda: listener_server.start(), daemon=True)
    thread_listener.start()

    replicator_receiver = ReplicatorReceiver()
    replicator_conn = replicator_receiver.open_connection()
    sent_items = []
    to_send = []

    while True:
        try_send_data(to_send,sent_items,replicator_receiver,replicator_conn)
        time.sleep(1)

        
if __name__ == "__main__":
    main()
