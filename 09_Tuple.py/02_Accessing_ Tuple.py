## ========= Accessing Tuple Elements ==========

# ------------------ Positive Indexing --------------
# we take positive index to get values

a = (10, 20, 30, 40)

print(a[0])  # o/p :10
print(a[2])   # o/p :30



# ----------------------Negitive Indexing ---------
# we take negitive index to get values


a = (10, 20, 30, 40)

print(a[-1])  # o/p :40
print(a[-2])   # o/p :30



# ------------------ Slicing --------------------------
# we here get values where to where range

a = (10, 20, 30, 40, 50)

print(a[1:4]) # (20, 30, 40)
print(a[:3])  #  (10, 20, 30)
print(a[2:])  # (30, 40, 50)

print(a[::-1]) # reverse Tuple o/p: (50, 40, 30, 20, 10)


# ------------------ Tuple Unpacking -----------------

a = (10, 20, 30)

x , y ,z = a

print(x) # o/p : 10
print(y) # o/p :20
print(z)  # o/p :30


