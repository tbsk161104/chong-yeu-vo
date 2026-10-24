import os
import sys
import argparse
import qrcode
from PIL import Image, ImageDraw

def create_pure_romantic_qr(target_url, output_path="qr_code.png"):
    print(f"[*] Dang tao QR code tinh yeu cho URL: {target_url}")
    
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=20,
        border=3,
    )
    qr.add_data(target_url)
    qr.make(fit=True)

    # Color: Deep romantic wine-rose on pure white
    qr_img = qr.make_image(
        fill_color="#880e4f",
        back_color="#ffffff"
    ).convert("RGBA")

    # Center heart badge
    w, h = qr_img.size
    badge_size = int(w * 0.22)
    badge = Image.new("RGBA", (badge_size, badge_size), (0, 0, 0, 0))
    b_draw = ImageDraw.Draw(badge)
    
    # White circular pill with rose border
    b_draw.ellipse((3, 3, badge_size - 3, badge_size - 3), fill="#ffffff", outline="#e91e63", width=5)

    # Heart shape inside
    cx, cy = badge_size // 2, badge_size // 2
    r = badge_size * 0.22
    import math
    heart_points = []
    for t in [i * 0.05 for i in range(126)]:
        x = 16 * (math.sin(t) ** 3)
        y = -(13 * math.cos(t) - 5 * math.cos(2*t) - 2 * math.cos(3*t) - math.cos(4*t))
        heart_points.append((cx + x * (r / 16), cy + y * (r / 16) - 2))
    b_draw.polygon(heart_points, fill="#e91e63")

    offset = ((w - badge_size) // 2, (h - badge_size) // 2)
    qr_img.paste(badge, offset, mask=badge)
    qr_img.save(output_path, "PNG")
    print(f"[+] Da tao xong ma QR code tinh yeu tai: {output_path}")

def main():
    parser = argparse.ArgumentParser(description="Tao ma QR Code tinh yeu")
    parser.add_argument("--url", type=str, default="https://tinyurl.com/gui-vo-yeu-cua-anh", help="URL trang web")
    args = parser.parse_args()
    create_pure_romantic_qr(args.url)

if __name__ == "__main__":
    main()
