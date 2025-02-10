# Write your solution here
from datetime import datetime, timedelta
import csv
def cheaters() -> list:
    daftarMulai = []
    with open("src/start_times.csv", mode='r', encoding='utf-8') as mulai:
        for baris in mulai:
            nama, waktu = baris.strip().split(";")
            jam, menit = map(int, waktu.split(":"))
            sekarang = timedelta(hours=jam, minutes=menit)
            daftarMulai.append({'name':nama, 'time': sekarang})
    
    daftarAkhir = []
    with open("src/submissions.csv", mode='r', encoding='utf-8') as start:
        for daftar in start:
            name, task, points, waktus = daftar.strip().split(";")
            jams, menits = map(int, waktus.split(":"))
            akhir = timedelta(hours=jams, minutes=menits)
            daftarAkhir.append({'name': name, 'task': task, 'points': points, 'time': akhir})

    curang = set()
    for i in daftarMulai:
        for j in daftarAkhir:
            if i["name"] == j["name"] and j["time"] - i["time"] > timedelta(hours=3):
                curang.add(i["name"])
    
    return list(curang)

if __name__ == "__main__":
    print(cheaters())