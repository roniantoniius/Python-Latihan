# Write your solution here
from string import ascii_letters, punctuation
def separate_characters(word: str) -> tuple:
    pertama = ""
    kedua = ""
    keiga = ""
    for kata in word:
        if kata in ascii_letters:
            pertama += kata
        elif kata in punctuation:
            kedua += kata
        else:
            keiga += kata
    return (pertama, kedua, keiga)
if __name__ == "__main__":
    parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")
    print(parts[0])
    print(parts[1])
    print(parts[2])