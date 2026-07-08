##  boolean  to other primitive data types
# in numarical language 
                # 1 represent True
                # 0 represent False

##### boolean to integer  int(bool)

a=True
b=int(a)
print(b)     # here gives 1
print(type(b)) #  it showes   <class 'int'>

a=False
b=int(a)
print(b)     # here gives 0
print(type(b)) #  it showes   <class 'int'>



#####  boolean to float (float(bool))

a=True
b=float(a)
print(b)     # here gives 1.0
print(type(b)) #  it showes   <class 'float'>

a=False
b=int(a)
print(b)     # here gives 0.0
print(type(b)) #  it showes   <class 'float'>


##### boolean to string    (str(bool))
a=True
b=str(a)
print(b)     # here gives 'True'
print(type(b)) #  it showes   <class 'str'>


a=False
b=str(a)
print(b)     # here gives 'False'
print(type(b)) #  it showes   <class 'str'>



#####  boolean to complex    (complex(bool))

a=True
b=complex(a)
print(b)     # here gives 1+0j
print(type(b)) #  it showes   <class 'complex'>


a=False
b=complex(a)
print(b)     # here gives 0j
print(type(b)) #  it showes   <class 'complex'>

