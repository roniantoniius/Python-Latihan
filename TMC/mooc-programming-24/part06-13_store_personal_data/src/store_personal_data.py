# Write your solution here
def store_personal_data(bio: tuple):
    with open("people.csv", "a") as file:
        name, age, height = bio
        file.write(f"{name};{age};{height}\n")

if __name__ == "__main__":
    store_personal_data(("Paul Paulson", 37, 175.5))