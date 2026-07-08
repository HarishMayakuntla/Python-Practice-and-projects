##  complex    
        # complex is a combination of  real part and imaginary part
        #  ex : 2+6j like
        #  here  only complex deals with string and boolean.

##### ----- complex to integer ----------
   #   so ---its ---shows--- error
a = 3 + 4j
print(int(a)) # TypeError: can't convert complex to int
# why because here twoparts there so int deals with only realpart but here other part is there thats why it shows error


#####--------complex to float ---------
  #------its ---shows--- error
a = 3 + 4j
print(float(a))  #TypeError: can't convert complex to float
# why because here twoparts there so float deals with only realpart but here other part is there thats why it shows error


####  ----------complex to  string-----------

a = 3 + 4j
print(str(a))   # it showes '(3+4j)' 
print(type(str(a)))#   and it is <class 'str'>



#####  --------------complex  to boolean -----------
a = 3 + 4j
b=bool(a)
print(b)   #   showes True
print(type(b))   #   showes <class 'bool'>


a= 0j
b=bool(a)
print(b)       #   showes False
print(type(b)) #   showes <class 'bool'>

