# Write your solution here
def line(num, s):
    if len(s) == 0:
        return print("*"*num)
    else:
        print(s[0]*num)
# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(5, "XXXXXX")