# Write your solution here
def count_matching_elements(my_matrix: list, element: int) -> int:
    return sum(row.count(element) for row in my_matrix)

if __name__ == "__main__":
    m = [[1, 2, 3], [2, 3, 1], [4, 5, 6]]
    print(count_matching_elements(m, 1))