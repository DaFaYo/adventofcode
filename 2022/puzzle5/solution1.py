import time
import re

starting_stacks_dict = {}
for dummy_index in range(9):
    starting_stacks_dict[dummy_index + 1] = []


def read_starting_stacks_input(ln):
    for index in range(0, 4 * 9, 4):
        if ln[index] == "[":
            starting_stacks_dict[(index / 4) + 1].append(ln[index + 1])


def rearrange_stack(ln):
    lst = [int(s) for s in re.findall(r'\b\d+\b', ln)]
    num_crates = lst[0]
    stack_from = lst[1]
    stack_to = lst[2]
    while num_crates > 0:
        crate = starting_stacks_dict[stack_from].pop(0)
        starting_stacks_dict[stack_to].insert(0, crate)
        num_crates -= 1


line_number = 0
start = time.time()
with open('input.txt', 'r') as f:
    for line in f:
        line_number += 1
        if line_number < 9:
            read_starting_stacks_input(line)

        elif line_number >= 11:
            rearrange_stack(line)


end = time.time()

top_crates = ""
for stack in starting_stacks_dict.values():
    top_crates += stack[0]


print(f"The crates that end up on top of each stack are: {top_crates}")
print(f"Process took: {round(end - start, 5)} seconds")
