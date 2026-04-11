class HangHoa:
    def __init__(self, ma_hang, ten_hang, nha_sx, gia):
        self.ma_hang = ma_hang
        self.ten_hang = ten_hang
        self.nha_sx = nha_sx
        self.gia = gia

    def xuat_thong_tin(self):
        print(f"Mã: {self.ma_hang} | Tên: {self.ten_hang} | NSX: {self.nha_sx} | Giá: {self.gia}", end="")

class HangDienMay(HangHoa):
    def __init__(self, ma_hang, ten_hang, nha_sx, gia, tg_baohanh, dien_ap, cong_suat):
        super().__init__(ma_hang, ten_hang, nha_sx, gia)
        self.tg_baohanh = tg_baohanh
        self.dien_ap = dien_ap
        self.cong_suat = cong_suat

    def xuat_thong_tin(self):
        super().xuat_thong_tin()
        print(f" | Bảo hành: {self.tg_baohanh} tháng | Điện áp: {self.dien_ap}V | Công suất: {self.cong_suat}W")

class HangSanhSu(HangHoa):
    def __init__(self, ma_hang, ten_hang, nha_sx, gia, loai_nguyen_lieu):
        super().__init__(ma_hang, ten_hang, nha_sx, gia)
        self.loai_nguyen_lieu = loai_nguyen_lieu

    def xuat_thong_tin(self):
        super().xuat_thong_tin()
        print(f" | Nguyên liệu: {self.loai_nguyen_lieu}")

class HangThucPham(HangHoa):
    def __init__(self, ma_hang, ten_hang, nha_sx, gia, ngay_sx, ngay_het_han):
        super().__init__(ma_hang, ten_hang, nha_sx, gia)
        self.ngay_sx = ngay_sx
        self.ngay_het_han = ngay_het_han

    def xuat_thong_tin(self):
        super().xuat_thong_tin()
        print(f" | Ngày SX: {self.ngay_sx} | Hạn dùng: {self.ngay_het_han}")


tu_lanh = HangDienMay("DM001", "Tủ lạnh LG", "LG", 12000000, 24, 220, 200)
bat_trang = HangSanhSu("SS001", "Bộ ấm trà", "Bát Tràng", 850000, "Gốm sứ cao cấp")
banh_mi = HangThucPham("TP001", "Bánh mì gối", "Kinh Đô", 25000, "11/04/2026", "18/04/2026")

print("--- DANH SÁCH MẶT HÀNG ---")
tu_lanh.xuat_thong_tin()
bat_trang.xuat_thong_tin()
banh_mi.xuat_thong_tin()