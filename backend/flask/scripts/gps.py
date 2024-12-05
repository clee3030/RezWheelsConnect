from flask import Flask, request, jsonify
import numpy as np
from scipy.optimize import least_squares

app = Flask(__name__)

# Helper function for trilateration
def trilaterate(satellite_positions, pseudoranges):
    # Initial guess for the receiver's position (x, y, z)
    initial_guess = [0, 0, 0]

    # Define residuals function for optimization
    def residuals(guess, satellite_positions, pseudoranges):
        res = []
        for i, sat_pos in enumerate(satellite_positions):
            # Calculate distance between the guess and satellite position
            distance = np.linalg.norm(np.array(guess) - np.array(sat_pos))
            # Residual is the difference between distance and pseudorange
            res.append(distance - pseudoranges[i])
        return res
    
    # Use least squares optimization to find the receiver's position
    result = least_squares(residuals, initial_guess, args=(satellite_positions, pseudoranges))
    return result.x

@app.route('/process_signals', methods=['POST'])
def process_signals():
    data = request.get_json()

    # Extract satellite positions and pseudoranges from the request
    satellite_data = data.get('satellite_data', [])
    pseudoranges = data.get('pseudoranges', [])

    if not satellite_data or not pseudoranges or len(satellite_data) < 4 or len(pseudoranges) < 4:
        return jsonify({"error": "Insufficient data. At least 4 satellites are required."}), 400

    # Extract positions of the satellites
    satellite_positions = []
    for satellite in satellite_data:
        satellite_positions.append(satellite['position'])

    # Perform trilateration to find the device's position
    try:
        device_position = trilaterate(satellite_positions, pseudoranges)
        return jsonify({
            "device_position": {
                "latitude": device_position[0],
                "longitude": device_position[1],
                "altitude": device_position[2]
            }
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def start():
    app.run(debug=True, host='0.0.0.0', port=4000)
