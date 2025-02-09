# Write your solution here
from datetime import datetime, timedelta
fileName = str(input("Filename: "))
waktuMulai = str(input("Starting date: "))
berapaHari = int(input("How many days: "))

# fileName = 'late_june.txt'
# waktuMulai = "24.6.2020"
# berapaHari  = 4

try:
    mulai = datetime.strptime(waktuMulai, "%d.%m.%Y")
except Exception as e:
    print(e)

waktuAkhir = mulai + timedelta(days=berapaHari-1)

waktu = f"Time period: {mulai.strftime("%d.%m.%Y")}-{waktuAkhir.strftime("%d.%m.%Y")}\n"

def ambil_data(mulai: datetime) -> dict:
    teks_waktu = {}
    print("Please type in screen time in minutes on each day (TV computer mobile):")
    for i in range(berapaHari):
        waktuBaru = mulai + timedelta(days=i)
        tek = str(input(f"Screen time {waktuBaru.strftime("%d.%m.%Y")}: "))
        teks_waktu[waktuBaru.strftime("%d.%m.%Y")] = tek
    return teks_waktu

data = ambil_data(mulai)

def menit(datas: dict) -> int:
    total = 0
    for _, value in datas.items():
        listAngka = value.split(' ')
        for i in listAngka:
            total += int(i)
    return total

hitung_menit = menit(data)
rataRata = hitung_menit / berapaHari

with open(fileName, "w") as fileBaru:
    fileBaru.write(waktu)
    fileBaru.write(f"Total minutes: {hitung_menit}\n")
    fileBaru.write(f"Average minutes: {rataRata}\n")
    for k, v in data.items():
        fileBaru.write(f"{k}: {v.replace(' ', '/')}\n")

    print(f"Data stored in file {fileName}")