# -*- coding: utf-8 -*-
import os
import shutil
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

from gen_base import (
    set_cell_background, set_cell_margins, add_header, add_p,
    add_callout, add_usecase_table, add_code_block
)

def build_document(output_path):
    doc = docx.Document()

    # Set page margins: 1 inch (2.54 cm) all around
    sections = doc.sections
    for s in sections:
        s.top_margin = Inches(1.0)
        s.bottom_margin = Inches(1.0)
        s.left_margin = Inches(1.0)
        s.right_margin = Inches(1.0)

    # Document Header / Title
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_before = Pt(0)
    p_title.paragraph_format.space_after = Pt(4)
    r_uni = p_title.add_run("BỘ MÔN CÔNG NGHỆ PHẦN MỀM - DỰ ÁN HỆ THỐNG QUẢN LÝ MẦM NON\n")
    r_uni.bold = True
    r_uni.font.name = 'Times New Roman'
    r_uni.font.size = Pt(13)
    r_uni.font.color.rgb = RGBColor(31, 78, 121)

    r_main_title = p_title.add_run("KẾ HOẠCH & TÀI LIỆU PHÂN TÍCH THIẾT KẾ HỆ THỐNG")
    r_main_title.bold = True
    r_main_title.font.name = 'Times New Roman'
    r_main_title.font.size = Pt(16)
    r_main_title.font.color.rgb = RGBColor(192, 0, 0)

    add_p(doc, "Tài liệu kỹ thuật theo dõi tiến độ và mô hình hóa hệ thống", italic=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=12)

    # ==========================================
    # PHẦN 1: MÔ TẢ NGHIỆP VỤ HỆ THỐNG (GIỮ NGUYÊN NỘI DUNG GỐC)
    # ==========================================
    add_header(doc, "PHẦN I: TỔNG QUAN CÁC MODULE NGHIỆP VỤ HỆ THỐNG", level=1)

    # 1. Quản lý trẻ em
    add_header(doc, "1. Quản lý trẻ em", level=2)
    add_p(doc, "Đây là chức năng trung tâm.", bold=True)
    add_p(doc, "Bao gồm:")
    add_p(doc, "• Thêm / sửa / xóa / xem thông tin trẻ\n• Hồ sơ cá nhân\n• Ngày sinh, giới tính\n• Thông tin sức khỏe cơ bản\n• Lớp đang học\n• Trạng thái học\n• Liên kết với phụ huynh\n• Lịch sử học tập/sinh hoạt nếu cần")
    add_p(doc, "Ví dụ cấu trúc phân rã chức năng:", italic=True)
    tree_tre_em = """Quản lý trẻ em
├── Danh sách trẻ
├── Thêm trẻ
├── Hồ sơ trẻ
├── Chỉnh sửa
└── Tìm kiếm / lọc"""
    add_code_block(doc, tree_tre_em)

    # 2. Quản lý giáo viên
    add_header(doc, "2. Quản lý giáo viên", level=2)
    add_p(doc, "Bao gồm:")
    add_p(doc, "• Thêm / sửa / xóa giáo viên\n• Hồ sơ giáo viên\n• Chuyên môn\n• Số điện thoại\n• Phân công lớp\n• Trạng thái làm việc")
    add_p(doc, "Mô hình liên kết luồng nghiệp vụ:", italic=True)
    flow_gv = """Giáo viên
    ↓
Lớp học
    ↓
Danh sách trẻ"""
    add_code_block(doc, flow_gv)

    # 3. Quản lý phụ huynh
    add_header(doc, "3. Quản lý phụ huynh", level=2)
    add_p(doc, "Bao gồm:")
    add_p(doc, "• Thông tin phụ huynh\n• Số điện thoại\n• Email\n• Địa chỉ\n• Quan hệ với trẻ\n• Quản lý nhiều con\n• Xem thông tin của con")
    add_p(doc, "Quan hệ database:")
    add_p(doc, "Phụ huynh 1 ───── N Trẻ", bold=True)
    add_p(doc, "Ví dụ một phụ huynh có thể có:")
    tree_ph = """Nguyễn Văn A
├── Nguyễn Minh B → Lớp Lá 1
└── Nguyễn Minh C → Lớp Chồi 2"""
    add_code_block(doc, tree_ph)

    # 4. Quản lý thực đơn
    add_header(doc, "4. Quản lý thực đơn", level=2)
    add_p(doc, "Chức năng mang tính đặc thù nghiệp vụ của trường mầm non, phục vụ quản lý dinh dưỡng và thông tin đến phụ huynh.")
    add_p(doc, "Có thể quản lý:")
    add_p(doc, "• Thực đơn theo ngày / theo tuần\n• Bữa sáng\n• Bữa trưa\n• Bữa phụ (xế)\n• Món ăn & thành phần món ăn\n• Giá tiền & dinh dưỡng\n• Cho phụ huynh xem thực đơn của con")
    add_p(doc, "Ví dụ lịch thực đơn mẫu:", italic=True)
    menu_sample = """THỨ 2 - 28/09/2026
Sáng:
  🥛 Sữa hạt
  🍞 Bánh mì bơ sữa
Trưa:
  🍚 Cơm trắng dẻo
  🥩 Thịt heo kho trứng cút
  🥬 Rau cải luộc sốt mè
  🍲 Canh bí đỏ thịt bằm
Xế:
  🍌 Chuối tiêu + Sữa chua"""
    add_code_block(doc, menu_sample)

    # 5. Quản lý học phí và thanh toán
    add_header(doc, "5. Quản lý học phí và thanh toán (Tính học phí + Tiền ăn + Thanh toán QR)", level=2)
    add_p(doc, "Module riêng biệt xử lý tài chính học phí, tiền ăn và đối soát thanh toán trực tuyến.")
    add_p(doc, "Bao gồm:")
    add_p(doc, "1. Tính học phí:")
    calc_hp = """Ví dụ Học phí tháng 09/2026:
----------------------------------------
Học phí cơ bản:       1.500.000 VNĐ
Tiền ăn:                600.000 VNĐ
Phí khác/dịch vụ:       100.000 VNĐ
Giảm trừ:                     0 VNĐ
----------------------------------------
Tổng cộng:            2.200.000 VNĐ

Công thức tính:
Tổng tiền = Học phí cơ bản + Tiền ăn + Phí dịch vụ - Giảm trừ"""
    add_code_block(doc, calc_hp)

    add_p(doc, "2. Tính tiền ăn:")
    add_p(doc, "• Công thức: Tiền ăn = (Số ngày ăn thực tế) × (Đơn giá/ngày)")
    add_p(doc, "• Ví dụ: 20 ngày × 30.000đ = 600.000đ")
    add_p(doc, "• Trường hợp trẻ nghỉ: Hệ thống tự động trừ tiền ăn dựa trên số ngày nghỉ có phép/báo trước theo quy định.")

    # 6. Thanh toán QR
    add_header(doc, "6. Thanh toán QR", level=2)
    add_p(doc, "Điểm nhấn kỹ thuật hỗ trợ trải nghiệm thanh toán không dùng tiền mặt tức thì qua chuẩn VietQR.")
    flow_qr = """Quy trình thanh toán QR:
Phụ huynh
    ↓
Xem học phí chi tiết
    ↓
Xem chi tiết các khoản phải trả (Học phí, Tiền ăn, Dịch vụ, Trừ ngày nghỉ)
    ↓
Nhấn nút "Thanh toán"
    ↓
Hệ thống tự động sinh mã VietQR động (chứa số tiền và mã hóa đơn)
    ↓
Quét QR bằng ứng dụng ngân hàng / Ví điện tử
    ↓
Hoàn tất giao dịch thanh toán
    ↓
Hệ thống nhận xác nhận và cập nhật trạng thái hóa đơn: "Đã thanh toán" """
    add_code_block(doc, flow_qr)

    # ==========================================
    # PHẦN 2: PHÂN CHIA NHIỆM VỤ DỰ ÁN
    # ==========================================
    add_header(doc, "PHẦN II: PHÂN CÔNG NHIỆM VỤ THÀNH VIÊN", level=1)

    add_header(doc, "A. Luân — Phân tích + Mô hình tổng thể", level=2)
    add_callout(doc, "LƯU Ý PHÂN CÔNG CỦA LUÂN", 
                "Phần việc này thuộc trách nhiệm của Luân. Để đảm bảo phân công lao động rõ ràng, đúng kế hoạch, "
                "phần này được giữ nguyên danh mục đầu việc để Luân độc lập thực hiện và tích hợp sau, "
                "không bị can thiệp hay làm thay.")
    add_p(doc, "Danh mục đầu việc của Luân:")
    add_p(doc, "1. Phân tích yêu cầu hệ thống (Yêu cầu chức năng, yêu cầu phi chức năng)\n"
               "2. Use Case tổng quát (Sơ đồ Use Case tổng thể toàn hệ thống)\n"
               "3. ERD (Entity Relationship Diagram - Thiết kế cơ sở dữ liệu quan hệ)\n"
               "4. Class Diagram (Sơ đồ lớp phân tích/thiết kế)")

    # ==========================================
    # PHẦN 3: NGUYÊN — MÔ HÌNH HÓA LUỒNG XỬ LÝ (TRỌNG TÂM THỰC HIỆN)
    # ==========================================
    doc.add_page_break()
    add_header(doc, "B. Nguyên — Mô hình hóa luồng xử lý", level=2)
    add_callout(doc, "PHẦN THỰC HIỆN BỞI NGUYÊN",
                "Phần dưới đây là toàn bộ nội dung do Nguyên phụ trách theo đúng kế hoạch: "
                "Use Case phân rã từng chức năng, Viết bảng đặc tả Use Case chi tiết theo form chuẩn, "
                "Mô hình hóa Activity Diagram (Sơ đồ hoạt động) và Sequence Diagram (Sơ đồ tuần tự).")

    # ----------------------------------------------------
    # MỤC 1: USE CASE PHÂN RÃ TỪNG CHỨC NĂNG
    # ----------------------------------------------------
    add_header(doc, "1. Use Case Phân rã từng chức năng", level=3)
    add_p(doc, "Dựa trên các yêu cầu nghiệp vụ cốt lõi của Trường Mầm non, hệ thống được phân rã chi tiết thành 5 phân hệ với các Use Case cụ thể như sau:")

    # Table of Use Cases
    p_t_uc = doc.add_paragraph()
    p_t_uc.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_t_uc = p_t_uc.add_run("Bảng phân rã chi tiết Use Case hệ thống Quản lý Mầm non")
    r_t_uc.bold = True
    r_t_uc.italic = True
    r_t_uc.font.name = 'Times New Roman'
    r_t_uc.font.size = Pt(11)

    uc_summary_table = doc.add_table(rows=27, cols=5)
    uc_summary_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    uc_summary_table.autofit = False

    t_widths = [Inches(0.9), Inches(1.3), Inches(1.8), Inches(1.3), Inches(1.2)]
    for r in uc_summary_table.rows:
        for idx, w in enumerate(t_widths):
            r.cells[idx].width = w

    headers = ["Mã UC", "Phân hệ", "Tên Use Case", "Tác nhân chính", "Quan hệ (nếu có)"]
    for idx, h in enumerate(headers):
        c = uc_summary_table.cell(0, idx)
        set_cell_background(c, "2E75B6")
        set_cell_margins(c, top=80, bottom=80, left=100, right=100)
        p = c.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(h)
        r.bold = True
        r.font.name = 'Times New Roman'
        r.font.size = Pt(10)
        r.font.color.rgb = RGBColor(255, 255, 255)

    uc_data = [
        # Phân hệ 1: Quản lý trẻ em
        ("UC-TE01", "1. Quản lý trẻ em", "Xem & Tra cứu danh sách trẻ", "Quản lý, Giáo viên", "-"),
        ("UC-TE02", "1. Quản lý trẻ em", "Thêm mới hồ sơ trẻ em", "Quản lý", "<<include>> UC-PH02"),
        ("UC-TE03", "1. Quản lý trẻ em", "Chỉnh sửa hồ sơ trẻ em", "Quản lý", "-"),
        ("UC-TE04", "1. Quản lý trẻ em", "Xóa/Cập nhật trạng thái học", "Quản lý", "-"),
        ("UC-TE05", "1. Quản lý trẻ em", "Ghi nhận sức khỏe & sinh hoạt", "Giáo viên", "-"),

        # Phân hệ 2: Quản lý giáo viên
        ("UC-GV01", "2. Quản lý giáo viên", "Xem danh sách giáo viên", "Quản lý", "-"),
        ("UC-GV02", "2. Quản lý giáo viên", "Thêm mới giáo viên", "Quản lý", "-"),
        ("UC-GV03", "2. Quản lý giáo viên", "Chỉnh sửa hồ sơ giáo viên", "Quản lý", "-"),
        ("UC-GV04", "2. Quản lý giáo viên", "Xóa / Khóa hồ sơ giáo viên", "Quản lý", "-"),
        ("UC-GV05", "2. Quản lý giáo viên", "Phân công lớp giảng dạy", "Quản lý", "-"),

        # Phân hệ 3: Quản lý phụ huynh
        ("UC-PH01", "3. Quản lý phụ huynh", "Xem danh sách phụ huynh", "Quản lý", "-"),
        ("UC-PH02", "3. Quản lý phụ huynh", "Thêm mới & liên kết phụ huynh - trẻ", "Quản lý", "-"),
        ("UC-PH03", "3. Quản lý phụ huynh", "Cập nhật thông tin phụ huynh", "Quản lý, Phụ huynh", "-"),
        ("UC-PH04", "3. Quản lý phụ huynh", "Hủy liên kết phụ huynh - trẻ", "Quản lý", "-"),
        ("UC-PH05", "3. Quản lý phụ huynh", "Xem hồ sơ & thông tin của con", "Phụ huynh", "-"),

        # Phân hệ 4: Quản lý thực đơn
        ("UC-TD01", "4. Quản lý thực đơn", "Xem danh sách thực đơn tuần", "Quản lý, Phụ huynh, GV", "-"),
        ("UC-TD02", "4. Quản lý thực đơn", "Lập thực đơn tuần mới", "Quản lý / Dinh dưỡng", "<<include>> UC-TD04"),
        ("UC-TD03", "4. Quản lý thực đơn", "Chỉnh sửa thực đơn tuần", "Quản lý / Dinh dưỡng", "-"),
        ("UC-TD04", "4. Quản lý thực đơn", "Quản lý danh mục món & dưỡng chất", "Quản lý / Dinh dưỡng", "-"),
        ("UC-TD05", "4. Quản lý thực đơn", "Phụ huynh xem thực đơn của con", "Phụ huynh", "-"),

        # Phân hệ 5: Học phí & Thanh toán
        ("UC-HP01", "5. Học phí & Thanh toán", "Lập bảng tính học phí & tiền ăn", "Kế toán / Quản lý", "<<include>> UC-HP02"),
        ("UC-HP02", "5. Học phí & Thanh toán", "Ghi nhận ngày nghỉ để trừ tiền ăn", "Giáo viên, Kế toán", "-"),
        ("UC-HP03", "5. Học phí & Thanh toán", "Phát hành thông báo học phí tháng", "Kế toán / Quản lý", "-"),
        ("UC-HP04", "5. Học phí & Thanh toán", "Phụ huynh xem chi tiết học phí", "Phụ huynh", "-"),
        ("UC-HP05", "5. Học phí & Thanh toán", "Thanh toán học phí qua mã VietQR", "Phụ huynh", "<<extend>> UC-HP04"),
        ("UC-HP06", "5. Học phí & Thanh toán", "Xác nhận & Cập nhật thanh toán", "Hệ thống Cổng/Ngân hàng", "-")
    ]

    for row_idx, data in enumerate(uc_data, start=1):
        bg = "FFFFFF" if row_idx % 2 == 1 else "F2F4F7"
        for col_idx, text in enumerate(data):
            c = uc_summary_table.cell(row_idx, col_idx)
            set_cell_background(c, bg)
            set_cell_margins(c, top=60, bottom=60, left=80, right=80)
            p = c.paragraphs[0]
            p.paragraph_format.space_before = Pt(1)
            p.paragraph_format.space_after = Pt(1)
            r = p.add_run(text)
            r.font.name = 'Times New Roman'
            r.font.size = Pt(9.5)
            if col_idx == 0:
                r.bold = True

    # Borders for summary table
    tblPr = uc_summary_table._tbl.tblPr
    borders = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>'
        f'<w:top w:val="single" w:sz="6" w:space="0" w:color="2E75B6"/>'
        f'<w:left w:val="single" w:sz="6" w:space="0" w:color="2E75B6"/>'
        f'<w:bottom w:val="single" w:sz="6" w:space="0" w:color="2E75B6"/>'
        f'<w:right w:val="single" w:sz="6" w:space="0" w:color="2E75B6"/>'
        f'<w:insideH w:val="single" w:sz="4" w:space="0" w:color="D9D9D9"/>'
        f'<w:insideV w:val="single" w:sz="4" w:space="0" w:color="D9D9D9"/>'
        f'</w:tblBorders>'
    )
    tblPr.append(borders)
    doc.add_paragraph().paragraph_format.space_after = Pt(8)

    add_p(doc, "Cấu trúc phân rã Use Case theo sơ đồ khối logic:", bold=True)
    uc_ascii = """HỆ THỐNG QUẢN LÝ TRƯỜNG MẦM NON
├── Phân hệ 1: Quản lý Trẻ em
│   ├── UC-TE01: Xem & Tìm kiếm danh sách trẻ
│   ├── UC-TE02: Thêm mới trẻ em ──<<include>>──> UC-PH02: Thêm/Liên kết phụ huynh
│   ├── UC-TE03: Chỉnh sửa hồ sơ trẻ em
│   ├── UC-TE04: Xóa/Chuyển trạng thái học (Đang học / Bảo lưu / Tốt nghiệp)
│   └── UC-TE05: Theo dõi sức khỏe & sinh hoạt
├── Phân hệ 2: Quản lý Giáo viên
│   ├── UC-GV01: Xem & Tìm kiếm giáo viên
│   ├── UC-GV02: Thêm mới giáo viên
│   ├── UC-GV03: Cập nhật hồ sơ giáo viên
│   ├── UC-GV04: Xóa/Khóa hồ sơ giáo viên
│   └── UC-GV05: Phân công giáo viên chủ nhiệm / phụ trách lớp học
├── Phân hệ 3: Quản lý Phụ huynh
│   ├── UC-PH01: Xem & Tra cứu danh sách phụ huynh
│   ├── UC-PH02: Thêm mới hồ sơ phụ huynh & liên kết trẻ (Quan hệ 1 PH - N Trẻ)
│   ├── UC-PH03: Cập nhật thông tin phụ huynh
│   ├── UC-PH04: Hủy liên kết phụ huynh - trẻ
│   └── UC-PH05: Phụ huynh xem thông tin, hồ sơ và kết quả học của con
├── Phân hệ 4: Quản lý Thực đơn
│   ├── UC-TD01: Xem danh sách thực đơn tuần / ngày
│   ├── UC-TD02: Lập thực đơn dinh dưỡng mới ──<<include>>──> UC-TD04: Quản lý món ăn
│   ├── UC-TD03: Cập nhật / Chỉnh sửa thực đơn tuần
│   ├── UC-TD04: Quản lý danh mục món ăn & thành phần dinh dưỡng
│   └── UC-TD05: Phụ huynh xem thực đơn dinh dưỡng của con
└── Phân hệ 5: Quản lý Học phí và Thanh toán
    ├── UC-HP01: Lập bảng tính học phí & tiền ăn tháng ──<<include>>──> UC-HP02: Ghi nhận ngày nghỉ
    ├── UC-HP02: Ghi nhận ngày nghỉ của trẻ để trừ tiền ăn
    ├── UC-HP03: Phát hành thông báo học phí / phiếu thu tháng
    ├── UC-HP04: Phụ huynh xem chi tiết các khoản phải trả
    ├── UC-HP05: Thanh toán học phí bằng mã QR VietQR động ──<<extend>>──> UC-HP04
    └── UC-HP06: Xác nhận & Cập nhật trạng thái thanh toán tự động"""
    add_code_block(doc, uc_ascii)

    # ----------------------------------------------------
    # MỤC 2: VIẾT ĐẶC TẢ CHI TIẾT TỪNG CHỨC NĂNG (THEO MẪU BẢNG 1)
    # ----------------------------------------------------
    doc.add_page_break()
    add_header(doc, "2. Viết đặc tả Use Case chi tiết cho từng chức năng", level=3)
    add_p(doc, "Dưới đây là các bảng đặc tả Use Case chi tiết cho các chức năng trọng tâm theo đúng biểu mẫu chuẩn của học phần (gồm Use Case ID, Tên Use Case, Tác nhân, Mô tả chức năng, Điều kiện tiên quyết, Yêu cầu, Kịch bản chính, Kịch bản phụ):")

    # Bảng 1: UC-TE02: Thêm mới hồ sơ trẻ em
    add_usecase_table(
        doc,
        table_num=1,
        title="Thêm mới hồ sơ trẻ em",
        uc_id="UC-TE02",
        uc_name="Thêm mới hồ sơ trẻ em",
        actors="Quản lý (Ban giám hiệu, Cán bộ tuyển sinh/giáo vụ)",
        desc="Cho phép người quản lý nhập thông tin tiếp nhận trẻ mới vào trường, thiết lập hồ sơ sức khỏe ban đầu, phân lớp học và liên kết với tài khoản phụ huynh.",
        preconditions="• Người quản lý đã đăng nhập thành công vào hệ thống với quyền hạn hợp lệ.\n• Danh mục khối lớp và danh sách lớp học của năm học hiện tại đã được cấu hình sẵn trong cơ sở dữ liệu.",
        requirements="• Hệ thống kiểm tra tính hợp lệ của các trường dữ liệu bắt buộc (Họ tên, Ngày sinh, Giới tính, Lớp tiếp nhận, Thông tin phụ huynh).\n• Không trùng lặp mã định danh/mã học sinh.\n• Dữ liệu trẻ mới được lưu trữ an toàn vào cơ sở dữ liệu và chuyển trạng thái sang 'Đang học'.",
        main_flow="1. Người quản lý truy cập chức năng 'Quản lý trẻ em' trên thanh điều hướng.\n"
                  "2. Hệ thống hiển thị giao diện danh sách trẻ em hiện có.\n"
                  "3. Người quản lý nhấn nút 'Thêm mới trẻ'.\n"
                  "4. Hệ thống hiển thị form nhập thông tin hồ sơ trẻ em (Họ tên, Ngày sinh, Giới tính, Quê quán/Địa chỉ, Tình trạng sức khỏe, Dị ứng, Chiều cao, Cân nặng, Lớp học tiếp nhận, Thông tin phụ huynh liên kết).\n"
                  "5. Người quản lý nhập đầy đủ các thông tin của trẻ và chọn lớp học dự kiến phân bổ.\n"
                  "6. Người quản lý tìm kiếm phụ huynh đã có sẵn trong hệ thống hoặc chọn 'Tạo mới hồ sơ phụ huynh' để liên kết.\n"
                  "7. Người quản lý nhấn nút 'Lưu hồ sơ'.\n"
                  "8. Hệ thống tiến hành kiểm tra tính hợp lệ của dữ liệu (ngày sinh hợp lệ độ tuổi mầm non từ 1-5 tuổi, thông tin liên lạc đầy đủ).\n"
                  "9. Hệ thống tự động sinh Mã học sinh duy nhất (VD: TE2026001) và lưu thông tin vào cơ sở dữ liệu.\n"
                  "10. Hệ thống hiển thị thông báo 'Thêm mới hồ sơ trẻ thành công' và chuyển về trang chi tiết hồ sơ của trẻ.",
        sub_flow="8.1. Thông tin nhập bị thiếu hoặc không hợp lệ (để trống trường bắt buộc, ngày sinh không đúng độ tuổi):\n"
                 "    8.1.1. Hệ thống giữ nguyên thông tin đã nhập trên form, làm nổi bật các trường sai sót bằng màu đỏ và hiển thị thông báo lỗi cụ thể (ví dụ: 'Ngày sinh không hợp lệ').\n"
                 "    8.1.2. Người quản lý sửa lại thông tin và nhấn 'Lưu hồ sơ' để tiếp tục.\n"
                 "8.2. Lớp học được chọn đã đủ sĩ số tối đa:\n"
                 "    8.2.1. Hệ thống hiển thị cảnh báo: 'Lớp học đã đạt sĩ số tối đa (30 trẻ/lớp). Bạn có muốn chọn lớp khác hoặc tiếp tục phân bổ đặc cách?'.\n"
                 "    8.2.2. Người quản lý chọn lớp khác phù hợp hoặc xác nhận đặc cách.\n"
                 "8.3. Người quản lý nhấn nút 'Hủy':\n"
                 "    8.3.1. Hệ thống hiển thị hộp thoại xác nhận hủy thao tác.\n"
                 "    8.3.2. Nếu xác nhận, hệ thống xóa dữ liệu trên form và quay lại màn hình danh sách trẻ."
    )

    # Bảng 2: UC-TE03: Chỉnh sửa hồ sơ trẻ em
    add_usecase_table(
        doc,
        table_num=2,
        title="Chỉnh sửa hồ sơ trẻ em",
        uc_id="UC-TE03",
        uc_name="Chỉnh sửa hồ sơ trẻ em",
        actors="Quản lý, Giáo viên chủ nhiệm",
        desc="Cho phép cập nhật các thông tin thay đổi trong quá trình học tập của trẻ (thông tin sức khỏe định kỳ, thay đổi người giám hộ, chuyển lớp hoặc cập nhật trạng thái học).",
        preconditions="• Người dùng đã đăng nhập hệ thống với quyền Quản lý hoặc Giáo viên được phân công.\n• Hồ sơ của trẻ đã tồn tại trên hệ thống.",
        requirements="• Hệ thống chỉ cho phép sửa đổi các thông tin hợp lệ.\n• Ghi nhận nhật ký lịch sử cập nhật (người sửa, thời gian sửa) để phục vụ đối soát.",
        main_flow="1. Người dùng tìm kiếm và chọn trẻ cần cập nhật trong 'Danh sách trẻ em'.\n"
                  "2. Hệ thống hiển thị chi tiết hồ sơ cá nhân hiện tại của trẻ.\n"
                  "3. Người dùng nhấn nút 'Chỉnh sửa'.\n"
                  "4. Hệ thống mở form chỉnh sửa cho phép cập nhật các trường dữ liệu (sức khỏe, lớp, liên hệ phụ huynh, trạng thái).\n"
                  "5. Người dùng thực hiện sửa đổi các thông tin cần thiết.\n"
                  "6. Người dùng nhấn nút 'Cập nhật'.\n"
                  "7. Hệ thống kiểm tra dữ liệu chỉnh sửa.\n"
                  "8. Hệ thống ghi nhận thay đổi vào cơ sở dữ liệu và lưu lịch sử chỉnh sửa.\n"
                  "9. Hệ thống hiển thị thông báo 'Cập nhật hồ sơ thành công'.",
        sub_flow="7.1. Dữ liệu chỉnh sửa không hợp lệ:\n"
                 "    7.1.1. Hệ thống báo lỗi và yêu cầu nhập lại trường không hợp lệ.\n"
                 "7.2. Người dùng nhấn nút 'Hủy bỏ':\n"
                 "    7.2.1. Hệ thống không lưu thay đổi và khôi phục lại dữ liệu ban đầu."
    )

    # Bảng 3: UC-GV05: Phân công giáo viên vào lớp học
    add_usecase_table(
        doc,
        table_num=3,
        title="Phân công lớp giảng dạy",
        uc_id="UC-GV05",
        uc_name="Phân công lớp giảng dạy",
        actors="Quản lý (Ban giám hiệu)",
        desc="Cho phép người quản lý phân công giáo viên làm giáo viên chủ nhiệm hoặc giáo viên phụ trách dinh dưỡng/bán trú cho một hoặc nhiều lớp học trong năm học.",
        preconditions="• Người quản lý đã đăng nhập với tài khoản có quyền phân công nhân sự.\n• Hồ sơ giáo viên và danh sách lớp học của năm học đã được kích hoạt.",
        requirements="• Đảm bảo mỗi lớp học có ít nhất 1 giáo viên chủ nhiệm.\n• Một giáo viên không bị trùng lịch chủ nhiệm hai lớp khác nhau trong cùng một khung thời gian.",
        main_flow="1. Người quản lý truy cập mục 'Quản lý giáo viên' -> chọn tab 'Phân công lớp'.\n"
                  "2. Hệ thống hiển thị bảng sơ đồ phân công hiện tại theo từng khối lớp (Mầm, Chồi, Lá).\n"
                  "3. Người quản lý chọn lớp học cần phân công (ví dụ: 'Lớp Lá 1').\n"
                  "4. Hệ thống hiển thị thông tin lớp học, danh sách trẻ hiện tại và danh sách giáo viên phụ trách hiện tại.\n"
                  "5. Người quản lý nhấn nút 'Thêm giáo viên phụ trách' và chọn giáo viên từ danh sách giáo viên đang làm việc.\n"
                  "6. Người quản lý chọn vai trò phân công (Chủ nhiệm chính / Phụ tá / Giáo viên năng khiếu).\n"
                  "7. Người quản lý nhấn 'Xác nhận phân công'.\n"
                  "8. Hệ thống kiểm tra ràng buộc phân công (giáo viên chưa chủ nhiệm lớp khác).\n"
                  "9. Hệ thống lưu liên kết Giáo viên - Lớp học vào cơ sở dữ liệu và cập nhật quyền quản lý danh sách trẻ của lớp cho giáo viên đó.\n"
                  "10. Hệ thống hiển thị thông báo: 'Phân công giáo viên thành công'.",
        sub_flow="8.1. Giáo viên đã được phân công chủ nhiệm một lớp khác trong cùng niên khóa:\n"
                 "    8.1.1. Hệ thống hiển thị cảnh báo: 'Giáo viên này hiện đang chủ nhiệm Lớp Chồi 2. Bạn có muốn chuyển giao phân công sang lớp mới?'.\n"
                 "    8.1.2. Người quản lý chọn 'Hủy' để chọn giáo viên khác, hoặc 'Xác nhận chuyển giao' để cập nhật lại phân công.\n"
                 "8.2. Lỗi mất kết nối mạng hoặc lỗi CSDL:\n"
                 "    8.2.1. Hệ thống rollback giao dịch và thông báo: 'Lỗi lưu dữ liệu phân công, vui lòng thử lại'."
    )

    # Bảng 4: UC-PH02: Thêm mới hồ sơ phụ huynh và liên kết với trẻ
    add_usecase_table(
        doc,
        table_num=4,
        title="Thêm mới & liên kết phụ huynh - trẻ",
        uc_id="UC-PH02",
        uc_name="Thêm mới & liên kết phụ huynh - trẻ",
        actors="Quản lý, Cán bộ tiếp nhận",
        desc="Tạo hồ sơ phụ huynh mới (hoặc cập nhật phụ huynh cũ) và thiết lập mối quan hệ 1 Phụ huynh liên kết với N Trẻ (quản lý nhiều con cùng lúc).",
        preconditions="• Người quản lý đã đăng nhập vào hệ thống.\n• Trẻ em cần liên kết đã có hồ sơ trong hệ thống hoặc đang trong quy trình tiếp nhận hồ sơ.",
        requirements="• Số điện thoại của phụ huynh phải là duy nhất để dùng làm tài khoản đăng nhập/nhận thông báo.\n• Thiết lập mối quan hệ chính xác: Cha, Mẹ, Ông, Bà, Người giám hộ hợp pháp.",
        main_flow="1. Người quản lý truy cập 'Quản lý phụ huynh' -> chọn 'Thêm phụ huynh'.\n"
                  "2. Hệ thống hiển thị biểu mẫu nhập thông tin phụ huynh (Họ tên, Số điện thoại, Email, Số CCCD, Địa chỉ thường trú, Nơi làm việc).\n"
                  "3. Người quản lý nhập thông tin chi tiết của phụ huynh.\n"
                  "4. Người quản lý chuyển sang phần 'Liên kết trẻ em' và nhấn 'Chọn trẻ em'.\n"
                  "5. Hệ thống hiển thị danh sách tìm kiếm trẻ theo tên hoặc mã trẻ.\n"
                  "6. Người quản lý chọn 1 hoặc nhiều trẻ (ví dụ: Bé B - Lớp Lá 1 và Bé C - Lớp Chồi 2) và chọn mối quan hệ tương ứng cho từng trẻ.\n"
                  "7. Người quản lý nhấn 'Lưu thông tin'.\n"
                  "8. Hệ thống kiểm tra số điện thoại không bị trùng lặp với phụ huynh khác.\n"
                  "9. Hệ thống lưu hồ sơ phụ huynh và tạo các bản ghi liên kết [Phụ huynh - Trẻ em] trong cơ sở dữ liệu.\n"
                  "10. Hệ thống hiển thị thông báo 'Tạo và liên kết phụ huynh thành công'.",
        sub_flow="8.1. Số điện thoại phụ huynh đã tồn tại trong hệ thống:\n"
                 "    8.1.1. Hệ thống thông báo: 'Số điện thoại này đã được đăng ký cho phụ huynh [Tên PH]. Bạn có muốn liên kết thêm trẻ mới vào hồ sơ phụ huynh đã có?'.\n"
                 "    8.1.2. Người quản lý chọn 'Đồng ý' -> Hệ thống tự động bổ sung trẻ vào danh sách con của phụ huynh đó.\n"
                 "8.2. Người quản lý nhập email sai định dạng:\n"
                 "    8.2.1. Hệ thống báo lỗi trường email và yêu cầu chỉnh sửa."
    )

    # Bảng 5: UC-PH05: Phụ huynh xem thông tin và quá trình học của con
    add_usecase_table(
        doc,
        table_num=5,
        title="Xem hồ sơ & thông tin của con",
        uc_id="UC-PH05",
        uc_name="Xem hồ sơ & thông tin của con",
        actors="Phụ huynh",
        desc="Cho phép phụ huynh sử dụng ứng dụng di động/web để theo dõi hồ sơ của con, thông tin lớp học, tình hình sức khỏe, lịch sử điểm danh và thực đơn hàng ngày.",
        preconditions="• Phụ huynh đã đăng nhập thành công vào ứng dụng phụ huynh bằng tài khoản được cấp.",
        requirements="• Phụ huynh chỉ xem được dữ liệu của đúng các trẻ mà mình có quyền liên kết giám hộ.\n• Hỗ trợ chuyển đổi nhanh chóng giữa các con nếu phụ huynh có nhiều con đang theo học.",
        main_flow="1. Phụ huynh đăng nhập vào ứng dụng di động/cổng thông tin phụ huynh.\n"
                  "2. Hệ thống tải thông tin tài khoản và kiểm tra danh sách trẻ liên kết.\n"
                  "3. Nếu phụ huynh có nhiều con, hệ thống hiển thị danh sách thẻ con để lựa chọn (ví dụ: Bé Nguyễn Minh B và Bé Nguyễn Minh C).\n"
                  "4. Phụ huynh nhấn chọn trẻ cần xem.\n"
                  "5. Hệ thống hiển thị bảng tin tổng quan của trẻ: Lớp học hiện tại, giáo viên chủ nhiệm, trạng thái điểm danh hôm nay, chỉ số sức khỏe gần nhất.\n"
                  "6. Phụ huynh chọn các mục chi tiết: 'Xem hồ sơ sức khỏe', 'Xem thực đơn tuần', 'Xem học phí & đóng tiền'.\n"
                  "7. Hệ thống hiển thị dữ liệu chi tiết tương ứng.",
        sub_flow="3.1. Phụ huynh chỉ có 1 con học tại trường:\n"
                 "    3.1.1. Hệ thống tự động chuyển thẳng vào màn hình tổng quan của trẻ mà không cần bước lựa chọn thẻ.\n"
                 "7.1. Phụ huynh muốn gửi tin nhắn/phản hồi cho giáo viên:\n"
                 "    7.1.1. Phụ huynh nhấn nút 'Nhắn tin cho cô giáo' -> Chuyển sang màn hình liên lạc."
    )

    # Bảng 6: UC-TD02: Lập thực đơn tuần mới
    add_usecase_table(
        doc,
        table_num=6,
        title="Lập thực đơn tuần mới",
        uc_id="UC-TD02",
        uc_name="Lập thực đơn tuần mới",
        actors="Quản lý, Cán bộ phụ trách dinh dưỡng",
        desc="Thiết lập lịch thực đơn chi tiết cho từng ngày trong tuần (từ Thứ 2 đến Thứ 6), phân chia cụ thể các bữa sáng, trưa, xế, định lượng món ăn và tính toán cân bằng dinh dưỡng.",
        preconditions="• Người dùng đã đăng nhập với tài khoản có quyền quản trị thực đơn.\n• Danh mục món ăn và thành phần dinh dưỡng đã có trong cơ sở dữ liệu.",
        requirements="• Mỗi ngày trong tuần phải có đủ 3 bữa: Bữa sáng, Bữa trưa, Bữa phụ/xế.\n• Chi phí nguyên liệu thực đơn không vượt quá định mức tiền ăn quy định/ngày.",
        main_flow="1. Người dùng vào mục 'Quản lý thực đơn' -> chọn 'Lập thực đơn tuần mới'.\n"
                  "2. Người dùng chọn tuần áp dụng (ví dụ: 'Tuần 40: 28/09/2026 - 02/10/2026') và khối lớp áp dụng.\n"
                  "3. Hệ thống hiển thị bảng ma trận thực đơn tuần (gồm các cột Thứ 2 đến Thứ 6 và các hàng Bữa Sáng, Bữa Trưa, Bữa Xế).\n"
                  "4. Với mỗi bữa ăn trong ngày, người dùng nhấn nút '+' để chọn món ăn từ danh mục (ví dụ: Trưa Thứ 2 chọn: Cơm, Thịt kho trứng, Canh bí, Rau cải).\n"
                  "5. Hệ thống hiển thị thành phần dinh dưỡng tương ứng (Calo, Protein, Lipid) và ước tính chi phí ngày.\n"
                  "6. Người dùng hoàn tất việc điền món ăn cho cả tuần.\n"
                  "7. Người dùng nhấn 'Lưu và Xuất bản thực đơn'.\n"
                  "8. Hệ thống kiểm tra tính đầy đủ của các bữa ăn trong tuần.\n"
                  "9. Hệ thống lưu thực đơn vào cơ sở dữ liệu và kích hoạt trạng thái 'Đã công bố' để phụ huynh có thể tra cứu.\n"
                  "10. Hệ thống hiển thị thông báo: 'Lập thực đơn tuần thành công'.",
        sub_flow="8.1. Một số bữa ăn trong tuần bị bỏ trống:\n"
                 "    8.1.1. Hệ thống cảnh báo: 'Chưa hoàn tất các bữa ăn cho Thứ 4. Bạn có muốn lưu bản nháp?'.\n"
                 "    8.1.2. Nếu người dùng chọn 'Lưu bản nháp', hệ thống lưu ở trạng thái nháp (chưa hiển thị cho phụ huynh).\n"
                 "7.1. Người dùng muốn sao chép từ thực đơn của tuần trước:\n"
                 "    7.1.1. Người dùng nhấn 'Sao chép thực đơn tuần trước' -> Hệ thống tự động đổ dữ liệu tuần trước sang form mới để người dùng chỉnh sửa nhanh."
    )

    # Bảng 7: UC-TD05: Phụ huynh xem thực đơn của con
    add_usecase_table(
        doc,
        table_num=7,
        title="Phụ huynh xem thực đơn của con",
        uc_id="UC-TD05",
        uc_name="Phụ huynh xem thực đơn của con",
        actors="Phụ huynh",
        desc="Cho phép phụ huynh tra cứu lịch ăn uống chi tiết trong ngày và trong tuần của con để nắm bắt chế độ dinh dưỡng và theo dõi dị ứng.",
        preconditions="• Phụ huynh đã đăng nhập vào hệ thống.\n• Thực đơn của tuần đã được nhà trường phê duyệt và công bố.",
        requirements="• Hiển thị trực quan món ăn theo từng bữa kèm hình ảnh minh họa (nếu có).\n• Cảnh báo nổi bật nếu trong thực đơn có món chứa thành phần mà con bị dị ứng (dựa trên hồ sơ sức khỏe).",
        main_flow="1. Phụ huynh chọn mục 'Thực đơn của bé' trên giao diện ứng dụng.\n"
                  "2. Hệ thống mặc định tải thực đơn của ngày hiện tại (ví dụ: Thứ 2, 28/09/2026).\n"
                  "3. Hệ thống hiển thị chi tiết: Bữa sáng (Sữa, Bánh mì), Bữa trưa (Cơm, Thịt kho, Canh bí), Bữa xế (Chuối tiêu, Sữa chua).\n"
                  "4. Hệ thống tự động so khớp thành phần món ăn với danh sách dị ứng trong hồ sơ của trẻ. Nếu phát hiện món gây dị ứng, hệ thống hiển thị icon cảnh báo màu đỏ.\n"
                  "5. Phụ huynh có thể lướt sang các ngày khác trong tuần hoặc chọn 'Xem toàn bộ tuần'.\n"
                  "6. Phụ huynh có thể để lại ghi chú dặn dò bữa ăn (ví dụ: 'Hôm nay bé đang ho, nhờ cô cho uống sữa ấm').",
        sub_flow="2.1. Nhà trường chưa công bố thực đơn cho tuần được chọn:\n"
                 "    2.1.1. Hệ thống hiển thị thông báo: 'Thực đơn tuần này đang được cập nhật, vui lòng quay lại sau'.\n"
                 "6.1. Phụ huynh nhấn gửi dặn dò ăn uống:\n"
                 "    6.1.1. Hệ thống gửi thông báo trực tiếp đến ứng dụng của giáo viên chủ nhiệm lớp."
    )

    # Bảng 8: UC-HP01: Lập bảng tính học phí và tiền ăn tháng
    add_usecase_table(
        doc,
        table_num=8,
        title="Lập bảng tính học phí & tiền ăn",
        uc_id="UC-HP01",
        uc_name="Lập bảng tính học phí & tiền ăn",
        actors="Kế toán, Ban giám hiệu",
        desc="Hệ thống tự động tính toán tổng học phí hàng tháng cho từng trẻ theo công thức: Tổng tiền = Học phí cơ bản + Tiền ăn (đã khấu trừ ngày nghỉ) + Phí dịch vụ khác - Giảm trừ.",
        preconditions="• Người dùng có quyền kế toán/quản lý tài chính.\n• Dữ liệu điểm danh và báo nghỉ của tháng trước đã được giáo viên chốt hoàn tất.\n• Bảng biểu phí cơ bản và đơn giá tiền ăn/ngày đã được thiết lập.",
        requirements="• Tính toán hoàn toàn tự động, chính xác theo công thức quy định.\n• Tiền ăn phải trừ đúng số ngày trẻ có đơn xin nghỉ phép hợp lệ được duyệt.",
        main_flow="1. Kế toán truy cập 'Quản lý học phí và thanh toán' -> chọn 'Lập bảng tính học phí tháng'.\n"
                  "2. Kế toán chọn Tháng/Năm tính học phí (ví dụ: Tháng 10/2026) và chọn Khối/Lớp (hoặc toàn trường).\n"
                  "3. Kế toán nhấn 'Chạy tính toán tự động'.\n"
                  "4. Hệ thống truy vấn danh sách trẻ đang học và lấy các thông số:\n"
                  "   - Học phí cơ bản theo lớp (ví dụ: 1.500.000đ).\n"
                  "   - Tiền dịch vụ/bán trú khác (ví dụ: 100.000đ).\n"
                  "   - Số ngày ăn tiêu chuẩn trong tháng (ví dụ: 22 ngày).\n"
                  "   - Truy vấn CSDL điểm danh: Lấy tổng số ngày nghỉ hợp lệ có báo trước của từng trẻ (ví dụ: trẻ nghỉ 2 ngày).\n"
                  "   - Tính số ngày ăn thực tế = 22 - 2 = 20 ngày.\n"
                  "   - Tính tiền ăn = 20 ngày × 30.000đ/ngày = 600.000đ.\n"
                  "   - Tính tổng tiền = 1.500.000 + 600.000 + 100.000 - 0 = 2.200.000đ.\n"
                  "5. Hệ thống hiển thị bảng kết quả tính toán chi tiết cho từng trẻ để kế toán kiểm tra đối soát.\n"
                  "6. Kế toán có thể điều chỉnh khoản giảm trừ hoặc ghi chú cho từng trường hợp đặc biệt.\n"
                  "7. Kế toán nhấn 'Lưu bảng tính và Tạo phiếu thu'.\n"
                  "8. Hệ thống lưu các bản ghi hóa đơn học phí với trạng thái 'Chưa thanh toán' và sinh mã hóa đơn duy nhất (ví dụ: HD202610-0012).",
        sub_flow="4.1. Lớp học chưa được giáo viên chốt dữ liệu điểm danh tháng:\n"
                 "    4.1.1. Hệ thống hiển thị cảnh báo: 'Lớp Chồi 1 chưa chốt điểm danh tháng. Số ngày ăn có thể chưa chính xác. Bạn có muốn tiếp tục?'.\n"
                 "    4.1.2. Kế toán có thể gửi thông báo nhắc nhở giáo viên chốt điểm danh trước khi tiếp tục.\n"
                 "6.1. Kế toán phát hiện sai sót dữ liệu:\n"
                 "    6.1.1. Kế toán chỉnh sửa trực tiếp số ngày trừ ăn hoặc số tiền miễn giảm trên dòng của trẻ đó và hệ thống tự động tính lại tổng tiền tức thì."
    )

    # Bảng 9: UC-HP02: Ghi nhận ngày nghỉ trẻ để trừ tiền ăn
    add_usecase_table(
        doc,
        table_num=9,
        title="Ghi nhận ngày nghỉ để trừ tiền ăn",
        uc_id="UC-HP02",
        uc_name="Ghi nhận ngày nghỉ để trừ tiền ăn",
        actors="Giáo viên chủ nhiệm, Phụ huynh (nộp đơn xin nghỉ)",
        desc="Ghi nhận và phê duyệt các ngày nghỉ phép có báo trước của trẻ, làm căn cứ khấu trừ tiền ăn hợp lệ khi tính học phí cuối tháng.",
        preconditions="• Phụ huynh nộp đơn xin nghỉ phép qua ứng dụng hoặc báo trực tiếp cho giáo viên.\n• Thời gian báo nghỉ phải trước giờ quy định chốt suất ăn (trước 7h30 sáng hàng ngày).",
        requirements="• Phân biệt rõ ràng giữa 'Nghỉ có phép báo trước' (được hoàn lại tiền ăn) và 'Nghỉ không phép / báo muộn' (không hoàn lại tiền ăn theo nội quy).",
        main_flow="1. Phụ huynh truy cập ứng dụng -> chọn 'Xin nghỉ phép cho con'.\n"
                  "2. Phụ huynh chọn ngày nghỉ (từ ngày - đến ngày), lý do nghỉ (ốm đau, việc gia đình) và gửi đơn.\n"
                  "3. Hệ thống kiểm tra thời gian gửi (nếu gửi trước 7h30 sáng thì đánh dấu 'Hợp lệ để hoàn tiền ăn').\n"
                  "4. Giáo viên chủ nhiệm nhận thông báo và duyệt đơn xin nghỉ trên ứng dụng quản trị lớp.\n"
                  "5. Hệ thống tự động ghi nhận vào sổ điểm danh điện tử với trạng thái 'Nghỉ có phép - Trừ tiền ăn'.\n"
                  "6. Bản ghi điểm danh này được lưu trữ để module UC-HP01 tự động nạp khi tính học phí.",
        sub_flow="3.1. Phụ huynh gửi đơn sau 7h30 sáng của ngày nghỉ:\n"
                 "    3.1.1. Hệ thống hiển thị lưu ý: 'Đơn nộp sau 7h30 sáng, suất ăn ngày hôm nay đã được chuẩn bị nên sẽ không được trừ tiền ăn ngày này theo quy định'.\n"
                 "4.1. Giáo viên từ chối đơn:\n"
                 "    4.1.1. Giáo viên nhập lý do từ chối -> Hệ thống gửi phản hồi cho phụ huynh."
    )

    # Bảng 10: UC-HP05: Thanh toán học phí bằng mã QR VietQR động
    add_usecase_table(
        doc,
        table_num=10,
        title="Thanh toán học phí qua mã VietQR",
        uc_id="UC-HP05",
        uc_name="Thanh toán học phí qua mã VietQR",
        actors="Phụ huynh, Hệ thống Ngân hàng / Cổng thanh toán (VietQR)",
        desc="Điểm nhấn kỹ thuật: Phụ huynh xem bảng kê học phí, nhấn thanh toán để sinh mã VietQR động có sẵn số tiền và nội dung hóa đơn, chuyển khoản qua App ngân hàng và hệ thống tự động gạch nợ tức thì.",
        preconditions="• Hóa đơn học phí tháng đã được nhà trường phát hành ở trạng thái 'Chưa thanh toán'.\n• Phụ huynh cài đặt app ngân hàng bất kỳ có hỗ trợ quét mã QR chuẩn Napas247 / VietQR.",
        requirements="• Mã VietQR sinh ra phải chuẩn EMVCo, chứa chính xác: Số tài khoản trường, Ngân hàng thụ hưởng, Số tiền cần nộp, Nội dung chuyển khoản chứa Mã hóa đơn duy nhất.\n• Cập nhật trạng thái 'Đã thanh toán' ngay khi nhận được tín hiệu giao dịch thành công (Webhook/IPN).",
        main_flow="1. Phụ huynh đăng nhập ứng dụng -> chọn mục 'Học phí & Thanh toán'.\n"
                  "2. Hệ thống hiển thị hóa đơn học phí tháng hiện tại (ví dụ: Tổng tiền 2.200.000 VNĐ kèm bảng phân tích chi tiết: Học phí cơ bản, Tiền ăn, Ngày nghỉ trừ tiền, Phí dịch vụ).\n"
                  "3. Phụ huynh kiểm tra chi tiết và nhấn nút 'Thanh toán trực tuyến'.\n"
                  "4. Hệ thống gọi dịch vụ sinh mã QR động (VietQR Generator Service) truyền vào Mã hóa đơn, Số tiền chính xác (2.200.000) và Nội dung chuyển tiền duy nhất (ví dụ: 'HP TE2026001 HD0926').\n"
                  "5. Hệ thống hiển thị mã VietQR trực quan trên màn hình kèm đồng hồ đếm ngược hiệu lực thanh toán (15 phút) và nút 'Tải ảnh QR' hoặc 'Mở App ngân hàng'.\n"
                  "6. Phụ huynh mở ứng dụng ngân hàng trên điện thoại, chọn tính năng quét QR và quét mã hiển thị.\n"
                  "7. Ứng dụng ngân hàng tự động điền đúng Số tài khoản nhận của trường, Tên người thụ hưởng, Số tiền 2.200.000đ và Nội dung chuyển khoản mà người dùng không cần gõ tay.\n"
                  "8. Phụ huynh xác thực bảo mật (vân tay / FaceID / OTP) và hoàn tất chuyển khoản trên App ngân hàng.\n"
                  "9. Cổng thanh toán / Ngân hàng xử lý giao dịch thành công và gửi thông báo Webhook (IPN Callback) về máy chủ hệ thống trường mầm non.\n"
                  "10. Hệ thống trường nhận dữ liệu Webhook, giải mã và đối soát Mã hóa đơn cùng Số tiền thực nhận.\n"
                  "11. Khi dữ liệu trùng khớp 100%, hệ thống tự động cập nhật trạng thái hóa đơn thành 'Đã thanh toán', lưu mã giao dịch ngân hàng và gửi thông báo thành công đến màn hình phụ huynh.\n"
                  "12. Màn hình của phụ huynh tự động đổi sang trạng thái 'Thanh toán thành công' kèm biên lai thu tiền điện tử.",
        sub_flow="5.1. Phụ huynh để quá 15 phút chưa quét mã QR (Hết hạn mã QR):\n"
                 "    5.1.1. Hệ thống báo: 'Mã QR đã hết hiệu lực để đảm bảo an toàn giao dịch. Vui lòng bấm để tạo lại mã mới'.\n"
                 "    5.1.2. Phụ huynh nhấn 'Làm mới mã QR' -> Hệ thống sinh mã mới.\n"
                 "10.1. Phụ huynh chuyển sai số tiền hoặc sai nội dung chuyển khoản:\n"
                 "    10.1.1. Hệ thống đối soát phát hiện sai lệch số tiền/nội dung -> Ghi nhận vào mục 'Giao dịch chờ đối soát thủ công' và gửi thông báo cho kế toán xử lý.\n"
                 "10.2. Phụ huynh nhấn nút 'Hủy thanh toán':\n"
                 "    10.2.1. Hệ thống đóng màn hình QR và giữ nguyên trạng thái hóa đơn 'Chưa thanh toán'."
    )

    # ----------------------------------------------------
    # MỤC 3: SƠ ĐỒ HOẠT ĐỘNG (ACTIVITY DIAGRAMS)
    # ----------------------------------------------------
    doc.add_page_break()
    add_header(doc, "3. Activity Diagram (Sơ đồ hoạt động) từng chức năng", level=3)
    add_p(doc, "Mô hình hóa luồng xử lý nghiệp vụ chi tiết của từng chức năng bằng Activity Diagram, thể hiện đầy đủ điểm bắt đầu (Start), các hành động (Action/Task), rẽ nhánh điều kiện (Decision node), luồng song song/đồng bộ (Fork/Join) và điểm kết thúc (End).")

    # Activity 1
    add_header(doc, "3.1. Activity Diagram: Thêm mới hồ sơ trẻ em và phân lớp (UC-TE02)", level=3)
    add_p(doc, "Sơ đồ mô tả luồng kiểm tra thông tin, ràng buộc sĩ số lớp và liên kết phụ huynh khi tiếp nhận trẻ mới:")
    act1_code = """@startuml Activity_ThemTreEm
title Sơ đồ hoạt động - Thêm mới hồ sơ trẻ em & Phân lớp

start
:Quản lý nhấn "Thêm mới trẻ em";
:Hệ thống hiển thị Form nhập thông tin trẻ;
repeat
  :Quản lý nhập họ tên, ngày sinh, giới tính, sức khỏe, lớp học;
  :Quản lý chọn hoặc nhập thông tin phụ huynh liên kết;
  :Nhấn "Lưu hồ sơ";
  :Hệ thống kiểm tra tính hợp lệ của dữ liệu;
backward:Hiển thị lỗi và yêu cầu sửa dữ liệu;
repeat while (Dữ liệu hợp lệ?) is (Không)
->Có;

if (Lớp học được chọn đã đủ sĩ số tối đa?) then (Đúng - Quá sĩ số)
  :Hiển thị cảnh báo lớp đã đầy;
  if (Quản lý chọn đặc cách nhận thêm?) then (Không)
    :Chọn lớp học khác còn chỗ;
  else (Đồng ý đặc cách)
    :Đánh dấu ghi chú tiếp nhận đặc cách;
  endif
else (Còn chỗ)
endif

:Hệ thống sinh tự động Mã học sinh duy nhất;
:Lưu hồ sơ trẻ vào CSDL;
:Tạo liên kết giữa Trẻ em và Phụ huynh;
:Cập nhật sĩ số lớp học;
:Hiển thị thông báo "Thêm trẻ thành công";
stop
@enduml"""
    add_code_block(doc, act1_code, caption="Mã nguồn PlantUML Activity Diagram: Thêm mới trẻ em (UC-TE02)")

    # Activity 2
    add_header(doc, "3.2. Activity Diagram: Phân công giáo viên phụ trách lớp học (UC-GV05)", level=3)
    add_p(doc, "Sơ đồ thể hiện quy trình phân công nhiệm vụ giáo viên vào lớp học và kiểm tra xung đột lịch giảng dạy:")
    act2_code = """@startuml Activity_PhanCongGiaoVien
title Sơ đồ hoạt động - Phân công giáo viên vào lớp học

start
:Quản lý mở giao diện Phân công lớp;
:Hệ thống hiển thị danh sách lớp và giáo viên hiện tại;
:Quản lý chọn Lớp học cần phân công;
:Quản lý chọn Giáo viên và vai trò (Chủ nhiệm / Bán trú / Năng khiếu);
:Nhấn "Xác nhận phân công";

:Hệ thống kiểm tra ràng buộc phân công của giáo viên;
if (Giáo viên đã chủ nhiệm lớp khác trong năm học?) then (Có trùng)
  :Hiển thị thông báo xung đột phân công;
  if (Xác nhận chuyển đổi lớp chủ nhiệm cho giáo viên?) then (Đồng ý chuyển)
    :Hủy phân công tại lớp cũ;
  else (Hủy thao tác)
    :Giữ nguyên phân công cũ;
    stop
  endif
else (Không trùng)
endif

:Lưu phân công mới vào CSDL;
:Cập nhật quyền quản lý trẻ của lớp cho giáo viên;
:Gửi thông báo phân công nhiệm vụ đến tài khoản giáo viên;
:Hiển thị thông báo "Phân công thành công";
stop
@enduml"""
    add_code_block(doc, act2_code, caption="Mã nguồn PlantUML Activity Diagram: Phân công giáo viên (UC-GV05)")

    # Activity 3
    add_header(doc, "3.3. Activity Diagram: Lập và ban hành thực đơn dinh dưỡng tuần (UC-TD02)", level=3)
    add_p(doc, "Sơ đồ thể hiện quy trình phối hợp lập thực đơn các bữa trong ngày, kiểm tra dinh dưỡng và xuất bản cho phụ huynh:")
    act3_code = """@startuml Activity_LapThucDon
title Sơ đồ hoạt động - Lập và ban hành thực đơn tuần

start
:Cán bộ dinh dưỡng chọn tuần cần lập thực đơn;
:Hệ thống hiển thị ma trận thực đơn tuần (Thứ 2 - Thứ 6; Bữa Sáng/Trưa/Xế);
if (Có muốn sao chép từ tuần trước?) then (Có)
  :Nạp dữ liệu thực đơn tuần trước sang;
else (Không)
  :Tạo bảng thực đơn trống;
endif

repeat
  :Chọn món ăn cho từng bữa từ danh mục món;
  :Hệ thống tự động tính tổng năng lượng Calo & chi phí dự kiến;
repeat while (Đã hoàn thiện tất cả các bữa trong tuần?) is (Chưa)
->Đã xong;

:Nhấn "Lưu và Phê duyệt";
if (Kiểm tra định mức chi phí và cân đối dinh dưỡng đạt chuẩn?) then (Chưa đạt)
  :Cảnh báo định mức vượt ngân sách hoặc thiếu dinh dưỡng;
  :Chỉnh sửa lại các món ăn;
else (Đạt chuẩn)
endif

:Lưu thực đơn chính thức vào CSDL;
:Chuyển trạng thái thực đơn sang "Đã công bố";
:Kích hoạt hiển thị trên App phụ huynh;
:Hiển thị thông báo "Ban hành thực đơn thành công";
stop
@enduml"""
    add_code_block(doc, act3_code, caption="Mã nguồn PlantUML Activity Diagram: Lập thực đơn (UC-TD02)")

    # Activity 4
    add_header(doc, "3.4. Activity Diagram: Tính tiền ăn và tổng hợp phiếu thu học phí tháng (UC-HP01)", level=3)
    add_p(doc, "Sơ đồ thể hiện quy trình tính tiền tự động dựa trên số ngày ăn thực tế và khấu trừ ngày nghỉ phép:")
    act4_code = """@startuml Activity_TinhHocPhi_TienAn
title Sơ đồ hoạt động - Tính tiền ăn và lập phiếu thu học phí

start
:Kế toán chọn Tháng/Năm cần tính học phí;
:Kế toán nhấn "Bắt đầu tính toán tự động";

:Hệ thống lấy danh sách toàn bộ trẻ đang theo học;
while (Còn trẻ em trong danh sách?) is (Còn)
  :Lấy thông tin học phí cơ bản và phí dịch vụ lớp;
  :Truy vấn sổ điểm danh điện tử trong tháng của trẻ;
  :Đếm số ngày nghỉ có phép hợp lệ báo trước;
  
  :Tính số ngày ăn thực tế = Tổng ngày ăn tiêu chuẩn - Số ngày nghỉ hợp lệ;
  :Tính tiền ăn = Số ngày ăn thực tế * Đơn giá ăn/ngày;
  :Tính Tổng tiền phải trả = Học phí + Tiền ăn + Phí dịch vụ - Giảm trừ;
  :Tạo bản ghi hóa đơn chi tiết tương ứng với trẻ;
endwhile (Hết danh sách)

:Hệ thống hiển thị bảng tổng hợp học phí toàn trường/khối lớp;
:Kế toán kiểm tra và đối soát các số liệu bất thường;
if (Kế toán duyệt bảng tính?) then (Đồng ý)
  :Lưu bảng học phí chính thức vào CSDL;
  :Sinh mã hóa đơn cho từng học sinh;
  :Phát hành phiếu thu điện tử tới tài khoản phụ huynh;
  :Hiển thị thông báo "Lập học phí tháng hoàn tất";
else (Cần chỉnh sửa)
  :Điều chỉnh khoản tiền miễn giảm/đặc thù thủ công;
endif
stop
@enduml"""
    add_code_block(doc, act4_code, caption="Mã nguồn PlantUML Activity Diagram: Tính tiền ăn & học phí (UC-HP01)")

    # Activity 5
    add_header(doc, "3.5. Activity Diagram: Sinh mã QR động & Thanh toán học phí trực tuyến (UC-HP05)", level=3)
    add_p(doc, "Sơ đồ thể hiện toàn bộ chu trình thanh toán không dùng tiền mặt, sinh mã VietQR động, đối soát tức thời qua Webhook:")
    act5_code = """@startuml Activity_ThanhToan_QR
title Sơ đồ hoạt động - Thanh toán học phí bằng mã QR VietQR động

start
:Phụ huynh mở ứng dụng và xem chi tiết khoản học phí;
:Phụ huynh nhấn nút "Thanh toán trực tuyến";

:Hệ thống gọi dịch vụ sinh mã QR động (VietQR);
:Sinh mã QR chứa: Số tài khoản trường, Số tiền chính xác, Mã hóa đơn duy nhất;
:Hiển thị mã QR lên màn hình kèm bộ đếm ngược thời gian (15 phút);

:Phụ huynh mở App Ngân hàng trên điện thoại cá nhân;
:Phụ huynh chọn quét mã QR trên màn hình;
:App Ngân hàng tự động nạp chính xác thông tin chuyển khoản;
:Phụ huynh xác thực giao dịch (Vân tay / FaceID / OTP);

if (Giao dịch thành công tại ngân hàng?) then (Thành công)
  :Ngân hàng trích tiền và gửi Webhook (IPN) về máy chủ trường mầm non;
  :Hệ thống trường nhận Webhook và kiểm tra chữ ký số bảo mật;
  :Hệ thống đối soát Mã hóa đơn và Số tiền giao dịch;
  
  if (Dữ liệu khớp hoàn toàn?) then (Khớp 100%)
    :Cập nhật trạng thái hóa đơn -> "Đã thanh toán";
    :Lưu mã giao dịch ngân hàng và thời gian thanh toán;
    :Sinh biên lai thu tiền điện tử;
    :Gửi thông báo đẩy về ứng dụng của Phụ huynh: "Thanh toán thành công";
    :Màn hình phụ huynh tự động đổi sang trạng thái hoàn tất;
  else (Sai lệch số tiền/nội dung)
    :Đánh dấu giao dịch vào hàng đợi "Chờ đối soát thủ công";
    :Gửi thông báo cảnh báo cho Kế toán;
  endif
else (Thất bại / Hủy bỏ)
  :App Ngân hàng báo giao dịch không thành công;
  :Hóa đơn giữ nguyên trạng thái "Chưa thanh toán";
endif
stop
@enduml"""
    add_code_block(doc, act5_code, caption="Mã nguồn PlantUML Activity Diagram: Thanh toán QR VietQR (UC-HP05)")

    # ----------------------------------------------------
    # MỤC 4: SƠ ĐỒ TUẦN TỰ (SEQUENCE DIAGRAMS)
    # ----------------------------------------------------
    doc.add_page_break()
    add_header(doc, "4. Sequence Diagram (Sơ đồ tuần tự) từng chức năng", level=3)
    add_p(doc, "Mô hình hóa sự tương tác trao đổi thông điệp tuần tự theo thời gian giữa các thành phần kiến trúc 3 lớp chuẩn phân tích thiết kế phần mềm hướng đối tượng:")
    add_p(doc, "• Actor: Tác nhân kích hoạt tương tác nghiệp vụ.\n"
               "• Boundary / UI: Lớp giao diện hiển thị và tiếp nhận dữ liệu người dùng.\n"
               "• Control / Service: Lớp điều khiển xử lý nghiệp vụ, kiểm tra ràng buộc và thuật toán.\n"
               "• Entity / Database: Lớp thực thể dữ liệu và cơ sở dữ liệu lưu trữ bền vững.\n"
               "• External Service: Các dịch vụ bên thứ ba (Cổng thanh toán VietQR, Ngân hàng).")

    # Sequence 1
    add_header(doc, "4.1. Sequence Diagram: Thêm mới hồ sơ trẻ em (UC-TE02)", level=3)
    seq1_code = """@startuml Sequence_ThemTreEm
autonumber
actor "Quản lý" as Admin
boundary "TreEmGUI" as GUI
control "TreEmController" as Ctrl
entity "TreEmService" as Service
database "Database" as DB

Admin -> GUI: 1. Nhấn nút "Thêm mới trẻ em"
activate GUI
GUI --> Admin: 2. Hiển thị form nhập hồ sơ trẻ
deactivate GUI

Admin -> GUI: 3. Nhập thông tin trẻ, sức khỏe, lớp & phụ huynh liên kết
activate GUI
Admin -> GUI: 4. Nhấn nút "Lưu hồ sơ"
GUI -> Ctrl: 5. postCreateChild(childDTO)
activate Ctrl

Ctrl -> Service: 6. validateChildData(childDTO)
activate Service
Service -> DB: 7. checkClassCapacity(classId)
activate DB
DB --> Service: 8. Return classAvailable: true
deactivate DB

Service -> Service: 9. generateChildCode()
Service -> DB: 10. insertChild(childEntity)
activate DB
DB --> Service: 11. Return childId: 105
deactivate DB

Service -> DB: 11. insertParentChildRelation(parentId, childId)
activate DB
DB --> Service: 12. Success
deactivate DB

Service --> Ctrl: 13. Return SuccessResult(childCode)
deactivate Service

Ctrl --> GUI: 14. Trả về kết quả thành công
deactivate Ctrl
GUI --> Admin: 15. Hiển thị thông báo "Thêm trẻ thành công"
deactivate GUI
@enduml"""
    add_code_block(doc, seq1_code, caption="Mã nguồn PlantUML Sequence Diagram: Thêm mới trẻ em (UC-TE02)")

    # Sequence 2
    add_header(doc, "4.2. Sequence Diagram: Phân công giáo viên vào lớp học (UC-GV05)", level=3)
    seq2_code = """@startuml Sequence_PhanCongGiaoVien
autonumber
actor "Quản lý" as Admin
boundary "PhanCongGUI" as GUI
control "PhanCongController" as Ctrl
entity "GiaoVienService" as Service
database "Database" as DB

Admin -> GUI: 1. Chọn Lớp học và Giáo viên cần phân công
activate GUI
Admin -> GUI: 2. Nhấn nút "Xác nhận phân công"
GUI -> Ctrl: 3. assignTeacherToClass(teacherId, classId, role)
activate Ctrl

Ctrl -> Service: 4. checkTeacherAssignmentConflict(teacherId, schoolYear)
activate Service
Service -> DB: 5. queryCurrentAssignments(teacherId)
activate DB
DB --> Service: 6. Return existingAssignments: Empty
deactivate DB

Service -> DB: 7. saveTeacherClassAssignment(teacherId, classId, role)
activate DB
DB --> Service: 8. Return Success
deactivate DB

Service -> DB: 9. updateTeacherPermission(teacherId, classId)
activate DB
DB --> Service: 10. Return PermissionsUpdated
deactivate DB

Service --> Ctrl: 11. Return AssignmentSuccess
deactivate Service

Ctrl --> GUI: 12. Trả về thông báo phân công thành công
deactivate Ctrl
GUI --> Admin: 13. Cập nhật bảng sơ đồ lớp và hiển thị thông báo
deactivate GUI
@enduml"""
    add_code_block(doc, seq2_code, caption="Mã nguồn PlantUML Sequence Diagram: Phân công giáo viên (UC-GV05)")

    # Sequence 3
    add_header(doc, "4.3. Sequence Diagram: Lập và ban hành thực đơn tuần (UC-TD02)", level=3)
    seq3_code = """@startuml Sequence_LapThucDon
autonumber
actor "Cán bộ Dinh dưỡng" as Staff
boundary "ThucDonGUI" as GUI
control "ThucDonController" as Ctrl
entity "ThucDonService" as Service
database "Database" as DB

Staff -> GUI: 1. Chọn tuần cần lập thực đơn & khối lớp
activate GUI
GUI --> Staff: 2. Hiển thị ma trận các bữa ăn (Sáng, Trưa, Xế)
deactivate GUI

Staff -> GUI: 3. Chọn các món ăn cho từng ngày trong tuần
activate GUI
Staff -> GUI: 4. Nhấn "Lưu & Xuất bản thực đơn"
GUI -> Ctrl: 5. submitWeeklyMenu(menuDTO)
activate Ctrl

Ctrl -> Service: 6. validateNutritionAndBudget(menuDTO)
activate Service
Service -> DB: 7. getDishNutrientDetails(dishIds)
activate DB
DB --> Service: 8. Return dishData (Calo, Protein, Price)
deactivate DB

Service -> Service: 9. calculateDailyTotals()
Service -> DB: 10. saveWeeklyMenu(weeklyMenuEntity)
activate DB
DB --> Service: 11. Return menuId: 88
deactivate DB

Service -> DB: 12. updateMenuStatus(menuId, "PUBLISHED")
activate DB
DB --> Service: 13. Return Published
deactivate DB

Service --> Ctrl: 14. Return PublishSuccess
deactivate Service

Ctrl --> GUI: 15. Trả về trạng thái hoàn tất
deactivate Ctrl
GUI --> Staff: 16. Hiển thị thông báo "Ban hành thực đơn thành công"
deactivate GUI
@enduml"""
    add_code_block(doc, seq3_code, caption="Mã nguồn PlantUML Sequence Diagram: Lập thực đơn tuần (UC-TD02)")

    # Sequence 4
    add_header(doc, "4.4. Sequence Diagram: Tính học phí & trừ tiền ăn tháng (UC-HP01)", level=3)
    seq4_code = """@startuml Sequence_TinhHocPhi_TienAn
autonumber
actor "Kế toán" as Accountant
boundary "HocPhiGUI" as GUI
control "HocPhiController" as Ctrl
entity "TinhHocPhiService" as Service
database "Database" as DB

Accountant -> GUI: 1. Chọn Tháng/Năm (Tháng 10/2026) & bấm "Tính học phí"
activate GUI
GUI -> Ctrl: 2. calculateMonthlyFees(month, year)
activate Ctrl

Ctrl -> Service: 3. executeFeeCalculation(month, year)
activate Service

Service -> DB: 4. getActiveChildrenList()
activate DB
DB --> Service: 5. Return List<Children>
deactivate DB

loop Với từng học sinh trong danh sách
  Service -> DB: 6. getAbsenceDaysWithNotice(childId, month, year)
  activate DB
  DB --> Service: 7. Return absenceDays (ví dụ: 2 ngày)
  deactivate DB
  
  Service -> Service: 8. calculateMealFee(standardDays=22, absenceDays=2, unitPrice=30000) -> 600,000đ
  Service -> Service: 9. calculateTotalFee(baseFee=1500000, mealFee=600000, otherFee=100000) -> 2,200,000đ
  
  Service -> DB: 10. saveInvoiceRecord(childId, invoiceDetails)
  activate DB
  DB --> Service: 11. Return invoiceId
  deactivate DB
end

Service --> Ctrl: 12. Return FeeCalculationSummary
deactivate Service

Ctrl --> GUI: 13. Trả về bảng tổng hợp học phí chi tiết
deactivate Ctrl
GUI --> Accountant: 14. Hiển thị danh sách hóa đơn sẵn sàng phát hành
deactivate GUI
@enduml"""
    add_code_block(doc, seq4_code, caption="Mã nguồn PlantUML Sequence Diagram: Tính tiền ăn & học phí (UC-HP01)")

    # Sequence 5
    add_header(doc, "4.5. Sequence Diagram: Thanh toán học phí bằng mã QR VietQR và Webhook xác nhận (UC-HP05)", level=3)
    seq5_code = """@startuml Sequence_ThanhToan_VietQR
autonumber
actor "Phụ huynh" as Parent
boundary "MobileAppGUI" as App
control "PaymentController" as PayCtrl
entity "VietQRService" as QRSvc
participant "Cổng VietQR / Napas" as Gateway
actor "App Ngân hàng" as BankApp
control "WebhookReceiver" as Webhook
database "Database" as DB

Parent -> App: 1. Xem chi tiết học phí và nhấn "Thanh toán QR"
activate App
App -> PayCtrl: 2. requestPaymentQR(invoiceId)
activate PayCtrl

PayCtrl -> DB: 3. getInvoiceInfo(invoiceId)
activate DB
DB --> PayCtrl: 4. Return Amount=2,200,000đ, Code="HD0926"
deactivate DB

PayCtrl -> QRSvc: 5. generateDynamicVietQR(amount, content="HP TE01 HD0926")
activate QRSvc
QRSvc -> Gateway: 6. callGenerateQRAPI()
activate Gateway
Gateway --> QRSvc: 7. Return qrImageData, qrString
deactivate Gateway
QRSvc --> PayCtrl: 8. Return QRPayload
deactivate QRSvc

PayCtrl --> App: 9. Trả về mã VietQR động
deactivate PayCtrl
App --> Parent: 10. Hiển thị mã QR và bộ đếm ngược 15 phút
deactivate App

Parent -> BankApp: 11. Mở App ngân hàng cá nhân & quét mã QR
activate BankApp
BankApp -> BankApp: 12. Tự động nạp: TK trường, 2.200.000đ, ND: "HP TE01 HD0926"
Parent -> BankApp: 13. Xác nhận chuyển tiền (FaceID / PIN)
BankApp -> Gateway: 14. Chuyển khoản liên ngân hàng Napas247
activate Gateway
Gateway --> BankApp: 15. Báo giao dịch thành công
deactivate BankApp

Gateway -> Webhook: 16. Gửi Webhook Instant Payment Notification (IPN)
activate Webhook
deactivate Gateway

Webhook -> Webhook: 17. Xác thực chữ ký số (Verify Signature)
Webhook -> DB: 18. updateInvoiceStatus(invoiceId, "PAID", transId)
activate DB
DB --> Webhook: 19. Invoice Updated Successfully
deactivate DB

Webhook -> App: 20. Push Notification qua Socket / Firebase: "Thanh toán thành công"
activate App
App --> Parent: 21. Màn hình tự động chuyển sang "Biên lai thanh toán thành công"
deactivate App
deactivate Webhook
@enduml"""
    add_code_block(doc, seq5_code, caption="Mã nguồn PlantUML Sequence Diagram: Thanh toán QR & Webhook (UC-HP05)")

    # ----------------------------------------------------
    # MỤC 5: HƯỚNG DẪN TÍCH HỢP VÀ MỞ TRÊN ASTAH COMMUNITY
    # ----------------------------------------------------
    doc.add_page_break()
    add_header(doc, "5. Hướng dẫn tích hợp và mở sơ đồ trên Astah Community", level=3)
    add_p(doc, "Để trực quan hóa các mô hình luồng xử lý trên công cụ Astah Community (đã được cài đặt sẵn tại máy tính theo đường dẫn: C:\\Program Files\\astah-community), các bước thực hiện như sau:")

    add_p(doc, "1. Cách vẽ Use Case Diagram trên Astah Community:", bold=True)
    add_p(doc, "• Bước 1: Khởi động Astah Community -> Chọn [File] -> [New].\n"
               "• Bước 2: Tại cây thư mục cấu trúc bên trái (Structure Tree), nhấn chuột phải vào Project -> Chọn [Create Diagram] -> Chọn [Use Case Diagram].\n"
               "• Bước 3: Đặt tên sơ đồ (ví dụ: 'PhanRa_QuanLyTreEm' hoặc 'PhanRa_HocPhi_ThanhToan').\n"
               "• Bước 4: Kéo thả các biểu tượng [Actor] từ thanh công cụ lên vùng vẽ (Quản lý, Giáo viên, Phụ huynh, Kế toán).\n"
               "• Bước 5: Kéo thả các biểu tượng [Use Case] hình oval và đặt tên tương ứng với mã Use Case trong bảng phân rã.\n"
               "• Bước 6: Sử dụng công cụ nối [Association] để liên kết Actor với Use Case; sử dụng công cụ [Include] và [Extend] để mô tả quan hệ phụ thuộc giữa các chức năng.")

    add_p(doc, "2. Cách vẽ Activity Diagram trên Astah Community:", bold=True)
    add_p(doc, "• Bước 1: Nhấn chuột phải vào gói (Package) hoặc Use Case -> Chọn [Create Diagram] -> Chọn [Activity Diagram].\n"
               "• Bước 2: Kéo [Initial Node] (nút tròn đen bắt đầu) lên góc trên vùng vẽ.\n"
               "• Bước 3: Tạo các [Action] hình chữ nhật bo tròn cho từng thao tác của người dùng và hệ thống.\n"
               "• Bước 4: Tạo các [Decision Node] (hình thoi) cho các điểm kiểm tra rẽ nhánh điều kiện (ví dụ: Dữ liệu hợp lệ? Đủ sĩ số? Đạt chuẩn chi phí?).\n"
               "• Bước 5: Nối các đường chuyển tiếp [Control Flow] và gán nhãn điều kiện [Đúng / Sai] trên từng nhánh.\n"
               "• Bước 6: Đặt [Activity Final Node] (vòng tròn có chấm đen ở tâm) tại các điểm kết thúc luồng.")

    add_p(doc, "3. Cách vẽ Sequence Diagram trên Astah Community:", bold=True)
    add_p(doc, "• Bước 1: Nhấn chuột phải vào Model -> Chọn [Create Diagram] -> Chọn [Sequence Diagram].\n"
               "• Bước 2: Kéo Actor (Quản lý, Phụ huynh,...) vào dòng đầu tiên.\n"
               "• Bước 3: Kéo thả các đối tượng (Lifeline) đại diện cho các lớp Boundary, Control, Entity và Database.\n"
               "• Bước 4: Sử dụng công cụ [Synchronous Message] (mũi tên nét liền đầu tam giác đặc) để vẽ các lời gọi hàm tuần tự.\n"
               "• Bước 5: Sử dụng công cụ [Reply Message] (mũi tên nét đứt) để vẽ thông điệp phản hồi kết quả.\n"
               "• Bước 6: Sử dụng khung [Combined Fragment] (chọn kiểu 'alt' cho rẽ nhánh hoặc 'loop' cho vòng lặp duyệt danh sách) để thể hiện logic điều khiển chuẩn UML.")

    add_callout(doc, "TÍCH HỢP TỰ ĐỘNG VÀ MÃ NGUỒN",
                "Toàn bộ mã nguồn PlantUML của 5 Use Case Diagrams, 5 Activity Diagrams và 5 Sequence Diagrams "
                "đã được biên soạn hoàn chỉnh và lưu trữ trong thư mục 'diagrams/' của repository GitHub. "
                "Có thể sử dụng plugin PlantUML để kết xuất trực tiếp sang hình ảnh PNG chất lượng cao hoặc "
                "vẽ nhanh chóng trên Astah Community theo đúng các thông điệp đã được định nghĩa.")

    doc.save(output_path)
    print(f"Document successfully written to: {output_path}")

if __name__ == "__main__":
    out = r"c:\Users\NGUYEN\AppData\Local\Temp\Zalo Temp\TempDownloads\KeHoachCNPM.docx"
    build_document(out)
