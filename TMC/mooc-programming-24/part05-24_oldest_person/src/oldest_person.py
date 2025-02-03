# Write your solution here
def oldest_person(people: list) -> str:
    awal = people[0]
    for ulang in range(len(people)):
        if people[ulang][1] < awal[1]:
            awal = people[ulang]
    return awal[0]
    
if __name__ == "__main__":
    p1 = ("Adam", 1997)
    p2 = ("Adk", 2001)
    p3 = ("bff", 2004)
    p4 = ("lsdsn", 1989)
    people = [p1, p2, p3, p4]
    print(oldest_person(people))