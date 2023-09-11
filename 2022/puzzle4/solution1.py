import math
import time


def pair_contains_other(elf_1, elf_2):
    elf_1_from, elf_1_to = list(map(int, elf_1.split("-")))
    elf_2_from, elf_2_to = list(map(int, elf_2.split("-")))

    return (elf_1_from <= elf_2_from and elf_1_to >= elf_2_to) or \
           (elf_2_from <= elf_1_from and elf_2_to >= elf_1_to)


pairs_containing_other = 0
start = time.time()
with open('input.txt', 'r') as f:
    for line in f:
        ln = line.strip()
        elf1, elf2 = ln.split(",")
        if pair_contains_other(elf1, elf2):
            pairs_containing_other += 1

end = time.time()

print(f"Number of pairs containing on or the other is: {pairs_containing_other}")
print(f"Process took: {round(end - start, 5)} seconds")
