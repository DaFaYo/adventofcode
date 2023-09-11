import time


class Node:
    def __init__(self, position, parent=None, move=None):
        self.position = position
        self.parent = parent
        self.move = move

        self.x = self.position[0]
        self.y = self.position[1]

    def update_move(self, other):
        if self.x == other.x - 1:
            self.move = "^"
        if self.x == other.x + 1:
            self.move = "V"
        if self.y == other.y - 1:
            self.move = "<"
        if self.y == other.y + 1:
            self.move = ">"

    def __repr__(self):
        return f"Node{self.position}"

    def __eq__(self, other):
        if type(other) is type(self):
            return (self.x == other.x) and (self.y == other.y)
        else:
            return False

    def __hash__(self):
        return hash((self.x, self.y))


alphabet = "abcdefghijklmnopqrstuvwxyz"
length = 0
width = 0
current_position = ""
best_signal_location = ""

nodes_to_height = {}
heights_to_ints = {}

for i in range(26):
    heights_to_ints[alphabet[i]] = i

heights_to_ints["S"] = 0
heights_to_ints["E"] = 25


def moves(grid_node, grid_width, grid_length):
    _moves = []
    x, y = grid_node.position
    if x > 0:
        _moves.append(Node(tuple([x - 1, y])))
    if x < (grid_length - 1):
        _moves.append(Node(tuple([x + 1, y])))
    if y > 0:
        _moves.append(Node(tuple([x, y - 1])))
    if y < (grid_width - 1):
        _moves.append(Node(tuple([x, y + 1])))

    return _moves


def bfs(graph, root, goal, graph_width, graph_length):
    queue = []
    explored = {}
    for key in graph.keys():
        explored[key] = False

    explored[root] = True
    queue.append(root)

    while queue:
        curr_node = queue.pop(0)
        if graph[curr_node] == graph[goal]:
            return curr_node
        for neighbour in moves(curr_node, graph_width, graph_length):
            if not explored[neighbour]:
                if (heights_to_ints[nodes_to_height[neighbour]]
                        <= heights_to_ints[nodes_to_height[curr_node]] + 1):
                    neighbour.update_move(curr_node)
                    explored[neighbour] = True
                    neighbour.parent = curr_node
                    queue.append(neighbour)


height_a_nodes = []
with open('input.txt', 'r') as f:
    for line in f:

        ln = line.strip()
        if width == 0:
            width = len(ln)

        for w in range(width):
            _height = ln[w]

            node = Node(tuple([length, w]))
            nodes_to_height[node] = _height
            if _height == "a":
                height_a_nodes.append(node)

            if _height == "S":
                height_a_nodes.append(node)
                current_position = node
            if _height == "E":
                best_signal_location = node

        length += 1


def compute_steps(sol_node):
    steps = {}
    while sol_node:
        if sol_node.parent:
            steps[sol_node.parent.position] = sol_node.move
        sol_node = sol_node.parent

    return steps


start = time.time()

num_steps = width * length
optimal_shortest_path_node = None
for starting_location in height_a_nodes:

    solution_node = bfs(nodes_to_height, starting_location, best_signal_location, width, length)

    if not solution_node:
        continue

    _steps = compute_steps(solution_node)

    if len(_steps) < num_steps:
        num_steps = len(_steps)
        optimal_shortest_path_node = solution_node

end = time.time()

fewest_steps = compute_steps(optimal_shortest_path_node)

for r in range(length):
    row = ["."] * width
    for c in range(width):
        if (r, c) in fewest_steps.keys():
            if fewest_steps[(r, c)]:
                row[c] = fewest_steps[(r, c)]
        if (r, c) == best_signal_location.position:
            row[c] = "E"
    print(" ".join(row))


print()
print(f"the fewest steps required to move from current position to the best signal location is: {len(fewest_steps.keys())}.")
print(f"Process took: {round(end - start, 5)} seconds")
