## ============================ local variable ==========================================

# A local variable is created inside a function. It can be used only inside that function

def student():

    name = "Harish"   # Local variable

    print(name)       # o/p : Harish

student()  # i create inside function so it is local variable

# it is only acces inside the function 


 # in valid progarm

def student():
    name = "Harish"

student()

print(name)  # o/p : NameError: name 'name' is not defined

# here i call name out side the function




## ================================  Global variable ===============================

#  A global variable is created outside all functions. It can be accessed from anywhere in the program.

# you cannot modify the gobal variable once you created 

# i can access any where in function inside ,outside it's our dependence

name = "Harish"    # Global variable

def student():
    print(name)

student()                      # o/p : Harish

print(name)                   # o/p :Harish







## =============================  local  vs global variable =====================

| Local Variable                        | Global Variable                          |
| ------------------------------------- | ---------------------------------------- |
| Declared inside a function            | Declared outside a function              |
| Accessible only inside that function  | Accessible throughout the program        |
| Destroyed after the function finishes | Exists until the program ends            |
| Cannot be used outside the function   | Can be used inside and outside functions |
