# Write your solution here
lst = []

while True:
    print(f"The list is now {lst}")
    choice = input("a(d)d, (r)emove or e(x)it: ").strip()

    if choice == 'd':
        if lst:
            lst.append(lst[-1] + 1)
        else:
            lst.append(1)
    elif choice == 'r' and lst:
        lst.pop()
    elif choice == 'x':
        print("Bye!")
        break
