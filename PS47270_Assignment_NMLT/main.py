import product_manager as pm


products = pm.load_data() #Đọc file và lưu vào 1 list
while True:
    try:
        print("\n--> App Quản Lý Kho Cửa Hàng Laptop <--")
        print("-"*39)
        print("1. Thêm sản phẩm")
        print("2. Xem toàn bộ sản phẩm")
        print("3. Thay đổi thông tin sản phẩm")
        print("4. Xóa sản phẩm")
        print("5. Tìm sản phẩm theo từ khóa")
        print("6. (Mở rộng) Xem danh sách theo tăng dần hoặc giảm dần")
        print("7. Thoát")
        choice = int(input("Vui lòng chọn chức năng(1/2/3/4/5/6/7): "))
        print("="*80)
        match choice:
            case 1:
                print("\n--> Thêm sản phẩm <--\n")
                pm.add_product(products)
                print("="*80)
            case 2:
                print("\n--> Xem toàn bộ sản phẩm <--\n")
                pm.display_all_products(products)
                print("="*80)
            case 3:
                print("\n--> Thay đổi thông tin sản phẩm <--\n")
                pm.display_all_products(products)
                pm.update_product(products) 
                print("="*80)
            case 4:
                print("--> Xóa sản phẩm <--\n")
                pm.display_all_products(products)
                pm.delete_product(products)
                print("="*80)
            case 5:
                print("--> Tìm sản phẩm theo từ khóa <--\n")
                pm.search_product_by_name(products)
                print("="*80)
            case 6:
                print("--> (Mở rộng) Xem danh sách theo tăng dần hoặc giảm dần <--")
                pm.sort_product_by_price(products)
                print("="*80)
            case 7:
                pm.save_data(products)
                print("\nCảm ơn bạn đã sử dụng app!\n")
                print("="*80)
                print()
                break
            case _:
                print("Không có chức năng này. Vui lòng chọn lại!\n")
    except :
        print("\nvui lòng chỉ nhập số từ 1 đến 7 để chọn chức năng\n")
    print("Bạn muốn sử dụng chức năng khác không ?")