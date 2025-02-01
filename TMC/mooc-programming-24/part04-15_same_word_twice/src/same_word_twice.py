# Write your solution here
lis = []
while True:
    inp = str(input("Word:"))
    lis.append(inp)
    if lis.count(inp) == 2:
        break
print(f"You typed in {len(lis)-1} different words")