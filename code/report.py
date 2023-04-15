import json

# various report format conversions
# TODO: any additional type checking we can do here? or at least prettier?
#       seems excessive to do the same as in environment monitor class as these will probably be called more often than once. 

def create_prometheus_report(environment_monitor):
    """
    Creates an environment report that can be consumed by prometheus
    
    Parameters:
    environment_monitor : Environment monitor object that has the needed methods
    """
    return "temperature " + str(environment_monitor.temperature()) + "\nhumidity " + str(environment_monitor.humidity()) + "\neCO2 " + str(environment_monitor.eCO2()) 

def create_json_report(environment_monitor):
    """
    Creates a JSON report that can be consumed by everyone that understands json

    Parameters:
    environment_monitor : Environment monitor object that has the needed methods
    """
    report = { "temperature": environment_monitor.temperature(), "humidity": environment_monitor.humidity(), "eCO2": environment_monitor.eCO2() }
    return json.dumps(report)
