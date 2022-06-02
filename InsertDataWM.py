import sqlite3


# help function
# def deleteRow(cursor, idMeter):
#    cursor.execute('''
#   delete from WATER_METER
#   where idMeter = :idMeter;''', {'idMeter' : idMeter})

# help function
def printRows(cursor):
    cursor.execute("SELECT * from WATER_METER;")
    rows = cursor.fetchall()
    for i in rows:
        print(i)


def insertData(cursor):
    try:
        cursor.execute('''
        INSERT INTO WATER_METER (idMeter, name, lastName, streetName, streetNumber, postNumber, city)
        VALUES
            (1, 'Slobodan', 'Zivkovic', 'Cegarskih junaka', 22, 18000, 'Nis'),

            (2, 'Djordje', 'Miletic', 'Ulica Radoja Krstica', 55, 37240, 'Trstenik'),
            (3, 'Milena', 'Mikic', 'Ulica Radoja Krstica', 55, 37240, 'Trstenik'),
            (4, 'Milovan', 'Tesic', 'Ulica Radoja Krstica', 46, 37240, 'Trstenik'),
            (5, 'Aleksandra', 'Simic', 'Ulica Radoja Krstica', 67, 37240, 'Trstenik'),
            (6, 'Andrija', 'Jovanovic', 'Ulica Radoja Krstica', 23, 37240, 'Trstenik'),

            (7, 'Stojan', 'Mirkovic', 'Ulica Svetog Save', 32, 32000, 'Cacak'),
            (8, 'Miloje', 'Milanovic', 'Ulica Svetog Save', 56, 32000, 'Cacak' ),
            (9, 'Jelena', 'Petrovic', 'Ulica Svetog Save', 12, 32000, 'Cacak' ),
            (10, 'Stanoje', 'Lakic', 'Ulica Svetog Save', 4, 32000, 'Cacak' ),
            (11, 'Stanka', 'Radomirovic', 'Ulica Svetog Save', 78, 32000, 'Cacak' ),

            (12, 'Zivorad', 'Simic', 'Bulevar Stepe Stepanovica', 4, 78000, 'Banja Luka'),
            (13, 'Veselinka', 'Petrovic', 'Bulevar Stepe Stepanovica', 24, 78000, 'Banja Luka'),
            (14, 'Milorad', 'Stojkovic', 'Bulevar Stepe Stepanovica', 33, 78000, 'Banja Luka'),
            (15, 'Slavica', 'Andric', 'Bulevar Stepe Stepanovica', 61, 78000, 'Banja Luka'),
            (16, 'Vera', 'Milinkovic', 'Bulevar Stepe Stepanovica', 52, 78000, 'Banja Luka'),       

            (17, 'Zivko', 'Miljkovic', 'Rackog', 16, 21131, 'Petrovaradin'),
            (18, 'Sladjana', 'Stanimiriovic', 'Rackog', 58, 21131, 'Petrovaradin'),
            (19, 'Rade', 'Tripkovic', 'Rackog', 93, 21131, 'Petrovaradin'),
            (20, 'Boris', 'Radic', 'Rackog', 102, 21131, 'Petrovaradin'),
            (21, 'Ana', 'Minic', 'Rackog', 11, 21131, 'Petrovaradin');''')

        conn.commit();

    except Exception as e:
        print(e)


if __name__ == "__main__":
    # create connection to WaterMeter.db
    conn = sqlite3.connect('WaterMeter.db')
    cursor = conn.cursor()

    insertData(cursor)
    #printRows(cursor)

