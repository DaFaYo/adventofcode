import time

grid = {}

i = 0
j = 0
N = 0


def calc_scenic_score(coords):
    row, col = coords
    tree_height = grid[coords]

    # look left from given tree
    l_col = col
    view_dist_left = 0
    while l_col > 0:
        if grid[(row, l_col - 1)] >= tree_height:
            view_dist_left += 1
            break
        else:
            view_dist_left += 1
            l_col -= 1

    # look right from given tree
    r_col = col
    view_dist_right = 0
    while r_col < N - 1:
        if grid[(row, r_col + 1)] >= tree_height:
            view_dist_right += 1
            break
        else:
            view_dist_right += 1
            r_col += 1

    # look down from given tree
    d_row = row
    view_dist_down = 0
    while d_row < N - 1:
        if grid[(d_row + 1, col)] >= tree_height:
            view_dist_down += 1
            break
        else:
            view_dist_down += 1
            d_row += 1

    # look down from given tree
    u_row = row
    view_dist_up = 0
    while u_row > 0:
        if grid[(u_row - 1, col)] >= tree_height:
            view_dist_up += 1
            break
        else:
            view_dist_up += 1
            u_row -= 1

    scenic_score = view_dist_left * view_dist_right * view_dist_up * view_dist_down
    # print(f"total score: {view_dist_left} * {view_dist_right} * {view_dist_up} * {view_dist_down} = {scenic_score}")
    return scenic_score

start = time.time()
with open('input.txt', 'r') as f:
    for line in f:
        ln = line.strip()
        if N == 0:
            N = len(ln)
        for j in range(N):
            grid[(i, j)] = int(ln[j])
        i += 1

max_scenic_score = 0
coord_tree = None
for i in range(1, N - 1):
    for j in range(1, N - 1):
        coordinates = (i, j)
        score = calc_scenic_score(coordinates)
        if score > max_scenic_score:
            max_scenic_score = score
            coord_tree = coordinates

end = time.time()

print(
    f"The max scenic score is: {max_scenic_score}, for tree: (x, y) = {coord_tree} with height = {grid[coord_tree]}.")
print(f"Process took: {round(end - start, 5)} seconds")
