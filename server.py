#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import http.server
import socketserver
import os
import sys

PORT = 8080

# Papkaga o'tish
os.chdir(os.path.dirname(os.path.abspath(__file__)))

class MyHTTPHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # CORS headers (xavfsizlik uchun)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()
    
    def log_message(self, format, *args):
        # Loglarni chiroyli qilish
        print(f"[{self.address_string()}] {format % args}")

def main():
    try:
        with socketserver.TCPServer(("0.0.0.0", PORT), MyHTTPHandler) as httpd:
            print("="*60)
            print("🚀 SERVER ISHGA TUSHDI!")
            print("="*60)
            print(f"📍 Lokal manzil:  http://localhost:{PORT}")
            
            # IP manzilni topish
            try:
                import socket
                hostname = socket.gethostname()
                local_ip = socket.gethostbyname(hostname)
                print(f"📍 Tarmoq manzili: http://{local_ip}:{PORT}")
            except:
                pass
            
            print("="*60)
            print("📱 Telefonda sinash:")
            print("   1. Ngrok ishlatilsa: ngrok http 8080")
            print("   2. Vercel ishlatilsa: vercel --prod")
            print("="*60)
            print("❌ To'xtatish: Ctrl+C")
            print("="*60)
            
            httpd.serve_forever()
            
    except KeyboardInterrupt:
        print("\n🛑 Server to'xtatildi.")
        sys.exit(0)
    except OSError as e:
        if "Address already in use" in str(e):
            print(f"❌ Xatolik: {PORT} port band!")
            print("   Iltimos, portni o'zgartiring yoki boshqa dasturni to'xtating.")
        else:
            print(f"❌ Xatolik: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()