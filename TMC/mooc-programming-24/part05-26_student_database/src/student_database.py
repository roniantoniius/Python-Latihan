# Write your solution here
def print_student(daftar: dict, name: str):
    if len(daftar) == 0:
        print("Database is empty!")
        return

    if name in daftar:
        print(f"{name}:")
        completed_courses = daftar[name]
        if len(completed_courses) > 0:
            print(f" {len(completed_courses)} completed courses:")
            total_grade = 0
            for course in completed_courses:
                print(f"  {course[0]} {course[1]}")
                total_grade += course[1]
            average_grade = total_grade / len(completed_courses)
            print(f" average grade {average_grade:.1f}")
        else:
            print(" no completed courses")
    else:
        print(f"{name}: no such person in the database")


def add_student(daftar: dict, name: str):
    daftar[name] = []


def add_course(daftar: dict, name: str, course: tuple):
    # Abaikan course dengan grade 0
    if course[1] == 0:
        return

    if name in daftar:
        # Cari apakah course sudah pernah didaftarkan
        for idx, existing_course in enumerate(daftar[name]):
            if existing_course[0] == course[0]:
                # Jika course sudah ada dan grade baru lebih tinggi, update nilainya
                if course[1] > existing_course[1]:
                    daftar[name][idx] = course
                # Jika grade baru lebih kecil atau sama, abaikan saja
                return
        # Jika course belum ada, tambahkan course baru
        daftar[name].append(course)
    else:
        print(f"Student '{name}' not found in the list.")


def summary(daftar: dict):
    if len(daftar) == 0:
        print("No students in the database.")
        return

    print(f"students {len(daftar)}")

    max_courses = -1
    max_average_grade = -1
    student_with_max_courses = ""
    student_with_max_average = ""

    for student, courses in daftar.items():
        num_courses = len(courses)
        total_grade = sum(course[1] for course in courses)
        average_grade = total_grade / num_courses if num_courses > 0 else 0

        if num_courses > max_courses:
            max_courses = num_courses
            student_with_max_courses = student

        if average_grade > max_average_grade:
            max_average_grade = average_grade
            student_with_max_average = student

    print(f"most courses completed {max_courses} {student_with_max_courses}")
    print(f"best average grade {max_average_grade:.1f} {student_with_max_average}")


if __name__ == "__main__":
    students = {}
    add_student(students, "Peter")
    add_course(students, "Peter", ("Software Development Methods", 0))
    print_student(students, "Peter")
    summary(students)