import board
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

# main entrypoint file
# contains mostly device specific code for Raspberry Pi Pico W and sensors

# main entrypoint file? should we separate the different modules into other files and let this one be a device-dependant file? then we can easily mock the others?


# TODO: wrappers if there are device specifics

# TODO: create an instance of EnvironmentMonitor to handle the devices

# TODO: create a webserver that interacts with the environment monitor
wifi_ssid = os.getenv("WIFI_SSID")
wifi_password = os.getenv("WIFI_PASSWORD")

wifi.radio.connect(wifi_ssid, wifi_password)
server = HTTPServer(socketpool.SocketPool(wifi.radio))

@server.route("/environment")
def environment_prometheus_handler(request):
    with HTTPResponse(request, content_type=MIMEType.TYPE_TXT) as response:
        response.send("todo")

@server.route("/environment.json")
def environment_json_handler(request):
    with HTTPResponse(request, content_type=MIMEType.TYPE_JSON) as response:
        response.send("{}")

print(str(wifi.radio.ipv4_address))
server.serve_forever(str(wifi.radio.ipv4_address))
