import copy

import rpyc
from rpyc.utils.server import ThreadedServer


class ReplicatorSenderService(rpyc.Service):
    def on_connect(self, conn): # pragma: no cover
        # code that runs when service is connected
        print("ReplicatorSender: Received connection")
        pass

    def on_disconnect(self, conn): # pragma: no cover
        # code that runs when service is disconnected
        print("ReplicatorSender: Disconnected")
        pass

    def exposed_print_message(self, message): # pragma: no cover
        print(message)

    def exposed_send_to_replicator(self, data): # pragma: no cover
        print("ReplicatorSender: Successfully received data")
        print(data)
        conn = rpyc.connect('localhost', 22278)
        print("ReplicatorSender: Opened connection to ReplicatorReceiver")
        conn.root.temporary_store_data(data)
        print("ReplicatorSender: Data sent")
        del conn
        print("ReplicatorSender: Closed connection to ReplicatorReceiver")
        # send_to_temp_storage(data)


def main(): # pragma: no cover
    server = ThreadedServer(ReplicatorSenderService(), port=22277)
    print("ReplicatorSender: Server started")
    server.start()


if __name__ == "__main__": # pragma: no cover
    main()


