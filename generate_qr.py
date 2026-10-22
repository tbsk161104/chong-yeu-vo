import os
import sys
import socket
import argparse
import qrcode
from PIL import Image, ImageDraw, ImageFont, ImageFilter

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    except Exception:
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip

def get_font(font_name, size):
    fonts_dir = os.path.join(os.environ.get('WINDIR', 'C:\\Windows'), 'Fonts')
    path = os.path.join(fonts_dir, font_name)
    if os.path.exists(path):
        try:
            return ImageFont.truetype(path, size)
        except Exception:
            pass
    return ImageFont.load_default()

def create_romantic_qr(target_url, output_path="qr_code.png", card_output_path="thiep_tang_vo.png"):
    print(f"[*] Dang tao QR code cho URL: {target_url}")
    
    # 1. Generate base QR Code with High Error Correction (30%)
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=20,
        border=4,
    )
    qr.add_data(target_url)
    qr.make(fit=True)

    # Convert to PIL Image with custom romantic colors
    # Foreground: Deep romantic burgundy / ruby rose
    # Background: Soft creamy pearl white
    qr_img = qr.make_image(
        fill_color="#880e4f",  # Deep romantic rose
        back_color="#fffafb"   # Soft petal white
    ).convert("RGBA")

    # Add a romantic heart badge in the center of the QR code
    qr_w, qr_h = qr_img.size
    badge_size = int(qr_w * 0.22)
    badge = Image.new("RGBA", (badge_size, badge_size), (0, 0, 0, 0))
    b_draw = ImageDraw.Draw(badge)
    
    # Circle background for badge
    b_draw.ellipse((2, 2, badge_size - 2, badge_size - 2), fill="#ffffff", outline="#d81b60", width=4)
    
    # Draw heart icon in badge
    h_cx, h_cy = badge_size // 2, badge_size // 2
    r = badge_size * 0.22
    # Heart shape using polygon or curves
    heart_points = []
    import math
    for t in [i * 0.05 for i in range(126)]:
        x = 16 * (math.sin(t) ** 3)
        y = -(13 * math.cos(t) - 5 * math.cos(2*t) - 2 * math.cos(3*t) - math.cos(4*t))
        heart_points.append((h_cx + x * (r / 16), h_cy + y * (r / 16) - 2))
    b_draw.polygon(heart_points, fill="#e91e63")

    # Paste badge onto QR code center
    offset = ((qr_w - badge_size) // 2, (qr_h - badge_size) // 2)
    qr_img.paste(badge, offset, mask=badge)
    qr_img.save(output_path, "PNG")
    print(f"[+] Da luu anh QR code tai: {output_path}")

    # 2. Generate a Luxury Romantic Gift Card ("Thiệp Tặng Vợ Yêu")
    card_w, card_h = 1080, 1520
    card = Image.new("RGBA", (card_w, card_h), "#120317")
    draw = ImageDraw.Draw(card)

    # Background Romantic Glow
    glow = Image.new("RGBA", (card_w, card_h), (0, 0, 0, 0))
    g_draw = ImageDraw.Draw(glow)
    g_draw.ellipse((card_w//2 - 380, 200, card_w//2 + 380, 960), fill=(255, 105, 180, 65))
    g_draw.ellipse((card_w//2 - 300, 700, card_w//2 + 300, 1300), fill=(255, 215, 0, 40))
    glow = glow.filter(ImageFilter.GaussianBlur(80))
    card.paste(glow, (0, 0), mask=glow)

    # Double Gold & Rose Border
    draw.rounded_rectangle((35, 35, card_w - 35, card_h - 35), radius=35, outline="#ffd700", width=3)
    draw.rounded_rectangle((48, 48, card_w - 48, card_h - 48), radius=28, outline=(255, 182, 193, 140), width=2)

    # Corner Floral Ornaments
    ornaments = [(70, 70), (card_w - 70, 70), (70, card_h - 70), (card_w - 70, card_h - 70)]
    for ox, oy in ornaments:
        draw.ellipse((ox - 8, oy - 8, ox + 8, oy + 8), fill="#ffd700")

    # Typography Fonts
    title_font = get_font("times.ttf", 62)
    sub_font = get_font("georgia.ttf", 34)
    tip_font = get_font("segoeui.ttf", 30)
    love_font = get_font("times.ttf", 52)
    sig_font = get_font("georgia.ttf", 36)

    # Header Texts
    def draw_centered_text(y, text, font, fill):
        bbox = draw.textbbox((0, 0), text, font=font)
        tw = bbox[2] - bbox[0]
        draw.text(((card_w - tw) // 2, y), text, font=font, fill=fill)

    draw_centered_text(110, "MÓN QUÀ BÍ MẬT DÀNH CHO VỢ", title_font, "#fff3d1")
    draw_centered_text(195, "Gửi người phụ nữ tuyệt vời nhất của anh ❤️", sub_font, "#ffb6c1")

    # Paste QR Code on an elegant card frame
    qr_frame_size = 560
    qr_resized = qr_img.resize((qr_frame_size, qr_frame_size), Image.Resampling.LANCZOS)
    
    # White/Gold rounded background for the QR code
    frame_x = (card_w - qr_frame_size) // 2
    frame_y = 285
    draw.rounded_rectangle(
        (frame_x - 18, frame_y - 18, frame_x + qr_frame_size + 18, frame_y + qr_frame_size + 18),
        radius=30,
        fill="#ffffff",
        outline="#ffd700",
        width=5
    )
    card.paste(qr_resized, (frame_x, frame_y), mask=qr_resized)

    # Scannable Call to Action
    draw_centered_text(920, "✨ Dùng camera điện thoại hoặc Zalo để quét mã ✨", tip_font, "#ffe6f2")
    draw_centered_text(975, "để mở lời nhắn và vườn hoa ly rực rỡ!", tip_font, "#ffd6eb")

    # Romantic Divider
    div_y = 1060
    draw.line((card_w//2 - 180, div_y, card_w//2 + 180, div_y), fill="#ffd700", width=2)
    draw.ellipse((card_w//2 - 6, div_y - 6, card_w//2 + 6, div_y + 6), fill="#ff4081")

    # Bottom Romantic Declaration
    draw_centered_text(1110, "CHỒNG YÊU VỢ RẤT NHIỀU", love_font, "#ffb3d9")
    draw_centered_text(1185, "Yêu em từ những điều giản dị nhất...", sig_font, "#ffffff")
    draw_centered_text(1250, "🌸 Bó hoa ly ngát hương dành riêng cho em 🌸", tip_font, "#ffc0cb")

    # Card Footer
    draw_centered_text(1410, "Forever & Always With You ❤️", get_font("georgia.ttf", 24), (255, 255, 255, 110))

    card.save(card_output_path, "PNG")
    print(f"[+] Da tao thiep tang lang man tai: {card_output_path}")

def main():
    parser = argparse.ArgumentParser(description="Tao ma QR Code va thiep tinh yeu lang man cho vo")
    parser.add_argument("--url", type=str, default="", help="Duong dan URL trang web (neu de trong se dung IP mang WiFi hien tai)")
    parser.add_argument("--port", type=int, default=8000, help="Port local server")
    args = parser.parse_args()

    if args.url:
        target_url = args.url
    else:
        ip = get_local_ip()
        target_url = f"http://{ip}:{args.port}"
        print(f"[*] Khong truyen URL, tu dong su dung IP WiFi hien tai: {target_url}")

    create_romantic_qr(target_url)
    print("\n" + "="*50)
    print("HOAN THANH!")
    print(f"1. Ma QR code le: qr_code.png")
    print(f"2. Thiep tang vo lang man: thiep_tang_vo.png")
    print(f"Target URL: {target_url}")
    print("="*50)

if __name__ == "__main__":
    main()
