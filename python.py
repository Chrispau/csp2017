import random as r

iterations = int(raw_input("How many iterations? >> "))
iterations = 100000

doors = ["goat", "goat", "car"]
wins = 0.0
losses = 0.0

for i in range(iterations):
    n = r.randrange(0,3)

    choice = doors[n]
    if n == 0:
        print "You chose door 1."
        print "Monty opens door 2. There is a goat behind this door."
        print "You swapped to door 3."
        wins += 1
        print "You won a " + doors[2] + "\n"
    elif n == 1:
        print "You chose door 2."
        print "Monty opens door 1. There is a goat behind this door."
        print "You swapped to door 3."
        wins += 1
        print "You won a " + doors[2] + "\n"
    elif n == 2:
        print "You chose door 3."
        print "Monty opens door 2. There is a goat behind this door."
        print "You swapped to door 1."
        losses += 1
        print "You won a " + doors[0] + "\n"
    else:
        print "You screwed up"

percentage = (wins/iterations) * 100
print "Wins: " + str(wins)
print "Losses: " + str(losses)
print "You won " + str(percentage) + "% of the time"