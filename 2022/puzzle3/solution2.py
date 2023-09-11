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


def find_same_item_trio(compartments):
    compartments.sort(key=lambda x: len(x))
    comp1 = compartments[0]
    comp2 = compartments[1]
    comp3 = compartments[2]
    for char1 in comp1:
        for char2 in comp2:
            if char2 == char1:
                for char3 in comp3:
                    if char3 == char1:
                        return char1


start = time.time()
counter = 0
compartments = []

with open('input.txt', 'r') as f:
    for line in f:
        ln = line.strip()

        counter += 1
        compartments.append(ln)
        if counter % 3 == 0:
            total_score += priority_dict[find_same_item_trio(compartments)]
            compartments = []

end = time.time()

print(f"Your total score is: {total_score}")
print(f"Process took: {round(end - start, 5)} seconds")
