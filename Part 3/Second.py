# Write your solution here
st = str(input("Please type in a string:"))
it = int(input("Please type in an amount:"))
print(st * it)

# Write your solution here
string1 = input("Please type in string 1: ")
string2 = input("Please type in string 2: ")

if len(string1) > len(string2):
    print(f"{string1} is longer")
elif len(string1) < len(string2):
    print(f"{string2} is longer")
else:
    print("The strings are equally long")

# Write your solution here
string = input("Please type in a string: ")
for char in reversed(string):
    print(char)

# Write your solution here
string = input("Please type in a string: ")

if len(string) < 2:
    print("The string is too short to compare.")
else:
    second_char = string[1]
    second_to_last_char = string[-2]
    
    if second_char == second_to_last_char:
        print(f"The second and the second to last characters are {second_char}")
    else:
        print("The second and the second to last characters are different")

# Write your solution here
pagar = int(input("Width:"))
print("#" * pagar)

# Write your solution here
lebar = int(input("Width:"))
tinggi = int(input("Height:"))
i = 0
while i < tinggi:
    print("#" * lebar)
    i+=1

# Write your solution here
while True:
    string = input("Please type in a string: ")
    
    if string == "":
        break
    
    print(string)
    print('-' * len(string))

# Write your solution here
string = input("Please type in a string: ")

stars_needed = 20 - len(string)

output_string = '*' * stars_needed + string

print(output_string)

# Write your solution here
kata = input("Word: ")
print("*" * 30)

cetakKata = 30 - len(kata) - 2 
setengah = cetakKata // 2
kosong = ' ' * setengah

if cetakKata % 2 != 0:
    output = "*" + kosong + kata + kosong + " " + "*"
else:
    output = "*" + kosong + kata + kosong + "*"

print(output)
print("*" * 30)

# Write your solution here
s = input("Please type in a string: ")
for i in range(1, len(s) + 1):
    print(s[:i])

# Write your solution here
s = input("Please type in a string: ")
for i in range(len(s)):
    if s[i] == s[-1]:
        print(s[i:])


# Write your solution here
s = input("Please type in a string: ")

a_found = "a found" if 'a' in s else "a not found"
e_found = "e found" if 'e' in s else "e not found"
o_found = "o found" if 'o' in s else "o not found"

print(a_found)
print(e_found)
print(o_found)

# Write your solution here
s = input("Please type in a word: ")
c = input("Please type in a character: ")

index = s.find(c)
if index != -1 and index + 3 <= len(s):
    print(s[index:index + 3])

s = input("Please type in a word: ")
c = input("Please type in a character: ")

for i in range(len(s) - 2):
    if s[i] == c:
        print(s[i:i + 3])

# Write your solution here
first = input("Please type in a string: ")
sub = input("Please type in a substring: ")
i = 0
jumpa = 0

while i <= len(first) - len(sub):
    if first[i:i + len(sub)] == sub:
        jumpa += 1
        if jumpa == 2:
            print(f"The second occurrence of the substring is at index {i}.")
            break
        i += len(sub)
    else:
        i += 1

if jumpa < 2:
    print("The substring does not occur twice in the string.")