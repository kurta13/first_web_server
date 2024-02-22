from http.server import SimpleHTTPRequestHandler, HTTPServer

# Define the server address
host = 'localhost'
port = 8000

# Create a custom request handler by subclassing SimpleHTTPRequestHandler
class CustomRequestHandler(SimpleHTTPRequestHandler):
    # Override the log_message method to suppress log messages to the console
    def log_message(self, format, *args):
        pass

# Create an HTTP server with the specified host and port, and use the custom request handler
try:
    with HTTPServer((host, port), CustomRequestHandler) as server:
        print(f"Server started at http://{host}:{port}")
        # Start the server and keep it running until interrupted
        server.serve_forever()
except KeyboardInterrupt:
    print("\nServer stopped.")

