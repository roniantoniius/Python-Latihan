# Write your solution here
from string import ascii_uppercase
def run(sistem: str) -> list:
    daftarVariabel = dict.fromkeys(ascii_uppercase, 0)
    cetak = []
    lokasi = {}

    for i, v in enumerate(sistem):
        if v.endswith(":"):
            lokasi[baris[:-1]] = i

    i = 0
    while i < len(sistem):
        baris = sistem[i].split()
        if baris[0].endswith(":"):
            i += 1
            continue
        elif baris[0] == "END":
            break
        elif baris[0] == "PRINT":
            cetak.append(daftarVariabel[baris[1]])
        elif baris[0] == "MOV":
            daftarVariabel[baris[1]] = int(baris[2]) if baris[2].isdigit() else daftarVariabel[baris[2]]
        elif baris[0] == "ADD":
            daftarVariabel[baris[1]] += int(baris[2]) if baris[2].isdigit() else daftarVariabel[baris[2]]
        elif baris[0] == "SUB":
            daftarVariabel[baris[1]] -= int(baris[2]) if baris[2].isdigit() else daftarVariabel[baris[2]]
        elif baris[0] == "MUL":
            daftarVariabel[baris[1]] *= int(baris[2]) if baris[2].isdigit() else daftarVariabel[baris[2]]
        elif baris[0] == "JUMP":
            if baris[1] in lokasi:
                i = lokasi[baris[1]]
                continue
        elif baris[0] == "IF":
            operator = baris[2]
            awal = int(baris[1] if baris[1].isdigit() else daftarVariabel[baris[1]])
            akhir = int(baris[3] if baris[3].isdigit() else daftarVariabel[baris[3]])
            kondisi = {
                "==": awal == akhir,
                "!=": awal != akhir,
                "<": awal < akhir,
                ">": awal > akhir,
                "<=": awal <= akhir,
                ">=": awal >= akhir,
            }
            if kondisi[operator] and baris[4] == "JUMP" and baris[5] in lokasi:
                i = lokasi[baris[5]]
                continue
        i += 1

    return cetak

if __name__ == '__main__':
    program1 = []
    program1.append("MOV A 10")
    program1.append("MOV B 2")
    program1.append("PRINT A")
    program1.append("PRINT B")
    program1.append("ADD A B")
    program1.append("PRINT A")
    program1.append("END")
    program1.append("MOV B A")
    program1.append("SUB B 8")
    program1.append("PRINT B")
    program1.append("SUB A B")
    program1.append("PRINT A")
    result = run(program1)
    print(result)