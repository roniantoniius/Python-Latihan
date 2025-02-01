# Write your solution here
def most_common_character(st: str) -> str:
    count = {} # dict key value
    
    for char in st:
        count[char] = count.get(char, 0) + 1
    
    max_count = max(count.values())
    
    for char in st:
        if count[char] == max_count:
            return char
        
if __name__ == "__main__":
    first_string = "abcdbde"
    print(most_common_character(first_string))

    second_string = "exemplaryelementary"
    print(most_common_character(second_string))