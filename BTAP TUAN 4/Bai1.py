class NhanVien:
    # Hằng số lương tối đa (LUONG_MAX)
    LUONG_MAX = 20000000.0

    def __init__(self, ten, luong_cb, he_so):
        self.__tenNhanVien = ten      # Thuộc tính private (có __)
        self.__luongCoBan = luong_cb
        self.__heSoLuong = he_so

    # Các hàm GET và SET
    def get_ten(self): return self.__tenNhanVien
    def set_ten(self, ten): self.__tenNhanVien = ten

    def get_he_so(self): return self.__heSoLuong
    def set_he_so(self, hs): self.__heSoLuong = hs

    # Phương thức tính lương
    def tinhLuong(self):
        return self.__luongCoBan * self.__heSoLuong

    # Phương thức tăng lương có kiểm tra điều kiện
    def tangLuong(self, delta):
        luong_moi = self.__luongCoBan * (self.__heSoLuong + delta)
        if luong_moi > self.LUONG_MAX:
            print("Thông báo: Lương vượt mức tối đa, không thể tăng!")
            return False
        self.__heSoLuong += delta
        return True

    def inTTin(self):
        print(f"Nhân viên: {self.__tenNhanVien} | Lương: {self.tinhLuong():,.0f} VNĐ")