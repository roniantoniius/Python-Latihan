# Write your solution here
import os

def filter_solutions():
    # Hapus file yang ada di folder utama jika ada
    if os.path.exists("correct.csv"):
        os.remove("correct.csv")
    if os.path.exists("incorrect.csv"):
        os.remove("incorrect.csv")

    with open("src/solutions.csv") as solusi:
        for operasi in solusi:
            parts = operasi.strip().split(";")
            name = str(parts[0])
            hasil = int(parts[2])
            contoh = parts[1].strip()

            if '-' in contoh:
                angka1, angka2 = contoh.split('-')
                operation = [int(angka1), '-', int(angka2)]
            elif '+' in contoh:
                angka1, angka2 = contoh.split('+')
                operation = [int(angka1), '+', int(angka2)]
            else:
                continue

            if operation[1] == "+":
                if operation[0] + operation[2] == hasil:
                    with open("correct.csv", "a") as benar:
                        benar.write(f"{name};{operation[0]}{operation[1]}{operation[2]};{hasil}\n")
                else:
                    with open("incorrect.csv", "a") as salah:
                        salah.write(f"{name};{operation[0]}{operation[1]}{operation[2]};{hasil}\n")
            elif operation[1] == "-":
                if operation[0] - operation[2] == hasil:
                    with open("correct.csv", "a") as benar:
                        benar.write(f"{name};{operation[0]}{operation[1]}{operation[2]};{hasil}\n")
                else:
                    with open("incorrect.csv", "a") as salah:
                        salah.write(f"{name};{operation[0]}{operation[1]}{operation[2]};{hasil}\n")

if __name__ == "__main__":
    filter_solutions()