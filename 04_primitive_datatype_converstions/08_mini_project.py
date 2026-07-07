# ============================================
# Primitive Data Type Conversion in Python
# ============================================

print("========== Integer Type Conversion ==========")
a = 10
print("Original:", a, type(a))

print("Integer -> Float   :", float(a), type(float(a)))
print("Integer -> String  :", str(a), type(str(a)))
print("Integer -> Boolean :", bool(a), type(bool(a)))
print("Integer -> Complex :", complex(a), type(complex(a)))

print("\n========== Float Type Conversion ==========")
b = 10.75
print("Original:", b, type(b))

print("Float -> Integer   :", int(b), type(int(b)))
print("Float -> String    :", str(b), type(str(b)))
print("Float -> Boolean   :", bool(b), type(bool(b)))
print("Float -> Complex   :", complex(b), type(complex(b)))

print("\n========== Boolean Type Conversion ==========")
c = True
print("Original:", c, type(c))

print("Boolean -> Integer :", int(c), type(int(c)))
print("Boolean -> Float   :", float(c), type(float(c)))
print("Boolean -> String  :", str(c), type(str(c)))
print("Boolean -> Complex :", complex(c), type(complex(c)))

print("\n========== String Type Conversion ==========")
d = "25"
print("Original:", d, type(d))

print("String -> Integer  :", int(d), type(int(d)))
print("String -> Float    :", float(d), type(float(d)))
print("String -> Boolean  :", bool(d), type(bool(d)))
print("String -> Complex  :", complex(d), type(complex(d)))

print("\n========== Complex Type Conversion ==========")
e = 5 + 3j
print("Original:", e, type(e))

print("Complex -> String  :", str(e), type(str(e)))
print("Complex -> Boolean :", bool(e), type(bool(e)))

print("\nComplex -> Integer : Not Allowed")
print("Complex -> Float   : Not Allowed")