# Write your solution here
num_items = int(input("How many items: "))
items = []

for i in range(1, num_items + 1):
    item = int(input(f"Item {i}: "))
    items.append(item)

print(items)