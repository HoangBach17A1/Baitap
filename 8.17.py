a =int(input("nhập vào số a:"))
b =int(input("nhập vào số b:"))
temp_a = a
temp_b = b
while temp_a != temp_b:
    if temp_a < temp_b:
        temp_a += a
    else:
        temp_b += b
bcnn = temp_a
print("Bội chung nhỏ nhất của hai số là:" ,bcnn)