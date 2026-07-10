##  infinity loop

# while True:
#     print('hello world')    # it give infinity values


## break with while
#The break statement immediately exits the loop.
i = 1
while True:
    print(i)      # it gives until i bcomes 5 after it exit the loop
    if i == 5:
        break
    i += 1


## continue with while
# The continue statement skips the rest of the current iteration and starts the next iteration.
i = 0

while i < 5:
    i += 1               # here i become 5 but it skip 3
    if i == 3:
        continue
    print(i)              

## pass with while
# The pass statement is a placeholder that does nothing.

i = 1
while i <= 5:
    pass       # it cannot give any output it execute
    i += 1 


## else with while
# The else block executes only if the loop ends normally.
i = 1

while i <= 3:
    print(i)
    i += 1                 # it will give normal output 
else:
    print("Loop Finished")