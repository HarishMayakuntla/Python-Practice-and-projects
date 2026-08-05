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

# ================== 'r' ----> READ()

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

file.close()        # o/p : ['i am harish mayakuntla and u am data science student']


# ===================== 'w' -------> write()


file = open("data.txt", "w")

file.write("Hello Python")

file.close()   # it will create txt file outside


  ##  write multiple lines

f = open("data.txt", "w")

f.write("Python\n")
f.write("NumPy\n")
f.write("Pandas\n")

f.close()



## writelines()

f = open("data.txt", "w")

lines = [
    "Python\n",
    "NumPy\n",
    "Pandas\n"
]

f.writelines(lines)

f.close()



## ====================== Append data -------> add data

f = open("data.txt", "a")

f.write("\nMatplotlib")

f.close()




## ====================== Create a new file ----------> create new file

f = open("newfile.txt", "x")

f.write("Hello")

f.close()



##  =======================  with open()--------------> open the file

with open("data.txt", "r") as f:
    data = f.read()

print(data)

