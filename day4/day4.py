day = "day4"


def get_first_number(range):
    return int(range.split('-')[0])


def get_second_number(range):
    return int(range.split('-')[1]) + 1


def pair_as_range(pair):
    return range(get_first_number(pair), get_second_number(pair), 1)


def is_completely_overlapping(range1, range2):
    first_range_as_list = range(get_first_number(range1), get_second_number(range1), 1)
    second_range_as_list = range(get_first_number(range2), get_second_number(range2), 1)

    return all(elem in first_range_as_list for elem in second_range_as_list) or \
           all(elem in second_range_as_list for elem in first_range_as_list)


def part_one(lines):
    sum_of_overlapping_pairs = 0

    for line in lines:
        pairs = line.strip().split(',')

        if is_completely_overlapping(pairs[0], pairs[1]):
            sum_of_overlapping_pairs += 1

    print(f'Outcome of part 1: {sum_of_overlapping_pairs}')


def part_two(lines):
    sum_of_partially_overlapping_pairs = 0

    for line in lines:
        pairs = line.strip().split(',')
        first_pair = pairs[0]
        second_pair = pairs[1]

        first_range_as_list = pair_as_range(first_pair)
        second_range_as_list = pair_as_range(second_pair)

        for i in first_range_as_list:
            if i in second_range_as_list:
                sum_of_partially_overlapping_pairs += 1
                break

    print(f'Outcome of part 2: {sum_of_partially_overlapping_pairs}')


with open(f"./puzzle-input-{day}.txt", "r") as file:
    lines = file.readlines()
    part_one(lines)
    part_two(lines)
