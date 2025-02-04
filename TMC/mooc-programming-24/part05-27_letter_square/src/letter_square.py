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
        daftar[baris][kolom] = huruf[layer-baris-1]

        # untuk masukin di tengah
        daftar[ukuran - baris - 1][kolom] = huruf[layer-baris-1]

        # untuk akhir
        daftar[kolom][baris] = huruf[layer-baris-1]
        daftar[kolom][ukuran - baris - 1] = huruf[layer-baris-1]
for row in daftar:
    print("".join(row))