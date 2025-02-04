# Write your solution here
# Nama file untuk menyimpan kamus
filename = "dictionary.txt"

dictionary = {}
try:
    with open(filename, "r") as file:
        for line in file:
            finnish, english = line.strip().split(" - ")
            dictionary[finnish] = english
except FileNotFoundError:
    pass

while True:
    print("1 - Add word, 2 - Search, 3 - Quit")
    function = input("Function: ")

    if function == "1":
        finnish = input("The word in Finnish: ")
        english = input("The word in English: ")
        dictionary[finnish] = english
        
        with open(filename, "a") as file:
            file.write(f"{finnish} - {english}\n")
        
        print("Dictionary entry added")

    elif function == "2":
        search_term = input("Search term: ")
        found = False
        
        for finnish, english in dictionary.items():
            if search_term in finnish or search_term in english:
                print(f"{finnish} - {english}")
                found = True
        
        if not found:
            print("No entries found.")

    elif function == "3":
        print("Bye!")
        break

    else:
        print("Invalid option. Please choose 1, 2, or 3.")