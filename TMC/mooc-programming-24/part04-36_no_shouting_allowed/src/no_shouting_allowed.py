# Write your solution here
def no_shouting(lis : list) -> list:
    return [string for string in lis if not string.isupper()]
if __name__ == "__main__":
    my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
    pruned_list = no_shouting(my_list)
    print(pruned_list)