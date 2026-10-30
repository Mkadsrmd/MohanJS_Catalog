from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import os
PORT=8765
class SPAHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        path=self.translate_path(self.path.split('?',1)[0])
        if os.path.exists(path):
            return super().do_GET()
        self.path='/index.html'
        return super().do_GET()
if __name__=='__main__':
    print(f'Catalogue: http://localhost:{PORT}/')
    print(f'Login:     http://localhost:{PORT}/login')
    print(f'Admin:     http://localhost:{PORT}/admin')
    ThreadingHTTPServer(('localhost',PORT),SPAHandler).serve_forever()
