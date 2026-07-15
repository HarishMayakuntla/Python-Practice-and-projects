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












# git status
# git add .
# git commit -m "Added list methods examples"
# git push origin main