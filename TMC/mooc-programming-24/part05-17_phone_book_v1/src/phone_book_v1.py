# Write your solution here
telpon = {}
while True:
    tanya = int(input("command (1. search, 2. add, 3. quit):"))
    if tanya == 1:
        nama = str(input("name:"))
        if nama in telpon:
            print(telpon[nama])
        else:
            print("no number")
    elif tanya == 2:
        nama = str(input("name:"))
        telp = str(input("number:"))
        telpon[nama] = telp
        print("ok!")
    elif tanya == 3:
        print("quitting...")
        break