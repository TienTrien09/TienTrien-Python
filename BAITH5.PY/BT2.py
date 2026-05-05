from collections import Counter

# Nhập 2 chuỗi
s1 = input("Nhập chuỗi S1: ")
s2 = input("Nhập chuỗi S2: ")

# a) Các ký tự xuất hiện trong cả 2 chuỗi
c1 = Counter(s1)
c2 = Counter(s2)

common = c1 & c2  # phép AND giữa 2 Counter

print("a) Ký tự xuất hiện trong cả 2 chuỗi:")
for ch in common:
    print(ch, end=" ")

# b) Đếm ký tự chỉ có ở S1 và chỉ có ở S2
only_s1 = set(s1) - set(s2)
only_s2 = set(s2) - set(s1)

print("\nb) Số ký tự chỉ có trong S1:", len(only_s1))
print("   Số ký tự chỉ có trong S2:", len(only_s2))

# c) In các ký tự riêng biệt
print("c) Ký tự có trong S1 nhưng không có trong S2:", only_s1)
print("   Ký tự có trong S2 nhưng không có trong S1:", only_s2)