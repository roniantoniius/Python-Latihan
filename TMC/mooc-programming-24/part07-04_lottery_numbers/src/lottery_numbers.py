# Write your solution here
from random import randint
def lottery_numbers(amount: int, lower: int, upper: int) -> list:
    daftar = []

    for i in range(amount):
        angka = randint(lower, upper)
        if angka not in daftar:
            daftar.append(angka)

    return sorted(daftar)
if __name__ == "__main__":
    for number in lottery_numbers(7, 1, 39):
        print(number)