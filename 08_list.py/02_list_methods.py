
## =========================== Common List Methods ========================================
## ---------------1. append() ------------
# Adds one element at the end of the list.

numbers = [1, 2, 3]

numbers.append(4)

print(numbers) # Output: [1, 2, 3, 4]

##---------------------2. extend() ------------------------------
# Adds multiple elements end of the list.

numbers = [1, 2]

numbers.extend([3, 4, 5])

print(numbers) # Output:[1, 2, 3, 4, 5]


## ------------------------------ 3. insert() ----------------
# Insert an element at a specific index.

numbers = [10, 20, 40]

numbers.insert(2, 30)

print(numbers) # Output:[10, 20, 30, 40]


## --------------------------4. remove() ---------------------------
# Removes the first matching value if gives to remove .

numbers = [10, 20, 30, 20]

numbers.remove(20)

print(numbers) # Output:[10, 30, 20]


## ------------------------5. pop() --------------------------
# Removes  an element at end of list.

numbers = [10, 20, 30]

x = numbers.pop()

print(numbers) # Output : [10, 20]

print(x) # Output: 30


## ------------------------------------ 6. clear() -----------------------------------
# Removes all elements what are present in list.
# it showes empty list as output

numbers = [1, 2, 3]

numbers.clear()

print(numbers) # Output:[]


## --------------------------  7. index() ------------------------
# Returns the index of a value.
# it tells the value index number .

numbers = [10, 20, 30]

print(numbers.index(20)) # Output: 1



## ------------------------ 8. count() ----------------
# Counts occurrences or how many times it repeats .abs

numbers = [1, 2, 2, 3, 2]

print(numbers.count(2)) # Output: 3


## ----------------------------- 9. sort() --------------------------
## Sorts the list in ascending order.

numbers = [5, 2, 9, 1]

numbers.sort() # here defaultly sort(reverse = False)

print(numbers) # Output:[1, 2, 5, 9]

# Descending order:

numbers.sort(reverse=True)

print(numbers) # Output:[9, 5, 2, 1]



## ----------------------------- 10. reverse() ---------------------------------
# Reverses the list in place.
# means last one comes  first to start back to front
# revers traversing

numbers = [1, 2, 3, 4]

numbers.reverse()

print(numbers) # Output: [4, 3, 2, 1]


## -------------------------------- 11. copy() --------------------
# Creates a shallow copy.

a = [1, 2, 3]

b = a.copy()

print(b) # Output:[1, 2, 3]



