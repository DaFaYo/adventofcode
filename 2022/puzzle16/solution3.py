import copy
import operator
import time

NUM = 10
TRUNCATE_NUM = 100
valve_flow_rate = {}
valve_neighbours = {}
start_valve = None
valves_zero_flow_rate = set()
valves_with_flow_rate = 0


# (("AA",), 0)
def bfs(root, root2=[]):
    explored = set()
    goal = []
    for r in root:
        explored.add(r[0][-1])

    for r in root2:
        explored.add(r[0][-1])

    queue = [((root[-1][0][-1],), root[-1][1])]

    while queue:
        v = queue.pop(0)

        last_valve = v[0][-1]
        if not (last_valve in valves_zero_flow_rate) and not (last_valve in explored):
            goal.append((v[0], v[1] + 1))

        for neighbour in valve_neighbours[last_valve]:

            if neighbour not in v[0]:
                _new_path = v[0] + (neighbour,)

                if (_new_path not in explored) and (v[1] < 26):
                    explored.add(_new_path)
                    node = (_new_path, v[1] + 1)
                    queue.append(node)

    return goal


def compute_score(_paths):
    _score = 0
    for p in _paths:
        minutes = p[1]
        _score += (26 - minutes) * valve_flow_rate[p[0][-1]]
    return _score


def compute_score_pairs(_paths):
    valve_visited = set()
    lst = _paths[0] + _paths[1]
    lst.sort(key=operator.itemgetter(1))

    _score = 0
    for _path, _steps in lst:
        if _path[-1] not in valve_visited:
            _score += (26 - _steps) * valve_flow_rate[_path[-1]]
            valve_visited.add(_path[-1])

    return _score


def truncate_goals(_goals, max_num):
    _path_valves = []
    for _goal in _goals:
        _score = compute_score([_goal])
        _path_valves.append(([_goal], _score))

    _path_valves.sort(key=operator.itemgetter(1), reverse=True)
    _path_valves = _path_valves[:max_num]

    return list(map(lambda x: x[0][0], _path_valves))


def truncate_goal_pairs(_goals, _path, max_num, rev=True):
    _path_valves = []
    for _goal in _goals:
        _score = compute_score_pairs(([_goal], _path))
        _path_valves.append(([_goal], _score))

    _path_valves.sort(key=operator.itemgetter(1), reverse=rev)
    _path_valves = _path_valves[:max_num]

    return list(map(lambda x: x[0][0], _path_valves))


def in_valves(valve, valves):
    valves = set(map(lambda x: x[0][-1], valves))
    return valve[0][-1] in valves


def make_pair_combinations(_paths, truncate_num):
    _pairs = set()
    all_pair_paths = []
    _path_valves = []
    _pair_paths = []
    num = len(_paths)
    i = 0
    while i < num:
        path_1 = _paths[i]
        for j in range(i, num):
            p_path = _paths[j]
            _pair_path = ([path_1], [p_path])
            _pair_paths.append(_pair_path)

        for _pp in _pair_paths:
            _score = compute_score_pairs(_pp)
            pair_score = (_pp, _score)
            _path_valves.append(pair_score)

        _path_valves.sort(key=operator.itemgetter(1), reverse=True)
        _path_valves = _path_valves[:truncate_num]
        all_pair_paths.extend(_path_valves)
        _pair_path = []
        _path_valves = []
        _pair_paths = []
        i += 1

    return all_pair_paths


# input
# Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
with open('test_input.txt', 'r') as f:
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

# Sort neighbours from high valve rates to low valve rates
for key, value in valve_neighbours.items():
    valve_and_rate = list(map(lambda x: (x, valve_flow_rate[x]), value))
    valve_and_rate.sort(key=operator.itemgetter(1), reverse=True)
    valve_and_rate = list(map(lambda x: x[0], valve_and_rate))
    valve_neighbours[key] = valve_and_rate

goals = bfs(start_valve)
goals = truncate_goals(goals, TRUNCATE_NUM)
goals = make_pair_combinations(goals, NUM)
goals.sort(key=operator.itemgetter(1), reverse=True)
path_valves = goals[:NUM]

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
        if (len(path[0]) + len(path[1])) == valves_with_flow_rate:
            found = True
            break
        else:
            new_goals = []
            new_goals1 = bfs(path[0], path[1])
            new_goals2 = bfs(path[1], path[0])

            new_goals1 = truncate_goal_pairs(new_goals1, path[1], TRUNCATE_NUM)
            new_goals2 = truncate_goal_pairs(new_goals2, path[0], TRUNCATE_NUM)

            for ng1 in new_goals1:
                if ng1[1] < 26:
                    for ng2 in new_goals2:
                        if ng2[1] < 26:
                            if not in_valves(ng2, [ng1]):
                                new_goals.append((path[0] + [ng1], path[1] + [ng2]))

            if new_goals:
                new_path_valves = []
                for new_path in new_goals:
                    if (len(new_path[0][-1]) + len(new_path[1][-1])) <= 26:
                        score = compute_score_pairs(new_path)
                        new_path_valves.append((new_path, score))

                new_path_valves.sort(key=operator.itemgetter(1), reverse=True)
                new_path_valves = new_path_valves[:NUM]
                new_paths.extend(new_path_valves)

    path_valves = new_paths
    new_paths = []
    iteration += 1

end = time.time()

solution.sort(key=operator.itemgetter(1), reverse=True)
solution = solution[:3]

num_valves = 0
p1, p2 = solution[0][0]

print(f"The best score is: {solution[0][1]}")
print(f"Paths are: {solution[0][0]}")
print(f"The number of valves opened are: {len(p1) + len(p2)}")
print(f"Process took: {round(end - start, 5)} seconds")
