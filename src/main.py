import time
#Module to add support for logging
import logging
#inport module variable
from variables import *

import os

import sys
#import for command line variables
import getopt
#import to handle JSON objects and files
import json
#import to handle threading
import threading
#import for xbee function
from xbeeHandler import xbeeProcess
#inport for flask
from flask_api import status 
import flask
from flask import render_template


def read_config():
	config = default
	try:
		#Get absolute path of this file 
		dirname = os.getcwd()
		#append path to file config file
		filename = os.path.join(dirname, '../config/config.json')
		#Now we have the absolute path of the config file
		#Check if the file exists
		if os.path.isfile(filename):
			#If file found Load configs is module variable
			logging.info("Config file exits .. Loading now !")
			with open(filename) as config_file:
				config = json.load(config_file)

	except Exception as e:
		print ("Exception Encountered " + str(e))

	#pretty print the loaded json config
	print (json.dumps(config, indent=4, sort_keys=True))

	return config

def main():
	global module
	#Read Configs
	module = read_config()
	#Get Command line arguments
	try:
		# read commandline arguments, first
		fullCmdArguments = sys.argv
		# - further arguments
		argumentList = fullCmdArguments[1:]
		arguments, values = getopt.getopt(argumentList, unixOptions, gnuOptions)
		# evaluate given options
		for currentArgument, currentValue in arguments:
			if currentArgument in ("-h", "--help"):
				print ("displaying help")
			elif currentArgument in ("-l", "--logging"):

				if currentValue == "DEBUG":
					module["logging"]["level"] = logging.DEBUG
				elif currentValue == "INFO":
					module["logging"]["level"] = logging.INFO
				elif currentValue == "WARNING":
					module["logging"]["level"] = logging.WARNING
				elif currentValue == "ERROR":
					module["logging"]["level"] = logging.ERROR
				elif currentValue == "CRITICAL":
					module["logging"]["level"] = logging.CRITICAL
				else:
					print ("Unknown Logging level...")
				print ("Log Level set to %s " % currentValue)

		#intialise logging element
		if module["logging"]["logFile"]:
			#If File defined load logs to file in write mode
			logging.basicConfig(filename=module["logging"]["logFile"], filemode='w', level=module["logging"]["level"])
		else:
			#log to stdout
			logging.basicConfig(level=module["logging"]["level"])


		if module["xbee"]:
			xbeeThread = threading.Thread(target = xbeeProcess , args = ( module , exitEvent))
			xbeeThread.start()


		app.run()
		exitEvent.set()
		if xbeeThread.is_alive():
			xbeeThread.join()

		print("Exitting the Server Now .. ! ")

	except Exception as err:
		# output error, and return with an error code
		print (str(err))
		sys.exit(2)


#api call to get the configuration of the system
@app.route('/systemConfig' , methods = ["GET" , "POST"])
def systemConfigApi():
	if flask.request.method == "GET":
		return module , status.HTTP_200_OK


#render static html files
@app.route("/")
def index():
    return render_template("index.html")




if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		print("DONE... Program Exiting...\n\n")