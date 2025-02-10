# Write your solution here
import json
def print_persons(filename: str):
    with open("src/"+filename) as fileName:
        data = fileName.read()
    orangs = json.loads(data)

    for orang in orangs:
        print(f"{orang["name"]} {orang["age"]} years ({', '.join(str(x) for x in orang["hobbies"])})")


if __name__ == "__main__":
    print_persons("file1.json")