## -------------Cricket Scorecard ---------------------

players = (
    ("Virat", 185),
    ("Rohit", 264),
    ("Gill", 156),
    ("Rahul", 117)
)

highest = players[0]

for player in players:
    if player[1] > highest[1]:
        highest = player

print("Top Scorer:", highest[0])
print("Runs:", highest[1])