var map;
var wp1;
var wp2;
var wp3;
var wp4;

document.addEventListener('DOMContentLoaded', function () {
    // Create a map instance and set the initial view coordinates and zoom level
    map = L.map('map').setView([37.773972, -122.431297], 13);
  
  
    // Add a tile layer to the map from OpenStreetMap
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);
  });

async function addPoints() {
    var add1 = document.getElementById("address1").value;
    var add2 = document.getElementById("address2").value;

    const response = await fetch('http://127.0.0.1:5000/addpoints?' + new URLSearchParams({
        "add1": add1,
        "add2": add2,
    }))

    response.text().then(function (text) {

        var numbers = text.split(" ");
        alert(numbers);

        wp1 = numbers[0];
        wp2 = numbers[1];
        wp3 = numbers[2];
        wp4 = numbers[3];

        L.marker([wp1, wp2]).addTo(map);
        L.marker([wp3, wp4]).addTo(map);
    });
        
}

async function addPolyLine() {
    const response = await fetch('http://127.0.0.1:5000/addRoute?' + new URLSearchParams({
        "wp1": wp1,
        "wp2": wp2,
        "wp3": wp3,
        "wp4": wp4
    }));

    response.text().then(function (text) {
        let stuff = JSON.parse(text)
        
        let polyLinePoints = []
        
        for (let i = 0; i< stuff.length; i+=2) {
            polyLinePoints.push([stuff[i], stuff[i+1]]);
        }

        L.polyline(polyLinePoints).addTo(map);
    });


}
