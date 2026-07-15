## ==================== List Slicing ==================
# it means wwe want to in between certain range
# syntax : List[start : end] 


numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])     # it give in between index 1 to index(n-1)4-1 
                        # o/p : [20, 30, 40]

print(numbers[:3])    # it take defalutly as index 0  and go 3-1
                      # o/p : [10,20, 30]

print(numbers[2:])   # here startswith index 2  and ends defaultly  last element 
                    # o/p : [30, 40, 50]

print(numbers[::-1]) # here it gives reverse a list
                     # o/p: [50, 40, 30, 20, 10]



## ========================  Useful Built-in Functions =======================
# some built in function used here

numbers = [1, 2, 8, 1,9]

print(len(numbers))   # 5   it give length of the list

print(max(numbers))   # 8    it give highest number in llist

print(min(numbers))   # 1   it give  lowest number in list

print(sum(numbers))   # 21   it add all elements in the list

print(sorted(numbers))# [1,1, 2, 8,9]   it give an order list




## ================================== List comphrehensions =====================
# syntax : new_list = [expression for item in iterable]
# we can write single line code in between
# it reduce the code and time


squares = [x * x for x in range(1, 6)]

print(squares)  # o/p : [1, 4, 9, 16, 25]



## with out List comphrehensions

# but here i used four line of code 

squares = []

for x in range(1, 6):
    squares.append(x**2)   

print(squares)     # o/p : [1, 4, 9, 16, 25]







