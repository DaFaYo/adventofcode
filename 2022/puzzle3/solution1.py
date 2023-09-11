import math
import time

priority_list = []
priority_list[:0] = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

priority_dict = {}
priority_value = 0
for letter in priority_list:
    priority_value += 1
    priority_dict[letter] = priority_value

total_score = 0


def find_same_item_pair(comp1, comp2):
    lt = len(comp1)
    for i in range(lt):
        for j in range(lt):
            if comp2[j] == comp1[i]:
                return comp1[i]


start = time.time()
with open('input.txt', 'r') as f:
    for line in f:
        ln = line.strip()
        length = len(ln)
        halve = math.floor(length / 2)
        compartment1 = ln[0:halve]
        compartment2 = ln[halve: length]
        total_score += priority_dict[find_same_item_pair(compartment1, compartment2)]

end = time.time()

print(f"Your total score is: {total_score}")
print(f"Process took: {round(end - start, 5)} seconds")
