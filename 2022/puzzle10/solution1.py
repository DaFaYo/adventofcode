import time

start = time.time()

tick = 0
register = 1
cycles_set = set()
cycles_0 = 20
for i in range(6):
    cycles_set.add(cycles_0 + (40 * i))

signal_strength = 0
instruction = None
with open('input.txt', 'r') as f:
    for line in f:
        ln = line.strip()
        ln_lst = ln.split(" ")

        instruction = ln_lst[0]
        if instruction == "noop":
            cycle = 1
            value = 0
        if instruction == "addx":
            cycle = 2
            value = int(ln_lst[1])

        while cycle != 0:
            tick += 1
            if tick in cycles_set:
                # print(f"(tick: {tick} * register: {register}) = {(tick * register)}")
                signal_strength += (tick * register)

            if cycle == 1:
                # print(f"Cycle 0, tick: {tick} register: {register}, value: {value}")
                register += value

            cycle -= 1

end = time.time()

print(f"The sum of the signal strengths is {signal_strength}.")
print(f"Process took: {round(end - start, 5)} seconds")
