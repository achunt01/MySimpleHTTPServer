from http.server import HTTPServer, BaseHTTPRequestHandler
import os

class Serv(BaseHTTPRequestHandler):

    def do_GET(self):
        try:
            # Set the path to index.html if no path is provided
            if self.path == '/':
                self.path = '/index.html'
            
            # Open the file in binary mode
            with open(self.path[1:], 'rb') as file:
                file_data = file.read()
            
            # Set the response code to 200 (OK) and send the file data
            self.send_response(200)
            self.end_headers()
            self.wfile.write(file_data)
        except FileNotFoundError:
            # If the file is not found, set the response code to 404 (Not Found)
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"File not found")

# Specify the IP address and port to listen on
server_address = ('localhost', 8080)

# Create an HTTP server
httpd = HTTPServer(server_address, Serv)

# Start the server and keep it running indefinitely
print('Starting server on {}:{}'.format(*server_address))
httpd.serve_forever()
