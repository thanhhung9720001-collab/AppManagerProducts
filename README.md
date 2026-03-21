ĐẶT VẤN ĐỀ 

Bạn đang vào vai một lập trình viên được giao nhiệm vụ xây dựng một phiên 
bản đầu tiên của ứng dụng quản lý cho một cửa hàng bán laptop có tên là POLY
LAP. Ứng dụng này cần chạy được trên máy tính cá nhân (dưới dạng console 
application) và có các chức năng cơ bản để giúp người quản lý có thể theo dõi 
và thao tác với các sản phẩm trong kho hàng của mình. 
Dữ liệu của các sản phẩm sẽ được lưu trữ trong một file để đảm bảo không bị 
mất sau mỗi lần tắt ứng dụng.

YÊU CẦU 
Bạn cần xây dựng một dự án Python hoàn chỉnh, có cấu trúc rõ ràng và đáp ứng 
đầy đủ các chức năng được mô tả dưới đây. 
Phần 1: Thiết kế cấu trúc dữ liệu và Module hóa 
PAGE 3 
ITA102 - Assignment 
1) Cấu trúc dữ liệu: 
Hãy thiết kế cấu trúc dữ liệu để lưu trữ danh sách các sản phẩm. Mỗi sản phẩm 
trong kho cần có các thông tin sau: 
✔ Mã sản phẩm (ID): Một chuỗi duy nhất, ví dụ: “LT01”, “LT02”. 
✔ Tên sản phẩm: Ví dụ: “Laptop Gaming Acer Nitro 5”. 
✔ Thương hiệu: Ví dụ: “Acer”. 
✔ Giá: Một số nguyên. 
✔ Số lượng tồn kho: Một số nguyên. 
Gợi ý: Một list chứa các dictionary là một lựa chọn rất phù hợp cho bài toán này. 
2) Module hóa mã nguồn: 
Tổ chức dự án thành ít nhất hai file .py: 
✔ main.py: File chính, chịu trách nhiệm hiển thị menu, nhận lựa chọn của 
người dùng và gọi các hàm xử lý tương ứng. 
✔ product_manager.py: Một module chứa tất cả các hàm logic để thao tác với 
dữ liệu sản phẩm (thêm, sửa, xóa, tìm kiếm, lưu/tải file...). 
Phần 2: Xây dựng các chức năng cốt lõi 
Hãy viết các hàm sau trong module product_manager.py: 
1) load_data(): 
✔ Hàm này chịu trách nhiệm đọc dữ liệu từ file products.json. 
✔ Nó phải xử lý được trường hợp file chưa tồn tại (lần đầu chạy chương trình) 
và trả về một danh sách rỗng. 
✔ Sử dụng try...except FileNotFoundError. 
2) save_data(products): 
✔ Hàm này nhận vào một danh sách sản phẩm và ghi nó vào file products.json. 
✔ Sử dụng thư viện json để ghi dữ liệu. 
3) add_product(products): 
✔ Hỏi người dùng nhập thông tin cho một sản phẩm mới. 
✔ Tự động tạo mã sản phẩm mới (có thể dựa trên số lượng sản phẩm hiện có). 
✔ Thêm sản phẩm mới (dưới dạng dictionary) vào danh sách products. 
PAGE 4 
ITA102 - Assignment 
✔ Trả về danh sách đã được cập nhật. 
4) update_product(products): 
✔ Hỏi người dùng nhập mã sản phẩm cần cập nhật. 
✔ Tìm kiếm sản phẩm trong danh sách. Nếu không tìm thấy, thông báo lỗi. 
✔ Nếu tìm thấy, cho phép người dùng cập nhật lại Tên, Thương hiệu, Giá, và 
Số lượng. 
5) delete_product(products): 
✔ Hỏi người dùng nhập mã sản phẩm cần xóa và xóa nó khỏi danh sách. 
6) search_product_by_name(products): 
✔ Hỏi người dùng nhập một từ khóa. 
✔ Tìm và hiển thị tất cả các sản phẩm mà tên của chúng chứa từ khóa đó (không 
phân biệt hoa/thường). 
7) display_all_products(products): 
✔ Hiển thị toàn bộ sản phẩm trong kho một cách ngay ngắn, dễ đọc. 
✔ Nếu kho rỗng, hiển thị thông báo “Kho hàng trống.” 
Phần 3: Xây dựng giao diện người dùng 
1) Import module: Import các hàm cần thiết từ product_manager. 
2) Luồng chính: 
✔ Khi chương trình bắt đầu, hãy gọi hàm load_data() để tải danh sách sản phẩm 
vào một biến. 
✔ Sử dụng vòng lặp while True để hiển thị một menu chính với các lựa chọn 
tương ứng với các chức năng đã xây dựng ở Phần 2. 
✔ Thêm một lựa chọn để Thoát. Khi người dùng chọn thoát, hãy nhớ gọi hàm 
save_data() để lưu lại mọi thay đổi trước khi kết thúc chương trình.
