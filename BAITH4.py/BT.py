# =========================
# BÀI THỰC HÀNH LAMBDA PYTHON
# =========================

import math

# ---------------------------------
# a) Hàm nhận 1 số nguyên n và trả về giá trị tuyệt đối của n
# ---------------------------------
abs_val = lambda n: abs(n)

print("a) |n| =", abs_val(-10))


# ---------------------------------
# b) Hàm nhận 1 số nguyên n và trả về giá trị n + 15
# ---------------------------------
plus_15 = lambda n: n + 15

print("b) n + 15 =", plus_15(5))


# ---------------------------------
# c) Hàm nhận 2 số nguyên (x, y), trả về tích của x và y
# ---------------------------------
product = lambda x, y: x * y

print("c) x * y =", product(3, 4))


# ---------------------------------
# d) Kiểm tra n có phải là bội của 13 hoặc 19 không
# ---------------------------------
is_multiple_13_19 = lambda n: n % 13 == 0 or n % 19 == 0

print("d) Có phải bội của 13 hoặc 19:", is_multiple_13_19(26))


# ---------------------------------
# e) Tính diện tích hình tròn với bán kính r
# Công thức: S = π * r^2
# ---------------------------------
circle_area = lambda r: math.pi * r * r

print("e) Diện tích hình tròn =", circle_area(2))


# ---------------------------------
# f) Tính chu vi hình chữ nhật
# Công thức: P = 2 * (d + r)
# ---------------------------------
rectangle_perimeter = lambda d, r: 2 * (d + r)

print("f) Chu vi hình chữ nhật =", rectangle_perimeter(3, 4))


# ---------------------------------
# g) Kiểm tra n có phải số chính phương không
# Số chính phương: căn bậc hai là số nguyên
# ---------------------------------
is_perfect_square = lambda n: int(n**0.5)**2 == n

print("g) Là số chính phương:", is_perfect_square(16))


# ---------------------------------
# h) Kiểm tra n có phải số nguyên tố không
# Số nguyên tố: chỉ chia hết cho 1 và chính nó
# ---------------------------------
is_prime = lambda n: n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))

print("h) Là số nguyên tố:", is_prime(7))


# ---------------------------------
# i) Kiểm tra 3 cạnh có tạo thành tam giác không
# Nếu có thì xác định loại tam giác
# ---------------------------------
triangle_type = lambda a, b, c: (
    "Không phải tam giác" if a + b <= c or a + c <= b or b + c <= a else
    "Tam giác đều" if a == b == c else
    "Tam giác cân" if a == b or b == c or a == c else
    "Tam giác vuông" if a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a else
    "Tam giác thường"
)

print("i) Loại tam giác:", triangle_type(3, 4, 5))