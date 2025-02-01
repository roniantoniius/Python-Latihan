# Write your solution here
def shortest(lis: list) -> str:
    shortest_word = lis[0]
    for word in lis:
        if len(word) < len(shortest_word):
            shortest_word = word
    return shortest_word
if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = shortest(my_list)
    print(result)