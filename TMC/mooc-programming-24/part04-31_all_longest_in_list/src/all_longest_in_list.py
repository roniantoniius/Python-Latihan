# Write your solution here
def all_the_longest(lis: list) -> list:
    max_length = max(len(word) for word in lis)
    
    longest_strings = [word for word in lis if len(word) == max_length]
    
    return longest_strings


if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = all_the_longest(my_list)
    print(result)