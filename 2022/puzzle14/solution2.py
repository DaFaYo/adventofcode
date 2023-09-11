import time

sand_point = (500, 0)
rocks = set()
grains_of_sand = set()


def can_move(sand):
    global floor
    x, y = sand

    if y + 1 == floor:
        return False
    for dest in [(x, y + 1), (x - 1, y + 1), (x + 1, y + 1)]:
        if (dest not in rocks) and (dest not in grains_of_sand):
            return True
    return False


def move(sand):
    x, y = sand
    _dest = (x, y + 1)
    if _dest not in rocks and _dest not in grains_of_sand:
        return _dest
    _dest = (x - 1, y + 1)
    if _dest not in rocks and _dest not in grains_of_sand:
        return _dest
    _dest = (x + 1, y + 1)
    if _dest not in rocks and _dest not in grains_of_sand:
        return _dest
    return None


# x is distance to the right
# y is the distance down
def update_rocks(rock1, rock2):
    x1, y1 = rock1
    x2, y2 = rock2
    rocks.add(rock1)
    rocks.add(rock2)

    if x1 < x2:
        for k in range(1, (x2 - x1)):
            rocks.add((x1 + k, y1))
    elif x1 > x2:
        for k in range(1, (x1 - x2)):
            rocks.add((x2 + k, y2))
    elif y1 < y2:
        for k in range(1, (y2 - y1)):
            rocks.add((x1, y1 + k))
    else:
        # y1 > y2:
        for k in range(1, (y1 - y2)):
            rocks.add((x2, y2 + k))


min_x = float('inf')
max_x = 0
min_y = 0  # This stay's zero
max_y = 0
floor = 0


def update_min_max_grid(x1, x2, y1, y2):
    global min_x, max_x, max_y

    if x1 <= x2:
        _min_x = x1
        _max_x = x2
    else:
        _min_x = x2
        _max_x = x1

    if y1 <= y2:
        _max_y = y2
    else:
        _max_y = y1

    if _min_x < min_x:
        min_x = _min_x
    if _max_x > max_x:
        max_x = _max_x
    if _max_y > max_y:
        max_y = _max_y


with open('input.txt', 'r') as f:
    for line in f:
        ln = line.strip()
        ln = ln.split(" -> ")

        for i in range(len(ln) - 1):
            c1 = ln[i].split(",")
            c2 = ln[i + 1].split(",")

            x_1 = int(c1[0])
            y_1 = int(c1[1])
            x_2 = int(c2[0])
            y_2 = int(c2[1])

            update_min_max_grid(x_1, x_2, y_1, y_2)
            update_rocks((x_1, y_1), (x_2, y_2))


def print_grid():
    global min_x, max_x, min_y, max_y

    for index in range(len(str(max_x))):
        row = [" "] * ((max_x + 1) - min_x)
        for x in range(min_x, max_x + 1):
            if x == 500:
                row[500 - min_x] = "500"[index]
            if x == min_x:
                row[0] = str(min_x)[index]
            if x == max_x:
                row[max_x - min_x] = str(max_x)[index]
        row = " ".join(row)
        print("  ".join([" ", row]))

    for y in range(min_y, max_y + 1):
        row = ["."] * ((max_x + 1) - min_x)
        for x in range(min_x, max_x + 1):
            if y == 0 and x == 500:
                row[500 - min_x] = "+"
            if (x, y) in rocks:
                row[x - min_x] = "#"
            if (x, y) in grains_of_sand:
                row[x - min_x] = "o"
        row = " ".join(row)
        print("  ".join([str(y), row]))


start = time.time()

floor = max_y + 2
while True:

    new_grain_of_sand = sand_point

    while can_move(new_grain_of_sand):

        new_grain_of_sand = move(new_grain_of_sand)

    grains_of_sand.add(new_grain_of_sand)
    if new_grain_of_sand == sand_point:
        break
    # print_grid()

end = time.time()

# print_grid()
# print()
print(f"The units of sand that come to rest before flowing into the abyss are: {len(grains_of_sand)}")
print(f"Process took: {round(end - start, 5)} seconds")
