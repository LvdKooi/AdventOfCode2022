day = 'day7'


def get_count_per_directory(lines):
    directory_map = {}
    current_path = list()

    for i, line in enumerate(lines):
        if '$ cd ' in line:
            if ' ..' in line:
                if len(current_path) > 1:
                    current_path.pop()
            else:
                new_dir = line.replace('$ cd ', '').strip()
                current_path.append(new_dir)

        if line[0].isdigit():
            size = line.split(' ')[0]
            dir_string = ''
            for dir in current_path:
                dir_string += dir + "/"

                if dir_string in directory_map:
                    directory_map[dir_string] += int(size)
                else:
                    directory_map[dir_string] = int(size)

    return directory_map


def part_one(directory_map):
    print(sum(list(filter(lambda number: number <= 100000, directory_map.values()))))


def part_two(directory_map):
    max_size = 70000000
    current_size = max(directory_map.values())

    print(min(list(filter(lambda number: (max_size - (current_size - number)) >= 30000000, directory_map.values()))))


with open(f"./puzzle-input-{day}.txt", "r") as file:
    lines = file.readlines()
    count_per_directory = get_count_per_directory(lines)
    part_one(count_per_directory)
    part_two(count_per_directory)
