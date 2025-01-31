# Write your solution here
umur = int(input("How old are you?"))
if umur >= 18:
    print("You are of age!")
else:
    print("You are not of age!")

# Write your solution here
angka1 = int(input("Please type in the first number:"))
angka2 = int(input("Please type in another number:"))

if angka1 == angka2:
    print("The numbers are equal!")
elif angka1 > angka2:
    print("The greater number was:", angka1)
else:
    print("The greater number was:", angka2)

# Write your solution here
print("Person 1:")
nama1 = str(input("Name:"))
age1 = int(input("Age:"))
print("Person 2:")
nama2 = str(input("Name:"))
age2 = int(input("Age:"))
if age1 == age2:
    print(f"{nama1} and {nama2} are the same age")
elif age1 > age2:
    print(f"The elder is {nama1}")
else:
    print(f"The elder is {nama2}")


# Write your solution here
kata1 = str(input("Please type in the 1st word:"))
kata2 = str(input("Please type in the 2nd word:"))
if kata1 == kata2:
    print("You gave the same word twice.")
elif kata1 < kata2:
    print(f"{kata2} comes alphabetically last.")
else:
    print(f"{kata1} comes alphabetically last.")

# Write your solution here
age = input("What is your age? ")

try:
    age = int(age)
    
    if age < 0:
        print("That must be a mistake")
    elif age < 5:
        print("I suspect you can't write quite yet...")
    else:
        print(f"Ok, you're {age} years old")
        
except ValueError:
    print("Please enter a valid number for your age.")

# Write your solution here
name = str(input("Please type in your name:"))
if name == "Huey" or name == "Dewey" or name == "Louie":
    print("I think you might be one of Donald Duck's nephews.")
elif name == "Morty" or name == "Ferdie":
    print("I think you might be one of Mickey Mouse's nephews.")
else:
    print("You're not a nephew of any character I know of.")

# Write your solution here
points = int(input("How many points [0-100]: "))

if points < 0 or points > 100:
    print("Grade: impossible!")
elif points < 50:
    print("Grade: fail")
elif points < 60:
    print("Grade: 1")
elif points < 70:
    print("Grade: 2")
elif points < 80:
    print("Grade: 3")
elif points < 90:
    print("Grade: 4")
elif points <= 100:
    print("Grade: 5")

# Write your solution here
num = int(input("Number:"))
if  num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
elif num % 5 == 0:
    print("Buzz")
elif num % 3 == 0:
    print("Fizz")

# Write your solution here
year = int(input("Please type in a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("That year is a leap year.")
else:
    print("That year is not a leap year.")

# Write your solution here
first_letter = input("1st letter: ")
second_letter = input("2nd letter: ")
third_letter = input("3rd letter: ")

if (first_letter <= second_letter <= third_letter) or (third_letter <= second_letter <= first_letter):
    middle_letter = second_letter
elif (second_letter <= first_letter <= third_letter) or (third_letter <= first_letter <= second_letter):
    middle_letter = first_letter
else:
    middle_letter = third_letter

print(f"The letter in the middle is {middle_letter}")

# Write your solution here
gift_value = float(input("Value of gift: "))

if gift_value < 5000:
    print("No tax!")
elif 5000 <= gift_value < 25000:
    tax = 100 + (gift_value - 5000) * 0.08
    print(f"Amount of tax: {tax:.1f} euros")
elif 25000 <= gift_value < 55000:
    tax = 1700 + (gift_value - 25000) * 0.10
    print(f"Amount of tax: {tax:.1f} euros")
elif 55000 <= gift_value < 200000:
    tax = 4700 + (gift_value - 55000) * 0.12
    print(f"Amount of tax: {tax:.1f} euros")
elif 200000 <= gift_value < 1000000:
    tax = 22100 + (gift_value - 200000) * 0.15
    print(f"Amount of tax: {tax:.1f} euros")
else:  # gift_value >= 1000000
    tax = 142100 + (gift_value - 1000000) * 0.17
    print(f"Amount of tax: {tax:.1f} euros")