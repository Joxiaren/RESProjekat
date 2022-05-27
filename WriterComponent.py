import rpyc


def open_connection():
    # connecting to ReplicatorSenderService
    conn = rpyc.connect("localhost", 22277)
    print("Writer connected.")
    return conn

def close_connection(conn):
    # disconnecting from ReplicatorSenderService
    del conn
    print("Writer disconnected.")

def input_data():
    pass


def send_data(conn):
    # here we should call function input_Data()
    try:
        idCounter, currentWaterConsuption = input_data()
        dict = {
            "idCounter" : idCounter,
            "currentWaterConsuption" : currentWaterConsuption
        }
        conn.root.send_to_replicator(dict)
    except TypeError as e:
       print(e)





if __name__ == "__main__": 


    conn = open_connection()

    while(True):
        print("Enter the number of action: ")
        print("1 - Input and send data: ")
        print("2 - Exit")
        try:
            action = int(input())
            if(action == 2):
                break
            send_data(conn)
            print("Data successfully sent")
        except:
            print("You have to enter number!")




