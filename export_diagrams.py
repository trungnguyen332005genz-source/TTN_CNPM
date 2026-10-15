# -*- coding: utf-8 -*-
"""
Export all PlantUML diagram files for Nguyen's part
"""
import os

diagrams_dir = os.path.join(os.path.dirname(__file__), "diagrams")
os.makedirs(diagrams_dir, exist_ok=True)

files = {
    # USE CASE DIAGRAMS
    "usecase_tre_em.puml": """@startuml UseCase_QuanLyTreEm
left to right direction
skinparam packageStyle rectangle

actor "Quản lý" as Admin
actor "Giáo viên" as Teacher
actor "Phụ huynh" as Parent

rectangle "Phân hệ Quản lý Trẻ em" {
    usecase "UC-TE01: Xem & Tìm kiếm danh sách trẻ" as UC_TE01
    usecase "UC-TE02: Thêm mới hồ sơ trẻ em" as UC_TE02
    usecase "UC-TE03: Chỉnh sửa hồ sơ trẻ em" as UC_TE03
    usecase "UC-TE04: Xóa / Cập nhật trạng thái học" as UC_TE04
    usecase "UC-TE05: Ghi nhận sức khỏe & sinh hoạt" as UC_TE05
    usecase "UC-PH02: Thêm mới & liên kết phụ huynh" as UC_PH02
}

Admin --> UC_TE01
Admin --> UC_TE02
Admin --> UC_TE03
Admin --> UC_TE04

Teacher --> UC_TE01
Teacher --> UC_TE05

Parent --> UC_TE01 : Xem thông tin con mình

UC_TE02 ..> UC_PH02 : <<include>>
@enduml""",

    "usecase_giao_vien.puml": """@startuml UseCase_QuanLyGiaoVien
left to right direction
skinparam packageStyle rectangle

actor "Quản lý / Ban Giám Hiệu" as Admin
actor "Giáo viên" as Teacher

rectangle "Phân hệ Quản lý Giáo viên" {
    usecase "UC-GV01: Xem danh sách giáo viên" as UC_GV01
    usecase "UC-GV02: Thêm mới giáo viên" as UC_GV02
    usecase "UC-GV03: Chỉnh sửa hồ sơ giáo viên" as UC_GV03
    usecase "UC-GV04: Xóa / Khóa hồ sơ giáo viên" as UC_GV04
    usecase "UC-GV05: Phân công lớp giảng dạy" as UC_GV05
}

Admin --> UC_GV01
Admin --> UC_GV02
Admin --> UC_GV03
Admin --> UC_GV04
Admin --> UC_GV05

Teacher --> UC_GV01 : Xem danh sách đồng nghiệp
@enduml""",

    "usecase_phu_huynh.puml": """@startuml UseCase_QuanLyPhuHuynh
left to right direction
skinparam packageStyle rectangle

actor "Quản lý" as Admin
actor "Phụ huynh" as Parent

rectangle "Phân hệ Quản lý Phụ huynh" {
    usecase "UC-PH01: Xem danh sách phụ huynh" as UC_PH01
    usecase "UC-PH02: Thêm mới & liên kết phụ huynh - trẻ" as UC_PH02
    usecase "UC-PH03: Cập nhật thông tin phụ huynh" as UC_PH03
    usecase "UC-PH04: Hủy liên kết phụ huynh - trẻ" as UC_PH04
    usecase "UC-PH05: Xem hồ sơ & thông tin của con" as UC_PH05
}

Admin --> UC_PH01
Admin --> UC_PH02
Admin --> UC_PH03
Admin --> UC_PH04

Parent --> UC_PH03 : Cập nhật số ĐT, địa chỉ
Parent --> UC_PH05 : Quản lý nhiều con (1 PH - N Trẻ)
@enduml""",

    "usecase_thuc_don.puml": """@startuml UseCase_QuanLyThucDon
left to right direction
skinparam packageStyle rectangle

actor "Cán bộ Dinh dưỡng / Quản lý" as Staff
actor "Phụ huynh" as Parent
actor "Giáo viên" as Teacher

rectangle "Phân hệ Quản lý Thực đơn" {
    usecase "UC-TD01: Xem danh sách thực đơn tuần" as UC_TD01
    usecase "UC-TD02: Lập thực đơn tuần mới" as UC_TD02
    usecase "UC-TD03: Chỉnh sửa thực đơn tuần" as UC_TD03
    usecase "UC-TD04: Quản lý danh mục món & dưỡng chất" as UC_TD04
    usecase "UC-TD05: Phụ huynh xem thực đơn của con" as UC_TD05
}

Staff --> UC_TD01
Staff --> UC_TD02
Staff --> UC_TD03
Staff --> UC_TD04

Parent --> UC_TD05
Teacher --> UC_TD01

UC_TD02 ..> UC_TD04 : <<include>>
@enduml""",

    "usecase_hoc_phi_thanhtoan.puml": """@startuml UseCase_HocPhi_ThanhToan
left to right direction
skinparam packageStyle rectangle

actor "Kế toán / Quản lý" as Accountant
actor "Phụ huynh" as Parent
actor "Giáo viên" as Teacher
actor "Cổng thanh toán / Ngân hàng" as Bank

rectangle "Phân hệ Quản lý Học phí & Thanh toán" {
    usecase "UC-HP01: Lập bảng tính học phí & tiền ăn" as UC_HP01
    usecase "UC-HP02: Ghi nhận ngày nghỉ để trừ tiền ăn" as UC_HP02
    usecase "UC-HP03: Phát hành thông báo học phí tháng" as UC_HP03
    usecase "UC-HP04: Phụ huynh xem chi tiết học phí" as UC_HP04
    usecase "UC-HP05: Thanh toán học phí qua mã VietQR" as UC_HP05
    usecase "UC-HP06: Xác nhận & Cập nhật thanh toán" as UC_HP06
}

Accountant --> UC_HP01
Accountant --> UC_HP03
Accountant --> UC_HP06

Teacher --> UC_HP02 : Điểm danh / Báo nghỉ
Parent --> UC_HP02 : Nộp đơn xin nghỉ
Parent --> UC_HP04 : Tra cứu tiền học
Parent --> UC_HP05 : Quét mã QR

Bank --> UC_HP06 : Gửi Webhook đối soát

UC_HP01 ..> UC_HP02 : <<include>>
UC_HP05 ..> UC_HP04 : <<extend>>
@enduml""",

    # ACTIVITY DIAGRAMS
    "activity_them_tre_em.puml": """@startuml Activity_ThemTreEm
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
@enduml""",

    "activity_phan_cong_gv.puml": """@startuml Activity_PhanCongGiaoVien
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
@enduml""",

    "activity_lap_thuc_don.puml": """@startuml Activity_LapThucDon
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
@enduml""",

    "activity_tinh_hoc_phi_tien_an.puml": """@startuml Activity_TinhHocPhi_TienAn
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
@enduml""",

    "activity_thanhtoan_vietqr.puml": """@startuml Activity_ThanhToan_QR
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
@enduml""",

    # SEQUENCE DIAGRAMS
    "sequence_them_tre_em.puml": """@startuml Sequence_ThemTreEm
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
@enduml""",

    "sequence_phan_cong_gv.puml": """@startuml Sequence_PhanCongGiaoVien
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
@enduml""",

    "sequence_lap_thuc_don.puml": """@startuml Sequence_LapThucDon
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
@enduml""",

    "sequence_tinh_hoc_phi_tien_an.puml": """@startuml Sequence_TinhHocPhi_TienAn
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
@enduml""",

    "sequence_thanhtoan_vietqr.puml": """@startuml Sequence_ThanhToan_VietQR
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
}

for filename, content in files.items():
    file_path = os.path.join(diagrams_dir, filename)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f"Exported: {filename}")

print(f"Total {len(files)} diagrams exported to {diagrams_dir}")
