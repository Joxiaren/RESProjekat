import sqlite3

# create table that describes Water Meter
try:
    connWaterMeter = sqlite3.connect('WaterMeter.db')

    cursorWaterMeter = connWaterMeter.cursor()

    cursorWaterMeter.execute("""
        CREATE TABLE WATER_METER(
            idMeter       int      PRIMARY KEY     NOT NULL,
            name          text,
            lastName      text, 
            streetName    text,
            streetNumber  int,  
            postNumber    int,  
            city          text);  """)
    connWaterMeter.commit()
    print("Successfully created table WATER_METER")

except Exception as eWM:
    print(eWM)

# create table that describes Water Consumption
try:

    connWaterConsumption = sqlite3.connect("WaterConsumption.db")

    cursorWaterConsumption = connWaterConsumption.cursor()

    cursorWaterConsumption.execute("""
           CREATE TABLE WATER_CONSUMPTION(
               idMeter         int   NOT NULL,
               consumption     real,
               month           text  NOT NULL,
               PRIMARY KEY(idMeter, month));  """)

    connWaterConsumption.commit()
    print("Successfully created table WATER_CONSUMPTION")
except Exception as eWCON:
    print(eWCON)


