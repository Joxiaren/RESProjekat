def openConnectionToDB():
    #here we should return conn variable that represents connection to WATER_CONSUMPTION or WATER_METER DB
    #suggestion: as a parameter, we can add name of DB such as "WaterMeter.db" or "WaterConsumption.db"
    conn = 0 # added 0 because variable not declared
    return conn

def closeConnectionToDB(conn):
    # closing connection to db
    return


def getReportForSpecificStreet(street):
    # should return Dictionary<string, float> with name of month as a key and water consumption in specific STREET as value
    return


def getReportForSpecificCounter(idCounter):
    # should return Dictionary<string, float> with name of month as a key and water consumption on specific COUNTER as value
    if (type(idCounter) != int):
        raise TypeError("Id Counter have to be whole number ")

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
    #conn = sqlite3.connect("WaterConsumption.db")
    conn = openConnectionToDB()
    cursor = conn.cursor()
    cursor.execute('''select month, consumption
               from water_consumption 
               where idMeter = :idMeter''', {'idMeter': idCounter})
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


def printReportForSpecificCounter(idCounter, data):
    # data is Dictionary<string, float> with name of month as a key and water consumption as value
    print("Water consumption on specific water meter with id: " + str(idCounter))
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



def printFormatedReports(typeOfReport, street="", idCounter=-1):

    if (typeOfReport == "street") and (street != ""):
        dict = getReportForSpecificStreet(street)
        printReportForSpecificStreet(street, dict)
        return

    elif (typeOfReport == "id") and (idCounter != -1):
        dict = getReportForSpecificCounter(idCounter)
        printReportForSpecificCounter(idCounter, dict)
        return

    else:
        raise WrongNumberOfArguments()
