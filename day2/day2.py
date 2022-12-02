day = "day2"

action_score_map = {'ROCK': 1, 'PAPER': 2, 'SCISSORS': 3}
action_loses_from_map = {'ROCK': 'PAPER', 'PAPER': 'SCISSORS', 'SCISSORS': 'ROCK'}
action_wins_from_map = {'ROCK': 'SCISSORS', 'PAPER': 'ROCK', 'SCISSORS': 'PAPER'}
decoded_outcomes_map = {'X': 'LOSE', 'Y': 'DRAW', 'Z': 'WIN'}

opponent_index = 0
self_index = 1


def calculate_score(opponent_action, own_action):
    score = action_score_map[own_action]

    if opponent_action == own_action:
        score += 3

    if action_loses_from_map[opponent_action] == own_action:
        score += 6

    return score


def get_action(action):
    if action in ['A', 'X']:
        return 'ROCK'
    if action in ['B', 'Y']:
        return 'PAPER'
    if action in ['C', 'Z']:
        return 'SCISSORS'


def determine_own_action(encoded_result, opponents_action):
    if decoded_outcomes_map[encoded_result] == 'LOSE':
        return action_wins_from_map[opponents_action]

    if decoded_outcomes_map[encoded_result] == 'DRAW':
        return opponents_action

    if decoded_outcomes_map[encoded_result] == 'WIN':
        return action_loses_from_map[opponents_action]


def part_one(lines):
    score_sum = 0

    for line in lines:
        round_actions = line.strip().split(' ')

        opponent_action = get_action(round_actions[opponent_index])
        own_action = get_action(round_actions[self_index])

        score_sum += calculate_score(opponent_action, own_action)

    print(f'Result of part 1: {score_sum}')


def part_two(lines):
    score_sum = 0

    for line in lines:
        round_actions = line.strip().split(' ')

        result = round_actions[self_index]
        opponent_action = get_action(round_actions[opponent_index])

        own_action = determine_own_action(result, opponent_action)

        score_sum += calculate_score(opponent_action, own_action)

    print(f'Result of part 2: {score_sum}')


with open(f"./puzzle-input-{day}.txt", "r") as file:
    lines = file.readlines()
    part_one(lines)
    part_two(lines)
