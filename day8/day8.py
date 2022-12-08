day = 'day8'

# #  part 1
with open(f"./puzzle-input-{day}.txt", "r") as file:
    lines = file.readlines()
    outside_count = (len(lines[0].strip()) * 2) + ((len(lines) - 2) * 2)
    number_of_lines = len(lines)
    number_of_characters = len(lines[0].strip())
    total_count = outside_count

    for i in range(1, number_of_lines - 1):

        for j in range(1, number_of_characters - 1):
            current_number = lines[i][j]
            top_count = 0
            bottom_count = 0
            left_count = 0
            right_count = 0

            # visible from top
            for k in range(0, i):
                compare = lines[k][j]
                if compare >= current_number:
                    top_count += 1

            if top_count == 0:
                total_count += 1
                continue

            # visible from bottom
            for k in range(i + 1, number_of_lines):
                compare = lines[k][j]
                if compare >= current_number:
                    bottom_count += 1

            if bottom_count == 0:
                total_count += 1
                continue

            # visible from left
            for k in range(0, j):
                compare = lines[i][k]
                if compare >= current_number:
                    left_count += 1

            if left_count == 0:
                total_count += 1
                continue

            # visible from right
            for k in range(j + 1, number_of_characters):
                compare = lines[i][k]
                if compare >= current_number:
                    right_count += 1

            if right_count == 0:
                total_count += 1
                continue

    print(total_count)

#  part 2
with open(f"./puzzle-input-{day}.txt", "r") as file:
    lines = file.readlines()
    number_of_lines = len(lines)
    number_of_characters = len(lines[0].strip())
    scenic_view_counts = []

    for i in range(1, number_of_lines - 1):

        for j in range(1, number_of_characters - 1):
            current_number = lines[i][j]
            top_count = 0
            bottom_count = 0
            left_count = 0
            right_count = 0

            # visible from top
            for k in range(i - 1, -1, -1):
                compare = lines[k][j]
                if compare < current_number:
                    top_count += 1

                if compare >= current_number:
                    top_count += 1
                    break

            # visible from bottom
            for k in range(i + 1, number_of_lines):
                compare = lines[k][j]
                if compare < current_number:
                    bottom_count += 1

                if compare >= current_number:
                    bottom_count += 1
                    break

            # visible from left
            for k in range(j - 1, -1, -1):
                compare = lines[i][k]
                if compare < current_number:
                    left_count += 1

                if compare >= current_number:
                    left_count += 1
                    break

            # visible from right
            for k in range(j + 1, number_of_characters):
                compare = lines[i][k]
                if compare < current_number:
                    right_count += 1

                if compare >= current_number:
                    right_count += 1
                    break

            scenic_view_counts.append(left_count * right_count * bottom_count * top_count)

    print(max(scenic_view_counts))
