#import for time options
import time
#import for threading options
import threading
#import to handle json
import json
#import to habdle xbee library
from digi.xbee.devices import XBeeDevice
#import for xbee variables
from xbeeVariables import ATCommandsXbee, xbeeConfig
#inport for API Server
from variables import app
#import for logging
import logging
#import for flask api
from flask_api import status 



def readConfigurations():
	i = 0
	try:
		#loop through all the AT Commands
		while i < len(ATCommandsXbee):
			resp = device.get_parameter(ATCommandsXbee[i])

			if ATCommandsXbee[i] in xbeeConfig:
				if ATCommandsXbee[i] == "NI":
					xbeeConfig[ATCommandsXbee[i]]["value"] =  resp.decode("utf-8") 
				else:
					xbeeConfig[ATCommandsXbee[i]]["value"] = int.from_bytes(resp, byteorder='big')

			i += 1
		logging.info("Done Reading configurations from xbee Device")
		return 1
	except Exception as e:
		logging.error("Xbee Read Config Error " + str(e))
		return -1


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
		readConfigurations()
		while not exitEvent.is_set():
			time.sleep(1)

	except Exception as e:
		logging.error("Xbee error " + str(e))


@app.route('/xbeeConfig' , methods = ["GET"])
def index():
	if readConfigurations() == 1:
		return xbeeConfig , status.HTTP_200_OK
	elif readConfigurations() == -1:
		return status.HTTP_503_SERVICE_UNAVAILABLE
	
