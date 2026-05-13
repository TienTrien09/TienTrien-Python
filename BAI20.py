def giai_quyet_doi_tien(so_tien_can_doi):
    # Danh sách các mệnh giá tiền từ lớn đến nhỏ
    menh_gia = [500, 200, 100, 50, 20, 10, 5, 2, 1]
    
    print(f"So tien {so_tien_can_doi} duoc doi thanh:")
    
    tong_so_to = 0
    tong_so_loai = 0
    
    for mg in menh_gia:
        so_to = so_tien_can_doi // mg
        if so_to > 0:
            print(f"Loai {mg} gom {so_to} to")
            tong_so_to += so_to
            tong_so_loai += 1
            # Cập nhật số tiền còn lại sau khi đã lấy mệnh giá hiện tại
            so_tien_can_doi %= mg
            
    print(f"Tong cong co {tong_so_to} to")
    print(f"Tong so loai = {tong_so_loai}")

def main():
    # Nhập a (tiền hàng) và b (tiền khách trả)
    try:
        a = int(input("Nhap so tien hang can tra (a): "))
        b = int(input("Nhap so tien khach thuc te tra (b): "))
        
        if a > b:
            print(f"Khach hang con thieu: {a - b}")
        elif a == b:
            print("Cam on khach hang. Hen gap lai")
        else:
            so_tien_thoi = b - a
            print(f"So tien can thoi lai cho khach la: {so_tien_thoi}")
            print("-" * 30)
            
            # Gọi hàm đổi tiền để tính số tờ ít nhất
            giai_quyet_doi_tien(so_tien_thoi)
            
            print("-" * 30)
            input("Nhan phim Enter de ket thuc...")
            print("Cam on khach hang. Hen gap lai")
            
    except ValueError:
        print("Vui long nhap so nguyen hop le.")

if __name__ == "__main__":
    main() 