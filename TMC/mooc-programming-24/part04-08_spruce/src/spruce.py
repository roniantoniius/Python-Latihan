# Write your solution here
# You can test your function by calling it within the following block
def spruce(size):
    print("a spruce!")  # Tambahkan print ini agar sesuai dengan ekspektasi
    for i in range(1, size + 1):
        for j in range(size - i):
            print(" ", end="")
        for k in range(1, i * 2):
            print("*", end="")
        print()
    for j in range(size - 1):
        print(" ", end="")
    print("*")

if __name__ == "__main__":
    spruce(3)
