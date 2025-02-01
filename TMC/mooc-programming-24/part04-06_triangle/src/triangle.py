# Copy here code of line function from previous exercise
def line(length):
    print('#' * length)

def triangle(height):
    for i in range(1, height + 1):
        line(i)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
