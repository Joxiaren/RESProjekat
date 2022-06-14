import sqlite3


def create_test_db():
    try:
        conn = sqlite3.connect('testDataBase.db')

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


def insert_data_to_wm():
    try:
        conn = sqlite3.connect('testDataBase.db')
        cursor = conn.cursor()
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

        conn.commit()
        print("Successfully inserted data in DB")
    except Exception as e:
        print(e)


def insert_one_row_to_wc_table(conn, idMeter, consumption, month):
    try:
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO WATER_CONSUMPTION (idMeter, consumption, month) 
        VALUES (:idMeter, :consumption, :month);
        ''', {'idMeter': idMeter, 'consumption': consumption, 'month': month})
        conn.commit()

    except Exception as e:
        print(e)


def insert_whole_table_wc():
    conn = sqlite3.connect('testDataBase.db')
    insert_one_row_to_wc_table(conn, 1, 24.5, 'January')
    insert_one_row_to_wc_table(conn, 1, 100.2, 'February')
    insert_one_row_to_wc_table(conn, 1, 2432.2, 'March')
    insert_one_row_to_wc_table(conn, 1, 23.2, 'April')
    insert_one_row_to_wc_table(conn, 1, 78.2, 'May')
    insert_one_row_to_wc_table(conn, 1, 1242.2, 'June')
    insert_one_row_to_wc_table(conn, 1, 12.2, 'July')
    insert_one_row_to_wc_table(conn, 1, 234.02, 'September')
    insert_one_row_to_wc_table(conn, 1, 98.2, 'October')
    insert_one_row_to_wc_table(conn, 1, 4.0, 'November')
    insert_one_row_to_wc_table(conn, 1, 15.2, 'December')
    insert_one_row_to_wc_table(conn, 1, 546.3, 'August')

    insert_one_row_to_wc_table(conn, 2, 24.5, 'February')
    insert_one_row_to_wc_table(conn, 2, 432.2, 'July')
    insert_one_row_to_wc_table(conn, 2, 2525.12, "September")
    print("Successfully inserted data")


def main():
    create_test_db()
    insert_data_to_wm()
    insert_whole_table_wc()




#if __name__ == "__main__":
   #main()