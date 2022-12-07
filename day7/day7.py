day = 'day7'

directory_map = {}

with open(f"./puzzle-input-{day}.txt", "r") as file:
    lines = file.readlines()

    current_dir = '/'
    current_path = []

    for i, line in enumerate(lines):

        if '$ cd ' in line:
            if ' ..' in line:
                if len(current_path) > 1:
                    current_path.pop()
            else:
                new_dir = line.replace('$ cd ', '').strip()

                if new_dir in current_path:
                    while new_dir != current_path.pop():
                        continue
                else:
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

    print(directory_map)
    print(sum(list(filter(lambda number: number <= 100000, directory_map.values()))))