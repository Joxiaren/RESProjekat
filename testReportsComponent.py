from time import sleep
import unittest
import sqlite3
import ReportsComponent
import CreateTestDataBase
import os.path
from os import path
from unittest.mock import patch, call

#REPORT PRINT TEST
@patch('builtins.print')
class TestPrintReportForSpecificStreet(unittest.TestCase):
    def test_empty_dict(self, mocked_print):
        ReportsComponent.print_report_for_specific_street("Kninska", {})
        assert mocked_print.mock_calls == [call("Water consumption in street: Kninska"),
                                           call("----------------------------------------------------"),
                                           call("----------------------------------------------------")]

    def test_regular_dict(self, mocked_print):
        ReportsComponent.print_report_for_specific_street("Kninska", {"January": 1.0, "February": 2.0, "March": 3.0})
        assert mocked_print.mock_calls == [call("Water consumption in street: Kninska"),
                                           call("----------------------------------------------------"),
                                           call("January : 1.0"), call("February : 2.0"), call("March : 3.0"),
                                           call("----------------------------------------------------")]

@patch('builtins.print')
class TestPrintReportForSpecificCounter(unittest.TestCase):
    def test_empty_dict(self, mocked_print):
        ReportsComponent.print_report_for_specific_meter(1, {})
        assert mocked_print.mock_calls == [call("Water consumption on specific water meter with id: 1"),
                                           call("----------------------------------------------------"),
                                           call("----------------------------------------------------")]

    def test_regular_dict(self, mocked_print):
        ReportsComponent.print_report_for_specific_meter(1, {"January": 1.0, "February": 2.0, "March": 3.0})
        assert mocked_print.mock_calls == [call("Water consumption on specific water meter with id: 1"),
                                           call("----------------------------------------------------"),
                                           call("January : 1.0"), call("February : 2.0"), call("March : 3.0"),
                                           call("----------------------------------------------------")]

#FETCHING DATA FROM DATABASE TEST
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
    def test_ok(self):
        #see if the funciton that returns report gets proper values
        report = {
        'January': 24.5,
        'February': 100.2,
        'March': 2432.2,
        'April': 23.2,
        'May': 78.2,
        'June': 1242.2,
        'July': 12.2,
        'August': 546.3,
        'September': 234.02,
        'October': 98.2,
        'November': 4.0,
        'December': 15.2
        }
        self.assertEqual(ReportsComponent.get_report_for_specific_street("Cegarskih junaka","testDataBase.db"),report)

class TestReportForSpecificIdCounter(unittest.TestCase):
    def test_id_not_int(self):
        self.assertRaises(TypeError, ReportsComponent.get_report_for_specific_meter, "mile", "testDataBase.db")
        self.assertRaises(TypeError, ReportsComponent.get_report_for_specific_meter, True, "testDataBase.db")
        self.assertRaises(TypeError, ReportsComponent.get_report_for_specific_meter, 2.5, "testDataBase.db")

    def test_db_not_str(self):
        self.assertRaises(TypeError, ReportsComponent.get_report_for_specific_meter, 1, 5)
        self.assertRaises(TypeError, ReportsComponent.get_report_for_specific_meter, 1, False)
        self.assertRaises(TypeError, ReportsComponent.get_report_for_specific_meter, 1, 5.5)

    def test_invalid_db_name(self):
        self.assertRaises(sqlite3.OperationalError, ReportsComponent.get_report_for_specific_meter, 1, "mile.db")

    def test_invalid_id_number(self):
        self.assertRaises(sqlite3.DataError, ReportsComponent.get_report_for_specific_meter, 50, "testDataBase.db")

    def test_ok(self):
        data = {
            'January': 24.5,
            'February': 100.2,
            'March': 2432.2,
            'April': 23.2,
            'May': 78.2,
            'June': 1242.2,
            'July': 12.2,
            'August': 546.3,
            'September': 234.02,
            'October': 98.2,
            'November': 4.0,
            'December': 15.2
        }
        self.assertEqual(ReportsComponent.get_report_for_specific_meter(1, "testDataBase.db"), data)

# USER INPUT TEST
class TestCaseInputNum(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(ReportsComponent.input_num("5", 10), 5)
        self.assertEqual(ReportsComponent.input_num("5"), 5)
        self.assertEqual(ReportsComponent.input_num("12", 20), 12)
        self.assertEqual(ReportsComponent.input_num(768, 1000), 768)
        self.assertEqual(ReportsComponent.input_num(13), 13)

    def test_over_limit(self):
        with self.assertRaises(ReportsComponent.InputOutOfRange):
            ReportsComponent.input_num(3, 2)
        with self.assertRaises(ReportsComponent.InputOutOfRange):
            ReportsComponent.input_num("17", 2)
        with self.assertRaises(ReportsComponent.InputOutOfRange):
            ReportsComponent.input_num(10, -5)

    def test_under_limit(self):
        with self.assertRaises(ReportsComponent.InputOutOfRange):
            ReportsComponent.input_num(-2, 2)
        with self.assertRaises(ReportsComponent.InputOutOfRange):
            ReportsComponent.input_num("-9", 2)
        with self.assertRaises(ReportsComponent.InputOutOfRange):
            ReportsComponent.input_num(3, 2)
        with self.assertRaises(ReportsComponent.InputOutOfRange):
            ReportsComponent.input_num(3, 2)

    def test_NAN(self):
        with self.assertRaises(Exception):
            ReportsComponent.input_num("pet", 2)
        with self.assertRaises(Exception):
            ReportsComponent.input_num("5e", 10)
        with self.assertRaises(Exception):
            ReportsComponent.input_num([1, 2])
        with self.assertRaises(Exception):
            ReportsComponent.input_num([], 2)
        with self.assertRaises(Exception):
            ReportsComponent.input_num({})
    # possible to add test for double input


if __name__ == '__main__':
    if not(path.exists("testDataBase.db")):
        CreateTestDataBase.main()
    unittest.main()
    #os.remove(os.getcwd(),"testDataBase.db") This line od code is not working, I guess script does not have permissions to remove .db file