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
        expected_json = json.loads("""
        {
          "temperature": 23.3,
          "humidity": 42.4,
          "eCO2": 420
        }
        """)
        self.assertEqual(expected_json, json.loads(json_report))
