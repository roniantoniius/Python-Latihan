# Write your solution here
import string

layer = int(input("Layers: "))
huruf = list(string.ascii_uppercase)

# ukuran matriksnya ada di (X*2) - 1
ukuran = layer * 2 - 1
mulai = 0

# bikin list semua huruf yang ada di layer terakhir nah nanti for loop untuk ubah itu pakai slicing
daftar = [[huruf[layer -1 ]for _ in range(ukuran)] for _ in range(ukuran)]

for baris in range(layer):
    # perulangan untuk kolom pada baris x
    for kolom in range(baris, ukuran - baris):
        # untuk awal
        daftar[baris][kolom] = huruf[baris]

        # untuk masukin di tengah
        daftar[ukuran - baris - 1][kolom] = huruf[baris]

        # untuk akhir
        daftar[kolom][baris] = huruf[baris]
        daftar[kolom][ukuran - baris - 1] = huruf[baris]
for row in daftar:
    print("".join(row))