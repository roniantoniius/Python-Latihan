# Write your solution here
def print_sudoku(daftar: list):
    for o in range(0, 9, 3):
        for i in range(o, o + 3):
            row = ""
            for j in range(0, 9, 3):
                for k in range(j, j + 3):
                    if daftar[i][k] == 0:
                        row += " _"
                    else:
                        row += f" {daftar[i][k]}"
                row += " "
            print(row.strip())
        print()

def add_number(daftar: list, m: int, n: int, value: int):
    daftar[m][n] = value

if __name__ == "__main__":
    sudoku  = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    print_sudoku(sudoku)
    add_number(sudoku, 0, 0, 2)
    add_number(sudoku, 1, 2, 7)
    add_number(sudoku, 5, 7, 3)
    print()
    print("Three numbers added:")
    print()
    print_sudoku(sudoku)