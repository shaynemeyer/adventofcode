total = 0

# Win states

# Rules
# Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock

# Opponents options
# A for Rock, B for Paper, and C for Scissors

# Your options
# X for Rock, Y for Paper, and Z for Scissors

# "CX" || "BZ" || "AY" -> 6
winStates = ["CX", "BZ", "AY"]
# Both equal -> 3


# Rock -> 1, Paper -> 2, Scissors -> 3
def roundScore(selection):
    if selection in "AX":
        # rock
        return 1
    elif selection in "BY":
        # paper
        return 2
    else:
        # scissors
        return 3


def outcome(x, y):
    if roundScore(x) == roundScore(y):
        # draw
        return 3, "draw", x
    elif x + y in winStates:
        # win
        return 6, "win"
    else:
        # loss
        return 0, "loss"


file = open("input.txt", "r")

for line in file:
    x, y = line.strip().split(" ")
    rScore = roundScore(y)
    oScore, result = outcome(x, y)

    totalForRound = rScore + oScore
    print("You", result, " - score for the round:", totalForRound)

    total += totalForRound
print(total)
