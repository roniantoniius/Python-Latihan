# Write your solution here
def greatest_number(n1, n2, n3):
    lis = [n1, n2, n3]
    return max(lis)
# You can test your function by calling it within the following block
if __name__ == "__main__":
    greatest = greatest_number(5, 4, 8)
    print(greatest)