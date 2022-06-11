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
    if type(street)!=str:
        raise TypeError("Street should be a string!")
    if type(db_name)!=str:
        raise TypeError("DB name should be a string!")
    if db_name!="Database.db" and db_name!="testDataBase.db" :
        raise(sqlite3.OperationalError("Incorrect DB name!"))
    
    conn = open_connection_to_db(db_name)
    cursor=conn.cursor()
    
    #if the given street name does not exist in the database, throw exception

    cursor.execute('''select streetName 
    from WATER_METER 
    where streetName = ?''',([street]))
    street = cursor.fetchall()
    if street == None:
        raise(sqlite3.DataError("The street does not exist!"))

    cursor.execute('''select month,sum(consumption)
    from WATER_CONSUMPTION as wc, WATER_METER as wm
    where wc.idMeter = wm.idMeter and wm.streetName=:street
    GROUP BY month;''',{"street":street})
    listOfMonths=cursor.fetchall()
    #we need to check what returns the DB if we enter the nonexsistent street!
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
    
    for monthConsumption in listOfMonths:
        report[monthConsumption[0]]=monthConsumption[1]
    
    close_connection_to_db(conn)

    return report


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
