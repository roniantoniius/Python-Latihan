# Copy here code of line function from previous exercise
def line(length, char):
    print(char * length)

def square(side_length, char):
    for _ in range(side_length):
        line(side_length, char)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square(5, "x")