document.addEventListener("DOMContentLoaded", function () {
    const map = L.map('map', {
        center: [19.0760, 72.8777],
        zoom: 6,
        minZoom: 3,
        maxZoom: 18,
        worldCopyJump: false,
        maxBounds: [
            [-90, -180],
            [90, 180]
        ],
        maxBoundsViscosity: 1.0
    });

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; OpenStreetMap contributors',
    }).addTo(map);

    let markersLayer = L.markerClusterGroup(); 
    let heatmapLayer; 
    let isHeatmap = false; 

    function plotLocations() {
        console.log("Getting location coordinates...");

        fetch("http://127.0.0.1:8000/get-location", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
        })
            .then(response => {
                if (!response.ok) throw new Error("Network response was not ok");
                return response.json();
            })
            .then(data => {
                console.log("Location data received from backend:", data);

                const locations = data.locations.map((loc) => {
                    return [loc.lat, loc.long];
                });

                markersLayer.clearLayers();

                locations.forEach((loc) => {
                    const marker = L.marker(loc);
                    marker.bindPopup(`Fraud reported here`);
                    markersLayer.addLayer(marker);
                });

                heatmapLayer = L.heatLayer(locations, {
                    radius: 25,
                    blur: 15,
                    maxZoom: 17,
                });

                map.addLayer(markersLayer);
            })
            .catch(error => console.error("Error plotting location:", error));
    }

    function toggleView() {
        if (isHeatmap) {
            map.removeLayer(heatmapLayer);
            map.addLayer(markersLayer);
            isHeatmap = false;
            document.getElementById('viewBtn').textContent = "Switch to Heatmap";
        } else {
            map.removeLayer(markersLayer);
            map.addLayer(heatmapLayer);
            isHeatmap = true;
            document.getElementById('viewBtn').textContent = "Switch to Markers";
        }
    }

    plotLocations();

    document.getElementById("viewBtn").addEventListener("click", toggleView);
});
