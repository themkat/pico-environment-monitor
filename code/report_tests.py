import unittest
from report import create_json_report

class ReportTests(unittest.TestCase):
    def test_json_report(self):
        mock_environment_monitor = type("MockEnvironmentMonitor", \
                                        (), \
                                        { "temperature":  lambda: 23.3, \
                                          "humidity": lambda: 42.4, \
                                          "eCO2": lambda: 420 })
        json_report = create_json_report(mock_environment_monitor)
        # TODO: best way to assert this? probably without much spacing?
        expected_json = """
        {
          "temperature": 23.3,
          "humidity": 42.4,
          "eCO2": 420
        }
        """.replace("\n        ", "").replace("{  ", "{").replace(", ", ",")
        self.assertEqual(expected_json, json_report)
