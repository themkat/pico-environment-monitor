import unittest
import json
from report import create_prometheus_report
from report import create_json_report

class ReportTests(unittest.TestCase):
    def test_prometheus_report(self):
        mock_environment_monitor = type("MockEnvironmentMonitor", \
                                        (), \
                                        { "temperature":  lambda: 23.3, \
                                          "humidity": lambda: 42.4, \
                                          "eCO2": lambda: 420 })
        prometheus_report = create_prometheus_report(mock_environment_monitor)
        expected_prometheus_report = \
"""temperature 23.3
humidity 42.4
eCO2 420"""
        self.assertEqual(expected_prometheus_report, prometheus_report)
    
    def test_json_report(self):
        mock_environment_monitor = type("MockEnvironmentMonitor", \
                                        (), \
                                        { "temperature":  lambda: 23.3, \
                                          "humidity": lambda: 42.4, \
                                          "eCO2": lambda: 420 })
        json_report = create_json_report(mock_environment_monitor)
        # TODO: best way to assert this? probably without much spacing?
        # TODO: json may come in different orders depending on implementation. Maybe a better way here is to use the built in json stuff and convert the objects back and forth.
        # got the error on the device
        # checking that the report is valid json is probabbly a good idea anyway...
        expected_json = json.loads("""
        {
          "temperature": 23.3,
          "humidity": 42.4,
          "eCO2": 420
        }
        """)
        self.assertEqual(expected_json, json.loads(json_report))
