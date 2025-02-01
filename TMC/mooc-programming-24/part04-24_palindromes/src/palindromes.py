def palindromes(teks: str) -> bool:
    return teks == teks[::-1]

while True:
    tugas = input("Please type in palindrome: ")
    if not palindromes(tugas):
        print("that wasn't a palindrome")
    else:
        print(f"{tugas} is a palindrome!")
        break
