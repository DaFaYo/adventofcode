import time

MAX_FILESIZE = 100000

# (path_from_root_to_directory) -> total_filesize

path_to_filesize = {}
current_path = None


# This programs assumes a start at the root directory
# And a smart elf To browse around the filesystem to assess the situation

def update_file_sizes(file_size, cur_path):
    while cur_path:
        path_to_filesize[cur_path] += file_size
        cur_path = cur_path[0:-1]


start = time.time()

with open('input.txt', 'r') as f:
    for line in f:
        ln = line.strip()

        if ln[0:4] == "$ ls" or ln[0:3] == "dir":
            continue

        elif ln[0:4] == "$ cd":
            directory = ln[5:]
            if directory == "..":
                current_path = current_path[0:-1]
            else:
                filesize = 0
                if current_path:
                    new_path = current_path + (directory, )
                    path_to_filesize[current_path] += filesize

                else:
                    new_path = tuple(directory)

                if new_path not in path_to_filesize:
                    path_to_filesize[new_path] = filesize

                current_path = new_path

        else:
            file = ln.split(" ")
            filesize = int(file[0])
            update_file_sizes(filesize, current_path)

sum_file_sizes = 0
for path in path_to_filesize:
    filesize = path_to_filesize[path]
    if filesize <= MAX_FILESIZE:
        sum_file_sizes += filesize

end = time.time()

# print(path_to_filesize)
print(f"The sum of the total sizes of dirs < 100000 is: {sum_file_sizes}")
print(f"Process took: {round(end - start, 5)} seconds")
