# int typecasting

##### integer to float  (float(int)) formula

a=65
b=float(a)
print(b)     # here gives 65.0
print(type(b)) # here gives  <class 'float'>


##### integer to complex   (complex(int))
# complex form is real+imaginary part like (2+6j)
a=59
b=complex(a)   # here i give only single value ,it take as real value
print(b)       # here gives (59+0j) why because we give only single value so imaginary 0
print(type(b)) # here gives <class 'complex'>

a=65
b=35
c=complex(a,b)   # here i give two value ,it take as first one real value  ,another imaginary value
print(c)       # here gives (65+35j) 
print(type(c)) # here gives <class 'complex'>



##### integer to boolean (bool(int))
# boolean contain only True and False
# in numarical language less than 0 , more than 0  but != 0 is True , 0 is False.
a=0
b=bool(a) 
print(b)   #  gives False
print(type(b)) # gives <class 'bool'>

a=1    # more than zero you can take 2 or 20856544 more than that gives True
b=bool(a) 
print(b)   #  gives True
print(type(b)) # gives <class 'bool'>

a=-1   # less than zer0   you can take more than -1 like take -589674  it gives True
b=bool(a) 
print(b)   #  gives True
print(type(b)) # gives <class 'bool'>

#####  integer to string (str(int))
a=25
b=str(a)
print(b)  #  it is gives '25'
print(type(b))   # <class 'str'>


'''
git status
git add .
git commit -m "Added primitive type conversion practice in Python"
git push origin maingit status

'''