# Write your solution here
def formatted(floats: list) -> list:
    return [f"{num:.2f}" for num in floats]
if __name__ == "__main__":
    my_list = [1.234, 0.3333, 0.11111, 3.446]
    result = formatted(my_list)
    print(result)