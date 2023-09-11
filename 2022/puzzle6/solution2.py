import time


def find_start_of_packet_marker(datastream, num_chars):
    length = len(datastream)
    for i in range((length - 1) + num_chars):
        marker_set = set(datastream[i:i + num_chars])
        if len(marker_set) == num_chars:
            return i + num_chars, datastream[i:i + num_chars]


start = time.time()
with open('input.txt', 'r') as f:
    for line in f:
        ln = line.strip()


index, packet_marker = find_start_of_packet_marker(ln, 14)
end = time.time()

print(f"The number of character to process before the first start-of-packet is: {index}")
print(f"The packet marker is: {packet_marker}")
print(f"Process took: {round(end - start, 5)} seconds")
