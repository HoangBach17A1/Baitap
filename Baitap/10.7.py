s = input("Nhập chuỗi của bạn: ")
s_sub = input("nhập chuốix s_hub: ")
s_find = input("nhập chuỗi s_find: ")
s_replace = input("nhập chuỗi s_replace: ")
print("chuỗi sau khi loại bỏ khoảng trắng ở dầu và cuối là: ", s.strip())
count = s.count(s_sub)
print("số lần chuỗi s_sub xuất hiện trong s: ", count)
chu_dau = s[0].upper()
print("chuỗi với chữ cái đầu tiên sau khi viết hoa là: ", chu_dau)
s_new = s.replace(s_find, s_replace)
print("chuỗi sau khi thay thế là:", s_new)