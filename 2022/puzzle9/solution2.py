import time


def perform_step_straight(row_head, col_head, row_tail, col_tail):
    diff_rows = abs(row_tail - row_head)
    diff_cols = abs(col_tail - col_head)

    if diff_rows == 2 and diff_cols == 0:
        if row_tail < row_head:
            return tuple([row_tail + 1, col_tail])
        else:
            return tuple([row_tail - 1, col_tail])
    if diff_rows == 0 and diff_cols == 2:
        if col_tail < col_head:
            return tuple([row_tail, col_tail + 1])
        else:
            return tuple([row_tail, col_tail - 1])


def perform_step_head(direction, head):
    row, col = head
    if direction == "L":
        return tuple([row, col - 1])
    if direction == "R":
        return tuple([row, col + 1])
    if direction == "U":
        return tuple([row + 1, col])
    if direction == "D":
        return tuple([row - 1, col])


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


def perform_step_tail(head, tail):
    row_head, col_head = head
    row_tail, col_tail = tail

    if abs(row_tail - row_head) <= 1 and abs(col_tail - col_head) <= 1:
        return tail

    if ((abs(row_tail - row_head) == 2 and abs(col_tail - col_head) == 0)
            or (abs(row_tail - row_head) == 0 and abs(col_tail - col_head) == 2)):
        return perform_step_straight(row_head, col_head, row_tail, col_tail)

    if ((abs(row_tail - row_head) == 2 and abs(col_tail - col_head) >= 1)
            or (abs(row_tail - row_head) >= 1 and abs(col_tail - col_head) == 2)):
        return perform_step_diagonally(row_head, col_head, row_tail, col_tail)


start = time.time()

initial_state = tuple([0, 0])

# {"H": (state), "1": (state), ..., "9": (state) }
rope_states = {}
for i in range(10):
    rope_states[i] = initial_state

rope_tail_paths = {}
for i in range(9):
    rope_tail_paths[i + 1] = {}
    rope_tail_paths[i + 1][initial_state] = 1

N = 21
M = 27

trans_row = 15
trans_col = 11
print_dict = {}


def print_grid(direction, steps, step=0):
    print()
    if step != 0:
        print(f"== {direction} {steps}  Step:{step} ==")
    else:
        print(f"== {direction} {steps} ==")
    print()

    for i in range(10):
        state = rope_states[i]
        print_dict[i] = (trans_row - state[0], trans_col + state[1])

    for i in range(N):
        row = ["."] * (M + 1)
        for j in range(M):
            if (i, j) in print_dict.values():
                for key in print_dict.keys():
                    if print_dict[key] == (i, j):
                        if key == 0:
                            letter = "H"
                        else:
                            letter = str(key)
                        row[j] = letter
                        break
        print(" ".join(row))


with open('input.txt', 'r') as f:
    for line in f:
        ln = line.strip()
        ln_lst = ln.split(" ")
        direction_head = ln_lst[0]
        num_steps = int(ln_lst[1])
        for dummy_index in range(num_steps):
            rope_states[0] = perform_step_head(direction_head, rope_states[0])
            for i in range(9):
                new_tail_state = perform_step_tail(rope_states[i], rope_states[i + 1])
                if new_tail_state != rope_states[i + 1]:
                    if new_tail_state in rope_tail_paths[i + 1]:
                        rope_tail_paths[i + 1][new_tail_state] += 1
                    else:
                        rope_tail_paths[i + 1][new_tail_state] = 1
                rope_states[i + 1] = new_tail_state

        # print_grid(direction_head, num_steps, step=0)

end = time.time()

tail_paths_9 = rope_tail_paths[9]

print_list = list(map(lambda n: (trans_row - n[0], trans_col + n[1]), tail_paths_9.keys()))

# print(tail_states)
# print(print_list)
# print()
# for i in range(21):
#     row_list = []
#     for j in range(27):
#         if (i, j) in print_list:
#             if (i, j) == initial_state:
#                 row_list.append("s")
#             else:
#                 row_list.append("#")
#         else:
#             row_list.append(".")
#     print(" ".join(row_list))
#
# print()
num_positions = 0
for visit in tail_paths_9.values():
    if visit >= 1:
        num_positions += 1

print(f"The number of positions the tail of the rope visit at least once is: {num_positions}")
print(f"Process took: {round(end - start, 5)} seconds")
