# Write your solution here
daftar = [1,2,3,4,5]
while True:
    ind = int(input("Index:"))
    if ind == -1:
        break
    new = int(input("New value:"))
    daftar[ind] = new
    print(daftar)