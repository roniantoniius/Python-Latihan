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

def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int) -> list:
    baru = [row[:] for row in sudoku]
    baru[row_no][column_no] = number
    return baru
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

    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)