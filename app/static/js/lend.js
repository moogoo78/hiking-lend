const map = L.map('map').setView([23.481, 120.932], 7);

const tiles = L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
  maxZoom: 19,
  attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

//map.on('click', function(e) {
//    alert("Lat, Lon : " + e.latlng.lat + ", " + e.latlng.lng)
//});
fetch('/api/v1/stores')
  .then(r => r.json())
  .then(resp => {
    for (let i in resp) {
      const lat = parseFloat(resp[i].coordinates[0]);
      const lng = parseFloat(resp[i].coordinates[1]);
      if (lat && lng) {
        const marker = L.marker([lat, lng]).addTo(map)
		        .bindPopup(`<b>${resp[i].title}</b><br />${resp[i].address}`);
      }
    }
  })
