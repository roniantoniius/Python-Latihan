# Write your solution here
def anagrams(str1 : str, str2 : str) -> bool:
    return True if sorted(str1) == sorted(str2) else False
if __name__ == "__main__":
    print(anagrams("house", "mouse"))