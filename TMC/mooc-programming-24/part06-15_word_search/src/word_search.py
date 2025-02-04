# Write your solution here
import re

def find_words(search_term: str) -> list:
    kataKata = []
    
    # Membaca semua kata dari file
    with open("src/words.txt") as file:
        for words in file:
            word = words.strip()
            kataKata.append(word)
    
    hasil = []
    
    # Mengubah wildcard '*' menjadi regex
    # '*' di awal berarti kata bisa diawali dengan karakter apapun
    # '*' di akhir berarti kata bisa diakhiri dengan karakter apapun
    # '.' tetap sebagai wildcard untuk satu karakter
    pattern = search_term.replace('.', '.')
    pattern = pattern.replace('*', '.*')  # Mengganti '*' dengan '.*' untuk regex
    
    # Menambahkan anchor untuk mencocokkan seluruh kata
    regex = re.compile(f'^{pattern}$')
    
    for kata in kataKata:
        if regex.match(kata):
            hasil.append(kata)
    
    return hasil

# Contoh penggunaan
if __name__ == "__main__":
    print(find_words("*vokes"))
    print(find_words("ca."))
    print(find_words(".n.g"))