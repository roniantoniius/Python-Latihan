# Write your solution here
from random import sample;
def words(n: int, huruf: str) -> list:
    new_file = open("src/words.txt").read().split()
    file = [kata for kata in new_file if kata.startswith(huruf)]
    coba = sample(file, n)

    if len(coba) < n:
        raise ValueError("Not enough suitable words can be found!")
    return coba

if __name__ == "__main__":
    word_list = words(3, "ca")
    for word in word_list:
        print(word)