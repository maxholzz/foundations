import http.server
import socketserver


handler = http.server.CGIHTTPRequestHandler


handler.cgi_directories = ["/Scripts"]


PORT = 8000
httpd = socketserver.TCPServer(("localhost", PORT), handler)


httpd.server_name = "myServer"
httpd.server_port = PORT

print("staring CGI server at localhost:8000")


httpd.serve_forever()
