# ================= voting system =========================
# use append()
# and count()

votes = []

while True:
    name = input("Vote or 'exit': ")    # here loop excutes until user get 'vote'

    if name == "exit":           # here  loop stops user give 'exit'
        break

    votes.append(name)         # here the name values add to the list

print("\nResults")

for candidate in votes:
    p=candidate
print(p, ":", votes.count(p))     # i need to how many times it appears



# o/p :

# Vote or 'exit': vote 
# Vote or 'exit': vote
# Vote or 'exit': vote
# Vote or 'exit': exit

# Results
# vote : 3