n = int(input("Nhập số nguyên dương n: "))
temp_n = n
tong = 0
tich = 1

while temp_n > 0:
    chu_so = temp_n % 10
    tong += chu_so
    tich *= chu_so
    temp_n //= 10

print(f"Tổng={tong}, Tích={tich}")