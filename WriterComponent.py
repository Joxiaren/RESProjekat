import rpyc

def check_input_data(idCounter,currentWaterCounsuption):
    if type(idCounter)!=int:
        raise TypeError("Water meter ID must be an integer!")
    if type(currentWaterCounsuption)==int or type(currentWaterCounsuption)==float:
        pass
    else:
        raise TypeError("The consumption is not a number!")
    dict = {}
    dict[idCounter]=currentWaterCounsuption
    return dict


def open_connection():
    # connecting to ReplicatorSenderService
    conn = rpyc.connect("localhost", 22277)
    print("Writer connected.")
    return conn

def close_connection(conn):
    # disconnecting from ReplicatorSenderService
    del conn
    print("Writer disconnected.")


def send_data(conn):
    # here we should call function input_Data()
    # idCounter, currentWaterConsuption = input_Data()
    # dict =
    #       {
    #          "idCounter" : idCounter,
    #          "currentWaterCounsuption" : currentWaterConsuption    
    #       }
    #
    
    conn.root.send_to_replicator(dict)


if __name__ == "__main__": 


    conn = open_connection()

    while(True):
        print("Water meter ID: ")
        idCounter=input()
        print("Water consumption for that meter ID: ")
        currentWaterCounsuption= input()

        sendDict = check_input_data(idCounter,currentWaterCounsuption)
        send_data(conn)

        print("For exit enter 'exit': ")
        exit = input()
        if(exit.lower == 'exit'):
            close_connection(conn)
            break    
