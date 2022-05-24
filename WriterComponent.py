import rpyc

def input_data():
    print("Water meter ID: ")
    idCounter=input()
    if type(idCounter)!=int:
        raise TypeError("Water meter ID must be an integer!")
    print("Water consumption for that meter ID: ")
    currentWaterCounsuption= input()
    if type(currentWaterCounsuption)==int or type(currentWaterCounsuption)==float:
        pass
    else:
        raise TypeError("The consumption is not a number!")

    return idCounter,currentWaterCounsuption


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
        
        send_data(conn)

        print("For exit enter 'exit': ")
        exit = input()
        if(exit.lower == 'exit'):
            close_connection(conn)
            break    
