n_str = input("Nhập số nguyên n: ")
la_so_may_man = True

for char in n_str:
    if char != '6' and char != '8':
        la_so_may_man = False
        break

if la_so_may_man:
    print(f"{n_str} là số may mắn.")
else:
    print(f"{n_str} KHÔNG phải số may mắn.")