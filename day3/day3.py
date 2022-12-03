import string

day = "day3"


def get_letter_value(find_letter):
    if find_letter.islower():
        for i, letter in enumerate(string.ascii_lowercase):
            if letter == find_letter:
                return i + 1

    if find_letter.isupper():
        for i, letter in enumerate(string.ascii_uppercase):
            if letter == find_letter:
                return i + 27


def get_first_half(line):
    current_line = line.strip()
    line_length = int(len(current_line))
    half = int(line_length / 2)

    return current_line[0:half]


def is_character_in_words(character, word1, word2):
    return character in word1 and character in word2


def part_one(lines):
    sum_values = 0

    for line in lines:
        letter_map = {}
        first_line = get_first_half(line)
        second_line = line.replace(first_line, "")

        for character in first_line:
            if character in second_line:
                letter_map[character] = get_letter_value(character)

        sum_values += sum(letter_map.values())
    print(f'Total of part 1: {sum_values}')


def part_two(lines):
    sum_values = 0
    items_list = []

    for line in lines:
        items_list.append(line.strip())

        if len(items_list) == 3:

            for character in items_list[0]:
                if is_character_in_words(character, items_list[1], items_list[2]):
                    sum_values += get_letter_value(character)
                    break

            items_list = []
        else:
            continue

    print(f'Total of part 2: {sum_values}')


with open(f"./puzzle-input-{day}.txt", "r") as file:
    lines = file.readlines()
    part_one(lines)
    part_two(lines)
