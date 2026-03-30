import math

# ==========================================
# PHẦN 1: HÌNH HỌC NÂNG CAO (POINT, CIRCLE, RECTANGLE)
# ==========================================

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Rectangle:
    """Lớp biểu diễn hình chữ nhật với góc trái dưới và kích thước"""
    def __init__(self, corner, width, height):
        self.corner = corner  # Đối tượng Point
        self.width = width
        self.height = height

class Circle:
    def __init__(self, center, radius):
        self.center = center  # Đối tượng Point
        self.radius = radius

    def point_in_circle(self, p):
        """Kiểm tra một điểm p có nằm trong hoặc trên biên hình tròn không"""
        d = math.sqrt((p.x - self.center.x)**2 + (p.y - self.center.y)**2)
        return d <= self.radius

    def rect_in_circle(self, rect):
        """Kiểm tra hình chữ nhật có nằm hoàn toàn trong hình tròn không"""
        # Kiểm tra cả 4 góc của hình chữ nhật
        corners = [
            rect.corner,
            Point(rect.corner.x + rect.width, rect.corner.y),
            Point(rect.corner.x, rect.corner.y + rect.height),
            Point(rect.corner.x + rect.width, rect.corner.y + rect.height)
        ]
        for p in corners:
            if not self.point_in_circle(p):
                return False
        return True

# ==========================================
# PHẦN 2: QUẢN LÝ NHÂN VIÊN (NHANVIEN)
# ==========================================

class NhanVien:
    LUONG_MAX = 20000000.0  # 20 triệu

    def __init__(self, ten, luong_cb, he_so):
        self._ten = ten
        self._luong_cb = luong_cb
        self._he_so = he_so

    def tinh_luong(self):
        return self._luong_cb * self._he_so

    def in_ttin(self):
        print(f"Nhân viên: {self._ten:15} | Hệ số: {self._he_so} | Lương: {self.tinh_luong():,.0f} VNĐ")

    def tang_luong(self, delta):
        luong_moi = self._luong_cb * (self._he_so + delta)
        if luong_moi > self.LUONG_MAX:
            print(f"!!! Không thể tăng lương cho {self._ten}: Vượt mức tối đa!")
            return False
        else:
            self._he_so += delta
            return True

# ==========================================
# KIỂM TRA CHƯƠNG TRÌNH
# ==========================================

print("--- KIỂM TRA HÌNH TRÒN ---")
center = Point(150, 100)
circle = Circle(center, 75)
p_test = Point(160, 110)
print(f"Điểm (160, 110) nằm trong hình tròn: {circle.point_in_circle(p_test)}")

print("\n--- KIỂM TRA NHÂN VIÊN ---")
nv1 = NhanVien("Thành", 5000000, 2.0)
nv1.in_ttin()
nv1.tang_luong(2.5) # Thử tăng vượt mức
nv1.in_ttin()