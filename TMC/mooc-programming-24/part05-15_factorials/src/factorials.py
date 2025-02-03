# Write your solution here
def factorials(n: int) -> dict:
    daftar = {}
    def recursive_factorial(n):
        if n in daftar:
            return daftar[n]
        if n == 1:
            daftar[n] = 1
            return 1
        result = n * recursive_factorial(n - 1)
        daftar[n] = result
        return result
    
    recursive_factorial(n)
    return daftar

if __name__ == "__main__":
    k = factorials(1)
    print(k[1])
    print(k)
