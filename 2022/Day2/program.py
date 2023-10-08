def score(val):
    # Opponent: A for Rock, B for Paper, and C for Scissors
    # Responses: X for Rock, Y for Paper, and Z for Scissors
    if val in ["A", "X"]:
        return 1
    elif val in ["B", "Y"]:
        return 2
    elif val in ["C", "Z"]:
        return 3
    else:
        return 0


def winner(p1, p2):
    if p1 > p2:
        return 1
    elif p1 < p2:
        return 2
    else:
        return 0


file = open("input.txt", "r")

player1Score = 0
player2Score = 0
wins = 0
losses = 0

for line in file:
    # strip whitespace
    values = line.strip().split(" ")

    opponentVal = values[0]
    yourVal = values[1]

    oppScore = score(opponentVal)
    yourScore = score(yourVal)

    roundWinner = winner(oppScore, yourScore)

    print(
        "Opponent Score:",
        oppScore,
        "Your Score:",
        yourScore,
        "Winner",
        roundWinner,
    )

    player1Score += oppScore
    player2Score += yourScore

    # (0 if you lost, 3 if the round was a draw, and 6 if you won)
    if roundWinner == 1:
        # opponent wins
        player1Score += 6
        player2Score += 0
        losses += 1
    elif roundWinner == 2:
        # you win
        player1Score += 0
        player2Score += 6
        wins += 1
    elif roundWinner == 0:
        # draw
        player1Score += 3
        player2Score += 3

if player1Score > player2Score:
    print("Opponent wins with a score:", player1Score, " to :", player2Score)
elif player1Score < player2Score:
    print("You win with score:", player2Score, " to :", player1Score)
else:
    print("Match ends in a draw, with a score:", player1Score, " to :", player2Score)
print("Wins:", wins)
print("Losses:", losses)
