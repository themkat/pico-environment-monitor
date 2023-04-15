class MissingMethodError(Exception):
    pass

class EnvironmentMonitor:
    """
    Wrapper class for environment monitor based operations (temperature, CO2 etc.).
    Makes it easy to switch out underlying hardware if one wants to without affecting the logic.
    """

    def __init__(self,
                 temperature_monitor = None,
                 humidity_monitor = None):
        """
        Creates a new environment monitor instance. Each argument can be a sensor object or a wrapper that wraps the sensor depending on the use case. See Parameters.

        Parameters:
            temperature_monitor : Object that has a method temperature to fetch temperatures in Celsius
            pressure_monitor : Object that has a ... 
        """
        
        if temperature_monitor and not hasattr(temperature_monitor, "temperature"):
            raise MissingMethodError
        self.temperature_monitor = temperature_monitor

        if humidity_monitor and not hasattr(humidity_monitor, "humidity"):
            raise MissingMethodError
        self.humidity_monitor = humidity_monitor
        
    def temperature(self):
        return self.temperature_monitor.temperature() if self.temperature_monitor else None

    def humidity(self):
        return self.humidity_monitor.humidity() if self.humidity_monitor else None
