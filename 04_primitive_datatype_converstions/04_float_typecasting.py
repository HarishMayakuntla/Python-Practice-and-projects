# float value to other datatypes


##### float to integer  (int(float))
a=65.6
b=int(a)
print(b)     # here gives 65
print(type(b)) #   it shows <class 'int'>

##### float to string (str(float))

a=523.06
b=str(a)
print(b)     # here gives '523'
print(type(b))  # <class 'str'>


##### float to boolean (bool(float))
a=12.05
b=bool(a)
print(b)     # here gives 12
print(type(b))


a=1.56    # more than zero you can take 1  to infinity values  that gives True
b=bool(a) 
print(b)   #  gives True
print(type(b)) # gives <class 'bool'>

a=-1.256  # less than zer0   you can take more than -1 like take -589674  it gives True
b=bool(a) 
print(b)   #  gives True
print(type(b)) # gives <class 'bool'>

a=0.0                
b=bool(a)
print(b)     # here gives 0 , only zero it gives False
print(type(b)) # gives <class 'bool'>



##### float to complex    (complex(float))

a=65.0
b=complex(a)
print(b)     # here gives 65+0j
print(type(b))