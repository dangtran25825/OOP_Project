import math

print("--- Câu 1: Thể tích hình cầu ---")
radius = 5
volume = (4/3) * math.pi * radius**3
print(f"Thể tích hình cầu bán kính 5 là: {volume:.2f}")

print("\n--- Câu 2: Tổng chi phí mua sách ---")
cover_price = 24.95
discount = 0.4
shipping_first = 3
shipping_additional = 0.75
quantity = 60

price_per_book = cover_price * (1 - discount)
total_shipping = shipping_first + (quantity - 1) * shipping_additional
total_cost = (price_per_book * quantity) + total_shipping
print(f"Tổng chi phí cho 60 cuốn sách là: ${total_cost:.2f}")

print("\n--- Câu 3: Thời gian về ăn sáng ---")
# Đổi thời gian chạy sang giây
easy_pace_seconds = 8 * 60 + 15
tempo_pace_seconds = 7 * 60 + 12

total_run_seconds = (easy_pace_seconds * 2) + (tempo_pace_seconds * 3)

# Thời gian bắt đầu: 6:52 AM tính theo giây từ lúc 0:00
start_time_seconds = (6 * 3600) + (52 * 60)
end_time_seconds = start_time_seconds + total_run_seconds

# Đổi ngược lại thành giờ:phút
end_hour = int(end_time_seconds // 3600)
end_minute = int((end_time_seconds % 3600) // 60)
end_second = int(end_time_seconds % 60)

print(f"Bạn sẽ về nhà vào lúc: {end_hour}:{end_minute:02d}:{end_second:02d} AM")