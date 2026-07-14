## ====================== Creating a list Same datatypes ==============

a=['i','am','harish','mayakuntla','data science ','student']   # it contains only strings

b=[12,52,45,65,89]      # integers

c=[10.2,3.215,60.58,258.01,1254783.025865]    # float 

d=[True,False,False,True]  # boolean(bool)

e=[1+8j,2+0j,547+65j]   # complex datatype

print(a)# o/p:['i','am','harish','mayakuntla','data science ','student'] 
print(type(a)) # <class 'list'>

print(b)# [12,52,45,65,89]
print(type(e))   # <class 'list'>

print(c)# [10.2,3.215,60.58,258.01,1254783.025865]
print(type(e))  #  <class 'list'>

print(d)# [True,False,False,True]
print(type(e)) #  <class 'list'>

print(e)#[1+8j,2+0j,547+65j]
print(type(e))   # <class 'list'>

# it will give all output without through any error






## ==================== Creating a list Multiple  data types ======================

a=['NAME','Harish',234,70.0,True,1+2j]
print(a)   
print(type(a))   # <class 'list'>

# o/p :['NAME', 'Harish', 234, 70.0, True, (1+2j)]
# it should access all type of data types 
# see above i give string,integer, float,boolean,compplex it should access.a



### ==================== index num of list ==============
#  then we understand what is index number

num = [25,698,145,369,875,698]


        # index                    values                   reverse index
   #  ----------------------------------------------------------------------
        # 0                           25                        -6   

        # 1                           698                       -5

        # 2                           145                       -4

        # 3                           369                       -3

        # 4                           875                       -2

        # 5                           698                       -1

# here it take 0 to n values and reverse -1 to -n values

print(num[0]) # it will give 25
print(num[-1]) # it will give 698



## ========================= Accessing the elements in list ==========================

a=['NAME','Harish',234,70.0,True,1+2j]

print(a[0])  # o/p : 'NAME'
print(type(a[0])) # <class 'str'>

print(a[1])  #  o/p : 'Harish'
print(type(a[1]))  # <class 'str'>

print(a[2])   # o/p: 234
print(type(a[2])) # <class 'int'>

print(a[3])   # o/p : 70.0
print(type(a[3]))# <class 'float'>