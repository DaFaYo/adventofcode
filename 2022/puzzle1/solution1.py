import time

calories = 0
max_calories = 0
elf = 0
elf_max_calories = 0

start = time.time()
with open('input.txt', 'r') as f:
    for line in f:
        number = line.strip()
        if len(number) > 0:
            calories += int(number)
        else:
            elf += 1
            if calories > max_calories:
                max_calories = calories
                elf_max_calories = elf
            calories = 0

    if calories > max_calories:
        max_calories = calories
        elf_max_calories = elf + 1

end = time.time()
print(f"Max calories are: {max_calories}, carried by Elf {elf_max_calories}")
print(f"Process took: {round(end - start, 5)} seconds")
