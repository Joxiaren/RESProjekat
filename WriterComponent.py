import rpyc

def check_input_data(idCounter,waterCounsuption, month):
    if type(idCounter)!=int:
        raise TypeError("Water meter ID must be an integer!")
    if type(waterCounsuption)==int or type(waterCounsuption)==float:
        pass
    else:
        raise TypeError("The consumption is not a number!")
    return idCounter,waterCounsuption, month

def convert_to_month_name(month):
    if(type(month) != int):
        raise TypeError("Month input has to be whole number!")

    converter = {
         1: 'January',
         2: 'February',
         3: 'March',
         4: 'April',
         5: 'May',
         6: 'June',
         7: 'July',
         8: 'August',
         9: 'September',
         10: 'October',
         11: 'November',
         12: 'December'
    }

    month_name = converter[month]
    return month_name

def open_connection(): # pragma: no cover
    # connecting to ReplicatorSenderService
    conn = rpyc.connect("localhost", 22277)
    print("Writer connected to ReplicatorSender.")
    return conn

def close_connection(conn): # pragma: no cover
    # disconnecting from ReplicatorSenderService
    del conn
    print("Writer disconnected from ReplicatorSender.")

def input_data(): # pragma: no cover
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
        #dict_as_string = f"idMeter:{id},consumption:{wc},month:{month}"
        tup = (id, wc, month)
        conn.root.send_to_replicator(tup)
    except TypeError as e:
       print(e)


def input_num(number, upper_limit=None):
    user_input = int(number)
    if user_input <= 0 or (upper_limit is not None and user_input > upper_limit):
        raise InputOutOfRange
    return user_input


if __name__ == "__main__": # pragma: no cover

    while True:
        print("Enter the number of action: ")
        print("1 - Input and send data: ")
        print("2 - Exit")
        try:
            action = input_num(input(), 2)
            if action == 2:
                break

            conn = open_connection()
            print("Opened connection")
            print("Water meter ID: ")
            idCounter=int(input())
            print("Water consumption for that meter ID: ")
            currentWaterCounsuption = float(input())
            print("Month [1-12] in which measurement took place: ")
            month = 0
            while True:
                try:
                    month = input_num(input(), 12)
                    break
                except Exception as e:
                    print(e)
                    print("Please retry the input")

            send_data(conn, idCounter, currentWaterCounsuption, convert_to_month_name(month))
            print("Data successfully sent")
            close_connection(conn)
            print("Closed connection")
        except:
            print("You have to enter number!")


class InputOutOfRange(Exception):
    def __init__(self, message=None):
        self.message = message

    def __str__(self): # pragma: no cover
        if self.message is None:
            return "Input number is out of option range"
        return self.message
    
