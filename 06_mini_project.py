## ========================= STUDENT MANAGEMENT SYSTEM ==================

students = []

def add_student():
    roll = input("Enter Roll No: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")

    student = {
        "Roll": roll,
        "Name": name,
        "Age": age,
        "Course": course
    }

    students.append(student)
    print("\nStudent Added Successfully!\n")


def view_students():
    if len(students) == 0:
        print("\nNo Student Records Found!\n")
    else:
        print("\n------ Student Records ------")
        for student in students:
            print(f"Roll   : {student['Roll']}")
            print(f"Name   : {student['Name']}")
            print(f"Age    : {student['Age']}")
            print(f"Course : {student['Course']}")
            print("-" * 30)


def search_student():
    roll = input("Enter Roll Number to Search: ")

    for student in students:
        if student["Roll"] == roll:
            print("\nStudent Found")
            print(student)
            return

    print("Student Not Found!")


def update_student():
    roll = input("Enter Roll Number to Update: ")

    for student in students:
        if student["Roll"] == roll:
            student["Name"] = input("Enter New Name: ")
            student["Age"] = input("Enter New Age: ")
            student["Course"] = input("Enter New Course: ")
            print("Student Updated Successfully!")
            return

    print("Student Not Found!")


def delete_student():
    roll = input("Enter Roll Number to Delete: ")

    for student in students:
        if student["Roll"] == roll:
            students.remove(student)
            print("Student Deleted Successfully!")
            return

    print("Student Not Found!")


while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")



### output  :



# ===== STUDENT MANAGEMENT SYSTEM =====
# 1. Add Student
# 2. View Students
# 3. Search Student
# 4. Update Student
# 5. Delete Student
# 6. Exit
# Enter Your Choice: 1
# Enter Roll No: 5
# Enter Name: p
# Enter Age: 4
# Enter Course: p6

# Student Added Successfully!


# ===== STUDENT MANAGEMENT SYSTEM =====
# 1. Add Student
# 2. View Students
# 3. Search Student
# 4. Update Student
# 5. Delete Student
# 6. Exit
# Enter Your Choice: 1 
# Enter Roll No: 6
# Enter Name: q
# Enter Age: 5
# Enter Course: p6

# Student Added Successfully!


# ===== STUDENT MANAGEMENT SYSTEM =====
# 1. Add Student
# 2. View Students
# 3. Search Student
# 4. Update Student
# 5. Delete Student
# 6. Exit
# Enter Your Choice: 2

# ------ Student Records ------
# Roll   : 5
# Name   : p
# Age    : 4
# Course : p6
# ------------------------------
# Roll   : 6
# Name   : q
# Age    : 5
# Course : p6
# ------------------------------

# ===== STUDENT MANAGEMENT SYSTEM =====
# 1. Add Student
# 2. View Students
# 3. Search Student
# 4. Update Student
# 5. Delete Student
# 6. Exit
# Enter Your Choice: 3
# Enter Roll Number to Search: 5

# Student Found
# {'Roll': '5', 'Name': 'p', 'Age': '4', 'Course': 'p6'}

# ===== STUDENT MANAGEMENT SYSTEM =====
# 1. Add Student
# 2. View Students
# 3. Search Student
# 4. Update Student
# 5. Delete Student
# 6. Exit
# Enter Your Choice: 4
# Enter Roll Number to Update: 6
# Enter New Name: R
# Enter New Age: 8
# Enter New Course: p7
# Student Updated Successfully!

# ===== STUDENT MANAGEMENT SYSTEM =====
# 1. Add Student
# 2. View Students
# 3. Search Student
# 4. Update Student
# 5. Delete Student
# 6. Exit
# Enter Your Choice: 2

# ------ Student Records ------
# Roll   : 5
# Name   : p
# Age    : 4
# Course : p6
# ------------------------------
# Roll   : 6
# Name   : R
# Age    : 8
# Course : p7
# ------------------------------

# ===== STUDENT MANAGEMENT SYSTEM =====
# 1. Add Student
# 2. View Students
# 3. Search Student
# 4. Update Student
# 5. Delete Student
# 6. Exit
# Enter Your Choice: 5
# Enter Roll Number to Delete: 6
# Student Deleted Successfully!

# ===== STUDENT MANAGEMENT SYSTEM =====
# 1. Add Student
# 2. View Students
# 3. Search Student
# 4. Update Student
# 5. Delete Student
# 6. Exit
# Enter Your Choice: 2

# ------ Student Records ------
# Roll   : 5
# Name   : p
# Age    : 4
# Course : p6
# ------------------------------

# ===== STUDENT MANAGEMENT SYSTEM =====
# 1. Add Student
# 2. View Students
# 3. Search Student
# 4. Update Student
# 5. Delete Student
# 6. Exit
# Enter Your Choice: 6
# Thank You!