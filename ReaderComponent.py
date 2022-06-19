import copy
import sqlite3
import rpyc
from rpyc.utils.server import ThreadedServer


class ReaderComponentService(rpyc.Service):
    def on_connect(self, conn):
        # code that runs when service is connected
        print("Reader: Connected")
        pass

    def on_disconnect(self, conn):
        # code that runs when service is disconnected
        print("Reader: Disconnected")
        pass

    def exposed_print_message(self, message):
        print(message)

    def exposed_send_to_reader(self, data):

        print("Reader: Successfully received data")
        write_to_database(data)
        print(data)
        return
def connect_to_database(db_name):
    connection_string = 'file:%s?mode=rw' % db_name
    conn = sqlite3.connect(connection_string, uri=True)
    return conn

  
def disconnect_from_database(conn):
    conn.close()
    return


def write_to_database(data):
    # data is list of dictionaries
    try:
        conn = connect_to_database('DataBase.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO WATER_CONSUMPTION (idMeter, consumption, month) VALUES (:idMeter, :consumption, :month);",
                           {'idMeter': data[0], 'consumption': data[1], 'month': data[2]})
        conn.commit()
        print("Reader: Successfully inserted data")
        disconnect_from_database(conn)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    server = ThreadedServer(ReaderComponentService(), port=32277)
    print("server started")
    server.start()
