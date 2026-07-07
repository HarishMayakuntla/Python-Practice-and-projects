## string  converstions


#####  string to integer  (int(str))
a='654'
b=int(a)
print(b)     # here gives 654
print(type(b))  # it showes <class 'int'>


#####  string to float    (float(str))

a="35.96"
b=float(a)
print(b)     # here gives 35.96
print(type(b)) #  it showes   <class 'float'>


#####  string  to boolean    (bool(str))
a="6589"
b=bool(a)
print(b)     # here gives True
print(type(b)) #  it showes   <class 'bool'>

a="0"
b=float(a)
print(b)     # here gives False
print(type(b)) #  it showes   <class 'bool'>


#####  string to complex   (complex(str))

a="35"
b=complex(a)
print(b)     # here gives 35+0j
print(type(b)) #  it showes   <class 'complex'>

a="35.96"
b=float(a,59)
print(b)     # here gives 35.96+59j
print(type(b)) #  it showes   <class 'complex'>