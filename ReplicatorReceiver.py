import time
import rpyc

data_list = []


class Data:
    def __init__(self, dictionary, timestamp):
        self.dictionary = dictionary
        self.timestamp = timestamp


class ReplicatorReceiver:
    def open_connection(self):
        # connecting to ReaderService
        conn = rpyc.connect("localhost", 32777)
        print("Replicator receiver connected.")
        return conn

    def close_connection(self, conn):
        # disconnecting from ReaderService
        del conn
        print("Replicator receiver disconnected.")

    def temporary_store_data(self, data):
        data_list.append(Data(data, time.time()))

    def send_data(self, conn, data):
        conn.root.send_to_reader(data)


def try_send_data(to_send,sent_items,replicator_receiver,replicator_conn):
    if len(data_list) > 0:
        for data in data_list:
            if time.time() - data.timestamp >= 10:  # see if time expired
                to_send.append(data.dictionary)
                # print("Data to the Reader is ready to send! [{}]".format(data.dictionary))
                sent_items.append(data)  # add sent items to the buffer
        if len(to_send) > 0:
            replicator_receiver.send_data(replicator_conn, to_send)
            print("Data to the reader has been sent!")
            to_send.clear()

        if len(sent_items) > 0:  # buffer not empty?
            for sent_item in sent_items:  # iterate through the buffer and delete those items from the data_list
                data_list.remove(sent_item)  # and remove them
                print("Removed [{}]".format(sent_item))
            sent_items = []  # zero the buffer


def main():
    replicator_receiver = ReplicatorReceiver()
    replicator_conn = replicator_receiver.open_connection()
    sent_items = []
    to_send = []

    while True:
        try_send_data(to_send,sent_items,replicator_receiver,replicator_conn)
        time.sleep(1)

        
if __name__ == "__main__":
    main()


