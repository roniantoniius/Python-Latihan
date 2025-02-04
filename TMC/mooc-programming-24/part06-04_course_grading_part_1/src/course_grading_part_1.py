# write your solution here
# student_info = "src/students1.csv"
# exercise_data = "src/exercises1.csv"
student_info = str(input("Student information: "))
exercise_data = str(input("Exercise completed: "))

murid = {}
with open(student_info) as new_file:
    for line in new_file:
        parts = line.split(";")
        if parts[0] == "id":
            continue
        murid[parts[0]] = (parts[1] + " " + parts[2]).strip()

ulangan = {}
with open(exercise_data) as new_file:
    for line in new_file:
        parts = line.split(";")
        if parts[0] == "id":
            continue
        nama = parts[0]
        ulangan[nama] = []
        for ulang in parts[1:]:
            ulangan[nama].append(int(ulang))

for ids, nama in murid.items():
    if ids in ulangan:
        ulang = ulangan[ids]
        jumlah = 0
        for item in ulang:
            jumlah += item
        print(f"{nama} {jumlah}")