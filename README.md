# 🌸 MÓN QUÀ TÌNH YÊU LÃNG MẠN DÀNH CHO VỢ / NGƯỜI YÊU

Dự án tạo mã **QR Code lãng mạn**: Khi người yêu / vợ dùng điện thoại quét mã, màn hình sẽ mở ra thông điệp **"Chồng Yêu Vợ ❤️"**, phát nhạc du dương và bung nở một bó hoa ly rực rỡ tràn ra toàn màn hình cùng mưa cánh hoa 3D và ngàn trái tim lấp lánh!

---

## ✨ Điểm nổi bật trong thiết kế
1. **Dòng chữ "Chồng Yêu Vợ ❤️" lộng lẫy**:
   - Phông chữ nghệ thuật lãng mạn, hiệu ứng ánh sáng hoàng kim & hồng ngọc tỏa sáng dịu dàng.
2. **Bó hoa ly bung nở & "Tràn ra màn hình"**:
   - Bó hoa ly Casablanca & Stargazer quý phái được đặt trang trọng ở trung tâm với dải lụa mềm mại.
   - Khi mở quà, **hàng chục bông hoa ly nở rộ bung tỏa từ tâm ra khắp màn hình** kết hợp cùng cơn mưa cánh hoa ly 3D chao lượn trong gió và bụi tiên lấp lánh.
3. **Tương tác chạm kỳ diệu (Touch & Tap)**:
   - Chạm vào bất kỳ vị trí nào trên màn hình điện thoại sẽ làm bùng nổ cánh hoa ly và trái tim phát sáng ngay dưới ngón tay.
   - Nút **"Thả ngàn hoa ly"** để tạo thêm đợt bão hoa rực rỡ bất cứ lúc nào.
4. **Nhạc nền hộp nhạc piano ngọt ngào (Web Audio API)**:
   - Tự động hòa âm du dương ngay khi mở quà mà không sợ lỗi bản quyền hay mất kết nối mạng.
5. **Bức thư tình bí mật (Parchment Love Letter)**:
   - Nút **"💌 Đọc tâm thư"** mở ra bức thư tình với những lời chúc chân thành, sâu lắng.

---

## 🚀 HƯỚNG DẪN SỬ DỤNG NHANH

### Cách 1: Quét thử ngay trên điện thoại (cùng mạng WiFi)
Chỉ cần chạy lệnh sau trên máy tính:
```bash
python server.py
```
1. Hệ thống sẽ tự động lấy địa chỉ IP của bạn (ví dụ `http://192.168.x.x:8000`).
2. Tự động hiển thị mã QR trực tiếp trên màn hình dòng lệnh và lưu ra file ảnh `qr_code.png` và thiệp `thiep_tang_vo.png`.
3. Bật camera điện thoại (kết nối cùng Wi-Fi với máy tính) quét mã là xem được ngay!

---

### Cách 2: Đưa lên mạng miễn phí để vợ quét ở bất cứ đâu (Khuyên dùng)

Để vợ hoặc người yêu có thể quét mã ở bất kỳ đâu (kể cả khi dùng 4G/5G khi đi làm, đi chơi hay in ra giấy làm thiệp tặng):

#### Lựa chọn A: Dùng Netlify Drop (Cực nhanh - 30 giây)
1. Truy cập: [https://app.netlify.com/drop](https://app.netlify.com/drop)
2. Kéo thả toàn bộ thư mục `busy-pythagoras` này vào trình duyệt.
3. Netlify sẽ cấp cho bạn một đường link miễn phí (Ví dụ: `https://yeu-vo-nhat-tren-doi.netlify.app`).
4. Chạy lệnh sau để tạo mã QR với link mới:
   ```bash
   python generate_qr.py --url https://yeu-vo-nhat-tren-doi.netlify.app
   ```
5. File `qr_code.png` và `thiep_tang_vo.png` sẽ được cập nhật với đường link mới!

#### Lựa chọn B: Dùng GitHub Pages (Vĩnh viễn & Miễn phí)
1. Tạo một repository mới trên GitHub (ví dụ: `tang-vo-yeu`).
2. Đẩy các file trong thư mục này lên GitHub:
   ```bash
   git add .
   git commit -m "Mon qua tang vo yeu"
   git branch -M main
   git remote add origin https://github.com/<tai-khoan-cua-ban>/tang-vo-yeu.git
   git push -u origin main
   ```
3. Vào **Settings** > **Pages** trên GitHub > Chọn nhánh `main` và ấn **Save**.
4. Bạn sẽ có link dạng: `https://<tai-khoan-cua-ban>.github.io/tang-vo-yeu/`.
5. Tạo lại mã QR:
   ```bash
   python generate_qr.py --url https://<tai-khoan-cua-ban>.github.io/tang-vo-yeu/
   ```

---

## 💌 TÙY CHỈNH LỜI NHẮN
Bạn có thể mở file `index.html` bằng bất kỳ trình soạn thảo nào để:
- Đổi câu chữ trong dòng tiêu đề hoặc lời nhắn (tìm chữ `Chồng Yêu Vợ` hoặc `Gửi Em, Vợ Yêu`).
- Thêm ngày kỷ niệm yêu nhau nếu muốn.
