import time

# The Elf finishes helping with the tent and sneaks back over to you.
# "Anyway, the second column says how the round needs to end: X means you need to lose, "
# "Y means you need to end the round in a draw, and Z means you need to win. Good luck!"

lookup_table = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}

pick_to_win = {"A": "B", "B": "C", "C": "A"}
pic_to_lose = {"A": "C", "B": "A", "C": "B"}

total_score = 0

start = time.time()
with open('input.txt', 'r') as f:
    for line in f:
        ln = line.strip()
        opponent = ln[0]
        you = ln[2]

        if you == "X":
            # You need to lose
            total_score += lookup_table[pic_to_lose[opponent]]
        if you == "Y":
            # You need a draw, you pick your opponent's guess
            total_score += lookup_table[opponent] + 3
        if you == "Z":
            # You need to win
            total_score += lookup_table[pick_to_win[opponent]] + 6

end = time.time()

print(f"Your total score is: {total_score}")
print(f"Process took: {round(end - start, 5)} seconds")
