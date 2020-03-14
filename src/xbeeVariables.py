#import for xbee device
from digi.xbee.devices import XBeeDevice


#Define the Device
device = XBeeDevice("/dev/ttymxc4" , 115200)

#-----------------------------------------------
#----------------ATCommands---------------------
#    CM - Channel Mask
#    ID - Network ID
#    MT - BroadCast Multi Transmits
#	 BR -  RF Data Rates
#    PL - TX Power level
#    RR - Unicast Retries
#    CE - Routing/Messaging Modes
#    BH - Broadcast Hops
#    NH - Network Hops
#    MR - Mesh Unicast Reties
#    SH - Serial Number High
#    SL - Serial Number Low
#    NI - Node Identifier
#    NT - Network Desicovery Backoff
#    NO - Network Discovery Options
#    CI - Cluster ID

xbeeConfig = {
	"CM" : {
		"Description" : "Channel Mask" , 
		"Value" : 0 ,
		"Editable" : True ,
		"Type" : "HEX"
	} , 
	"ID" : {
		"Description" : "Network ID" , 
		"Value" : 0 , 
		"Editable" : True , 
		"Type" : "HEX"
	} , 
	"BR" : {
		"Description" : "RF Data Rates" , 
		"Value" : 0 , 
		"Editable" : True , 
		"Type" : "HEX"
	} , 
	"PL" : {
		"Description" : "TX Power level" , 
		"Value" : 0 , 
		"Editable" : True , 
		"Type" : "HEX"
	} , 
	"RR" : {
		"Description" : "Unicast Retries" , 
		"Value" : 0 , 
		"Editable" : True , 
		"Type" : "HEX"
	} , 
	"CE" : {
		"Description" : "Routing/Messaging Modes" , 
		"Value" : 0 , 
		"Editable" : True , 
		"Type" : "HEX"
	} , 
	"BH" : {
		"Description" : "Broadcast Hops" , 
		"Value" : 0 , 
		"Editable" : True , 
		"Type" : "HEX"
	} , 
	"NH" : {
		"Description" : "Network Hops" , 
		"Value" : 0 , 
		"Editable" : True , 
		"Type" : "HEX"
	} , 
	"MR" : {
		"Description" : "Mesh Unicast Reties" , 
		"Value" : 0 , 
		"Editable" : True , 
		"Type" : "HEX"
	} , 
	"SH" : {
		"Description" : "Serial Number High" , 
		"Value" : 0 , 
		"Editable" : False , 
		"Type" : "HEX"
	} , 
	"SL" : {
		"Description" : "Serial Number Low" , 
		"Value" : 0 , 
		"Editable" : False , 
		"Type" : "HEX"
	} , 
	"NI" : {
		"Description" : "Node Identifier" , 
		"Value" : 0 , 
		"Editable" : True , 
		"Type" : "STRING"
	} , 
	"NT" : {
		"Description" : "Network Discovery Backoff" , 
		"Value" : 0 , 
		"Editable" : True , 
		"Type" : "HEX"
	} , 
	"NO" : {
		"Description" : "Network Discovery Options" , 
		"Value" : 0 , 
		"Editable" : True , 
		"Type" : "HEX"
	} , 
	"CI" : {
		"Description" : "Cluster ID" , 
		"Value" : 0 , 
		"Editable" : True , 
		"Type" : "HEX"
	} , 
}
