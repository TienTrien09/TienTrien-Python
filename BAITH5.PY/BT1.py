# Hàm kiểm tra số nguyên tố
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


# Danh sách lưu các số
lst = []

# Nhập nhiều lần
while True:
    x = int(input("Nhập số nguyên: "))
    lst.append(x)

    choice = input("Nhập tiếp? (Y/N): ")
    if choice.lower() != 'y':
        break

# a) In các số nguyên tố
print("Các số nguyên tố:", end=" ")
for num in lst:
    if is_prime(num):
        print(num, end=" ")

# b) Tính trung bình cộng số dương và số âm
sum_pos = count_pos = 0
sum_neg = count_neg = 0

for num in lst:
    if num > 0:
        sum_pos += num
        count_pos += 1
    elif num < 0:
        sum_neg += num
        count_neg += 1

if count_pos > 0:
    print("\nTBC số dương:", sum_pos / count_pos)
else:
    print("\nKhông có số dương")

if count_neg > 0:
    print("TBC số âm:", sum_neg / count_neg)
else:
    print("Không có số âm")

# c) Tìm max, min
print("Số lớn nhất:", max(lst))
print("Số nhỏ nhất:", min(lst))

# d) Kiểm tra tăng dần
is_increasing = True
for i in range(len(lst) - 1):
    if lst[i] > lst[i + 1]:
        is_increasing = False
        break

if is_increasing:
    print("Danh sách đã được sắp xếp tăng dần")
else:
    print("Danh sách chưa được sắp xếp tăng dần")