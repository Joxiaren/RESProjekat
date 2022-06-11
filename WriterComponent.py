import rpyc

def check_input_data(idCounter,currentWaterCounsuption, month):
    if type(idCounter)!=int:
        raise TypeError("Water meter ID must be an integer!")
    if type(currentWaterCounsuption)==int or type(currentWaterCounsuption)==float:
        pass
    else:
        raise TypeError("The consumption is not a number!")
    return idCounter,currentWaterCounsuption, month


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


def send_data(conn,idCounter,currentWaterCounsuption, month):
    # here we should call function input_Data()
    try:
        id, wc, month = check_input_data(idCounter,currentWaterCounsuption, month)
        dict = {
            "idMeter" : id,
            "consumption" : wc,
            "month" : month
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
            print("Water meter ID: ")
            idCounter=int(input())
            print("Water consumption for that meter ID: ")
            currentWaterCounsuption= float(input())
            send_data(conn,idCounter,currentWaterCounsuption)
            print("Data successfully sent")
        except:
            print("You have to enter number!")
