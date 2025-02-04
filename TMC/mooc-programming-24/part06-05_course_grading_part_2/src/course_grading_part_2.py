# wwite your solution here
# student_info = "src/students1.csv"
# exercise_data = "src/exercises1.csv"
# exam_point = "src/exam_points1.csv"
student_info = str(input("Student information: "))
exercise_data = str(input("Exercise completed: "))
exam_point = str(input("Exam points: "))
murid = {}
with open(student_info) as new_file:
    for line in new_file:
        parts = line.split(";")
        if parts[0] == "id":
            continue
        murid[parts[0]] = (parts[1] + " " + parts[2]).strip()

latihan = {}
with open(exercise_data) as new_file:
    for line in new_file:
        parts = line.split(";")
        if parts[0] == "id":
            continue
        nama = parts[0]
        latihan[nama] = []
        for ulang in parts[1:]:
            latihan[nama].append(int(ulang))

ulangan = {}
with open(exam_point) as new_file:
    for line in new_file:
        parts = line.split(";")
        if parts[0] == "id":
            continue
        nama = parts[0]
        ulangan[nama] = []
        for ulang in parts[1:]:
            ulangan[nama].append(int(ulang))

for ids, nama in murid.items():
    if ids in ulangan and ids in latihan:
        ulang = sum(ulangan[ids])
        latih = sum(latihan[ids])
        
        percentage_completed = (latih / 40) * 100
        
        if percentage_completed >= 100:
            points = 10
        elif percentage_completed >= 90:
            points = 9
        elif percentage_completed >= 80:
            points = 8
        elif percentage_completed >= 70:
            points = 7
        elif percentage_completed >= 60:
            points = 6
        elif percentage_completed >= 50:
            points = 5
        elif percentage_completed >= 40:
            points = 4
        elif percentage_completed >= 30:
            points = 3
        elif percentage_completed >= 20:
            points = 2
        elif percentage_completed >= 10:
            points = 1
        else:
            points = 0
        
        total_point = ulang + points

        if total_point < 15:
            grade = 0
        elif 15 <= total_point <= 17:
            grade = 1
        elif 18 <= total_point <= 20:
            grade = 2
        elif 21 <= total_point <= 23:
            grade = 3
        elif 24 <= total_point <= 27:
            grade = 4
        else:
            grade = 5
        
        print(f"{nama} {grade}")