# test_server.py
from http.server import HTTPServer, SimpleHTTPRequestHandler


class CustomHandler(SimpleHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(length)
        response = f"Your email is: {post_data.decode('utf-8').split('=')[1]}"
        self.send_response(200)
        self.end_headers()
        self.wfile.write(response.encode('utf-8'))


if __name__ == "__main__":
    httpd = HTTPServer(('0.0.0.0', 8000), CustomHandler)
    print("Serving on port 8000...")
    httpd.serve_forever()
