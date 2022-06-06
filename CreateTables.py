import sqlite3

# create table that describes Water Meter
try:
    conn = sqlite3.connect('DataBase.db')

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE WATER_METER(
            idMeter       int      PRIMARY KEY     NOT NULL,
            name          text,
            lastName      text, 
            streetName    text,
            streetNumber  int,  
            postNumber    int,  
            city          text);  """)
    conn.commit()

    print("Successfully created table WATER_METER")

    cursor.execute("""
        CREATE TABLE WATER_CONSUMPTION(
            idMeter         int   NOT NULL,
            consumption     real,
            month           text  NOT NULL,
            PRIMARY KEY(idMeter, month));  """)

    conn.commit()
    print("Successfully created table WATER_CONSUMPTION")
    conn.close()

except Exception as e:
    print(e)