# Write your solution here
angka = int(input("Please type in a number:"))
j = 1
while j <= angka:
    i = 1
    while i <= angka:
        print(f"{j} x {i} = {i*j}")
        i+=1
    j+=1

# Write your solution here
st = str(input("Please type in a sentence:"))
daftar = st.split()
for kata in daftar:
    print(kata[0])

# Write your solution here
while True:
    fac = int(input("Please type in a number: "))
    
    if fac <= 0:
        print("Thanks and bye!")
        break
    else:
        i = 1
        sum = 1
        while i <= fac:
            sum *= i
            i += 1
        
        print(f"The factorial of the number {fac} is {sum}")

# Write your solution here
teks = int(input("Please type in a number:"))
i = 1
while i <= teks:
    if i + 1 <= teks:
        print(f"{i+1}")
    print(i)
    i += 2

# Write your solution here
teks = int(input("Please type in a number:"))
i = 1
j = teks
while i <= j:
    print(i)
    if j != i:
        print(j)
    i+=1
    j-=1

# Write your solution here
# You can test your function by calling it within the following block
# if __name__ == "__main__":
#   seven_brothers()
def seven_brothers():
    stra = ["Aapo", "Eero", "Juhani", "Lauri", "Simeoni", "Timo", "Tuomas"]
    for na in stra:
        print(na)

if __name__ == "__main__":
    seven_brothers()

def first_character(text):
# write your code here
    print(text[0])
# testing the function:
if __name__ == "__main__":
    first_character('python')
    first_character('yellow')
    first_character('tomorrow')
    first_character('heliotrope')
    first_character('open')
    first_character('night')

# Write your code here
# Testing the function
def mean(num1, num2, num3):
    mean = num1 + num2 + num3
    meanS = mean / 3
    print(meanS)
if __name__ == "__main__":
    mean(1, 2, 3)

# Write your solution here
def print_many_times(txt, n):
    for _ in range(n):
        print(txt)
# You can test your function by calling it within the following block
if __name__ == "__main__":
    print_many_times("python", 5)

# Write your solution here
def hash_square(number):
    for _ in range(number):
        print("#" * number)
# You can test your function by calling it within the following block
if __name__ == "__main__":
    hash_square(5)

# Write your solution here
def chessboard(number):
    for i in range(number):
        for j in range(number):
            # kalau genap dia 1 kalau ganjil dia 0, genap disini antara i dan j
            print("1" if (i + j) % 2 == 0 else "0", end="")
        print()
# Testing the function
if __name__ == "__main__":
    chessboard(3)

