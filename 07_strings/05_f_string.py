## =======================================  f string  ==============
# An f-string (formatted string ) is a modern and easy way to insert variables, expressions, or function results directly into a string.
# it was introduced in python 3.6
# syntax : f " {} "


name = "Harish"
age = 22

print(f"My name is {name} and I am {age} years old.")



## ======================== format ()==================
# it is old but very powerful to insert values into string 
# syntax:"string {}".format(value)

name = "Harish"
print("My name is {}.".format(name)) # it takes name as in between {}


# multiple values

name = "Harish"
age = 21

print("My name is {} and I am {} years old.".format(name, age))