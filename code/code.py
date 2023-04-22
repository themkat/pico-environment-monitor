import board
import busio
import adafruit_bme680
import adafruit_sgp30
# WHY DOESNT LOCAL ENV FIND THE HTTPSERVER?!?!?
# really tedious to develop without any completion here...
from adafruit_httpserver.server import HTTPServer
from adafruit_httpserver.mime_type import MIMEType
from adafruit_httpserver.response import HTTPResponse
import os
import socketpool
import wifi

from envmon import EnvironmentMonitor
from report import create_json_report
from report import create_prometheus_report

# TODO: idea for production variant:
# https://learn.adafruit.com/welcome-to-circuitpython/troubleshooting#code-dot-py-restarts-constantly-3108374
# maybe have a setting for this in settings.toml?


# main entrypoint file
# contains mostly device specific code for Raspberry Pi Pico W and sensors


# Set up EnvironmentMonitor abstractions and hardware wrappers
# TODO: decide on the pins being used for each
bme688_i2c = busio.I2C(board.GP1, board.GP0)
bme688 = adafruit_bme680.Adafruit_BME680_I2C(bme688_i2c)

sgp30_i2c = busio.I2C(board.GP3, board.GP2, frequency=100000)
sgp30 = adafruit_sgp30.Adafruit_SGP30(sgp30_i2c)

# TODO: check why we can't take self as input. CircuitPython specifics? Or is is that I'm rusty with Python knowledge?
class BME688TemperatureWrapper:
    def temperature():
        # TODO: adafruit uses 5 as the offset in their examples. Find a suitable one
        return bme688.temperature - 5.0
class BME688HumidityWrapper:
    def humidity():
        return bme688.relative_humidity
class SGP30ECO2Wrapper:
    def eCO2():
        return sgp30.eCO2

environment_monitor = EnvironmentMonitor(temperature_monitor = BME688TemperatureWrapper, humidity_monitor = BME688HumidityWrapper, eco2_monitor = SGP30ECO2Wrapper)


# network specifics and usage of service layer EnvironmentMonitor in web-routes
wifi_ssid = os.getenv("WIFI_SSID")
wifi_password = os.getenv("WIFI_PASSWORD")

wifi.radio.connect(wifi_ssid, wifi_password)
server = HTTPServer(socketpool.SocketPool(wifi.radio))

# TODO: a welcome page at root just for fun? :P
#      maybe a cute image, some data parsed with a simple JS etc.?

@server.route("/environment")
def environment_prometheus_handler(request):
    with HTTPResponse(request, content_type=MIMEType.TYPE_TXT) as response:
        response.send(create_prometheus_report(environment_monitor))

@server.route("/environment.json")
def environment_json_handler(request):
    with HTTPResponse(request, content_type=MIMEType.TYPE_JSON) as response:
        response.send(create_json_report(environment_monitor))

print(str(wifi.radio.ipv4_address))
server.serve_forever(str(wifi.radio.ipv4_address))
