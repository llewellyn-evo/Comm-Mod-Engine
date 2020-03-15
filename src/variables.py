import threading 
from flask import Flask
#import to fix CORS error
from flask_cors import CORS

#Comm Module Default config
default = {
	'logging' : {

		#-------------------------------
		#Level   		Numeric value
		#CRITICAL  			50
		#ERROR				40
		#WARNING			30
		#INFO				20
		#DEBUG				10
		#NOTSET				0
		#-------------------------------
		'level': 30 ,
		'logFile' : '/var/log/Module' 
	},
	"xbee" : {
		"type" : "SX 868",
		"tcpPort" : 9000 ,
		"baudRate" : 115200 ,
		"serialPort" : "/dev/ttyUSB0"
	} ,
	"gps" : {
		"type" : "UBLOX M8N",
		"tcpPort" : 9001 , 
		"BaudRate" : 115200 ,
		"serialPort" : "/dev/ttymxc1"
	} ,
	"wifi" : {
		"type" : "EmbedAir100",
	},
	"system" : {
		"tcpPort" : 9002 , 
		"ntpserver" : 1 ,
		"IMU" : 1 ,
		"IMURate" : 10 
	}
}

module = {}


#Command Line arguments
unixOptions = "hl:"
gnuOptions = ["help", "logging=", ]
#------------------------------------------
#long argument   short argument  with value
#------------------------------------------
#--help           -h              no
#--logging        -o              yes
#------------------------------------------


#Variables for Threading 
exitEvent= threading.Event()
xbeeThread = threading.Thread()

#Variables for REST API Server
app = Flask(__name__)
CORS(app)