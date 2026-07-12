## ================ String is Immutable ===================
# name = "Python"
# name[0] = "J"  #  it showes TypeError we cannot modify after creation


## ================= Indexing ==============================
# here we extract the values in using indexind numbers

word = "Python"

print(word[0])  #  o/p : p
print(word[3])  # o/p :h
print(word[-1]) # o/p :n


## ================== Slicing =====================
#  string[start:stop:step] means it gives where to where you want

text = "Python Programming"
print(text[0:6])  # it give 0 index to (6-1) index

text = "Python"
print(text[:]) # here it acces all the stringgit status

print(text[2:]) # here it takes 2 index  to last index

print(text[:4]) # here starts with 0 index and (n-1) means (4-1) index

print(text[::-1]) #  it gives reverse string



## =================== String Length ==================
# found the string length mean how many chacters in string
# we use  len() keyword

name = "Python"

print(len(name))   # o/p: 6  here it counts how many letters are there in given string


## ==================== Traversing strings =============
# using for loop

name = "Python"

for i in name:
    print(i)    # here it gives  each letter as a string



## =================== Membership Operators ==========
# Check if a value exists in a sequence
# it gives bool type like True or False

text = "Python Programming"

print("Python" in text)     # it's give True 
print("Java" in text)       # # it's give False


## ================== String Comparison ================
# here we copare with strings

print("apple" == "apple") # True
print("apple" == "Apple") # False
print("cat" > "bat")      # True

## ============= new line ===========
print('hello\npython')

















# git add .
# git commit -m "Added string practice programs"
# git push origin main