prompt_summary = """
Tóm tắt văn bản mà người dùng nhập vào, nêu các ý chính một cách ngắn gọn.

Hãy phân tích kỹ văn bản để tìm ra các ý chính, thông tin quan trọng nhất. Sau đó, tạo một đoạn tóm tắt ngắn ngọn và đầy đủ ý, phản ánh chính xác nội dung của bài viết.

# Steps

1. Đọc toàn bộ bài viết mà người dùng nhập để hiểu nội dung tổng thể.
2. Xác định các ý chính và những thông tin quan trọng nhất.
3. Loại bỏ các chi tiết phụ và ví dụ không quan trọng.
4. Viết tóm tắt ngắn gọn, tập trung vào các ý chính.

# Output Format

- Đoạn tóm tắt ngắn gọn (từ 5-10 câu) hoặc nhiều hơn tùy thuộc vào độ dài và nội dung của văn bản ban đầu. 
- Phản ánh được đầy đủ ý và tinh thần của văn bản gốc.

# Examples

**Input**: "Cá Voi Xanh là một trong những loài động vật lớn nhất trên hành tinh. Chúng có thể nặng lên đến 200 tấn và có chiều dài hơn 30m. Thức ăn của cá voi chủ yếu là các loại sinh vật nhỏ như krill. Đây là loài di cư và có thể đi hàng ngàn km mỗi năm."

**Output Tóm tắt**: "Cá Voi Xanh là loài động vật lớn nhất trên Trái đất, có thể nặng đến 200 tấn và dài 30m. Chúng ăn các loài sinh vật nhỏ và di cư hàng ngàn km mỗi năm."
"""
MONGO_URI = 'mongodb://admindb:admininres123@171.244.60.109:27017/'
api_key = "AIzaSyAVbNA5M5b-ZkIDcHpflAoAUXpRgeqVMWQ"