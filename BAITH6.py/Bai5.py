# ==============================
# BÀI THỰC HÀNH I/O FILE TRONG PYTHON
# ĐÃ SỬA LỖI FileNotFoundError
# ==============================

import os

# Tên file
ten_file = "fileName.txt"

# ==============================
# KIỂM TRA FILE CÓ TỒN TẠI KHÔNG
# ==============================

if not os.path.exists(ten_file):

    # Nếu chưa có file thì tự tạo
    f = open(ten_file, "w", encoding="utf-8")

    # Ghi nội dung mẫu
    f.write("""Thuyen va bien
Chi co thuyen moi hieu
Bien menh mong nhuong nao
Chi co bien moi biet""")

    f.close()

    print("Đã tự tạo file fileName.txt")

# ==============================
# PHẦN 1: NÉN FILE
# ==============================

# Mở file để đọc
f = open(ten_file, "r", encoding="utf-8")

# Đọc nội dung
noi_dung = f.read()

# Đóng file
f.close()

# Tách từ
words = noi_dung.split()

# Danh sách từ duy nhất
tu_don = []

# Danh sách vị trí
vi_tri = []

# Duyệt từng từ
for w in words:

    # Nếu từ chưa có thì thêm vào
    if w not in tu_don:
        tu_don.append(w)

    # Lưu vị trí
    vi_tri.append(tu_don.index(w))

# Ghi file nén
f = open("compressed.txt", "w", encoding="utf-8")

# Ghi danh sách từ
f.write(" ".join(tu_don))
f.write("\n")

# Ghi vị trí
f.write(" ".join(map(str, vi_tri)))

f.close()

print("Đã tạo file compressed.txt")

# ==============================
# PHẦN 2: GIẢI NÉN FILE
# ==============================

# Đọc file nén
f = open("compressed.txt", "r", encoding="utf-8")

lines = f.readlines()

f.close()

# Danh sách từ
tu_don = lines[0].split()

# Danh sách vị trí
vi_tri = list(map(int, lines[1].split()))

# Khôi phục văn bản
ket_qua = []

for i in vi_tri:
    ket_qua.append(tu_don[i])

# Ghép lại
van_ban_goc = " ".join(ket_qua)

# Ghi file khôi phục
f = open("restore.txt", "w", encoding="utf-8")

f.write(van_ban_goc)

f.close()

print("Đã tạo file restore.txt")
print("Hoàn thành chương trình!")