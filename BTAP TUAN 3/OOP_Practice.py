import math

# --- PHẦN 1: ĐỊNH NGHĨA CÁC LỚP (CLASSES) ---

class Point:
    """Lớp biểu diễn một điểm trong không gian 2D"""
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def display(self):
        print(f"Tọa độ điểm: ({self.x}, {self.y})")

    def distance_to_origin(self):
        # Công thức: d = sqrt(x^2 + y^2)
        return math.sqrt(self.x**2 + self.y**2)

    def distance_to(self, other):
        # Công thức tính khoảng cách giữa 2 điểm
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

class SieuNhan:
    """Lớp biểu diễn đối tượng Siêu Nhân với các thuộc tính cơ bản"""
    def __init__(self, ten, vu_khi, mau_sac):
        self.ten = ten
        self.vu_khi = vu_khi
        self.mau_sac = mau_sac

    def info(self):
        print(f"Siêu nhân: {self.ten:10} | Vũ khí: {self.vu_khi:10} | Màu sắc: {self.mau_sac}")

# --- PHẦN 2: THỰC THI CHƯƠNG TRÌNH ---

print("=== BÀI 1: HÌNH HỌC 2D (POINT) ===")
# Tạo điểm A(3, 4) và hiển thị
A = Point(3, 4)
A.display()

# Tạo điểm B từ bàn phím
try:
    bx = int(input("Nhập tọa độ x cho B: "))
    by = int(input("Nhập tọa độ y cho B: "))
    B = Point(bx, by)
    
    # Tạo điểm C đối xứng với B qua gốc O
    C = Point(-B.x, -B.y)
    print("Điểm C (đối xứng B qua O):")
    C.display()
    
    # Tính các khoảng cách
    print(f"Khoảng cách từ B đến gốc tọa độ O: {B.distance_to_origin():.2f}")
    print(f"Khoảng cách từ A đến B: {A.distance_to(B):.2f}")
except ValueError:
    print("Lỗi: Vui lòng nhập số nguyên cho tọa độ!")

print("\n=== BÀI 2 & 3: QUẢN LÝ SIÊU NHÂN ===")
# Khởi tạo mặc định 2 siêu nhân
sn_A = SieuNhan("A", "Kiếm", "Đỏ")
sn_B = SieuNhan("B", "Khiên", "Xanh")

danh_sach_sn = [sn_A, sn_B]

# Dùng while để nhập thêm danh sách
while True:
    tiep_tuc = input("Bạn có muốn nhập thêm siêu nhân không? (y/n): ").lower()
    if tiep_tuc != 'y':
        break
    
    ten = input("Tên siêu nhân: ")
    vu_khi = input("Vũ khí: ")
    mau_sac = input("Màu sắc: ")
    
    danh_sach_sn.append(SieuNhan(ten, vu_khi, mau_sac))

# Dùng for để in danh sách kèm thuộc tính
print("\nDANH SÁCH SIÊU NHÂN TOÀN THẾ GIỚI:")
for sn in danh_sach_sn:
    sn.info()