# Write your solution here
def no_vowels(st : str) -> str:
    vowels = "aeiou"
    return ''.join([char for char in st if char not in vowels])
if __name__ == "__main__":
    my_string = "this is an example"
    print(no_vowels(my_string))