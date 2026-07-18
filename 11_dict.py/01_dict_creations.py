## ======================== creating dictonary ===================

#------- empty dict -----------

d = {}
print(type(d))  # <class 'dict'>


# ---------- using dict() -----------

student = dict(name="Harish", age=22, course="Python")
print(student)

# o/p:  {'name': 'Harish', 'age': 22, 'course': 'Python'}


#---------- Accessing Values ------------

student = {
    "name": "Harish",
    "age": 21
}

print(student["name"])


# o/p : Harish

# ------------  list to dict -----------

a= [('hari',70.0),('ramesh',80)]
print(dict(a))

# o/p : {'hari': 70.0, 'ramesh': 80}