import time
import json


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

# 1 2 3 4  5  6  7
# 1 4 7 10 13 16 19
# 0 2 4 6  8  10 12


sum_of_pairs_right_order = 0
for pair, pair_items in pairs.items():

    if compare_lists(pair_items[0], pair_items[1]) == 1:
        print(pair + (pair - 1) * 2)
        sum_of_pairs_right_order += pair

end = time.time()

print(f"The sum of the indices pairs in the right order is: {sum_of_pairs_right_order}")
print(f"Process took: {round(end - start, 5)} seconds")
