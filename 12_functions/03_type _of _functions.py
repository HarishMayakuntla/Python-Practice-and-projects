## ======================= buil-in- functions ================

- Built-in functions are functions that are already provided by Python

- syntax :
     
          function_name(arguments)

          
#----------------------- most use built in --------------

use print() to show the out put 

Use len() to find the length of a string.

Use max() to find the largest number in a list.

Use min() to find the smallest number in a tuple.

Use sum() to calculate the total of a list.

Use sorted() to sort a list in ascending and descending order.

Use abs() to find the absolute value of a negative number.

Use round() to round decimal numbers to different places.

Use zip() to combine two lists.

Use enumerate() to print the index and value of a list.

Use type() and isinstance() to identify the type of different objects 




# # example :

def example():

    a= [14,25,85,65,74,1]

    return  len(a), max(a),min(a),sum(a) 

print(example())




we can write all fuction


##   ============================ user-define-fuction ======================


- user-defined function is a function created by the programmer to perform a specific task .

- you create user-defined functions using the def keyword

- Reuse code

- Reduce code duplication

- Improve readability

-Make debugging easier

-Organize programs into smaller modules

- syntax :

        def function_name(parameters):

            # user code

             return  values


# example :

def greet():
    print("Welcome to Python")

greet()    # o/p : Welcome to Python


# example :  with parametrs 


def add(a, b):
    print(a + b)

add(10, 20)





## ============================== User-Defined vs Built-in-Functions ==========================



| Built-in Functions                    | User-Defined Functions                      |
| ------------------------------------- | ------------------------------------------- |
| Already provided by Python            | Created by the programmer                   |
| No need to define                     | Must be defined using `def`                 |
| Examples: `print()`, `len()`, `sum()` | Examples: `add()`, `factorial()`, `greet()` |
| Ready to use                          | Need to be created before use               |
