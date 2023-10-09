# Rock -> 1, Paper -> 2, Scissors -> 3
def roundScore(selection):
    if selection == "A":
        # rock
        return 1
    elif selection == "B":
        # paper
        return 2
    else:
        # scissors
        return 3


def toWin(x):
    if x == "C":
        # Rock beats scissors
        return "A"
    elif x == "B":
        # Scissors defeats Paper
        return "C"
    else:
        #  Paper defeats Rock
        return "B"


def toLose(x):
    if x == "A":
        # Rock beats scissors
        return "C"
    elif x == "B":
        # Paper beats Rock
        return "A"
    else:
        # Scissors beats Paper
        return "B"


# X means you need to lose,
# Y means you need to end the round in a draw,
# and Z means you need to win.
def actionToTake(action, opponent):
    if action == "Y":
        return "draw", 3, opponent
    elif action == "X":
        toPlay = toLose(opponent)
        return "lose", 0, toPlay
    else:
        toPlay = toWin(opponent)
        return "win", 6, toPlay


total = 0

file = open("input.txt", "r")

for line in file:
    x, y = line.strip().split(" ")

    result, outcomeScore, play = actionToTake(y, x)
    roundTotal = roundScore(play) + outcomeScore
    print("Round score:", roundTotal)
    total += roundTotal
    print(result)

print(total)
