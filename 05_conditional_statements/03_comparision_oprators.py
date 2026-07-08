# Comparison Operators in One Program

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("\nComparison Operators Results")
print("-" * 35)

# Equal to
if a == b:
    print(f"{a} == {b} : True")
else:
    print(f"{a} == {b} : False")

# Not Equal to
if a != b:
    print(f"{a} != {b} : True")
else:
    print(f"{a} != {b} : False")

# Greater than
if a > b:
    print(f"{a} > {b} : True")
else:
    print(f"{a} > {b} : False")

# Less than
if a < b:
    print(f"{a} < {b} : True")
else:
    print(f"{a} < {b} : False")

# Greater than or Equal to
if a >= b:
    print(f"{a} >= {b} : True")
else:
    print(f"{a} >= {b} : False")

# Less than or Equal to
if a <= b:
    print(f"{a} <= {b} : True")
else:
    print(f"{a} <= {b} : False")