from http.server import BaseHTTPRequestHandler, HTTPServer
import time

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><body><h1>Lobby Server E-Sport Aktif!</h1></body></html>", "utf-8"))

if __name__ == "__main__":
    webServer = HTTPServer(("0.0.0.0", 8080), MyServer)
    print("Server berjalan di port 8080...")
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass
    webServer.server_close()
    print("Server berhenti.")
