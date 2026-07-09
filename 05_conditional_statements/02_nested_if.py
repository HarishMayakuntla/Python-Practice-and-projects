
# nested if : if condition inside another if condition



age = 20
citizen = True

if age >= 18:       # here check on one statement
    if citizen:     # inside there is another statement
        print("Eligible to vote")
    else:
        print("Not a citizen")   
else:
    print("Too young")          # out put is : Eligible to voteS