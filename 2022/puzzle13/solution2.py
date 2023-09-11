import time
import json
from copy import deepcopy


def compare_lists(first, second):
    while len(first) > 0 and len(second) > 0:
        left = first.pop(0)
        right = second.pop(0)

        if type(left) == int and type(right) == int:
            if left < right:
                return 1
            elif left > right:
                return -1
        if type(left) == list and type(right) == list:
            sub_comparison = compare_lists(left, right)
            if sub_comparison != 0:
                return sub_comparison
        if type(left) == int and type(right) == list:
            sub_comparison = compare_lists(list([left]), right)
            if sub_comparison != 0:
                return sub_comparison
        if type(left) == list and type(right) == int:
            sub_comparison = compare_lists(left, list([right]))
            if sub_comparison != 0:
                return sub_comparison

    if len(first) < len(second):
        return 1
    elif len(first) > len(second):
        return -1
    else:
        return 0


pairs = {}
pair = 0
pair_set = []
with open('input.txt', 'r') as f:
    for line in f:
        ln = line.strip()

        if ln:
            res = json.loads(ln)
            pair_set.append(res)
        else:
            pair += 1
            pairs[pair] = pair_set
            pair_set = []

    pair += 1
    pairs[pair] = pair_set
    pair_set = []

start = time.time()

# x = [[2]]
# y = [[6]]


pair_x = 0
pair_y = 0
total = 0
for pair_items in pairs.values():
    total += 2

    if compare_lists(deepcopy(pair_items[0]), [[2]]) == 1:
        pair_x += 1
    if compare_lists(deepcopy(pair_items[1]), [[2]]) == 1:
        pair_x += 1
    if compare_lists(deepcopy(pair_items[0]), [[6]]) == 1:
        pair_y += 1
    if compare_lists(deepcopy(pair_items[1]), [[6]]) == 1:
        pair_y += 1

end = time.time()

print(total)
print(pair_x)
print(pair_y)
decoder_key = (pair_x + 1) * (pair_y + 2)

print(f"The decoder key for the distress signal is: {decoder_key}")
