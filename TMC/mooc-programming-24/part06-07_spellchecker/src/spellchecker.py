# write your solution here
with open("src/wordlist.txt") as f:
    words = set(f.read().lower().split())

text = input("Write text: ")
print(" ".join(f"*{w}*" if w.lower() not in words else w for w in text.split()))