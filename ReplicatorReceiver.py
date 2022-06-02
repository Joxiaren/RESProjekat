import time
import rpyc

data_list = []

class ReplicatorReceiver():
    def open_connection():
        # connecting to ReaderService
        conn = rpyc.connect("localhost", 32777)
        print("Writer connected.")
        return conn

    def close_connection(conn):
        # disconnecting from ReaderService
        del conn
        print("Writer disconnected.")

    def temporary_store_data(data):
        data_list.append({data:time.time()})
        
    def send_data(conn, data):
        conn.root.send_to_reader(data)


if __name__=="main":
    replicator_receiver=ReplicatorReceiver()
    replicator_conn = replicator_receiver.open_connection()
    while(True):
        for data in data_list:
            if data[list(data_list)[0]] - time.time() <= 10: #see if time expired
                replicator_receiver.send_data(replicator_conn,data)