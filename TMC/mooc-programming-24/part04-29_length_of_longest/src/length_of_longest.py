# Write your solution here
def length_of_longest(lis: list) -> int:
    now = len(lis[0])
    for i in range(1, len(lis)):
        if len(lis[i]) > now:
            now = len(lis[i])
    return now

if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = length_of_longest(my_list)
    print(result)