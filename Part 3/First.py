# Write your solution here
number = 0
while number < 30:
    number+=2
    print(number)

# Fix the program
print("Are you ready?")
number = int(input("Please type in a number: "))
while number > 0:
    print(number)
    number-=1
print("Now!")

# Write your solution here
num = int(input("Upper limit:"))
i = 1
while i < num:
    print(i)
    i+=1

# Write your solution here
number = 1
num = int(input("Upper limit:"))
while number <= num:
    print(number)
    number *= 2

# Write your solution here
num = int(input("Upper limit: "))
bas = int(input("Base: "))
i = 1
while i <= num:
    print(i)
    i *= bas

# Write your solution here
lim = int(input("Limit: "))
i = 0
j = 0
while j < lim:
    j+=i
    i+=1
print(j)


# Write your solution here
lim = int(input("Limit: "))
i = 0
j = 0
k = ""
while j < lim:
    i += 1
    j += i
    k += f"{i} + "
k = k[:-3]
print(f"The consecutive sum: {k} = {j}")

