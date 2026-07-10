##  break with for loop
# it immediatly stops the loop

for i in range(1, 11):
    if i == 6:     # it has range i to 11 but here it give only 6 values after it will be stop
        break
    print(i)


## continue Statement
# continue statement skip the present iteration and moves next iteration.abs

for i in range(1, 6):
    if i == 3:
        continue   # it will skip the 3 value 
    print(i)

## pass Statement 
#  pass acts like place holder , mean it's does nothing.
for i in range(5):
    pass    # it's a condition but here nothing

print("Loop Finished")


## else with for 
#  it is execute the for normally.

for i in range(10):
    print(i)
else:
    print('iteration complete')

    