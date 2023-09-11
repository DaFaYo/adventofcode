import time

grid = {}

i = 0
j = 0
N = 0


def is_tree_visible(coords):
    row, col = coords
    tree_height = grid[coords]

    # look from left
    l_col = 0
    while l_col < col:
        if grid[(row, l_col)] >= tree_height:
            break
        else:
            l_col += 1
    if l_col == col:
        return True

    # look from right
    r_col = N - 1
    while r_col > col:
        if grid[(row, r_col)] >= tree_height:
            break
        else:
            r_col -= 1
    if r_col == col:
        return True

    # look down
    d_row = 0
    while d_row < row:
        if grid[(d_row, col)] >= tree_height:
            break
        else:
            d_row += 1
    if d_row == row:
        return True

    # look up
    u_row = N - 1
    while u_row > row:
        if grid[(u_row, col)] >= tree_height:
            break
        else:
            u_row -= 1
    if u_row == row:
        return True

    # print(f"coords: {coords}, height: {grid[coords]}")
    return False


start = time.time()
with open('input.txt', 'r') as f:
    for line in f:
        ln = line.strip()
        if N == 0:
            N = len(ln)
        for j in range(N):
            grid[(i, j)] = int(ln[j])
        i += 1

trees_int = 0
print(f"Square is {N} by {N}.")
for i in range(1, N - 1):
    for j in range(1, N - 1):
        coordinates = (i, j)
        if is_tree_visible(coordinates):
            # print(coordinates)
            # print(grid[coordinates])
            trees_int += 1

end = time.time()

trees_extr = (4 * N) - 4
total_trees = trees_int + trees_extr

# print(grid)
print(
    f"The total number of trees visible are: outside = {trees_extr} + interior = {trees_int}. Gives a total of {total_trees}.")
print(f"Process took: {round(end - start, 5)} seconds")
