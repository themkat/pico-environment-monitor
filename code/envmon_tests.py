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

class EnvironmentMonitorHumidityTests(unittest.TestCase):
    def test_humidity_none(self):
        environment_monitor = EnvironmentMonitor()
        self.assertIsNone(environment_monitor.humidity())

    def test_humidity_input_no_suitable_method(self):
        mock = type("MockHumidity", (), {})
        self.assertRaises(MissingMethodError, lambda: EnvironmentMonitor(humidity_monitor = mock))

    def test_humidity(self):
        mock = type("MockHumidity", (), { "humidity":  lambda: 45.5 })
        environment_monitor = EnvironmentMonitor(humidity_monitor = mock)
        humidity = environment_monitor.humidity()
        self.assertIsNotNone(humidity)
        self.assertAlmostEqual(45.5, humidity if humidity else float('nan'))

class EnvironmentMonitorECO2Tests(unittest.TestCase):
    def test_eco2_none(self):
        environment_monitor = EnvironmentMonitor()
        self.assertIsNone(environment_monitor.eCO2())

    def test_eco2_input_no_suitable_method(self):
        mock = type("MockCO2", (), {})
        self.assertRaises(MissingMethodError, lambda: EnvironmentMonitor(eco2_monitor = mock))

    def test_eco2(self):
        mock = type("MockCO2", (), { "eCO2":  lambda: 410 })
        environment_monitor = EnvironmentMonitor(eco2_monitor = mock)
        eco2 = environment_monitor.eCO2()
        self.assertIsNotNone(eco2)
        self.assertEqual(410, eco2)
