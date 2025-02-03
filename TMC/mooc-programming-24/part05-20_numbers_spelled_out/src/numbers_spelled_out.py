# Write your solution here
def dict_of_numbers():
    satuan = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    belasan = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    puluhan = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    
    angka = {}
    
    for i in range(100):
        if i < 10:
            angka[i] = satuan[i]
        elif i < 20:
            angka[i] = belasan[i - 10]
        else:
            angka[i] = puluhan[i // 10] + ('' if i % 10 == 0 else '-' + satuan[i % 10])
    
    return angka

if __name__ == "__main__":
    numbers = dict_of_numbers()
    print(numbers[2])
    print(numbers[11])
    print(numbers[45])
    print(numbers[99])
    print(numbers[20])
    print(numbers[0])