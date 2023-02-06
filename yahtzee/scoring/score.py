from .check_dice import CheckDice

# Find highest score
def find_high_score(values):
    high_score = 0
    score = CheckDice.check_three_of_kind(values)
    if score > high_score:
        high_score = score

    score = CheckDice.check_four_of_kind(values)
    if score > high_score:
        high_score = score

    score = CheckDice.check_five_of_kind(values)
    if score > high_score:
        high_score = score

    score = CheckDice.check_full_house(values)
    if score > high_score:
        high_score = score

    for val in range(1, 7):
        score = CheckDice.check_singles(values, val)
        if score > high_score:
            high_score = score

    score = CheckDice.check_straight(values)
    if score > high_score:
        high_score = score

    return high_score

# Add all occurences of goal value
def score_singles(dice, goal):
    score = 0

    for i in range(len(dice)):
        if dice[i] == goal:
            score += goal

    return score