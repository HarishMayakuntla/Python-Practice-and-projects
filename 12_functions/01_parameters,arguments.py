### ========================== Parameters in function ======================

# A parameter is a variable inside the function definition that receives a value when the function is called

# parameter can store any data type

# -  syntax :

#         def function_name(parameter):
#                 # code


# explain :

def greet(name):

    print(name)

greet('hello')   # o/p : hello

# Here,

#     greet → Function name
#     name → Parameter



## ================================== Arguments =========================

# An argument is the actual value passed to the function

# -  syntax :

#         def function_name(parameter):
#                 # code
           
#         function_name('argument')



def greet(name):

    print("Hello", name)

greet('harish')   # here we pass harish argument


# here 

#      greet → Function name

#      harish → Argument



# =============================  parameter vs arguments ===========================

| Parameter                       | Argument                        |
| ------------------------------- | ------------------------------- |
| Variable in function definition | Actual value passed to function |
| Receives data                   | Sends data                      |
| Defined using `def`             | Used while calling function     |
      


      