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


# part 1
with open(f"./puzzle-input-{day}.txt", "r") as file:
    lines = file.readlines()
    letter_map = {}
    sum_values = 0

    for line in lines:
        letter_map = {}
        current_line = line.strip()
        line_length = int(len(current_line))
        half = int(line_length / 2)

        first_line = current_line[0:half]
        second_line = current_line[half:line_length]

        for character in first_line:
            if character in second_line:
                letter_map[character] = get_letter_value(character)

        sum_values += sum(letter_map.values())
    print(sum_values)

# part 2

with open(f"./puzzle-input-{day}.txt", "r") as file:
    lines = file.readlines()
    group_map = {}
    letter_map = {}
    sum_values = 0
    items_list = []

    for line in lines:
        if len(items_list) <= 3:
            items_list.append(line.strip())
            if len(items_list) == 3:

                for character in items_list[0]:
                    if character in items_list[1] and character in items_list[2]:
                        letter_map[character] = get_letter_value(character)
                        break
                sum_values += sum(letter_map.values())
                items_list = []
                letter_map = {}
            else:
                continue

print(sum_values)
