# Write your solution here
def create_tuple(first: int, second: int, third: int) -> tuple:
    tups = [first, second, third]
    tup = (min(tups), max(tups), sum(tups))
    return tup

if __name__ == "__main__":
    print(create_tuple(5, 3, -1))