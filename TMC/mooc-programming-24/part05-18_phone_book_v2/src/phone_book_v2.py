# Write your solution here
telpon = {}
while True:
    tanya = int(input("command (1. search, 2. add, 3. quit):"))
    if tanya == 1:
        nama = input("name:")
        if nama in telpon:
            for i in telpon[nama]:
                print(i)
        else:
            print("no number")
    elif tanya == 2:
        nama = input("name:")
        telp = input("number:")
        if nama in telpon:
            telpon[nama].append(telp)
        else:
            telpon[nama] = [telp]
        print("ok!")
    elif tanya == 3:
        print("quitting...")
        break