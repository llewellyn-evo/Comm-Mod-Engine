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

ATCommandsXbee = ["CM" , "ID" , "MT" , "BR" , "PL" , "RR" , "CE" , "BH" , "NH" , "MR" , "SH" , "SL" , "NI" , "NT" , "NO" , "CI"]

xbeeConfig = {
	"CM" : {
		"Description" : "Channel Mask" , 
		"Value" : 0
	} , 
	"ID" : {
		"Description" : "Network ID" , 
		"Value" : 0
	} , 
	"BR" : {
		"Description" : "RF Data Rates" , 
		"Value" : 0
	} , 
	"PL" : {
		"Description" : "TX Power level" , 
		"Value" : 0
	} , 
	"RR" : {
		"Description" : "Unicast Retries" , 
		"Value" : 0
	} , 
	"CE" : {
		"Description" : "Routing/Messaging Modes" , 
		"Value" : 0
	} , 
	"BH" : {
		"Description" : "Broadcast Hops" , 
		"Value" : 0
	} , 
	"NH" : {
		"Description" : "Network Hops" , 
		"Value" : 0
	} , 
	"MR" : {
		"Description" : "Mesh Unicast Reties" , 
		"Value" : 0
	} , 
	"SH" : {
		"Description" : "Serial Number High" , 
		"Value" : 0
	} , 
	"SL" : {
		"Description" : "Serial Number Low" , 
		"Value" : 0
	} , 
	"NI" : {
		"Description" : "Node Identifier" , 
		"Value" : 0
	} , 
	"NT" : {
		"Description" : "Network Discovery Backoff" , 
		"Value" : 0
	} , 
	"NO" : {
		"Description" : "Network Discovery Options" , 
		"Value" : 0
	} , 
	"NI" : {
		"Description" : "Cluster ID" , 
		"Value" : 0
	} , 
}
