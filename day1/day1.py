elfMap = {}

# part 1
with open("./day1/puzzle-input-day1.txt", "r") as file:
    current_elf = 1
    current_sum = 0

    for line in file.readlines():
        if line != "\n":
            current_sum += int(line)
        else:
            elfMap[current_elf] = current_sum
            current_sum = 0
            current_elf += 1

calories_list = list(elfMap.values())

print(f'Most calories carried by one elf: {max(calories_list)}')

# part 2
calories_list.sort(reverse=True)

total_of_top_3 = 0

for i, element in enumerate(calories_list):
    if i < 3:
        total_of_top_3 += element
    else:
        break

print(f'Total calories of top 3 elfs: {total_of_top_3}')
