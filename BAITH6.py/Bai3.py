# Nhập số điện thoại
S = input("Nhập số điện thoại: ")

# Danh sách lưu các số không xuất hiện
khong_co = []

# Kiểm tra từ 0 đến 9
for i in range(10):
    # Chuyển số thành chuỗi để kiểm tra
    if str(i) not in S:
        khong_co.append(i)

# In kết quả
print("Các chữ số không xuất hiện là:", khong_co)