import time

# A = "Rock"
# B = "Paper"
# C = "Scissors"
#
# X = "Rock"
# Y = "Paper"
# Z = "Scissors"

# Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock
#
# Your total score is the sum of your scores for each round.
# The score for a single round is the score for the shape you selected
# (1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the
# outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).
#

lookup_table = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}

# If the difference of (X|Y|Z - A|B|C)  = 1 or -2 you won. If the difference = -1 or 2
# you loss and if the difference = 0. It's a draw
score_card = {-2: 6, -1: 0, 0: 3, 1: 6, 2: 0}

total_score = 0

start = time.time()
with open('input.txt', 'r') as f:
    for line in f:
        ln = line.strip()
        opponent = ln[0]
        you = ln[2]

        difference = lookup_table[you] - lookup_table[opponent]
        total_score += lookup_table[you] + score_card[difference]

end = time.time()

print(f"Your total score is: {total_score}")
print(f"Process took: {round(end - start, 5)} seconds")
