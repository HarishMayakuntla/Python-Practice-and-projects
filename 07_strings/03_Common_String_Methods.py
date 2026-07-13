
## ===================== uppercase ================
#Converts a string into upper case

name = "python"
print(name.upper()) # it gives PYTHON

## ====================  Lowercase ===============
# Converts a string into lower case
name = "PYTHON"
print(name.lower()) # it gives  python

## =================== Title case ===============
# it takes as a title name

text = "python programming"
print(text.title())    # itgive  python programmin

## ======================== Capitalize ==============
# it first letter upper 

text = "house"
print(text.capitalize()) # it give  House

## ======================= Swap Case =================
#  it converts upper to lower and lower to upper

text = "House"

print(text.swapcase()) #  hOUSE

## ====================== Strip Spaces =====================
# it removes spaces 
text = "  Python   world"

print(text.strip()) # pythonworld


## ====================== Replace ===================
# it's gives replace the value 

text = "I like Java"

print(text.replace("Java", "Python"))   # I like python


## ======================== split ===================
# split means it gives differents strings

text = "Python Java C++"

print(text.split())  # 'Python', 'Java', 'C++'


## ====================== join =================
# it gives some modification 
words = ['Python', 'Java', 'C++']

print("-".join(words))    # Python-Java-C++



## ======================= find ==================
#  we will found the value 

text = "Python Programming"

print(text.find("Program"))  #7


## ======================= count ===========
# it counts the value how many times it repeat

text = "banana"

print(text.count("a")) #  3 times repaet a

## ====================== startswith ================
# which gives the letter or word startwiths
text = "Python Programming"
 
print(text.startswith("Python"))   # true


##=========================  endswith  ===============
# which gives the letter or word endswiths

text = "Python Programming"

print(text.endswith("ing"))   # True




git add .
git commit -m "Added string practice programs"
git push origin main





































































