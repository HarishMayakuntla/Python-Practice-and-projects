print("=" * 50)
print("      STUDENT RESULT MINI PROJECT")
print("=" * 50)

# Input
name = input("Enter Student Name: ")

m1 = int(input("Enter Python Marks: "))
m2 = int(input("Enter SQL Marks: "))
m3 = int(input("Enter Data Science Marks: "))

# ------------------------------
# Arithmetic Operators
# ------------------------------
total = m1 + m2 + m3
average = total / 3

print("\n----- Arithmetic Operators -----")
print("Total =", total)
print("Average =", average)
print("Difference =", m1 - m2)
print("Product =", m1 * m2)
print("Division =", m1 / m2)
print("Floor Division =", m1 // m2)
print("Modulus =", m1 % m2)
print("Power =", m1 ** 2)

# ------------------------------
# Assignment Operators
# ------------------------------
print("\n----- Assignment Operators -----")
bonus = total

bonus += 5
print("After += 5 :", bonus)

bonus -= 5
print("After -= 5 :", bonus)

bonus *= 2
print("After *= 2 :", bonus)

bonus //= 2
print("After //= 2 :", bonus)

# ------------------------------
# Comparison Operators
# ------------------------------
print("\n----- Comparison Operators -----")
print("Python > SQL :", m1 > m2)
print("Python < SQL :", m1 < m2)
print("Python == SQL :", m1 == m2)
print("Python != SQL :", m1 != m2)
print("Python >= SQL :", m1 >= m2)
print("Python <= SQL :", m1 <= m2)

# ------------------------------
# Logical Operators
# ------------------------------
print("\n----- Logical Operators -----")
print("All subjects passed :", (m1 >= 35 and m2 >= 35 and m3 >= 35))
print("At least one distinction :", (m1 >= 75 or m2 >= 75 or m3 >= 75))
print("Not Failed :", not(total < 105))

# ------------------------------
# Identity Operators
# ------------------------------
print("\n----- Identity Operators -----")
list1 = [10, 20, 30]
list2 = list1
list3 = [10, 20, 30]

print("list1 is list2 :", list1 is list2)
print("list1 is list3 :", list1 is list3)
print("list1 is not list3 :", list1 is not list3)

# ------------------------------
# Membership Operators
# ------------------------------
print("\n----- Membership Operators -----")
subjects = ["Python", "SQL", "Power BI", "Excel"]

print("Python in subjects :", "Python" in subjects)
print("Java in subjects :", "Java" in subjects)
print("Java not in subjects :", "Java" not in subjects)

# ------------------------------
# Bitwise Operators
# ------------------------------
print("\n----- Bitwise Operators -----")
a = 10
b = 5

print("a =", a)
print("b =", b)
print("a & b =", a & b)
print("a | b =", a | b)
print("a ^ b =", a ^ b)
print("~a =", ~a)
print("a << 1 =", a << 1)
print("a >> 1 =", a >> 1)

# ------------------------------
# Result
# ------------------------------
print("\n----- Final Result -----")

if average >= 75:
    grade = "A"
elif average >= 60:
    grade = "B"
elif average >= 50:
    grade = "C"
elif average >= 35:
    grade = "D"
else:
    grade = "Fail"

print("Student :", name)
print("Total :", total)
print("Average :", round(average, 2))
print("Grade :", grade)

print("=" * 50)
print("Project Completed Successfully")
print("=" * 50)