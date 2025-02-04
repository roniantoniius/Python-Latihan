# Write your solution here
from string import ascii_lowercase
from random import randint
import string
def generate_password(jumlah: int) -> str:
    daftar_lower = list(string.ascii_lowercase)
    kataKata = ''
    for i in range(jumlah):
        acak = randint(0, len(daftar_lower)-1)
        kataKata += daftar_lower[acak]
    return kataKata

if __name__ == "__main__":
    for i in range(10):
        print(generate_password(8))