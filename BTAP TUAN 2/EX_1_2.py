# 1. Tính số giây trong 42 phút 42 giây
total_seconds = 42 * 60 + 42
print(f"1. Tổng số giây: {total_seconds} giây")

# 2. Đổi 10 km sang dặm (miles)
kilometers = 10
miles = kilometers / 1.61
print(f"2. 10 km tương đương: {miles:.2f} dặm")

# 3. Tính tốc độ trung bình (Average Pace & Average Speed)
# Tính Pace (số giây trên mỗi dặm)
seconds_per_mile = total_seconds / miles
pace_minutes = int(seconds_per_mile // 60)
pace_seconds = int(seconds_per_mile % 60)

# Tính Speed (dặm trên giờ)
total_hours = total_seconds / 3600
miles_per_hour = miles / total_hours

print(f"3. Tốc độ trung bình:")
print(f"   - Pace: {pace_minutes} phút {pace_seconds} giây mỗi dặm")
print(f"   - Speed: {miles_per_hour:.2f} dặm/giờ")