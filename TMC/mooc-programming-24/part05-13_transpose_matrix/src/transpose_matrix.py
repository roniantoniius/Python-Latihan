# Write your solution here
def transpose(matrix: list):
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):  # Start from i + 1 to avoid re-swapping elements
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

if __name__ == "__main__":
    matrix = [[1,2],[1,1]]
    transpose(matrix)
    print(matrix)