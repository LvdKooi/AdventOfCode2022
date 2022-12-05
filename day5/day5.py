day = "day5"

initial_stacks = {1: ['S', 'T', 'H', 'F', 'W', 'R'],
                  2: ['S', 'G', 'D', 'Q', 'W'],
                  3: ['B', 'T', 'W'],
                  4: ['D', 'R', 'W', 'T', 'N', 'Q', 'Z', 'J'],
                  5: ['F', 'B', 'H', 'G', 'L', 'V', 'T', 'Z'],
                  6: ['L', 'P', 'T', 'C', 'V', 'B', 'S', 'G'],
                  7: ['Z', 'B', 'R', 'T', 'W', 'G', 'P'],
                  8: ['N', 'G', 'M', 'T', 'C', 'J', 'R'],
                  9: ['L', 'G', 'B', 'W']}

# part 1
with open(f"./puzzle-input-{day}.txt", "r") as file:
    lines = file.readlines()

    for line in lines:
        line.strip()
        instructions = line.replace('move ', '').replace(' from ', ",").replace(' to ', ",").strip().split(',')
        number_of_containers = int(instructions[0])
        from_container = int(instructions[1])
        to_container = int(instructions[2])

        container_list = []
        for number in range(0, number_of_containers):
            container_list.append(initial_stacks[from_container].pop())

        for container in container_list:
            initial_stacks[to_container].append(container)


    for stack in initial_stacks.values():
        print(stack.pop())

# part 2
with open(f"./puzzle-input-{day}.txt", "r") as file:
    lines = file.readlines()

    for line in lines:
        line.strip()
        instructions = line.replace('move ', '').replace(' from ', ",").replace(' to ', ",").strip().split(',')
        number_of_containers = int(instructions[0])
        from_container = int(instructions[1])
        to_container = int(instructions[2])

        container_list = initial_stacks[from_container][-number_of_containers:]

        for number in range(0, number_of_containers):
         initial_stacks[from_container].pop()

        for container in container_list:
            initial_stacks[to_container].append(container)

    print(initial_stacks)

    for stack in initial_stacks.values():
        print(stack.pop())
