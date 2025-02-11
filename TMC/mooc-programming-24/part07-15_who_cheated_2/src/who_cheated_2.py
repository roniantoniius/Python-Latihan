# Write your solution here
from datetime import timedelta
def mulai() -> list:
    daftarMulai = []
    with open("src/start_times.csv", mode='r', encoding='utf-8') as mulai:
        for baris in mulai:
            nama, waktu = baris.strip().split(";")
            jam, menit = map(int, waktu.split(":"))
            sekarang = timedelta(hours=jam, minutes=menit)
            daftarMulai.append({'name':nama, 'time': sekarang})
    return daftarMulai

def submisiNilai() -> list:
    daftarAkhir = []
    with open("src/submissions.csv", mode='r', encoding='utf-8') as start:
        for daftar in start:
            name, task, points, waktus = daftar.strip().split(";")
            jams, menits = map(int, waktus.split(":"))
            akhir = timedelta(hours=jams, minutes=menits)
            daftarAkhir.append({'name': name, 'task': task, 'points': points, 'time': akhir})
    return daftarAkhir

def cheaters() -> list:
    daftarMulai = mulai()
    daftarAkhir = submisiNilai()

    curang = set()
    for i in daftarMulai:
        for j in daftarAkhir:
            if i["name"] == j["name"] and j["time"] - i["time"] > timedelta(hours=3):
                curang.add(i["name"])
    
    return list(curang)

def final_points() -> dict:
    daftarMulai = mulai()
    daftarAkhir = submisiNilai()
    final = {}
    for i in daftarMulai:
        for j in daftarAkhir:
            if i["name"] == j["name"] and j["time"] - i["time"] < timedelta(hours=3):
                submisi = int(j["task"])
                nilai = int(j["points"])
                if 1 <= submisi <= 8 and 0 <= nilai <= 6:
                    if i["name"] not in final:
                        final[i["name"]] = {}
                    if submisi in final[i["name"]]:
                        final[i["name"]][submisi] = max(final[i["name"]][submisi], nilai)
                    else:
                        final[i["name"]][submisi] = nilai

    baru = {}
    for key, value in final.items():
        jumlah = 0
        for k, v in value.items():
            jumlah += v
        baru[key] = jumlah
    return baru
if __name__ == "__main__":
    print(final_points())
