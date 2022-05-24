import rpyc

def open_connection():
    pass

def close_connection(conn):
    pass


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

        


