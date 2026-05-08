# Nhập chuỗi
S = input("Nhập chuỗi: ")

# Tách chuỗi thành các từ
ds_tu = S.split()

# Tập hợp lưu các từ đã xuất hiện
da_xuat_hien = set()

# Biến lưu từ lặp đầu tiên
ket_qua = None

# Duyệt từng từ
for tu in ds_tu:
    if tu in da_xuat_hien:
        ket_qua = tu
        break
    da_xuat_hien.add(tu)

# In kết quả
print("Từ lặp đầu tiên là:", ket_qua)