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
        # data check
        # send to temporary storage
        # send_to_temp_storage(data)

if __name__ == "__main__":
    server = ThreadedServer(ReplicatorSenderService(), port=22277)
    print("server started")
    server.start()


