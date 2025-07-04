from http.server import BaseHTTPRequestHandler, HTTPServer


lua_code = 'print("Eu vim do python!")'

class LuaHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/script.lua":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(lua_code.encode())
        else:
            self.send_response(404)
            self.end_headers()

host = "0.0.0.0"
port = 8080
print(f"Servidor rodando em http://localhost:{port}/script.lua")
HTTPServer((host, port), LuaHandler).serve_forever()
