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
