import unittest
import sqlite3
import ReportsComponent


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


if __name__ == "__main__":
    unittest.main()
