## ================================== * args =======================

# *args allows a function to accept any number of positional arguments.

# most use full in functions 

# it stores as a tuple

# syntax :

#           def function_name(*args):
#                    print(args)


def numbers(*args):  # here * after you take any variable name

    for i in args:

        print(i,end=" ")   # here it takes all arguments in once

numbers(5, 10, 15, 20)     # 5 10 15 20



def total(*num): # here i take num variable name it works
 
    s = 0
 
    for i in num:
 
        s += i
 
    print(s)

total(10, 20, 30)      # o/p : 60



## ======================= ** kwags ============================

# **kwargs allows a function to accept any number of keyword arguments

# it gives as key : value pair output like dict

# syntax :

#    def function_name(**kwargs):
                  
#                 print(kwargs)




def student(**kwargs):
    print(kwargs)

student(name="Harish", age=22, city="Kadiri")

# o/p : {'name': 'Harish', 'age': 22, 'city': 'Kadiri'}


def student(**kwargs):
    for key, value in kwargs.items():   # it take dict and it performs
        print(key, ":", value)

student(name="Harish", age=22, course="Python")

# out put :

# name : Harish
# age : 22
# course : Python




##  ======================================  *args vs ** kwags ==================================

| `*args`               | `**kwargs`               |
| --------------------- | ------------------------ |
| Positional arguments  | Keyword arguments        |
| Stored as a tuple     | Stored as a dictionary   |
| Uses one `*`          | Uses two `**`            |
| Example: `10, 20, 30` | Example: `name="Harish"` |
