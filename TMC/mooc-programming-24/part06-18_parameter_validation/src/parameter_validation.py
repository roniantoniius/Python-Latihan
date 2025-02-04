# Write your solution here
def new_person(name: str, age: int) -> tuple:
    if name == "" or len(name.split(" ")) < 2 or len(name) > 40 or age < 0 or age > 150:
        raise ValueError('Check parameters again')

    return (name, age)

if __name__ == "__main__":
    periksa = new_person("Roni", 21)
    print(periksa)