def invert(daftar: dict):
    # Membuat dictionary baru untuk menyimpan hasil invert
    inverted = {v: k for k, v in daftar.items()}
    # Mengosongkan dictionary asli dan mengisinya dengan hasil invert
    daftar.clear()
    daftar.update(inverted)

if __name__ == "__main__":
    s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
    invert(s)
    print(s)