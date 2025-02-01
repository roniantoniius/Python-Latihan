# Write your solution here
def everything_reversed(strings: list) -> list:
    return [word[::-1] for word in strings][::-1]
if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = everything_reversed(my_list)
    print(result)