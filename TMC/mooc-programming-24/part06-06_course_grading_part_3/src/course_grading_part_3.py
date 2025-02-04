# tee ratkaisu tänne
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
        parts = line.strip().split(";")
        if parts[0] == "id":
            continue
        murid[parts[0]] = (parts[1] + " " + parts[2]).strip()

latihan = {}
with open(exercise_data) as new_file:
    for line in new_file:
        parts = line.strip().split(";")
        if parts[0] == "id":
            continue
        latihan[parts[0]] = sum(int(x) for x in parts[1:])

ulangan = {}
with open(exam_point) as new_file:
    for line in new_file:
        parts = line.strip().split(";")
        if parts[0] == "id":
            continue
        ulangan[parts[0]] = sum(int(x) for x in parts[1:])

print(f"{'name':30}{'exec_nbr':10}{'exec_pts.':10}{'exm_pts.':10}{'tot_pts.':10}{'grade':10}")

for ids, nama in murid.items():
    if ids in latihan and ids in ulangan:
        latih = latihan[ids]
        ulang = ulangan[ids]
        
        exec_pts = latih // 4
        
        total_point = ulang + exec_pts

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

        print(f"{nama:30}{latih:<10}{exec_pts:<10}{ulang:<10}{total_point:<10}{grade:<10}")
