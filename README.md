# HỆ THỐNG QUẢN LÝ TRƯỜNG MẦM NON (KMS)
> **Môn học:** Công nghệ Phần mềm / Phân tích Thiết kế Hệ thống Thông tin  
> **Repository:** [TTN_CNPM](https://github.com/trungnguyen332005genz-source/TTN_CNPM.git)  
> **Tài liệu đặc tả:** [KeHoachCNPM.docx](./KeHoachCNPM.docx)

---

## 📌 PHÂN CÔNG TRÁCH NHIỆM

| Thành viên | Trách nhiệm được giao | Trạng thái |
| :--- | :--- | :--- |
| **Luân** | **Phân tích + Mô hình tổng thể**<br>- Phân tích yêu cầu hệ thống<br>- Use Case tổng quát<br>- ERD (Cơ sở dữ liệu)<br>- Class Diagram | *Phần phụ trách của Luân (Đang tiến hành độc lập)* |
| **Nguyên** | **Mô hình hóa luồng xử lý**<br>- Use Case phân rã từng chức năng<br>- Viết đặc tả Use Case chi tiết (theo mẫu bảng chuẩn)<br>- Activity Diagram từng chức năng<br>- Sequence Diagram từng chức năng | **ĐÃ HOÀN THÀNH 100%** |

---

## 📋 NỘI DUNG THỰC HIỆN CỦA NGUYÊN (MÔ HÌNH HÓA LUỒNG XỬ LÝ)

### 1. Phân rã Use Case theo 5 Phân hệ nghiệp vụ
1. **Phân hệ 1: Quản lý Trẻ em**
   - `UC-TE01`: Xem & Tra cứu danh sách trẻ em
   - `UC-TE02`: Thêm mới hồ sơ trẻ em (`<<include>> UC-PH02`)
   - `UC-TE03`: Chỉnh sửa hồ sơ trẻ em
   - `UC-TE04`: Xóa / Chuyển trạng thái học (Đang học / Bảo lưu / Tốt nghiệp)
   - `UC-TE05`: Ghi nhận theo dõi sức khỏe & sinh hoạt
2. **Phân hệ 2: Quản lý Giáo viên**
   - `UC-GV01`: Xem danh sách & tìm kiếm giáo viên
   - `UC-GV02`: Thêm mới giáo viên
   - `UC-GV03`: Chỉnh sửa hồ sơ giáo viên
   - `UC-GV04`: Xóa / Khóa tài khoản giáo viên
   - `UC-GV05`: Phân công lớp giảng dạy (Chủ nhiệm / Bán trú / Năng khiếu)
3. **Phân hệ 3: Quản lý Phụ huynh**
   - `UC-PH01`: Xem & Tra cứu danh sách phụ huynh
   - `UC-PH02`: Thêm mới & Liên kết phụ huynh - trẻ (Hỗ trợ 1 Phụ huynh - N Trẻ)
   - `UC-PH03`: Cập nhật thông tin phụ huynh
   - `UC-PH04`: Hủy liên kết phụ huynh - trẻ
   - `UC-PH05`: Phụ huynh xem thông tin & quá trình học của con
4. **Phân hệ 4: Quản lý Thực đơn**
   - `UC-TD01`: Xem danh sách thực đơn tuần / ngày
   - `UC-TD02`: Lập thực đơn tuần mới (`<<include>> UC-TD04`)
   - `UC-TD03`: Chỉnh sửa thực đơn tuần
   - `UC-TD04`: Quản lý danh mục món ăn & thành phần dinh dưỡng
   - `UC-TD05`: Phụ huynh xem thực đơn của con
5. **Phân hệ 5: Quản lý Học phí và Thanh toán**
   - `UC-HP01`: Lập bảng tính học phí & tiền ăn tháng (`<<include>> UC-HP02`)
   - `UC-HP02`: Ghi nhận ngày nghỉ để khấu trừ tiền ăn
   - `UC-HP03`: Phát hành thông báo học phí / phiếu thu tháng
   - `UC-HP04`: Phụ huynh xem chi tiết học phí
   - `UC-HP05`: Thanh toán học phí bằng mã QR VietQR động (`<<extend>> UC-HP04`)
   - `UC-HP06`: Xác nhận & Cập nhật thanh toán tự động qua Webhook

---

### 2. Danh mục Bảng đặc tả Use Case chi tiết (Chuẩn form mẫu)
Tất cả 10 Use Case cốt lõi được đặc tả đầy đủ theo cấu trúc:
- **Use Case ID**
- **Tên Use Case**
- **Tác nhân**
- **Mô tả chức năng**
- **Điều kiện tiên quyết**
- **Yêu cầu**
- **Kịch bản chính (Main Flow)**
- **Kịch bản phụ / Ngoại lệ (Sub/Exception Flow)**

| Bảng | Mã Use Case | Tên chức năng đặc tả |
| :---: | :---: | :--- |
| Bảng 1 | `UC-TE02` | Thêm mới hồ sơ trẻ em & xếp lớp |
| Bảng 2 | `UC-TE03` | Chỉnh sửa thông tin hồ sơ trẻ em |
| Bảng 3 | `UC-GV05` | Phân công giáo viên vào lớp học |
| Bảng 4 | `UC-PH02` | Thêm mới hồ sơ phụ huynh và liên kết với trẻ |
| Bảng 5 | `UC-PH05` | Phụ huynh xem thông tin và hồ sơ của con |
| Bảng 6 | `UC-TD02` | Lập thực đơn dinh dưỡng theo tuần / ngày |
| Bảng 7 | `UC-TD05` | Phụ huynh xem thực đơn dinh dưỡng của con |
| Bảng 8 | `UC-HP01` | Lập bảng tính học phí và tiền ăn tháng |
| Bảng 9 | `UC-HP02` | Ghi nhận ngày nghỉ trẻ để tự động trừ tiền ăn |
| Bảng 10 | `UC-HP05` | Thanh toán học phí bằng mã QR VietQR động |

---

### 3. Sơ đồ Hoạt động (Activity Diagrams)
Các sơ đồ nằm trong thư mục [`diagrams/`](./diagrams/):
- [`activity_them_tre_em.puml`](./diagrams/activity_them_tre_em.puml): Quy trình tiếp nhận trẻ & phân lớp
- [`activity_phan_cong_gv.puml`](./diagrams/activity_phan_cong_gv.puml): Quy trình phân công giáo viên phụ trách
- [`activity_lap_thuc_don.puml`](./diagrams/activity_lap_thuc_don.puml): Quy trình lập & ban hành thực đơn tuần
- [`activity_tinh_hoc_phi_tien_an.puml`](./diagrams/activity_tinh_hoc_phi_tien_an.puml): Quy trình trừ tiền ăn & tính tổng học phí
- [`activity_thanhtoan_vietqr.puml`](./diagrams/activity_thanhtoan_vietqr.puml): Quy trình sinh mã VietQR & Webhook đối soát

---

### 4. Sơ đồ Tuần tự (Sequence Diagrams)
Các sơ đồ tương tác 3 lớp (Boundary - Control - Entity) nằm trong thư mục [`diagrams/`](./diagrams/):
- [`sequence_them_tre_em.puml`](./diagrams/sequence_them_tre_em.puml)
- [`sequence_phan_cong_gv.puml`](./diagrams/sequence_phan_cong_gv.puml)
- [`sequence_lap_thuc_don.puml`](./diagrams/sequence_lap_thuc_don.puml)
- [`sequence_tinh_hoc_phi_tien_an.puml`](./diagrams/sequence_tinh_hoc_phi_tien_an.puml)
- [`sequence_thanhtoan_vietqr.puml`](./diagrams/sequence_thanhtoan_vietqr.puml)

---

## 🛠 HƯỚNG DẪN MỞ VÀ VẼ TRÊN ASTAH COMMUNITY
Phần mềm **Astah Community** được cài đặt tại `C:\Program Files\astah-community`.
1. **Khởi động:** Mở Astah Community từ menu Start hoặc đường dẫn trên.
2. **Use Case Diagram:** Chuột phải vào Project -> `Create Diagram` -> `Use Case Diagram`. Kéo thả Actor và Use Case từ thanh công cụ.
3. **Activity Diagram:** Chuột phải vào Package -> `Create Diagram` -> `Activity Diagram`. Kéo thả Initial Node, Action, Decision Node và Activity Final Node.
4. **Sequence Diagram:** Chuột phải vào Package -> `Create Diagram` -> `Sequence Diagram`. Kéo thả Lifeline (Boundary, Control, Entity), kẻ các thông điệp Synchronous Message và Reply Message.
