import time
import operator
import copy

N = 8
valve_flow_rate = {}
valve_neighbours = {}
start_valve = None
valves_zero_flow_rate = set()
valves_with_flow_rate = 0


# (("AA",), 0)
def bfs(root):
    explored = set()
    goal = []
    for r in root:
        explored.add(r[0][-1])

    queue = [((root[-1][0][-1],), root[-1][1])]

    while queue:
        v = queue.pop()

        last_valve = v[0][-1]
        if not (last_valve in valves_zero_flow_rate) and not (last_valve in explored):
            goal.append((v[0], v[1] + 1))

        for neighbour in valve_neighbours[last_valve]:

            if neighbour not in v[0]:
                _new_path = v[0] + (neighbour,)

                if (_new_path not in explored) and (v[1] < 30):
                    explored.add(_new_path)
                    node = (_new_path, v[1] + 1)
                    queue.append(node)

    return goal


def compute_score(_paths):
    _score = 0
    for p in _paths:
        minutes = p[1]
        _score += (30 - minutes) * valve_flow_rate[p[0][-1]]
    return _score


# input
# Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
with open('input.txt', 'r') as f:
    for line in f:
        ln = line.strip()

        _input = ln.split(";")
        part1 = _input[0].split(" ")
        part2 = _input[1].split(" ")
        _valve = part1[1]
        _flow_rate_equals = part1[4].split("=")
        _flow_rate = int(_flow_rate_equals[1])

        valve_flow_rate[_valve] = _flow_rate

        _temp = "".join(part2[5:])
        valve_neighbours[_valve] = _temp.split(",")

        if _valve == "AA":
            start_valve = [((_valve,), 0)]
        if _flow_rate == 0:
            valves_zero_flow_rate.add(_valve)
        else:
            valves_with_flow_rate += 1

start = time.time()

goals = bfs(start_valve)

path_valves = []
for _goal in goals:
    score = compute_score([_goal])
    path_valves.append(([_goal], score))

path_valves.sort(key=operator.itemgetter(1), reverse=True)
path_valves = path_valves[:N]

new_paths = []
found = False
solution = []
iteration = 0
while not found:

    if not path_valves:
        break
    else:
        print(f"iteration: {iteration}")
        print(f"number of paths: {len(path_valves)}")

    solution = copy.deepcopy(path_valves)
    path_valves = list(map(lambda x: x[0], path_valves))
    for path in path_valves:
        if len(path) == valves_with_flow_rate:
            found = True
            break
        else:
            new_goals = bfs(path)
            if new_goals:
                new_path_valves = []
                for new_path in new_goals:
                    if new_path[1] < 30:
                        new_path = path + [new_path]
                        score = compute_score(new_path)
                        new_path_valves.append((new_path, score))

                new_path_valves.sort(key=operator.itemgetter(1), reverse=True)
                new_path_valves = new_path_valves[:N]
                new_paths.extend(new_path_valves)

    path_valves = new_paths
    new_paths = []
    iteration += 1

end = time.time()

solution.sort(key=operator.itemgetter(1), reverse=True)
solution = solution[:3]

# print(solution)
print()
print(f"The best score is: {solution[0][1]}")
print(f"The number of valves opened are: {len(solution[0][0])}")
print(f"Process took: {round(end - start, 5)} seconds")
