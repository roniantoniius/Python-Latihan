# Write your solution here
def longest(strings: list) -> str:
    return max(strings, key=len)

if __name__ == "__main__":
    strings = ['first', 'second', 'third']
    print(longest(strings))