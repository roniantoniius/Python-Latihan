# Write your solution here
def distinct_numbers(numbers: list) -> list:
    return sorted(set(numbers))

if __name__ == "__main__":
    my_list = [3, 2, 2, 1, 3, 3, 1]
    print(distinct_numbers(my_list))