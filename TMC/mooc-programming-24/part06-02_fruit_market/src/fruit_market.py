# write your solution here
def read_fruits() -> dict:
    with open("src/fruits.csv") as buahBuah:
        daftar = {}
        for buah in buahBuah:
            buah = buah.replace("\n", "")
            parts = buah.split(";")
            name = str(parts[0])
            price = parts[1]
            daftar[name] = float(price)
        return daftar

if __name__ == "__main__":
    print(read_fruits())