import http.server, socketserver

PORT = 8080
DIR = '.'

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIR, **kwargs)

print(f'Server: http://localhost:{PORT}')
print(f'Open: http://localhost:{PORT}/%E5%86%85%E5%A4%96%E4%BC%A0%E8%BE%93%E4%B8%80%E7%A0%81%E9%80%9A.html')

with socketserver.TCPServer(('', PORT), Handler) as httpd:
    httpd.serve_forever()
