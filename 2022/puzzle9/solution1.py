import time


def perform_step_straight(direction, knot):
    row, col = knot
    if direction == "L":
        return tuple([row, col - 1])
    if direction == "R":
        return tuple([row, col + 1])
    if direction == "U":
        return tuple([row + 1, col])
    if direction == "D":
        return tuple([row - 1, col])


def perform_step_head(direction, head):
    return perform_step_straight(direction, head)


def perform_step_diagonally(row_head, col_head, row_tail, col_tail):
    diff_rows = abs(row_tail - row_head)
    diff_cols = abs(col_tail - col_head)

    if row_head > row_tail:
        new_row = row_head - (diff_rows - 1)
    else:
        new_row = row_head + (diff_rows - 1)
    if col_head > col_tail:
        new_col = col_head - (diff_cols - 1)
    else:
        new_col = col_head + (diff_cols - 1)
    return tuple([new_row, new_col])


def perform_step_tail(direction, head, tail):
    row_head, col_head = head
    row_tail, col_tail = tail

    if abs(row_tail - row_head) <= 1 and abs(col_tail - col_head) <= 1:
        return tail

    if ((abs(row_tail - row_head) == 2 and abs(col_tail - col_head) == 0)
            or (abs(row_tail - row_head) == 0 and abs(col_tail - col_head) == 2)):
        return perform_step_straight(direction, tail)

    if ((abs(row_tail - row_head) == 2 and abs(col_tail - col_head) >= 1)
            or (abs(row_tail - row_head) >= 1 and abs(col_tail - col_head) == 2)):
        return perform_step_diagonally(row_head, col_head, row_tail, col_tail)


start = time.time()
tail_states = {}

# initial states
initial_state = (0, 0)
head_state = initial_state
tail_state = initial_state
tail_states[tail_state] = 1

with open('input.txt', 'r') as f:
    for line in f:
        ln = line.strip()
        ln_lst = ln.split(" ")
        direction_head = ln_lst[0]
        num_steps = int(ln_lst[1])
        for dummy_index in range(num_steps):
            head_state = perform_step_head(direction_head, head_state)
            new_tail_state = perform_step_tail(direction_head, head_state, tail_state)
            if new_tail_state != tail_state:
                if new_tail_state in tail_states:
                    tail_states[new_tail_state] += 1
                else:
                    tail_states[new_tail_state] = 1
            tail_state = new_tail_state

end = time.time()

min_x = 100
min_y = 100
max_x = -100
max_y = -100
for coord in tail_states.keys():
    x, y = coord
    if x < min_x:
        min_x = x
    if y < min_y:
        min_y = y
    if abs(x) > max_x:
        max_x = abs(x)
    if abs(y) > max_y:
        max_y = abs(y)

print(f"max_x: {max_x}, min_x: {min_x}, max_y: {max_y}, min_y: {min_y}")

# print(tail_states)

trans_row = 4
trans_col = 0
print_list = list(map(lambda n: (trans_row - n[0], n[1]), tail_states.keys()))

# print(tail_states)
# print(print_list)

# for i in range(max_x + 1):
#     row_list = []
#     for j in range(max_y + 2):
#         if (i, j) in print_list:
#             if (i, j) == initial_state:
#                 row_list.append("s")
#             else:
#                 row_list.append("#")
#         else:
#             row_list.append(".")
#     print(" ".join(row_list))

num_positions = 0
for visit in tail_states.values():
    if visit >= 1:
        num_positions += 1

print(f"The number of positions the tail of the rope visit at least once is: {num_positions}")
print(f"Process took: {round(end - start, 5)} seconds")
