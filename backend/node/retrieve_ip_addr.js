const express = require('express');
const mysql = require('mysql2/promise');
const app = express();
const PORT = 5000;

// Database connection configuration
const dbConfig = {
    host: 'localhost',
    user: 'your_db_user',
    password: 'your_db_password',
    database: 'your_database_name'
};

// Endpoint to get a user's IP by username
app.get('/get_ip', async (req, res) => {
    const { username } = req.query;

    if (!username) {
        return res.status(400).json({ error: 'Please provide a username.' });
    }

    try {
        // Connect to the database
        const connection = await mysql.createConnection(dbConfig);

        // Query the database for the user's IP
        const [rows] = await connection.execute(
            'SELECT ip_address FROM users WHERE username = ?',
            [username]
        );

        // Close the database connection
        await connection.end();

        if (rows.length > 0) {
            // Return the IP address if found
            res.json({ status: 'success', ip_address: rows[0].ip_address });
        } else {
            // Handle case where the username is not found
            res.status(404).json({ error: 'Username not found.' });
        }
    } catch (error) {
        // Handle any database or server errors
        res.status(500).json({ error: 'An error occurred while retrieving the IP address.' });
        console.error(error);
    }
});

// Start the server
app.listen(PORT, () => {
    console.log(`API server is running on http://localhost:${PORT}`);
});
