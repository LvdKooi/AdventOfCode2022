day = 'day8'

# #  part 1
with open(f"./puzzle-input-{day}.txt", "r") as file:
    lines = file.readlines()
    outside_count = (len(lines[0].strip()) * 2) + ((len(lines) - 2) *2)
    number_of_lines = len(lines)
    number_of_characters = len(lines[0].strip())
    total_count = outside_count

    for i in range(1, number_of_lines -1):

        for j in range(1, number_of_characters - 1):
            current_number = lines[i][j]
            number_of_trees_larger_from_top = 0
            number_of_trees_larger_from_bottom = 0
            number_of_trees_larger_from_left = 0
            number_of_trees_larger_from_right = 0

            # visible from top
            for k in range(0, i):
                compare = lines[k][j]
                if compare >= current_number:
                    number_of_trees_larger_from_top += 1

            if number_of_trees_larger_from_top == 0:
                total_count += 1
                continue

            # visible from bottom
            for k in range(i + 1, number_of_lines):
                compare = lines[k][j]
                if compare >= current_number:
                    number_of_trees_larger_from_bottom += 1

            if number_of_trees_larger_from_bottom == 0:
                total_count += 1
                continue

            # visible from left
            for k in range(0, j):
                compare = lines[i][k]
                if compare >= current_number:
                    number_of_trees_larger_from_left += 1

            if number_of_trees_larger_from_left == 0:
                total_count += 1
                continue

            # visible from right
            for k in range(j + 1, number_of_characters):
                compare = lines[i][k]
                if compare >= current_number:
                    number_of_trees_larger_from_right += 1

            if number_of_trees_larger_from_right == 0:
                total_count += 1
                continue

    print(total_count)


#  part 2
with open(f"./puzzle-input-{day}.txt", "r") as file:
    lines = file.readlines()
    outside_count = (len(lines[0].strip()) * 2) + ((len(lines) - 2) * 2)
    number_of_lines = len(lines)
    number_of_characters = len(lines[0].strip())
    total_count = outside_count
    scenic_view_counts = []

    for i in range(1, number_of_lines - 1):

        for j in range(1, number_of_characters - 1):
            current_number = lines[i][j]
            number_of_trees_larger_from_top = 0
            number_of_trees_larger_from_bottom = 0
            number_of_trees_larger_from_left = 0
            number_of_trees_larger_from_right = 0

            # visible from top
            for k in range(i - 1, -1, -1):
                compare = lines[k][j]
                if compare < current_number:
                    number_of_trees_larger_from_top += 1

                if compare >= current_number:
                    number_of_trees_larger_from_top += 1
                    break

            # visible from bottom
            for k in range(i + 1, number_of_lines):
                compare = lines[k][j]
                if compare < current_number:
                    number_of_trees_larger_from_bottom += 1

                if compare >= current_number:
                    number_of_trees_larger_from_bottom += 1
                    break

                    # visible from left
            for k in range(j - 1, -1, -1):
                compare = lines[i][k]
                if compare < current_number:
                    number_of_trees_larger_from_left += 1

                if compare >= current_number:
                    number_of_trees_larger_from_left += 1
                    break

                    # visible from right
            for k in range(j + 1, number_of_characters):
                compare = lines[i][k]
                if compare < current_number:
                    number_of_trees_larger_from_right += 1

                if compare >= current_number:
                    number_of_trees_larger_from_right += 1
                    break

            scenic_view_counts.append(
                number_of_trees_larger_from_left * number_of_trees_larger_from_right * number_of_trees_larger_from_bottom * number_of_trees_larger_from_top)

    print(max(scenic_view_counts))
