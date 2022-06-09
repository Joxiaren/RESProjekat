import rpyc
from rpyc.utils.server import ThreadedServer


class ReaderComponentService(rpyc.Service):
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

    def exposed_send_to_reader(self, data):
        print("successfully received data")
        print(data)
        # data check
        # send to temporary storage
        # send_to_temp_storage(data)

def connectToDatabase():
    pass


def disconnectFromDatabase(conn):
    pass


def writeToDatabase(data):
#data is list of dictionaries
    try:
        conn = connectToDatabase()
        cursor = conn.cursor()

        for dictionary in data:
            cursor.execute("INSERT INTO WATER_CONSUMPTION (idMeter, consumption, month) VALUES (:idMeter, :consumption, :month);",
                           {'idMeter': dictionary["idMeter"], 'consumption': dictionary["consumption"], 'month': dictionary["month"]})
            conn.commit()
            disconnectFromDatabase(conn)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    server = ThreadedServer(ReaderComponentService(), port=42277)
    print("server started")
    server.start()