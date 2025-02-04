# write your solution here
def matrix():
    with open("src/matrix.txt") as daftarMatriks:
        matriks = []
        for baris in daftarMatriks:
            baris = baris.replace("\n", "")
            indek = [int(x) for x in baris.split(",")]
            kolom = indek[0:]
            matriks.append(kolom)
        return matriks

def matrix_sum() -> int:
    daftar = matrix()
    jumlah = 0
    for i in range(len(daftar)):
        for j in daftar[i]:
            jumlah += j
    return jumlah

def matrix_max() -> int:
    daftar = matrix()
    maks = 0
    for i in range(len(daftar)):
        if max(daftar[i]) > maks:
            maks = max(daftar[i])
    return maks

def row_sums() -> list:
    daftar = matrix()
    total = []
    for i in range(len(daftar)):
        jml = 0
        for j in daftar[i]:
            jml += j
        total.append(jml)
    return total

if __name__ == "__main__":
    print(matrix_sum())
    print(matrix_max())
    print(row_sums())