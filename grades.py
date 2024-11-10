students = []

def add_student(name, grade):
    students.append({"name": name, "grade": grade})

def get_highest_grade():
    highest = max(students, key=lambda x: x["grade"])
    return highest

def get_lowest_grade():
    lowest = min(students, key=lambda x: x["grade"])
    return lowest

def show_students():
    for student in students:
        print(f"{student['name']}: {student['grade']}")

# Adding students
add_student("Alice", 85)
add_student("Bob", 90)
add_student("Charlie", 78)

# Display all students
show_students()

# Get highest and lowest grade
print(f"Highest grade: {get_highest_grade()}")
print(f"Lowest grade: {get_lowest_grade()}")
