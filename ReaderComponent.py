import sqlite3

@staticmethod
def connectToDatabase(dbName):
    connection_string = 'file:%s?mode=rw' % dbName
    conn = sqlite3.connect(dbName)
    return conn


@staticmethod
def disconnectFromDatabase(conn):
    conn.close()
    return

def writeToDatabase(data):
    # data is list of dictionaries
    try:
        conn = connectToDatabase('DataBase.db')
        cursor = conn.cursor()

        for dictionary in data:
            cursor.execute("INSERT INTO WATER_CONSUMPTION (idMeter, consumption, month) VALUES (:idMeter, :consumption, :month);",
                           {'idMeter': dictionary["idMeter"], 'consumption': dictionary["consumption"], 'month': dictionary["month"]})
            conn.commit()
        disconnectFromDatabase(conn)
    except Exception as e:
        print(e)

