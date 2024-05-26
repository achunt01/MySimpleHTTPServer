# MySimpleHTTPServer

This Python script creates a simple HTTP server using the `http.server` module, allowing you to serve static files from your local machine.

## Usage

1. Place the files you want to serve in the same directory as the script.

2. Run the script using Python 3:

   ```sh
   python server.py
   ```
3. Open your web browser and navigate to http://localhost:8080/ to view the files.

## Features

- **Automatic Index File**: If no file is specified in the URL (e.g., `http://localhost:8080/`), it serves `index.html` by default.

- **Error Handling**: If the requested file is not found, the server responds with a 404 status code and a "File not found" message.

- **Customizable Port**: You can change the port number by modifying the `server_address` variable in the script.
