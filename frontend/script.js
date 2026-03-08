// initialize map
var map = L.map('map').setView([13.0827, 80.2707], 13);

// load tiles
L.tileLayer(
'https://tile.openstreetmap.org/{z}/{x}/{y}.png',
{ maxZoom: 19 }
).addTo(map);

let detectionCount = 0;

// load potholes
function loadPotholes(){

fetch("http://127.0.0.1:5000/get_potholes")

.then(res => res.json())

.then(data => {

data.forEach(p => {

L.marker([p.lat, p.lon])
.addTo(map)
.bindPopup("Pothole detected");

detectionCount++;

document.getElementById("total-count").innerText = detectionCount;

});

});

}

// button event
document.getElementById("startBtn").addEventListener("click", function(){

loadPotholes();

});