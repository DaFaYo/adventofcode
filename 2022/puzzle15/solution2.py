import time
import re
import math

sensors_distance = {}
relevant_sensors = {}


#
# def row_positions_not_containing_beacon(selected_row, limit=math.inf):
#     _positions = set()
#
#     for _sensor, _distance in sensors_distance.items():
#         sensor_row = _sensor[1]
#         sensor_col = _sensor[0]
#
#         diff_rows = abs(sensor_row - selected_row)
#         if _distance >= diff_rows:
#             rest_distance = abs(_distance - diff_rows)
#
#             for i in range(rest_distance + 1):
#
#                 new_col = sensor_col + i
#                 if 0 <= new_col <= limit:
#                     _positions.add((new_col, selected_row))
#
#                 new_col = sensor_col - i
#                 if 0 <= new_col <= limit:
#                     _positions.add((new_col, selected_row))
#
#     return _positions
#

def get_beacon_column(pair, minimum=0, maximum=20):
    _sorted_set = sorted(pair[0], key=lambda pair: pair[0])
    min_col = _sorted_set[0][0]
    max_col = _sorted_set[0][1]
    pairs = pair[1]
    for n in range(pairs - 1):
        _min_col, _max_col = _sorted_set[n + 1]
        if _min_col > max_col:
            return max_col + 1
        if _max_col > max_col:
            max_col = _max_col

    if min_col > minimum:
        return minimum
    if max_col < maximum:
        return maximum


# {(-8, 12), (14, 26), (6, 10), (12, 14)}
def set_contains_beacon(pair, minimum=0, maximum=20):
    _sorted_set = sorted(pair[0], key=lambda pair: pair[0])
    min_col = _sorted_set[0][0]
    max_col = _sorted_set[0][1]
    pairs = pair[1]
    for n in range(pairs - 1):
        _min_col, _max_col = _sorted_set[n + 1]
        if _min_col > max_col:
            return True
        if _max_col > max_col:
            max_col = _max_col

    return (min_col > minimum) or (max_col < maximum)


def row_positions_not_containing_beacon(selected_row):
    _positions = set()
    length = 0

    for _sensor, _distance in sensors_distance.items():
        sensor_row = _sensor[1]
        sensor_col = _sensor[0]

        diff_rows = abs(sensor_row - selected_row)
        if _distance >= diff_rows:
            rest_distance = abs(_distance - diff_rows)

            max_col = sensor_col + rest_distance
            min_col = sensor_col - rest_distance
            _positions.add((min_col, max_col))
            length += 1

    return _positions, length


# Sensor at x=2, y=18: closest beacon is at x=-2, y=15
with open('input.txt', 'r') as f:
    for line in f:
        ln = line.strip()
        numbers = re.findall(r'-?\d+', ln)
        info = [int(s) for s in numbers]
        sensor = (info[0], info[1])
        beacon = (info[2], info[3])

        # Manhattan distance
        distance = abs(info[0] - info[2]) + abs(info[1] - info[3])
        sensors_distance[sensor] = distance

start = time.time()

# max_row_col = 20
max_row_col = 4000000
found_row = False
found_row_num = 0
found_col_num = 0
for index in range(max_row_col + 1):

    if index % 1000000 == 0:
        print(f"The row with desired beacon is larger than {index}.")

    positions = row_positions_not_containing_beacon(index)
    if set_contains_beacon(positions, 0, max_row_col):
        found_row = True
        found_row_num = index
        found_col_num = get_beacon_column(positions, 0, max_row_col)
        print(f"The coordinates of desired beacon is {(found_col_num, found_row_num)}.")
        break

end = time.time()

if found_row:
    print(f"The distress beacon's signal's tuning frequency is {(found_col_num * 4000000) + found_row_num}.")
else:
    print("Didn't find a solution.")
print(f"Process took: {round(end - start, 5)} seconds")
