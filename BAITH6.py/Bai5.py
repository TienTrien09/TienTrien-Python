import os
import json

def solve_io_assignment():
    input_filename = "test.txt"
    compressed_filename = "compressed.json"
    restored_filename = "restored.txt"

    # --- BƯỚC 0: CHO PHÉP NGƯỜI DÙNG NHẬP ĐOẠN VĂN ---
    print("Nhập đoạn văn bản của bạn (Nhấn Enter để kết thúc):")
    user_input = input("> ") # Lấy dữ liệu từ bàn phím
    
    # Lưu nội dung vừa nhập vào file test.txt
    with open(input_filename, 'w', encoding='utf-8') as f:
        f.write(user_input)
    
    print(f"\n--- Đang xử lý nén file ---")

    # --- BƯỚC 1: NÉN FILE ---
    with open(input_filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    words = content.split()
    dictionary = []
    word_to_id = {}
    encoded_data = []

    for w in words:
        if w not in word_to_id:
            word_to_id[w] = len(dictionary)
            dictionary.append(w)
        encoded_data.append(word_to_id[w])

    data_to_save = {"dict": dictionary, "data": encoded_data}
    
    with open(compressed_filename, 'w', encoding='utf-8') as f:
        json.dump(data_to_save, f, ensure_ascii=False)
    
    # --- BƯỚC 2: GIẢI NÉN VÀ HIỂN THỊ ---
    with open(compressed_filename, 'r', encoding='utf-8') as f:
        loaded_data = json.load(f)
        
    indices = loaded_data["data"]
    dict_data = loaded_data["dict"]
    
    # Khôi phục
    restored_content = " ".join([dict_data[i] for i in indices])
    
    with open(restored_filename, 'w', encoding='utf-8') as f:
        f.write(restored_content)

    print(f"1. Nội dung đã nén lưu tại: {compressed_filename}")
    print(f"2. Nội dung sau giải nén: {restored_content}")
    print(f"3. File khôi phục đã lưu tại: {restored_filename}")

if __name__ == "__main__":
    solve_io_assignment()