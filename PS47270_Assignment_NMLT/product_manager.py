import json


#Hàm đọc file 
def load_data():
    """
    Đọc dữ liệu từ file json

    Returns:
        Trả về một list chứa các dict sản phẩm. Nếu không thấy file, trả về list rỗng [ ]
    """
    try:
        with open ('products.json', 'r', encoding = 'utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print("Không tìm thấy file, vui lòng kiểm tra lại!")
        return []


#Hàm ghi file
def save_data(products):
    """
    Ghi dữ liệu mới vào file json

    Args:
        products (list): 1 list chứa nhiều dictionary
    """
    with open ('products.json', 'w', encoding='utf-8') as f:
        json.dump(products, f, ensure_ascii=False, indent=4)


# 1. Hàm thêm sản phẩm
def add_product(products):
    """
    Thêm 1 sản phẩm từ việc nhập từng thông tin của sản phẩm.
    
    Mỗi lần thêm 1 sản phẩm thì ID sẽ tự động tạo mới không trùng lặp do cộng 1 từ số ID lớn nhất.

    Nếu sản phẩm đã có trong kho thì tự động cập nhật số lượng.

    Args:
        products (list): 1 list chứa nhiều dictionary

    Return:
        list: Danh sách đã được cập nhật thêm mới hoặc cộng dồn số lượng.
    """
    product_name = input("Vui lòng nhập tên sản phẩm: ")
    brand = input("Vui lòng nhập thương hiệu: ")

    while True:
        try:
            price = int(input("Vui lòng nhập giá: "))
            break
        except ValueError:
            print("Vui lòng nhập lại con số hợp lệ!")
    
    while True:
        try:
            inventory = int(input("Vui lòng nhập số lượng: "))
            break
        except ValueError:
            print("Vui lòng nhập lại con số hợp lệ!")
    
    is_exist = False
    for item in products:
        if product_name.lower().strip() == item['product_name'].lower().strip() and brand.lower().strip() == item['brand'].lower().strip():
            is_exist = True
            print(f"\nSản phẩm {item['product_name']} đã có trong kho")
            choice = input("Bạn có muốn cộng thêm vào số lượng tồn kho không? (y/n): ")
            if choice == "y":
                item['inventory'] += inventory
                print(f"Đã cập nhật số lượng tồn kho cho sản phẩm {item['product_name']} mã sp: {item['ID']}")
                save_data(products)
                return products
            else:
                return products
    
    # ID = f"LT0{len(products) + 1}"
    lst_ID_num = []
    if not products:
        ID = "LT01"
    else:
        for item in products:
            lst_ID_num.append(int(item['ID'][2:]))
        ID = f"LT{max(lst_ID_num) + 1:02d}"  
    
    confirm = input("Xác nhận thêm sản phẩm này (y/n): ")
    if confirm == "y":
        items = {
            'product_name': product_name,
            'brand': brand,   
            'price': price,
            'inventory': inventory,
            'ID': ID
        }
        products.append(items)
        save_data(products)
        print("Thêm thành công !")
    else:
        print("Thêm sản phẩm thất bại!")
    return products


# 2. Hàm hiện ra danh sách sản phẩm 
def display_all_products(products):
    """In ra danh sách sản phẩm đã được định dạng f-string.
    
    Args:
        products (list): 1 list chứa nhiều dictionary.
    """
    if not products:
        print("\nKho hàng trống!")
    else:
        print(f"{'ID':<5}|{'Tên sản phẩm':^30}|{'Thương hiệu':^15}|{'Giá (VND)':^15}|{'Tồn kho (sp)':^5}")
        print("-"*76)
        for item in products:
            format_inventory = f"{item['inventory']:02d}"
            format_price = f"{item['price']:,}"
            print(f"{item['ID']:<5}|{item['product_name']:<30}|{item['brand']:<15}|{format_price:^15} VND|{format_inventory:^5}")
        print("-"*76)    


# Hàm chỉ cho người dùng nhập số hoặc bỏ trống để thay đổi hoặc giữ giá trị cũ từ hàm input
def get_number_input(string, old_value):
    """
    Hàm bổ trợ cho hàm update.

    Hỗ trợ lấy dữ liệu số từ người dùng hoặc giữ lại giá trị cũ nếu bỏ trống.

    Hàm này sẽ lặp cho đến khi người dùng nhập đúng định dạng số hoặc nhấn Enter.
    Thường dùng cho chức năng cập nhật thông tin sản phẩm.

    Args:
        string (str): Câu thông báo hiển thị cho người dùng (Prompt).
        old_value (int): Giá trị hiện tại của sản phẩm để trả về nếu người dùng bỏ qua.

    Returns:
        int: Giá trị số mới được nhập hoặc giá trị cũ nếu người dùng nhấn Enter.
    """
    while True:
        user_input = input(string).strip()
        if user_input == "":
            return old_value
        elif user_input.isdigit() == False:
            print("\nVui lòng nhập số\n")
        else:
            return int(user_input)


# 3. Hàm cập nhật sản phẩm
def update_product(products):
    """
    Cho phép thay đổi các thông tin một dictionary trong list bằng cách duyệt qua key 'ID'

    Args:
        products (list): 1 list chứa nhiều dictionary.
    """
    ID_update = input("Vui lòng nhập ID sản phẩm cần chỉnh sửa: ")
    found = False
    for item in products:
        if ID_update.lower().strip() == item['ID'].lower().strip():
            found = True
            print("\nThông tin sản phẩm cần sửa:")
            format_inventory = f"{item['inventory']:02d}"
            format_price = f"{item['price']:,} VND"
            print(f"{item['ID']:<5}|{item['product_name']:<30}|{item['brand']:<15}|{format_price:<15}|{format_inventory:<5}\n")
            new_product_name = input("\nVui lòng nhập tên mới cho sản phẩm (nhấn Enter để bỏ qua): ")
            new_brand = input("Vui lòng nhập tên thương hiệu mới (nhấn Enter để bỏ qua): ")
            new_price = get_number_input("Vui lòng nhập giá mới (nhấn Enter để bỏ qua): ", item['price'])
            new_inventory = get_number_input("Vui lòng nhập lại số lượng (nhấn Enter để bỏ qua): ", item['inventory'] ) 
            print()
            confirm = (input("Xác nhận thay đổi(y/n): "))
            if confirm.lower().strip() == "y":
                if new_product_name != "":
                    item['product_name'] = new_product_name
                if new_brand != "":
                    item['brand'] = new_brand
                item['price'] = new_price
                item['inventory'] = new_inventory
                save_data(products)
                print("\nCập nhật thông tin sản phẩm thành công !")
            else:
                print("\nSản phẩm chưa được lưu!")
            break
    if found == False:
        print("\nKhông tìm thấy mã sản phẩm này!")


# 4. Hàm xóa sản phẩm
def delete_product(products):
    """
    Cho phép xóa một dictionary trong list bằng cách duyệt qua key 'ID'

    Args:
        products (list): 1 list chứa nhiều dictionary.
    """
    ID_del = input("Vui lòng nhập ID cần xóa: ")
    print("-"*80,"\n")
    found = False
    for item in products:
        if ID_del.lower().strip() == item['ID'].lower().strip():
            found = True
            print("Sản phẩm bạn muốn xóa là:")
            print(f"{'ID':<5}|{'Tên sản phẩm':^30}|{'Thương hiệu':^15}|{'Giá (VND)':^15}|{'Tồn kho (sp)':^5}")
            format_inventory = f"{item['inventory']:02d}"
            format_price = f"{item['price']:,} VND"
            print(f"{item['ID']:<5}|{item['product_name']:<30}|{item['brand']:<15}|{format_price:<15}|{format_inventory:^5}\n")
            confirm = input("Bạn có muốn xóa vĩnh viễn sản phẩm này không? (y/n): ")
            if confirm.lower().strip() == "y":
                products.remove(item)
                save_data(products)
                print("\nXóa thành công!")
            else:
                print("\nXóa thất bại!")
            break
    if not found:
        print("\nKhông tìm thấy mã sản phẩm này!")
        

# 5. Hàm tìm sản phẩm theo keyword
def search_product_by_name(products):
    """
    Hiển thị các dictionary phù hợp với ký tự người dùng nhập vào bằng toán tử in

    Args:
        products (list): 1 list chứa nhiều dictionary.
    """
    key_word = input("Vui lòng nhập từ khóa bạn muốn tìm: ")
    clean_keyword = key_word.lower().strip()
    lst_products = []
    found = False
    for item in products:
        if clean_keyword in item['product_name'].lower() or clean_keyword in item['brand'].lower() :
            found = True
            lst_products.append(item)
    if found == False:
        print("Không tìm thấy sản phẩm thích hợp với tìm kiếm của bạn")
    else:
        display_all_products(lst_products)


# 6. (Mở rộng) Tìm kiếm sản phẩm theo giá thấp nhất hoặc cao nhất
def sort_product_by_price(products):
    """
    Cho phép người dùng xem danh sách theo giá thấp nhất hoặc cao nhất bằng cách chọn.

    Args:
        products (list): 1 list chứa nhiều dictionary
    """
    products_copy = products.copy()
    while True:
        try:
            print("1. Xem danh sách theo giá tăng dần")
            print("2. xem danh sách theo giá giảm dần")
            print("3. Quay ra meuu chính")
            choice = int(input("Vui lòng chọn kiểu xem danh sách (1/2/3): "))
            match choice:
                case 1: 
                    for i in range (len(products_copy) - 1):
                        for j in range (i+1, len(products_copy)):
                            if products_copy[i]['price'] > products_copy[j]['price']:
                                products_copy[i], products_copy[j] = products_copy[j], products_copy[i]
                    print("\nDanh sách giá tăng dần")
                    display_all_products(products_copy)
                case 2:
                    for i in range (len(products_copy) - 1):
                        for j in range (i+1, len(products_copy)):
                            if products_copy[i]['price'] < products_copy[j]['price']:
                                products_copy[i], products_copy[j] = products_copy[j], products_copy[i]
                    print("\nDanh sách giá giảm dần")
                    display_all_products(products_copy)
                case 3:
                    break
                case _:
                    print("Vui lòng nhập số 1/2/3")
        except ValueError:
            print("Vui lòng nhập số 1/2/3") 
            print()                           