day = 'day6'


def part_one_and_two(line, number_of_unique_characters, log_statement):
    character_list = []

    for i, character in enumerate(line):
        character_list.append(character)

        if len(character_list) == number_of_unique_characters:
            counts = []
            for item in character_list:
                counts.append(character_list.count(item))

            number_of_double_occurences = len(list(filter(lambda number: number > 1, counts)))

            if number_of_double_occurences == 0:
                print(f'{log_statement}{i + 1}')
                break

            character_list.pop(0)


with open(f"./puzzle-input-{day}.txt", "r") as file:
    line = file.readlines()[0]

    part_one_and_two(line, 4, 'Result part 1: ')
    part_one_and_two(line, 14, 'Result part 2: ')
