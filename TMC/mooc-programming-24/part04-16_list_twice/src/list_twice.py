# Write your solution here
lis = []
while True:
    satu = int(input("New item:"))
    if satu == 0:
        print("Bye!")
        break
    lis.append(satu)
    print(f"The list now: {lis}")
    sote = lis[:]
    sote.sort()
    print(f"The list in order: {sote}")