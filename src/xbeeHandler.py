#import for time options
import time
#import for threading options
import threading
#import to handle json
import json
#import to habdle xbee library
from digi.xbee.devices import XBeeDevice
#import for xbee variables
from xbeeVariables import *
#inport for API Server
from variables import app
#import for logging
import logging
#import for flask api
from flask_api import status 
import flask
#import for TCP Socket Server stuff
import socketserver


def dataReceiveCallback(xbee_message):
	print("From %s >> %s" % (xbee_message.remote_device.get_64bit_addr(),xbee_message.data.decode()))



def Command(operation , addr , data):
	i = 0
	try:
		#Read Configs from Device
		if operation == 1:
			#loop through all the AT Commands
			commands = xbeeConfig.keys()
			#Iterate through keys in json 
			for key in commands:
				#Get At commands
				resp = device.get_parameter(key)
				if xbeeConfig[key]["Type"] == "STRING":
					xbeeConfig[key]["Value"] =  resp.decode("utf-8") 
				elif xbeeConfig[key]["Type"] == "HEX":
					xbeeConfig[key]["Value"] = int.from_bytes(resp, byteorder='big')

			logging.info("Done Reading configurations from xbee Device")
			return 1
		elif operation == 2:
			#write configs to Device
			commands = data.keys()
			for key in commands:
				if data[key]["Type"] == "STRING":
					device.set_parameter(key , bytearray(data[key]["Value"], "utf8"))
				elif data[key]["Type"] == "HEX":
					device.set_parameter(key , data[key]["Value"].to_bytes( byteorder="big"))
			logging.info("Done Writting configurations to xbee Device")
			return 1
		elif operation == 3:
			#write Data to Device
			device.send_data(addr, data)
			logging.info("Done Sending Data to xbee Device")
			return 1
		else:
			#unknows operation
			return -1
	except Exception as e:
		logging.error("Xbee Read Config Error " + str(e))
		return -1


class XbeeTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """
    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        # just send back the same data, but upper-cased
        self.request.sendall(self.data.upper())


def xbeeProcess(module , exitEvent ):
	global device
	try:
		#intialise logging element
		if module["logging"]["logFile"]:
			#If File defined load logs to file in write mode
			logging.basicConfig(filename=module["logging"]["logFile"], filemode='w', level=module["logging"]["level"])
		else:
			#log to stdout
			logging.basicConfig(level=module["logging"]["level"])
		#Initialize the device
		device = XBeeDevice(module["xbee"]["serialPort"] , module["xbee"]["baudRate"])
		#open the Device
		device.open()
		#Add Callback for Recieving data
		device.add_data_received_callback(dataReceiveCallback)
		#Read configs from xbee Config
		Command(1 , None  , None)
		server = socketserver.TCPServer(("localhost", module["xbee"]["tcpPort"]) , XbeeTCPHandler)
		#settimeout for handle requests
		server.timeout = 0.5
		while not exitEvent.is_set():
			server.handle_request()
			time.sleep(0.5)

	except Exception as e:
		logging.error("Xbee error " + str(e))


@app.route('/xbeeConfig' , methods = ["GET" , "POST"])
def index():
	if flask.request.method == "GET":
		resp = Command(1 , None  , None)
		if resp == 1:
			return xbeeConfig , status.HTTP_200_OK
		elif resp == -1:
			return status.HTTP_503_SERVICE_UNAVAILABLE
	
