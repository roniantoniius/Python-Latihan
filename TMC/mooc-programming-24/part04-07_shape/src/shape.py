def line(length, char):
    print(char * length)

def shape(triangle_width, triangle_char, rectangle_height, rectangle_char):
    for i in range(1, triangle_width + 1):
        line(i, triangle_char)
    
    for _ in range(rectangle_height):
        line(triangle_width, rectangle_char)

if __name__ == "__main__":
    shape(5, "X", 3, "*")