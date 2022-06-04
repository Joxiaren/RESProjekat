import time
import rpyc

data_list = []

class Data():
    def __init__(self,dictionary,timestamp):
        self.dictionary = dictionary
        self.timestamp=timestamp

class ReplicatorReceiver():
    def open_connection(self):
        # connecting to ReaderService
        conn = rpyc.connect("localhost", 32777)
        print("Replicator receiver connected.")
        return conn

    def close_connection(self,conn):
        # disconnecting from ReaderService
        del conn
        print("Replicator receiver disconnected.")

    def temporary_store_data(self,data):
        data_list.append(Data(data,time.time()))
        
    def send_data(self,conn, data):
        conn.root.send_to_reader(data)


if __name__=="main":
    replicator_receiver=ReplicatorReceiver()
    replicator_conn = replicator_receiver.open_connection()
    sent_items=[]

    while(True):
        for data in data_list:
            if data.timestamp - time.time() <= 10: #see if time expired
                replicator_receiver.send_data(replicator_conn,data.dictionary)
                print("Data to the Reader is sent! [{}]".format(data.dictionary))
                sent_items.append(data) #add the sent items to the buffer

        if len(sent_items)>0: #buffer not empty?
            for sent_item in sent_items: #iterate trough the buffer and delete those items from the data_list
                data_list.remove(sent_item) #and remove them
                print("Removed [{}]".format(sent_item))
            sent_items=[] #zero the buffer

            
                