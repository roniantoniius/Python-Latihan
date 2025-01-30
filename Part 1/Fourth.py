# Write your solution here
number = int(input("Please type in a number:"))
print(f"{number} times 5 is {number*5}")

# Write your solution here
name = str(input("What is your name?"))
umur = int(input("Which year were you born?"))
print(f"Hi {name}, you will be {2021-umur} years old at the end of the year 2021")

# Write your solution here
day = int(input("How many days?"))
print(f"Seconds in that many days: {day*24*60*60}")

# Fix the code
number1 = int(input("Please type in the first number: "))
number2 = int(input("Please type in the second number: "))
number3 = int(input("Please type in the third number: "))

product = number1 * number2 * number3

print("The product is", product)


# Write your solution here
number1 = int(input("Number 1:"))
number2 = int(input("Number 2:"))
print(f"The sum of the numbers: {number1+number2}")
print(f"The product of the numbers: {number1*number2}")

# Write your solution here
number1 = int(input("Number 1:"))
number2 = int(input("Number 2:"))
number3 = int(input("Number 3:"))
number4 = int(input("Number 4:"))
sums = number1+number2+number3+number4
mean = sums / 4 
print(f"The sum of the numbers is {sums} and the mean is {mean}")

# Write your solution here
q1 = int(input("How many times a week do you eat at the student cafeteria?"))
q2 = float(input("The price of a typical student lunch?"))
q3 = float(input("How much money do you spend on groceries in a week?"))
print("")
print("Average food expenditure")
week = q1 * q2 + q3
perp = week / 7
print(f"Daily: {perp} euros")
print(f"Weekly: {week} euros")

# Write your solution here
jumlah = int(input("How many students on the course?"))
group = int(input("Desired group size?"))
hasil = jumlah / group
if hasil % 2 == 0:
    print(f"Number of groups formed: {hasil}")
else:
    hasill = jumlah // group + 1
    print(f"Number of groups formed: {hasill}")

