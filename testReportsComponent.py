import unittest
import sqlite3
import ReportsComponent


class TestReportSpecificStreet(unittest.TestCase):
    def test_street_not_str(self):
        self.assertRaises(TypeError,ReportsComponent.get_report_for_specific_street,2,"DataBase.db")
        self.assertRaises(TypeError,ReportsComponent.get_report_for_specific_street,True,"DataBase.db")
        self.assertRaises(TypeError,ReportsComponent.get_report_for_specific_street,2.5,"DataBase.db")
    def test_db_not_str(self):
        self.assertRaises(TypeError,ReportsComponent.get_report_for_specific_street,"Bulevar Oslobodjenja",2)
        self.assertRaises(TypeError,ReportsComponent.get_report_for_specific_street,"Bulevar Oslobodjenja",True)
        self.assertRaises(TypeError,ReportsComponent.get_report_for_specific_street,"Bulevar Oslobodjenja",2.5)
    def test_invalid_db_name(self):
        self.assertRaises(sqlite3.OperationalError,ReportsComponent.get_report_for_specific_street,"Bulevar Oslobodjenja","invalid.db")
    def test_invalid_street_name(self):
        self.assertRaises(sqlite3.DataError,ReportsComponent.get_report_for_specific_street,"Bulevar Oslobodjenja","testDataBase.db")
    #def test_ok(self):
        #maybe we should call a script which fills in the data into the test DB
        #and see if it returns what is expected

if __name__ == '__main__':
    unittest.main()