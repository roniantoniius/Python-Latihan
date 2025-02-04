# Write your solution here
from string import ascii_lowercase, digits
from random import randint, choice
import string
def generate_strong_password(jumlah: int, second: bool, third: bool) -> str:
    # huruf pertama
    pertama = choice(ascii_lowercase)
    spesial = "!?=+-()#"
    daftarLower = ascii_lowercase

    # kalau second True
    if second:
        pertama = tambah_karakter(pertama, digits)
        daftarLower+=digits

    if third:
        pertama = tambah_karakter(pertama, spesial)
        daftarLower+=spesial
    
    #sisanya
    while (len(pertama) < jumlah):
        pertama = tambah_karakter(pertama, daftarLower)

    return pertama

def tambah_karakter(pertama: str, karakter) -> str:
    karakterSekarang = choice(karakter)
    if randint(1,2) == 1:
        return karakterSekarang + pertama
    else:
        return pertama + karakterSekarang

if __name__ == "__main__":
    for i in range(10):
        print(generate_strong_password(8, True, True))