def solve_strobogrammatic():
    LIMIT = 1000000
    
    # 1. Sàng số nguyên tố lên đến 1 triệu
    is_prime = [True] * LIMIT
    is_prime[0] = is_prime[1] = False
    for p in range(2, int(LIMIT**0.5) + 1):
        if is_prime[p]:
            for i in range(p * p, LIMIT, p):
                is_prime[i] = False

    # Định nghĩa các cặp số xoay
    map_basic = {'0': '0', '1': '1', '8': '8', '6': '9', '9': '6'}
    map_ext = {'0': '0', '1': '1', '8': '8', '6': '9', '9': '6', '2': '2', '5': '5'}

    def get_rotated_val(n, mapping):
        """Xoay số n theo quy tắc trong mapping. Trả về giá trị int hoặc None nếu ko xoay được."""
        s = str(n)
        res = ""
        for char in reversed(s):
            if char not in mapping:
                return None
            res += mapping[char]
        return int(res)

    def is_strobogrammatic(n, mapping):
        """Kiểm tra số n có tự đối xứng qua tâm hay không."""
        s = str(n)
        rotated_str = ""
        for char in reversed(s):
            if char not in mapping: return False
            rotated_str += mapping[char]
        return s == rotated_str

    # Các danh sách kết quả
    list_a = [] # Strobo cơ bản
    list_b = [] # Strobo cơ bản + Nguyên tố
    list_c = [] # Strobo mở rộng
    list_d = [] # Strobo mở rộng + Nguyên tố
    list_e = [] # Không strobo, không nguyên tố, nhưng xoay xong là nguyên tố

    for i in range(LIMIT):
        # Kiểm tra strobo cơ bản
        if is_strobogrammatic(i, map_basic):
            list_a.append(i)
            if is_prime[i]:
                list_b.append(i)
        
        # Kiểm tra strobo mở rộng
        is_strobo_ext = is_strobogrammatic(i, map_ext)
        if is_strobo_ext:
            list_c.append(i)
            if is_prime[i]:
                list_d.append(i)
        
        # Xử lý câu e (dựa trên hệ thống mở rộng)
        if not is_strobo_ext and not is_prime[i]:
            rotated_v = get_rotated_val(i, map_ext)
            if rotated_v is not None and rotated_v < LIMIT:
                if is_prime[rotated_v]:
                    list_e.append(i)

    # In kết quả
    print("a.- Các số strobogrammatic nhỏ hơn 1 triệu:")
    # print(list_a) # Bỏ comment nếu muốn xem toàn bộ
    print(f"Số lượng: {len(list_a)}")

    print("\nb.- Các số nguyên tố strobogrammatic nhỏ hơn 1 triệu:")
    print(", ".join(map(str, list_b)))

    print("\nc.- Các số strobogrammatic mở rộng nhỏ hơn 1 triệu:")
    print(f"Số lượng: {len(list_c)}")

    print("\nd.- Các số nguyên tố strobogrammatic mở rộng nhỏ hơn 1 triệu:")
    print(", ".join(map(str, list_d)))

    print("\ne.- Số không phải strobo, không phải nguyên tố, nhưng xoay xong là nguyên tố:")
    print(f"Ví dụ một số: {list_e[:20]} ...")
    print(f"Số lượng tìm thấy: {len(list_e)}")

# Chạy chương trình
if __name__ == "__main__":
    solve_strobogrammatic()