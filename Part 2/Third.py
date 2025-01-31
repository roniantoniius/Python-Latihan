# Write your solution here
while True:
    print("Hi")
    s = str(input("Shall we continue?"))
    if s == "no":
        print("okay then")
        break

import math
from math import sqrt
# Write your solution here
while True:
    number = int(input("Please type in a number: "))
    
    if number < 0:
        print("Invalid number")
    elif number > 0:
        sqrt_value = math.sqrt(number)
        print(float(sqrt_value))
    else:
        print("Exiting...")
        break

number = 5
print("Countdown!")
while True:
    print(number)
    number -= 1
    if number < 1:
        break

print("Now!")

# Write your solution here
p1 = str(input("Password"))
while True:
    p2 = str(input("Repeat password:"))

    if p1 != p2:
        print("They do not match!")
    else:
        break
print("User account created!")

# Write your solution here
atemp = 0
while True:
    st = int(input("PIN:"))
    atemp += 1
    if st == 4321 and atemp == 1:
        print("Correct! It only took you one single attempt!")
        break
    if st != 4321:
        print("Wrong")
    else:
        print(f"Correct! It took you {atemp} attempts")
        break

# Write your solution here
year = int(input("Year: "))

next_year = year + 1

while True:
    if (next_year % 4 == 0 and next_year % 100 != 0) or (next_year % 400 == 0):
        break
    next_year += 1

print(f"The next leap year after {year} is {next_year}")

# Write your solution here
words = ""
last = None
while True:
    word = str(input("Please type in a word:"))

    if word == "end" or word == last:
        break
    
    words += word + " "
    last = word

print(words)

# Write your solution here
atemp = 0
jml = 0
pos = 0
min = 0
print("Please type in integer numbers. Type in 0 to finish.")
while True:
    num = int(input("Number:"))
    if num == 0:
        break
    atemp += 1
    jml += num
    if num > 0:
        pos += 1
    else:
        min +=1

print(f"Numbers typed in {atemp}")
print(f"The sum of numbers is {jml}")
if (atemp > 0):
    print(f"The mean of the numbers is {jml / atemp}")
else:
    print("No positive numbers were entered, so the mean cannot be calculated.")

print(f"Positive numbers {pos}")
print(f"Negative numbers {min}")