import time
import re

sensors_beacon = {}
sensors_distance = {}


def row_positions_not_containing_beacon(selected_row):
    _positions = set()

    for _sensor, _distance in sensors_distance.items():
        sensor_row = _sensor[1]
        sensor_col = _sensor[0]
        diff_rows = abs(sensor_row - selected_row)
        if _distance >= diff_rows:
            rest_distance = abs(_distance - diff_rows)

            for i in range(rest_distance + 1):
                _positions.add((sensor_col + i, selected_row))
                _positions.add((sensor_col - i, selected_row))

    return _positions


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

        sensors_beacon[sensor] = beacon
        sensors_distance[sensor] = distance

start = time.time()

# row = 10
row = 2000000
positions = row_positions_not_containing_beacon(row)

end = time.time()

# print(sensors_beacon)
# print(sensors_distance)

print(f"In the row where y={row}, There are {len(positions) - 1} positions that cannot contain a beacon?")
print(f"Process took: {round(end - start, 5)} seconds")
