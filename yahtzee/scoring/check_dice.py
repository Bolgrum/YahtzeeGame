class CheckDice():
    # Check for yahtzee
    def check_yahtzee(dice) -> bool:
        if len(set(dice)) == 1:
            return True
        
        return False
    
    # Check for full house
    def check_full_house(dice) -> bool:
        dice.sort()
        if (len(set(dice))) != 2:
            return False
        elif dice[0] != dice[3] and dice[1] != dice[4]:
            return True
    
        return False            
    # Check for three of a kind
    def check_three_of_kind(dice) -> bool:
        dice.sort()
        if (dice[0] == dice[2]) or (dice[1] == dice[3]) or (dice[2] == dice[4]):
            return True
        return False       
    
    # Check for four of a kind
    def check_four_of_kind(dice) -> bool:
        dice.sort()
        # Check for two options
        if dice[0] == dice[3] or dice[1] == dice[4]:
            return True
        return False
    
    # Check for small straight
    def check_small_straight(dice) -> bool:
        dice.sort()
        if len(set(dice)) == 4 and ((dice[0] == 1 and dice[4] == 4) or (dice[0] == 2 and dice[4] == 5) or (dice[0] == 3 and dice[4] == 6)):
            return True
        if len(set(dice)) == 5  and ((dice[0] == 1 and dice[4] == 4) or (dice[1] == 2 and dice[4] == 5) or (dice[1] == 3 and dice[4] == 6)):
            return True
        return False
    
    # Check for large straight
    def check_large_straight(dice) -> bool:
        dice.sort()
        if len(set(dice)) == 5 and ((dice[0] == 1 and dice[4] == 5) or (dice[0] == 2 and dice[4] == 6)):
            return True
        
        return False