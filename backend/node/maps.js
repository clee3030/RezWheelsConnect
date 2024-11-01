const express = require('express');
const axios = require('axios');
const leaflet = require('leaflet');

const app = express();
const PORT = 5000;

// Middleware to parse JSON bodies
app.use(express.json());

// Route to process signals
app.post('/process_signals', async (req, res) => {
    try {
        // Forward the request to the Flask API
        const response = await axios.post('http://127.0.0.1:4000/process_signals', req.body);
        console.log("Sent request to flask API.");
        
        // Extract device position from the response
        const devicePosition = response.data.device_position;

        // Check if device position is available
        if (devicePosition) {
            // Return the device position in a format suitable for mapping
            res.json({
                status: 'success',
                device_position: {
                    latitude: devicePosition.y, // Assuming y is latitude
                    longitude: devicePosition.x, // Assuming x is longitude
                    altitude: devicePosition.z    // Altitude if needed
                }
            });
            console.log("Successful");
            var map = leaflet.map('map').setView([51.505, -0.09], 13);

            leaflet.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
                attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
            }).addTo(map);

            leaflet.marker([latitude, longitude]).addTo(map)
            .bindPopup('A pretty CSS popup.<br> Easily customizable.')
            .openPopup();
        } else {
            res.status(400).json({ error: 'Device position not found.' });
            console.error("Something happened...");
        }
    } catch (error) {
        // Handle errors from the Flask API
        if (error.response) {
            res.status(error.response.status).json({ error: error.response.data.error });
        } else {
            res.status(500).json({ error: 'An error occurred while processing the request: ', error });
            console.error("[ERROR]: ", error.response);
        }
    }
});

// Start the server
app.listen(PORT, () => {
    console.log(`Node.js server is running on http://localhost:${PORT}`);
});
