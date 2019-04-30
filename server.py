import socketserver
from jinja2 import Template
from config import *
from http import server
chars = []

class RequestHandler(server.SimpleHTTPRequestHandler):
    
    def do_GET(self):
        page = self.create_page()
        self.send_page(page)
            
        
    def create_page(self):
        
        with open(HTML_INDEX_PATH, "rt") as reader:
            template = reader.read()
   
        temp = Template(template) #This is the central template object. This class represents a compiled template and is used to evaluate it.
        
        page = temp.render(characters=chars)  
           
        return page
        
        
    def send_page(self, page, status=200):
        self.send_response(status)
        self.send_header("Content-type", "text/html")
        self.send_header("Content-Length", str(len(page)))
        self.end_headers()
        self.wfile.write(page.encode('utf-8'))
        
        
def run(PORT = 8080):
    
    print("Serving at port", PORT)
    print("Press Ctrl+c twice to exit")
    httpd = socketserver.TCPServer(("", PORT), RequestHandler)
    
    try:
        httpd.serve_forever()
        
    except KeyboardInterrupt:
        raise KeyboardInterrupt()