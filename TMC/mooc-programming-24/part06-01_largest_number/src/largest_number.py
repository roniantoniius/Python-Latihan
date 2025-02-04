# write your solution here
def largest() -> int:
    with open("src/numbers.txt") as file:
        sekarang = file.readlines()
        daftar = [int(line.strip()) for line in sekarang]
        daftar.sort()
    return daftar[-1]

if __name__ == "__main__":
    print(largest())