# Logical Operators in One Program

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("\nLogical Operators Results")
print("-" * 35)

# AND Operator
if a > 0 and b > 0:
    print("AND : Both numbers are positive.")
else:
    print("AND : Both numbers are not positive.")

# OR Operator
if a > 0 or b > 0:
    print("OR  : At least one number is positive.")
else:
    print("OR  : Both numbers are non-positive.")

# NOT Operator
if not(a > b):
    print("NOT : a is not greater than b.")
else:
    print("NOT : a is greater than b.")