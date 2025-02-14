# Write your solution here
import string
def change_case(orig_string: str) -> str:
    kata = ""
    for huruf in orig_string:
        if huruf.islower():
            kata += huruf.upper()
        else:
            kata += huruf.lower()
    return kata

def split_in_half(orig_string: str) -> tuple:
    awal = ""
    akhir = ""
    panjang = len(orig_string)
    tengah = panjang // 2
    for i in range(panjang):
        if i < tengah:
            awal += orig_string[i]
        else:
            akhir += orig_string[i]
    return awal, akhir

def remove_special_characters(orig_string: str) -> str:
    huruf = ""
    for kata in orig_string:
        if kata.isalnum() or kata.isspace():
            huruf += kata
    return huruf