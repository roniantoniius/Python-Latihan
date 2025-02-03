# Write your solution here
def histogram(teks: str) -> str:
    daftar = {}
    for i in teks:
        if i in daftar:
            daftar[i] += 1
        else:
            daftar[i] = 1
    for j in daftar:
        print(f"{j} {"*" * daftar[j]}")

if __name__ == "__main__":
    histogram("statistically")