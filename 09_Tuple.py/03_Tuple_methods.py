## ========================= Tuple Methods ==========================
# what are the handles or deals with Tuple 
# they methods were come though bult in Tuple data type
# here only 2 methods are there 
# why beacause we can't modify the Tuples

# -----------count()--------

# Counts how many times an element appears.

a = (1, 2, 3, 2, 2)

print(a.count(2))  # o/p: 3


# ------------------index () -----------
# Tuple is immutable but it has order

# it gives  the index of the first occurrence

a = (10, 20, 30, 20)

print(a.index(30)) # o/p :  2 
# in positive index 30 locate in 2 index 
# in negitive index 30 locate in -2 index 






## ============================= concatenation ==================
# add to more than on tuple 

a=(10,20,30,True)
b=('hari',20.32,5+6j,False)

print(a+b) # o/p : (10, 20, 30, True, 'hari', 20.32, (5+6j), False)




## ======================== Built-in Functions ================
  
b = (10, 20, 30, 40)

print(len(b))   # give length of tuple 
# o/p :4

print(max(b))  # it give heighest value in tuple
# o/p : 40

print(min(b))  # it give lowest value in tuole 
# o/p : 10

print(sum(b))  # it give totalallvalues in tiple
# o/p : 100


