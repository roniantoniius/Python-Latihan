# Write your solution here
from fractions import Fraction
def fractionate(amount: int) -> list:
    fraksi = []
    for i in range(amount):
        fraksi.append(Fraction(1, amount))
    return fraksi

if __name__ == "__main__":
    for p in fractionate(3):
        print(p)

    print()

    print(fractionate(5))