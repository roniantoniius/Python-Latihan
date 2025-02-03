# Write your solution here
def older_people(people: list, year: int) -> str:
    total = []
    for ulang in range(len(people)):
        if people[ulang][1] < year:
            total.append(people[ulang][0])
    return total
    
if __name__ == "__main__":
    person_list = [('Arthur', 1977), ('Emily', 2014)]
    result = older_people(person_list, 2010)
    print(result)