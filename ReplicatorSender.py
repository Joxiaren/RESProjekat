import rpyc
from rpyc.utils.server import ThreadedServer


class ReplicatorSenderService(rpyc.Service):
    def on_connect(self, conn):
        # code that runs when service is connected
        print("i am connected")
        pass

    def on_disconnect(self, conn):
        # code that runs when service is disconnected
        print("i am disconnected")
        pass

    def exposed_print_message(self, message):
        print(message)

    def exposed_send_to_replicator(self, data):
        print("successfully received data")
        print(data)
        conn = rpyc.connect('localhost', 22278)
        print("opened connection to ReplicatorReceiver")
        conn.root.temporary_store_data(data)
        print("Data sent")
        del conn
        print("Closed connection to ReplicatorReceiver")
        # send_to_temp_storage(data)


def main():
    server = ThreadedServer(ReplicatorSenderService(), port=22277)
    print("server started")
    server.start()


if __name__ == "__main__":
    main()


