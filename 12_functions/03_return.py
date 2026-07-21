## ======================== Return in function ==================

 The return statement is used to send a value back from a function to the place where the function was called

 syntax :

          def function_name():
               return value

# ================ Why Do We Need return =================

Without return, a function can only print the result.


Use it in another calculation.

Pass it to another function.

Reuse the returned value anywhere in the program



# example 

def add():
    return 10 + 20

result = add()

print(result)    # o/p : 30






## =========================== print()  vs  return ===========================


| Think of `print()` as... | Think of `return` as... |
| ------------------------ | ----------------------- |
| **Display**              | **Give Back**           |
| Shows the result         | Returns the result      |
| Cannot be reused         | Can be reused anywhere  |
| For user output          | For program logic       |
| there no return elements | here return every elements |
| is used for debugging    |send a value back from a function|

print() = Show the result
return = Give the result back to the program