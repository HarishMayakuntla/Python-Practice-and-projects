# if checks a condition,if it's True go inside  ,False it never execute
# else runs when the condition is False.
# elif checks additional conditions.
# Python uses indentation (4 spaces) to define code blocks.
# Conditions always evaluate to either True or False.


num = 6
if num > 0:   # here check the condition if its True go inside
    print("Positive")  # outpput: positive


num = 7

if num % 2 == 0:   # codition is False go to   else block
    print("Even")   
else:
    print("Odd")    # out put: odd



marks = 75

if marks >= 90:      # i need check multiple state ments
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:                      # output :Grade B
    print("Fail")