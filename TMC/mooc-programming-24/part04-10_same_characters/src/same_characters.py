# Write your solution here
def same_chars(st, n1, n2):
    lis = [n1, n2]
    if max(lis) < len(st):
        if st[n1] == st[n2]:
            return True
        else:
            return False
    else:
        return False
    
# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 10))