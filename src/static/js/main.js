var REQUEST_URL = "http://localhost:5000/"

$(document).ready(function(){
	$.getJSON( REQUEST_URL +'systemConfig', function(resp){
		if (resp.hasOwnProperty("wifi") && resp["wifi"]["type"]){
			document.getElementById("WIFITAB").innerHTML = resp["wifi"]["type"];
			document.getElementById("WIFITAB").style.display = "block";
		}

		if (resp.hasOwnProperty("xbee") && resp["xbee"]["type"]){
			document.getElementById("RFTAB").innerHTML = resp["xbee"]["type"];
			document.getElementById("RFTAB").style.display = "block";
		}

		if (resp.hasOwnProperty("system") ){
			document.getElementById("SYSTEMTAB").style.display = "block";
		}

		if (resp.hasOwnProperty("gps") && resp["gps"]["type"]){
			document.getElementById("GPSTAB").innerHTML = resp["gps"]["type"];
			document.getElementById("GPSTAB").style.display = "block";

		}
	});
});

document.getElementById("RFTAB").addEventListener("click", RFTABClick);

function RFTABClick() {
	openPage('RF', this , 'grey')
	$.getJSON( REQUEST_URL +'xbeeConfig', function(resp){
		console.log(resp)
	});
}




function openPage(pageName,elmnt,color) {
  var i, tabcontent, tablinks;
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }
  tablinks = document.getElementsByClassName("tablink");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].style.backgroundColor = "";
  }
  document.getElementById(pageName).style.display = "block";
  elmnt.style.backgroundColor = color;
}

//Open SystemTAB By default
document.getElementById("SYSTEMTAB").click();
