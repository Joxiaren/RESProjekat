import sqlite3


def openConnectionToDB():
    #here we should return conn variable that represents connection to WATER_CONSUMPTION or WATER_METER DB
    #suggestion: as a parameter, we can add name of DB such as "DataBase.db"
    conn = 0 # added 0 because variable not declared
    return conn

def closeConnectionToDB(conn):
    # closing connection to db
    return


def getReportForSpecificStreet(street, dbName):
    # should return Dictionary<string, float> with name of month as a key and water consumption in specific STREET as value
    return


def getReportForSpecificMeter(idMeter, dbName):
    # should return Dictionary<string, float> with name of month as a key and water consumption on specific COUNTER as value
    if (type(idMeter) != int):
        raise TypeError("Id Meter have to be whole number ")
    if (type(dbName) != str):
        raise TypeError("Name of DB have to be string!")
    if (dbName != "DataBase.db" and dbName != "testDataBase.db"):
        raise sqlite3.OperationalError("Incorrect name of DB")


    report = {
        'January': 0,
        'February': 0,
        'March': 0,
        'April': 0,
        'May': 0,
        'June': 0,
        'July': 0,
        'August': 0,
        'September': 0,
        'October': 0,
        'November': 0,
        'December': 0
    }

    conn = openConnectionToDB(dbName)
    cursor = conn.cursor()
    cursor.execute('''select month, consumption
               from water_consumption 
               where idMeter = :idMeter''', {'idMeter': idMeter})
    listOfTuples = cursor.fetchall()

    for tuple in listOfTuples:
        report[tuple[0]] = tuple[1]

    closeConnectionToDB(conn)
    return report




def printReportForSpecificStreet(street, data):
    # data is Dictionary<string, float> with name of month as a key and water consumption as value
    print("Water consumption in street: " + street)
    print("----------------------------------------------------")
    for month in data:
        print(month + " : " + str(data[month]))

    print("----------------------------------------------------")
    return


def printReportForSpecificMeter(idMeter, data):
    # data is Dictionary<string, float> with name of month as a key and water consumption as value
    print("Water consumption on specific water meter with id: " + str(idMeter))
    print("----------------------------------------------------")
    for month in data:
        print(month + " : " + str(data[month]))

    print("----------------------------------------------------")
    return



class WrongNumberOfArguments(Exception):
    def __init__(self, message=None):
        self.message = message

    def __str__(self):
        if self.message is None:
            return "You did not pass correct number of arguments in function call."
        else:
            return self.message



def printFormatedReports(typeOfReport, street="", idMeter=-1):

    if (typeOfReport == "street") and (street != ""):
        dict = getReportForSpecificStreet(street, "DataBase.db")
        printReportForSpecificStreet(street, dict)
        return

    elif (typeOfReport == "id") and (idMeter != -1):
        dict = getReportForSpecificMeter(idMeter, "DataBase.db")
        printReportForSpecificMeter(idMeter, dict)
        return

    else:
        raise WrongNumberOfArguments()


def input_num(number, limit=-1):

    user_input = int(number)
    if number <= 0 or (limit != -1 and number > limit):
        raise InputOutOfRange
    return user_input


def main():
    while True:
        print("Enter number in front of desired report")
        print("1. Report for monthly consumption of a single street")
        print("2. Report for consumption throughout months for one water meter")

        while True:
            try:
                user_input = input_num(input(), 2)
                break
            except Exception as e:
                print(e)

        if user_input == 1:
            print("Input street name")
            # validation and return value should be double-checked (open to discussion)
            street_name = input()
            printReportForSpecificStreet(street_name, getReportForSpecificStreet(street_name, 'DataBase.db'))
            pass
        elif user_input == 2:
            print("Input water meter id")
            # validation and return value should be double-checked (open to discussion)
            id_meter = input()
            printReportForSpecificMeter(id_meter, getReportForSpecificMeter(id_meter, 'DataBase.db'))
            pass


if __name__ == "__main__":
    main()


class InputOutOfRange(Exception):
    def __init__(self, message=None):
        self.message = message

    def __str__(self):
        if self.message is None:
            return "Input number is out of option range"
        return self.message
