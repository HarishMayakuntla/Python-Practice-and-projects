## ========== Nested Dictionary in Python ===============
# A nested dictionary is a dictionary inside another dictionary.
# syntax :  
# students = {
#     key1: {sub_key1: value1, sub_key2: value2},
#     key2: {sub_key1: value1, sub_key2: value2}
# }



students = {
    101: {
        "name": "Harish",
        "age": 22
    },
    102: {
        "name": "Ravi",
        "age": 21
    }
}

print(students[101]["name"])


# o/p :  Harish