import time

calories = 0
elf = 0

start = time.time()

calories_to_elf_dict = {}

with open('input.txt', 'r') as f:
    for line in f:
        number = line.strip()
        if len(number) > 0:
            calories += int(number)
        else:
            elf += 1
            calories_to_elf_dict[calories] = elf
            calories = 0

    calories_to_elf_dict[calories] = elf + 1

calories_list = list(calories_to_elf_dict.keys())
calories_list.sort(reverse=True)

elf_top_1 = calories_list[0]
elf_top_2 = calories_list[1]
elf_top_3 = calories_list[2]

total = elf_top_1 + elf_top_2 + elf_top_3

end = time.time()

print(f"The total number of calories carried are {total}")
print(f"Process took: {round(end - start, 5)} seconds")
