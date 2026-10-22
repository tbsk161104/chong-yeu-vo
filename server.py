import http.server
import socketserver
import os
import sys
import qrcode
from generate_qr import get_local_ip, create_romantic_qr

PORT = 8000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

def print_ascii_qr(url):
    qr = qrcode.QRCode()
    qr.add_data(url)
    qr.make(fit=True)
    print("\n" + "="*54)
    print("✨ MA QR CODE DANG SAN SANG DE QUET TRUC TIEP ✨")
    print("="*54)
    try:
        qr.print_ascii(invert=True)
    except Exception:
        pass
    print("="*54)

def main():
    ip = get_local_ip()
    url = f"http://{ip}:{PORT}"
    
    print("\n" + "🌸"*25)
    print("    DANG KHOI TAO MAY CHU CHO MON QUA LANG MAN")
    print("🌸"*25)
    
    # Generate fresh QR code and gift card
    create_romantic_qr(url)
    
    # Print ASCII QR directly in console
    print_ascii_qr(url)
    
    print(f"\n[+] Dia chi xem tren may tinh: http://localhost:{PORT}")
    print(f"[+] Dia chi de dien thoai quet (cung mang WiFi): {url}")
    print(f"[+] File anh QR code: qr_code.png")
    print(f"[+] File thiep tang:  thiep_tang_vo.png")
    print("\n--> May chu dang chay... (Nhan Ctrl+C de dung)")
    
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nDa dung may chu. Chuc hai ban luon hanh phuc ben nhau! ❤️")

if __name__ == "__main__":
    main()
