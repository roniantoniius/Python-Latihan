# Write your solution here
def read_input(prompt: str, lower_bound: int, upper_bound: int) -> int:
    while True:
        user_input = input(prompt)
        try:
            number = int(user_input)
            if lower_bound <= number <= upper_bound:
                return number
        except ValueError:
            pass
        print(f"You must type in an integer between {lower_bound} and {upper_bound}")
if __name__ == "__main__":
    number = read_input("Please type in a number: ", 95, 105)
    print("You typed in:", number)