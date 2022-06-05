def connectToDatabase():
    pass


def disconnectFromDatabase(conn):
    pass


def writeToDatabase(data):
#data is list of dictionaries
    try:
        conn = connectToDatabase()
        cursor = conn.cursor()

        for dictionary in data:
            cursor.execute("INSERT INTO WATER_CONSUMPTION (idMeter, consumption, month) VALUES (:idMeter, :consumption, :month);",
                           {'idMeter': dictionary["idMeter"], 'consumption': dictionary["consumption"], 'month': dictionary["month"]})
            conn.commit()
            disconnectFromDatabase(conn)
    except Exception as e:
        print(e)
