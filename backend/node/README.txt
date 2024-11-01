* maps.js *

maps.js is a Node.js application that serves as a middleware between a client and a Flask API responsible for processing satellite signals and performing trilateration to determine device positions. This application listens for incoming POST requests, forwards them to the Flask API, and returns the processed device position to the client.
Features

    JSON Body Parsing: The application uses middleware to parse incoming JSON requests.
    Error Handling: It includes error handling for both the request to the Flask API and the response processing.
    Device Positioning: It extracts the device position from the Flask API response and formats it for mapping applications.

** Dependencies **

    Express: A web framework for Node.js.
    Axios: A promise-based HTTP client for making requests to the Flask API.

** Installation **

    Clone the Repository: Clone the repository containing maps.js to your local machine.

Install Dependencies: Navigate to the project directory and install the required dependencies using npm.

npm install express axios

Run the Flask API: Ensure that the Flask API is running on port 4000. You can do this by executing the Flask application provided in the backend code.

    python gps.py

Start the Node.js Server: Start the Node.js server by running the following command in the terminal.

    node maps.js

    The server will start and listen on port 5000.

** API Endpoint **
POST /process_signals

    Description: This endpoint processes incoming signals, forwards them to the Flask API, and returns the device position.
    Request Body: The request should contain a JSON object with the following structure:

This is an example request with placeholders.

{
    "satellite_data": [
        {"position": [x1, y1, z1]},
        {"position": [x2, y2, z2]},
        {"position": [x3, y3, z3]},
        {"position": [x4, y4, z4]}
    ],
    "pseudoranges": [p1, p2, p3, p4]
}

    Response: The response will be a JSON object containing the device position:

{
    "status": "success",
    "device_position": {
        "latitude": <latitude>,
        "longitude": <longitude>,
        "altitude": <altitude>
    }
}

    Error Handling: If the request fails or if the device position is not found, the server will return an error message with an appropriate status code.

** Example Usage **

To test the application, you can use a tool like Postman or cURL to send a POST request to the /process_signals endpoint:

curl -X POST http://localhost:5000/process_signals \
-H "Content-Type: application/json" \
-d '{
    "satellite_data": [
        {"position": [1, 2, 3]},
        {"position": [4, 5, 6]},
        {"position": [7, 8, 9]},
        {"position": [10, 11, 12]}
    ],
    "pseudoranges": [10, 10, 10, 10]
}'
