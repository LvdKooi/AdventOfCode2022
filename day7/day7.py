day = 'day7'

directory_map = {}

with open(f"./puzzle-input-{day}.txt", "r") as file:
    lines = file.readlines()

    current_dir = '/'
    current_path = ['/']


    for i, line in enumerate(lines):

        if '$ cd ' in line:
            if ' ..' in line:
                current_path.pop()

            else:
                new_dir = line.replace('$ cd ')

                while new_dir != current_path.pop():
                    continue


        if '.' in line:
            size = line.split(' ')[0]

            for dir in current_path :
                directory_map[dir] += int(size)



