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

class CheckDice():
    # Check for yahtzee
    def check_yahtzee(self, dice):
        if len(set(dice)) == 1:
            return True
        
        return False
    
    # Check for full house
    def check_full_house(self, dice):
        dice.sort()
        if (len(set(dice))) != 2:
            return False
        elif dice[0] != dice[3] and dice[1] != dice[4]:
            return True
    
        return False            
    # Check for three of a kind
    def check_three_of_kind(self, dice):
        dice.sort()
        if (dice[0] == dice[2]) or (dice[1] == dice[3]) or (dice[2] == dice[4]):
            return True
        return False       
    
    # Check for four of a kind
    def check_four_of_kind(self, dice):
        dice.sort()
        # Check for two options
        if dice[0] == dice[3] or dice[1] == dice[4]:
            return True
        return False
    
    # Check for small straight
    def check_small_straight(self, dice):
        dice.sort()
        if len(set(dice)) == 4 and ((dice[0] == 1 and dice[4] == 4) or (dice[0] == 2 and dice[4] == 5) or (dice[0] == 3 and dice[4] == 6)):
            return True
        if len(set(dice)) == 5  and ((dice[0] == 1 and dice[4] == 4) or (dice[1] == 2 and dice[4] == 5) or (dice[1] == 3 and dice[4] == 6)):
            return True
        return False
    
    # Check for large straight
    def check_large_straight(self, dice):
        dice.sort()
        if len(set(dice)) == 5 and ((dice[0] == 1 and dice[4] == 5) or (dice[0] == 2 and dice[4] == 6)):
            return True
        
        return False
    
    # Add all occurences of goal value
    def check_singles(dice, goal):
        score = 0

        for i in range(len(dice)):
            if dice[i] == goal:
                score += goal

        return score