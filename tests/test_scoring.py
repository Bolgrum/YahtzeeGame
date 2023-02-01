from yahtzee import generator

class CheckDice():
    def __init__(self):
        pass

    def check_yahtzee(self, dice):
        if len(set(dice)) == 1:
            return True
        
        return False
    
    def check_full_house(self, dice):
        dice.sort()
        if (len(set(dice))) != 2:
            return False
        elif dice[0] != dice[3] and dice[1] != dice[4]:
            return True
    
        return False            
    
    def check_three_of_kind(self, dice):
        dice.sort()
        if (dice[0] == dice[2]) or (dice[1] == dice[3]) or (dice[2] == dice[4]):
            return True
        return False       
    
    # Check for four of a kind (score = 40)
    def check_four_of_kind(self, dice):
        dice.sort()
        # Check for two options
        if dice[0] == dice[3] or dice[1] == dice[4]:
            return True
        return False
    
    def check_small_straight(self, dice):
        dice.sort()
        if len(set(dice)) == 4 and ((dice[0] == 1 and dice[4] == 4) or (dice[0] == 2 and dice[4] == 5) or (dice[0] == 3 and dice[4] == 6)):
            return True
        if len(set(dice)) == 5  and ((dice[0] == 1 and dice[4] == 4) or (dice[1] == 2 and dice[4] == 5) or (dice[1] == 3 and dice[4] == 6)):
            return True
        return False
    
    def check_large_straight(self, dice):
        dice.sort()
        if len(set(dice)) == 5 and ((dice[0] == 1 and dice[4] == 5) or (dice[0] == 2 and dice[4] == 6)):
            return True
        
        return False   

def brute_force_checks():
    dice = CheckDice()
    
    print("Yahtzee Tests")
    print("=" * 50)
    print(f"Yahtzee? {dice.check_yahtzee([5,5,5,5,5])}")
    print(f"Yahtzee? {dice.check_yahtzee([5,5,5,5,1])}")

    print("Small Straight Tests")
    print("=" * 50)
    print(f"Small_Straight? {dice.check_small_straight([1,2,3,4,5])}")
    print(f"Small_Straight? {dice.check_small_straight([6,2,3,4,5])}")
    print(f"Small_Straight? {dice.check_small_straight([6,4,1,5,3])}")
    print(f"Small_Straight? {dice.check_small_straight([5,5,2,4,3])}")
    print(f"Small_Straight? {dice.check_small_straight([6,6,5,3,4])}")
    print(f"Small_Straight? {dice.check_small_straight([1,2,3,3,5])}")
    print(f"Small_Straight? {dice.check_small_straight([5,6,3,3,4])}")

    print("\nLarge Straight Tests")
    print("=" * 50)
    print(f"Large_Straight? {dice.check_large_straight([1,2,3,4,5])}")
    print(f"Large_Straight? {dice.check_large_straight([2,3,4,5,6])}")
    print(f"Large_Straight? {dice.check_large_straight([1,2,4,4,5])}")

    print("\nThree of a Kind Tests")
    print("=" * 50)
    print(f"Three of a Kind? {dice.check_three_of_kind([1,1,1,4,5])}")
    print(f"Three of a Kind? {dice.check_three_of_kind([1,2,1,4,1])}")
    print(f"Three of a Kind? {dice.check_three_of_kind([4,5,1,1,1])}")
    print(f"Three of a Kind? {dice.check_three_of_kind([1,3,6,1,1])}")
    print(f"Three of a Kind? {dice.check_three_of_kind([1,1,3,4,5])}")

    print("\nFour of a Kind Tests")
    print("=" * 50)
    print(f"Four of a Kind? {dice.check_four_of_kind([1,2,2,2,2])}")
    print(f"Four of a Kind? {dice.check_four_of_kind([3,2,3,3,3])}")
    print(f"Four of a Kind? {dice.check_four_of_kind([4,4,4,4,5])}")
    print(f"Four of a Kind? {dice.check_four_of_kind([1,1,3,4,5])}")

    print("\nFull House Tests")
    print("=" * 50)
    print(f"Full House? {dice.check_full_house([1,1,3,4,5])}")
    print(f"Full House? {dice.check_full_house([1,1,3,3,3])}")
    print(f"Full House? {dice.check_full_house([5,4,4,5,4])}")
    print(f"Full House? {dice.check_full_house([2,6,6,6,6])}")
    print(f"Full House? {dice.check_full_house([2,2,2,2,6])}")

def test_dice_checks():
    check_dice = CheckDice()
    
    for roll in range(1,10):
        random_dice_roll = generator.generate_dice_roll(5)
        if roll == 1:
            print('=' * 50)
            
        print(f"Round {roll}")
        print('=' * 50)
        print(f"Three of a Kind? Roll {random_dice_roll} = {check_dice.check_three_of_kind(random_dice_roll)}")
        print(f"Four of a Kind?  Roll {random_dice_roll} = {check_dice.check_four_of_kind(random_dice_roll)}")
        print(f"Large_Straight?  Roll {random_dice_roll} = {check_dice.check_large_straight(random_dice_roll)}")
        print(f"Small_Straight?  Roll {random_dice_roll} = {check_dice.check_small_straight(random_dice_roll)}")
        print(f"Full House?      Roll {random_dice_roll} = {check_dice.check_full_house(random_dice_roll)}")
        print(f"Yahtzee?         Roll {random_dice_roll} = {check_dice.check_yahtzee(random_dice_roll)}")
        print('=' * 50, "\n")
        
# Test Script
# brute_force_checks()
test_dice_checks()