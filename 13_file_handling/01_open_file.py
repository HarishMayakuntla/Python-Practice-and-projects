## ============= what is file ==================

#  A file is a place where data is stored permanently.

# examples :
    # file.csv
    # file.json
    # file.txt
    # image.png

# python allows to :

   # Read files
   # Write files
   # Append the data
   # Delete files
   # Renamefiles

## ========================== opening file ========================

# Syntax:
#    
#     file=open('file_name','mode')
#  
#     file.close()


## ============ modes =========

# 'r' ----> READ()

# Syntax :

#      file=open('file_name','r')

#      file.close()




# example :


file = open('i_am.txt','r')

print(file.read())

file.close()   # o/p : i am harish mayakuntla and u am data science student




## we can give instuction to read() mode how many count letters
# 

file = open('i_am.txt','r')

print(file.read(22))

file.close()        # o/p : i am harish mayakuntla

## read all lines

file = open("i_am.txt", "r")
print(file.readlines())
file.close()


# 'w' -------> write()


