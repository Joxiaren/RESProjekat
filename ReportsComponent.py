def getReportForSpecificStreet(street):
    # should return Dictionary<string, float> with name of month as a key and water consumption in specific STREET as value
    return


def getReportForSpecificCounter(idCounter):
    # should return Dictionary<string, float> with name of month as a key and water consumption on specific COUNTER as value
    return



def printReportForSpecificStreet(street, data):
    # data is Dictionary<string, float> with name of month as a key and water consumption as value
    print("Water consumption in street: " + street)
    print("----------------------------------------------------")
    for month in data:
        print(month + " : " + data[month])

    print("----------------------------------------------------")
    return


def printReportForSpecificCounter(idCounter, data):
    # data is Dictionary<string, float> with name of month as a key and water consumption as value
    print("Water consumption on specific water meter with id: " + idCounter)
    print("----------------------------------------------------")
    for month in data:
        print(month + " : " + data[month])

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
