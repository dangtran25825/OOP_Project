import time

# Lấy tổng số giây hiện tại kể từ Epoch
total_seconds = time.time()

# 1. Tính số ngày đã trôi qua
# 1 ngày có 24 giờ * 60 phút * 60 giây = 86400 giây
seconds_in_day = 24 * 60 * 60
days_since_epoch = int(total_seconds // seconds_in_day)

# 2. Tính thời gian còn lại của ngày hiện tại (số giây dư ra)
remaining_seconds = total_seconds % seconds_in_day

# 3. Đổi số giây còn lại đó sang Giờ, Phút, Giây
hours = int(remaining_seconds // 3600)
minutes = int((remaining_seconds % 3600) // 60)
seconds = int(remaining_seconds % 60)

print(f"Số ngày kể từ Epoch: {days_since_epoch} ngày")
print(f"Giờ hiện tại (GMT): {hours}:{minutes:02d}:{seconds:02d}")