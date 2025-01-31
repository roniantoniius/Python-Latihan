# Fix the program
number = int(input("Please type in a number: "))
if number > 100:
    print("The number was greater than one hundred")
    number -= 100
    print("Now its value has decreased by one hundred")
    print("Its value is now", number)
print(number, "must be my lucky number!")
print("Have a nice day!")

# Write your solution here
masuk = str(input("Please type in a word:"))
if len(masuk) < 2:
    print("Thank you!")
elif len(masuk) > 2:
    print(f"There are {len(masuk)} letters in the word {masuk}")
    print("Thank you!")

# Write your solution here
angka = float(input("Please type in a number:"))
print(f"Integer part: {int(angka)}")
s = float(angka - int(angka))
print(f"Decimal part: {s}")

