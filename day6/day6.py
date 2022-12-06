day = 'day6'


def check_more_than_one_occurence(number):
    if number > 1:
        return True

    return False


with open(f"./puzzle-input-{day}.txt", "r") as file:
    line = file.readlines()[0]

    print(line)

    character_list = []

    for i, character in enumerate(line):
        character_list.append(character)

        if len(character_list) == 14:
            count_map = {}
            for item in character_list:
                count_map[item] = character_list.count(item)

            even_numbers_iterator = filter(check_more_than_one_occurence, count_map.values())

            number_of_double_occurences = len(list(even_numbers_iterator))
            if number_of_double_occurences == 0:
                print(i + 1)
                break

            character_list.pop(0)
            continue
