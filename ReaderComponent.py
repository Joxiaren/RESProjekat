import sqlite3


@staticmethod
def connect_to_database(db_name):
    connection_string = 'file:%s?mode=rw' % db_name
    conn = sqlite3.connect(db_name)
    return conn


@staticmethod
def disconnect_from_database(conn):
    conn.close()
    return


def write_to_database(data):
    # data is list of dictionaries
    try:
        conn = connect_to_database('DataBase.db')
        cursor = conn.cursor()

        for dictionary in data:
            cursor.execute("INSERT INTO WATER_CONSUMPTION (idMeter, consumption, month) VALUES (:idMeter, :consumption, :month);",
                           {'idMeter': dictionary["idMeter"], 'consumption': dictionary["consumption"], 'month': dictionary["month"]})
            conn.commit()
        disconnect_from_database(conn)
    except Exception as e:
        print(e)

