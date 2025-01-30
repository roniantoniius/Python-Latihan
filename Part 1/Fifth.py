from math import *;
# Write your solution here
number = int(input("Please type in a number:"))
if number == 1984:
    print("Orwell")

# Write your solution here
number = int(input("Please type in a number:"))
if number > 0:
    print(f"The absolute value of this number is {number}")
else:
    print(f"The absolute value of this number is {number*-1}")

# Write your solution here
name = str(input("Please tell me your name:"))
if name == "Jerry":
    print("Next please!")
else:
    how = int(input("How many portions of soup?"))
    if name != "jerry":
        print(f"The total cost is {how*5.90}")
        print("Next please!")

# Write your solution here
number = int(input("Please type in a number:"))
if number >= 1000:
    print("Thank you!")
elif number < 1000:
    print("This number is smaller than 1000")
    if number < 100:
        print("This number is smaller than 100")
        if number < 10:
            print("This number is smaller than 10")
    print("Thank you!")

# Write your solution here
number1 = int(input("Number 1: "))
number2 = int(input("Number 2: "))
operation = input("Operation: ").strip().lower()

if operation == "add":
    result = number1 + number2
    print(f"{number1} + {number2} = {result}")
elif operation == "multiply":
    result = number1 * number2
    print(f"{number1} * {number2} = {result}")
elif operation == "subtract":
    result = number1 - number2
    print(f"{number1} - {number2} = {result}")
else:
    pass

# Write your solution here
fahrenheit = float(input("Please type in a temperature (F): "))
celsius = (fahrenheit - 32) * 5 / 9

print(f"{fahrenheit} degrees Fahrenheit equals {celsius} degrees Celsius")

if celsius < 0:
    print("Brr! It's cold in here!")

# Write your solution here
hourly_wage = float(input("Hourly wage: "))
hours_worked = float(input("Hours worked: "))
day_of_week = input("Day of the week: ").strip().lower()

if day_of_week == "sunday":
    daily_wages = hourly_wage * hours_worked * 2
else:
    daily_wages = hourly_wage * hours_worked

print(f"Daily wages: {daily_wages} euros")

# Fix the program
points = int(input("How many points are on your card? "))
if points < 100:
    points *= 1.1
    print("Your bonus is 10 %")
elif points >= 100:
    points *= 1.15
    print("Your bonus is 15 %")

print("You now have", points, "points")

# Write your solution here
temperature = int(input("What is the weather forecast for tomorrow?\nTemperature: "))
will_rain = input("Will it rain (yes/no): ").strip().lower()

if temperature > 20:
    print("Wear jeans and a T-shirt")
elif temperature > 10:
    print("Wear jeans and a T-shirt")
    print("I recommend a jumper as well")
elif temperature > 5:
    print("Wear jeans and a T-shirt")
    print("I recommend a jumper as well")
    print("Take a jacket with you")
else:
    print("Wear jeans and a T-shirt")
    print("I recommend a jumper as well")
    print("Take a jacket with you")
    print("Make it a warm coat, actually")
    print("I think gloves are in order")

if will_rain == "yes":
    print("Don't forget your umbrella!")

# Write your solution here
# Let's take the square root of math-module in use
from math import sqrt

# Note that the square root can also be calculated using power.
# sqrt(9) is equivalent to 9 ** 0.5

# Get coefficients from the user
a = float(input("Value of a: "))
b = float(input("Value of b: "))
c = float(input("Value of c: "))

# Calculate the discriminant
discriminant = b**2 - 4*a*c

# Calculate the two roots using the quadratic formula
root1 = (-b + sqrt(discriminant)) / (2 * a)
root2 = (-b - sqrt(discriminant)) / (2 * a)

# Print the results
print(f"The roots are {root1} and {root2}")