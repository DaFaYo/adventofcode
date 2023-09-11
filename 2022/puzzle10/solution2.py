import time

start = time.time()

tick = 0
register = 1
instruction = None

sprite_position = "###....................................."
crt_row = []
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
            position = (tick - 1) % 40
            pixel = sprite_position[position]
            crt_row.append(pixel)

            if tick % 40 == 0:
                # print(f"(tick: {tick} * register: {register}) = {(tick * register)}")
                print(" ".join(crt_row))
                crt_row = []

            if cycle == 1:
                # print(f"Cycle 0, tick: {tick} register: {register}, value: {value}")
                if value != 0:
                    register += value

                    new_sprite_position = ["."] * 41
                    new_sprite_position[register - 1] = "#"
                    new_sprite_position[register] = "#"
                    new_sprite_position[register + 1] = "#"
                    sprite_position = "".join(new_sprite_position)

            cycle -= 1

end = time.time()

print(f"Process took: {round(end - start, 5)} seconds")
