import unittest
from envmon import MissingMethodError
from envmon import EnvironmentMonitor

class EnvironmentMonitorTemperatureTests(unittest.TestCase):
    def test_temperature_none(self):
        environment_monitor = EnvironmentMonitor()
        self.assertIsNone(environment_monitor.temperature())

    def test_temperature_input_no_suitable_method(self):
        mock = type("MockTemperature", (), {})
        self.assertRaises(MissingMethodError, lambda: EnvironmentMonitor(temperature_monitor = mock))

    def test_temperature(self):
        mock = type("MockTemperature", (), { "temperature":  lambda: 22.2 })
        environment_monitor = EnvironmentMonitor(temperature_monitor = mock)
        temperature = environment_monitor.temperature()
        self.assertIsNotNone(temperature)
        self.assertAlmostEqual(22.2, temperature if temperature else float('nan'))

# TODO: test classes for the other variants
