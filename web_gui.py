#!/usr/bin/env python3
"""
Braython Web Interface - Uses only Python standard library (no external dependencies).
Run with: python web_gui.py
A browser window will automatically open.
"""

import http.server
import socketserver
import json
import sys
import webbrowser
import time
from io import StringIO
from urllib.parse import urlparse, parse_qs
from compiler import Compiler

PORT = 8000
compiler = Compiler()

class BraythonHandler(http.server.BaseHTTPRequestHandler):
    
    def do_GET(self):
        """Serve the HTML interface"""
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            with open('templates/index.html', 'rb') as f:
                self.wfile.write(f.read())
        else:
            self.send_response(404)
            self.end_headers()
    
    def do_POST(self):
        """Handle compile and translate requests"""
        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length).decode('utf-8')
        
        try:
            data = json.loads(body)
        except:
            self.send_response(400)
            self.end_headers()
            return
        
        code = data.get('code', '')
        language = data.get('language', 'pt')
        
        if self.path == '/compile':
            output = self._compile_and_run(code, language)
        elif self.path == '/translate':
            output = self._translate_only(code, language)
        else:
            self.send_response(404)
            self.end_headers()
            return
        
        self.send_response(200)
        self.send_header('Content-type', 'application/json; charset=utf-8')
        self.end_headers()
        self.wfile.write(json.dumps(output).encode('utf-8'))
    
    def _compile_and_run(self, code, language):
        """Compile and run code"""
        if not code.strip():
            return {'error': 'Por favor, digite algum código!', 'output': ''}
        
        old_stdout = sys.stdout
        sys.stdout = output_buffer = StringIO()
        
        try:
            compiler.compile_and_run(code, language)
            output = output_buffer.getvalue()
            return {'output': output if output else '(Sem saída)', 'error': None}
        except Exception as e:
            return {'output': '', 'error': f"Erro: {str(e)}"}
        finally:
            sys.stdout = old_stdout
    
    def _translate_only(self, code, language):
        """Just translate without running"""
        if not code.strip():
            return {'error': 'Por favor, digite algum código!', 'translated': ''}
        
        try:
            translated = compiler.compile(code, language)
            return {'translated': translated, 'error': None}
        except Exception as e:
            return {'translated': '', 'error': str(e)}
    
    def log_message(self, format, *args):
        """Suppress logging"""
        pass

if __name__ == '__main__':
    handler = BraythonHandler
    with socketserver.TCPServer(("", PORT), handler) as httpd:
        print("=" * 60)
        print("Braython - Compilador Português/Espanhol → Python")
        print("=" * 60)
        print(f"\n✓ Servidor iniciado em: http://localhost:{PORT}")
        print(f"\n  Abrindo navegador automaticamente...")
        print("\n  Pressione Ctrl+C para parar o servidor\n")
        print("=" * 60)
        
        # Wait a moment then open browser
        time.sleep(1)
        webbrowser.open(f'http://localhost:{PORT}')
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\nServidor parado.")
            sys.exit(0)
