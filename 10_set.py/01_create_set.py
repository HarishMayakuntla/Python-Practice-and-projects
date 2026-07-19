## =================== create a set ===============

# ------------------ empty set --------------

a=set()

print(a)   # set()

print(type(a))  # < class 'set'>

a={}  # give the {} to difine set but it call as dict

print(type(a)) #  < class 'dict'>


# -------------------  single data type ----------------
a={1,2,3,4,5,4,5,4,6}

print(a) #{1, 2, 3, 4, 5, 6}   here set removes duplicates

print(type(a)) # < class 'set'>

# ---------------------  multiple data types -------------

a={1,2.3,'hari',True}

print(a) #  {1,2.3,'hari',True}

print(type(a)) # < class 'set'>


