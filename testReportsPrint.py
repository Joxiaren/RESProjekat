import unittest
import ReportsComponent
from unittest.mock import patch, call


@patch('builtins.print')
class TestPrintReportForSpecificStreet(unittest.TestCase):
    def test_empty_dict(self, mocked_print):
        ReportsComponent.printReportForSpecificStreet("Kninska", {})
        assert mocked_print.mock_calls == [call("Water consumption in street: Kninska"),
                                           call("----------------------------------------------------"),
                                           call("----------------------------------------------------")]

    def test_regular_dict(self, mocked_print):
        ReportsComponent.printReportForSpecificStreet("Kninska", {"January": 1.0, "February": 2.0, "March": 3.0})
        assert mocked_print.mock_calls == [call("Water consumption in street: Kninska"),
                                           call("----------------------------------------------------"),
                                           call("January : 1.0"), call("February : 2.0"), call("March : 3.0"),
                                           call("----------------------------------------------------")]

@patch('builtins.print')
class TestPrintReportForSpecificCounter(unittest.TestCase):
    def test_empty_dict(self, mocked_print):
        ReportsComponent.printReportForSpecificCounter(1, {})
        assert mocked_print.mock_calls == [call("Water consumption on specific water meter with id: 1"),
                                           call("----------------------------------------------------"),
                                           call("----------------------------------------------------")]

    def test_regular_dict(self, mocked_print):
        ReportsComponent.printReportForSpecificCounter(1, {"January": 1.0, "February": 2.0, "March": 3.0})
        assert mocked_print.mock_calls == [call("Water consumption on specific water meter with id: 1"),
                                           call("----------------------------------------------------"),
                                           call("January : 1.0"), call("February : 2.0"), call("March : 3.0"),
                                           call("----------------------------------------------------")]


if __name__ == '__main__':
    unittest.main()
