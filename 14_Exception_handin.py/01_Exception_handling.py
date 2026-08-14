## ============================= Python Exception Handling =======================

# Exception handling is used to handle errors without stopping the entire program

## for example 

a = 10
b = 0

print(a / b)

# output : ZeroDivisionError: division by zero



## instead of we can use

try:
    a = 10
    b = 0
    print(a / b)

except ZeroDivisionError:
    print("Cannot divide by zero")  # o/p : Cannot divide by zero



## =================  What is Exception =================

## An exception is an error that occurs while a program is running

example:

print(10 / 0)

exception

 ZeroDivisionError    #  like that


 # Without exception handling:

num = int(input("Enter number: "))
print(100 / num)
print("Program completed")

# if user give 0 as input then it will show the error

With exception handling


try:
    num = int(input("Enter number: "))
    print(100 / num)

except ZeroDivisionError:
    print("Cannot divide by zero")

print("Program completed")

# here it gives if user gives 0

# o/p : "Cannot divide by zero"
#       program completed




##### ===========================  try  &  except ============================
# 
#
# Syntax :
# 

        try:
            # risky code

        except:
            
            # error handling




# exanple :


try:
    x = 10 / 0

except ZeroDivisionError 
:
    print("Something went wrong")   

# o/p : Something went wrong

### ============  common python exceptions ====================

| Exception             | Meaning                       |
| --------------------- | ----------------------------- |
| `ValueError`          | Wrong value                   |
| `TypeError`           | Wrong data type               |
| `ZeroDivisionError`   | Division by zero              |
| `NameError`           | Variable doesn't exist        |
| `IndexError`          | Invalid list index            |
| `KeyError`            | Dictionary key doesn't exist  |
| `FileNotFoundError`   | File doesn't exist            |
| `AttributeError`      | Invalid attribute/method      |
| `ImportError`         | Import problem                |
| `ModuleNotFoundError` | Module doesn't exist          |
| `PermissionError`     | Permission denied             |
| `OverflowError`       | Numeric calculation too large |
| `RuntimeError`        | General runtime error         |






#### ============= else ==================

# else executes only when there is no exception

Syntax :

try:
    # code

except:
    # error

else:
    # successful code



# Example :

try:
    num = int(input("Enter number: "))

except ValueError:
    print("Invalid number")

else:
    print("You entered:", num)


# if user give 20

# o/p : You entered: 20



##### =============================  finally ===========================

# finally always executes, whether an exception occurs or not.

Syntax 

try:
    print(10 / 2)

except ZeroDivisionError:
    print("Cannot divide")

finally:
    print("Program finished")


# o/p :

5.0
Program finished



#### ==================== try-except-else-finally =========================

Syntax :


try:
    # risky code

except SomeError:
    # handle error

else:
    # executes if no error

finally:
    # always executes



## example :


try:
    num = int(input("Enter number: "))
    result = 100 / num

except ValueError:
    print("Enter numbers only")

except ZeroDivisionError:
    print("Cannot divide by zero")

else:
    print("Result:", result)

finally:
    print("Execution completed")


## output :

0
Cannot divide by zero
Execution completed

git status
git add .
git commit -m "Added Python  practice programs"
git push origin main



