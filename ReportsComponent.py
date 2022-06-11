import sqlite3


def open_connection_to_db(db_name):
    connection_string = 'file:%s?mode=rw' % db_name
    conn = sqlite3.connect(connection_string, uri=True)
    return conn


def close_connection_to_db(conn):
    conn.close()
    return


def get_report_for_specific_street(street, db_name):
    # should return Dictionary<string, float> with name of month as a key and water consumption in specific STREET as value
    return


def get_report_for_specific_meter(id_meter, db_name):
    # should return Dictionary<string, float> with name of month as a key and water consumption on specific COUNTER as value
    if type(id_meter) != int:
        raise TypeError("Id Meter have to be whole number ")
    if type(db_name) != str:
        raise TypeError("Name of DB have to be string!")
    if db_name != "DataBase.db" and db_name != "testDataBase.db":
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

    conn = open_connection_to_db(db_name)
    cursor = conn.cursor()
    cursor.execute('''select month, consumption
               from water_consumption 
               where idMeter = :idMeter''', {'idMeter': id_meter})
    list_of_tuples = cursor.fetchall()

    for t in list_of_tuples:
        report[t[0]] = t[1]

    close_connection_to_db(conn)
    return report


def print_report_for_specific_street(street, data):
    # data is Dictionary<string, float> with name of month as a key and water consumption as value
    print("Water consumption in street: " + street)
    print("----------------------------------------------------")
    for month in data:
        print(month + " : " + str(data[month]))

    print("----------------------------------------------------")
    return


def print_report_for_specific_meter(id_meter, data):
    # data is Dictionary<string, float> with name of month as a key and water consumption as value
    print("Water consumption on specific water meter with id: " + str(id_meter))
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


def print_formatted_reports(type_of_report, street="", id_meter=-1):

    if (type_of_report == "street") and (street != ""):
        dictionary = get_report_for_specific_street(street, "DataBase.db")
        print_report_for_specific_street(street, dictionary)
        return

    elif (type_of_report == "id") and (id_meter != -1):
        dictionary = get_report_for_specific_meter(id_meter, "DataBase.db")
        print_report_for_specific_meter(id_meter, dict)
        return

    else:
        raise WrongNumberOfArguments()


def input_num(number, upper_limit=None):
    user_input = int(number)
    if user_input <= 0 or (upper_limit is not None and user_input > upper_limit):
        raise InputOutOfRange
    return user_input


def main():
    user_input = 0
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
