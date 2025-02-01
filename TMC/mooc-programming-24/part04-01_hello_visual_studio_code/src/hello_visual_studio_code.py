# Write your solution here
while True:
    ets = str(input("Editor:"))
    ets1 = ets.lower()
    if ets1 == "visual studio code":
        print("an excellent choice!")
        break
    elif ets1 == "word" or ets1 == "notepad":
        print("awful")
    else:
        print("not good")
