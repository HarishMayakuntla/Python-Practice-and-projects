## ========== create a tuple =============
## ------------- same data type --------------

a = (10, 20, 30, 40) # integers

print(a)      # o/p :(10, 20, 30, 40)
print(type(a)) # <class 'tuple'>


a = (10.32, 2.630, 30.96, 1.40) # float

print(a)      # o/p :(10.32, 2.630, 30.96, 1.40)
print(type(a)) # <class 'tuple'>

a = ('t','u','p','l','e') # string

print(a)      # o/p :('t', 'u', 'p', 'l', 'e')
print(type(a)) # <class 'tuple'>



## -------------- multiple datatypes  -----------------------

a=(10,3.65,'hari',True)

print(a)        # o/p : (10,3.65,'hari',True)

print(type(a))  #  <class 'tuple'>




## -------------------------allowes duplicates ------------------------------

b = (10,20,10,30,10,30,50)

print(b) # o/p :(10,20,10,30,10,30,50)
print(type(b))  #  <class 'tuple'>


## -------------- tuple is mutable -------------
# we cannot modify the Tuple 

# b = (10, 20, 30)

# b[1] = 50
# print(b)  # o/p : TypeError: 'tuple' object does not support item assignment