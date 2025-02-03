# Write your solution here
grades = []

def calculate_grade(exam, exercises):
    if exam < 10:
        return 0
    total = exam + (exercises // 10)
    if total < 15:
        return 0
    elif total < 18:
        return 1
    elif total < 21:
        return 2
    elif total < 24:
        return 3
    elif total < 28:
        return 4
    else:
        return 5

def get_statistics(grades):
    if not grades:
        return
    avg = sum(g[0] + (g[1] // 10) for g in grades) / len(grades)
    passed = [g for g in grades if calculate_grade(g[0], g[1]) > 0]
    pass_percentage = (len(passed) / len(grades)) * 100
    distribution = {i: "" for i in range(5, -1, -1)}
    for g in grades:
        distribution[calculate_grade(g[0], g[1])] += "*"
    print("Statistics:")
    print(f"Points average: {avg:.1f}")
    print(f"Pass percentage: {pass_percentage:.1f}")
    print("Grade distribution:")
    for k, v in distribution.items():
        print(f"  {k}: {v}")
while True:
    entry = input("Exam points and exercises completed: ").strip()
    if not entry:
        break
    exam, exercises = map(int, entry.split())
    grades.append((exam, exercises))
get_statistics(grades)
