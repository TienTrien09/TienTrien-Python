n = int(input("Nhập số nguyên dương n: "))
max_digit = 0
temp_n = n

while temp_n > 0:
    chu_so = temp_n % 10
    if chu_so > max_digit:
        max_digit = chu_so
    temp_n //= 10

print(f"Số lớn nhất={max_digit}")