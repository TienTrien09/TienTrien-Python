def giai_bai_117():
    print("--- CHƯƠNG TRÌNH TÍNH TỔNG BÌNH PHƯƠNG SỐ CON ---")
    
    # Bước 1: Nhập số nguyên dương n
    n_str = input("Nhập số nguyên dương n: ").strip()
    
    # Kiểm tra điều kiện n > 0
    if not n_str.isdigit() or int(n_str) <= 0:
        print("Lỗi: Vui lòng nhập một số nguyên dương!")
        return

    tong_binh_phuong = 0
    do_dai = len(n_str)
    danh_sach_so_con = [] # Dùng để lưu lại các số con để kiểm tra (không bắt buộc)

    # Bước 2: Duyệt qua tất cả các chuỗi con bằng 2 vòng lặp
    # i là vị trí bắt đầu, j là vị trí kết thúc
    for i in range(do_dai):
        for j in range(i + 1, do_dai + 1):
            sub_str = n_str[i:j]        # Lấy chuỗi con từ index i đến j
            sub_num = int(sub_str)      # Chuyển chuỗi thành số (xử lý được số 0 ở đầu)
            
            # Bước 3: Cộng dồn bình phương vào tổng
            tong_binh_phuong += (sub_num ** 2)
            danh_sach_so_con.append(sub_str)

    # In kết quả
    print(f"\nCác số con tìm được: {', '.join(danh_sach_so_con)}")
    print(f"Tổng bình phương S = {tong_binh_phuong}")

# Chạy chương trình
if __name__ == "__main__":
    giai_bai_117()