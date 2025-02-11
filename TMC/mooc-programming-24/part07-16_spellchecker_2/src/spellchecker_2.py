# Write your solution here
from difflib import get_close_matches

user = input("Write text: ")

with open('src/wordlist.txt') as file:
    word_list = []
    dafar = []
    for line in file:
        word_list.append(line.strip())
    for word in user.split(' '):
        if word.lower() in word_list:
            print(word, end=' ')
        else:
            dafar.append(word)
            print(f'*{word}*', end=' ')
    print("\nsuggestions:")
    for kata in dafar:
        rekomendasi = get_close_matches(kata, word_list)
        print(f"{kata}: {', '.join(rekomendasi)}")