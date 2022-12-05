day = "day5"


def get_initial_stacks():
    return {1: ['S', 'T', 'H', 'F', 'W', 'R'],
            2: ['S', 'G', 'D', 'Q', 'W'],
            3: ['B', 'T', 'W'],
            4: ['D', 'R', 'W', 'T', 'N', 'Q', 'Z', 'J'],
            5: ['F', 'B', 'H', 'G', 'L', 'V', 'T', 'Z'],
            6: ['L', 'P', 'T', 'C', 'V', 'B', 'S', 'G'],
            7: ['Z', 'B', 'R', 'T', 'W', 'G', 'P'],
            8: ['N', 'G', 'M', 'T', 'C', 'J', 'R'],
            9: ['L', 'G', 'B', 'W']}


def get_instructions_list(line):
    return line.replace('move ', '').replace(' from ', ",").replace(' to ', ",").strip().split(',')


def part_one(lines):
    stacks = get_initial_stacks()
    result = ''

    for line in lines:
        instructions = get_instructions_list(line)
        number_of_containers = int(instructions[0])
        from_container = int(instructions[1])
        to_container = int(instructions[2])

        container_list = []
        for number in range(0, number_of_containers):
            container_list.append(stacks[from_container].pop())

        for container in container_list:
            stacks[to_container].append(container)

    for stack in stacks.values():
        result += stack.pop()

    print(f'Result part 1: {result}')


def part_two(lines):
    stacks = get_initial_stacks()
    result = ''

    for line in lines:
        instructions = get_instructions_list(line)
        number_of_containers = int(instructions[0])
        from_container = int(instructions[1])
        to_container = int(instructions[2])

        container_list = stacks[from_container][-number_of_containers:]

        for number in range(0, number_of_containers):
            stacks[from_container].pop()

        for container in container_list:
            stacks[to_container].append(container)

    for stack in stacks.values():
        result += stack.pop()

    print(f'Result part 2: {result}')


with open(f"./puzzle-input-{day}.txt", "r") as file:
    lines = file.readlines()
    part_one(lines)
    part_two(lines)
