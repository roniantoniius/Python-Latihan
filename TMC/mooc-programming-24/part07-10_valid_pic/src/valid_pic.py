# Write your solution here
from datetime import datetime;
def periksa_marker(marker: str) -> bool:
    validCuy = ["+", "-", "A"]
    if marker in validCuy:
        return True

def periksa_tahun(waktu, markerCentury) -> bool:
    if markerCentury == '+':
        tahun = 1800
    elif markerCentury == '-':
        tahun = 1900
    elif markerCentury == 'A':
        tahun = 2000

    hari = int(waktu[:2])
    bulan = int(waktu[2:4])
    tahun += int(waktu[4:6])

    try:
        waktus = datetime(tahun, bulan, hari)
    except Exception as e:
        return False
    return True
    
def periksa_control(pic: str) -> str:
    nines = int(''.join([x for x in pic[:-1] if x.isdigit()]))
    hasil = nines % 31
    karakter = '0123456789ABCDEFHJKLMNPRSTUVWXY'
    return karakter[hasil]

def is_it_valid(pic: str) -> bool:

    # # ambil data
    # waktu = pic[:6]
    # markerCentury = pic[6]
    # personalIdentifier = pic[7:10]
    # controlChar = pic[-1]

    if len(pic) == 11:
        cekTanda = periksa_marker(pic[6])
        if cekTanda:
            waktu = periksa_tahun(pic, pic[6])
            if waktu:
                hitungControl = periksa_control(pic)
                if hitungControl == pic[-1]:
                    return True
    return False



if __name__ == "__main__":
    print(is_it_valid("230827-906F"))