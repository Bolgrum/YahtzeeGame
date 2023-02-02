from yahtzee import generator
from yahtzee.scoring import CheckDice
 

def brute_force_checks():
    
    print("Yahtzee Tests")
    print("=" * 50)
    print(f"Yahtzee? {CheckDice.check_yahtzee([5,5,5,5,5])}")
    print(f"Yahtzee? {CheckDice.check_yahtzee([5,5,5,5,1])}")

    print("Small Straight Tests")
    print("=" * 50)
    print(f"Small_Straight? {CheckDice.check_small_straight([1,2,3,4,5])}")
    print(f"Small_Straight? {CheckDice.check_small_straight([6,2,3,4,5])}")
    print(f"Small_Straight? {CheckDice.check_small_straight([6,4,1,5,3])}")
    print(f"Small_Straight? {CheckDice.check_small_straight([5,5,2,4,3])}")
    print(f"Small_Straight? {CheckDice.check_small_straight([6,6,5,3,4])}")
    print(f"Small_Straight? {CheckDice.check_small_straight([1,2,3,3,5])}")
    print(f"Small_Straight? {CheckDice.check_small_straight([5,6,3,3,4])}")

    print("\nLarge Straight Tests")
    print("=" * 50)
    print(f"Large_Straight? {CheckDice.check_large_straight([1,2,3,4,5])}")
    print(f"Large_Straight? {CheckDice.check_large_straight([2,3,4,5,6])}")
    print(f"Large_Straight? {CheckDice.check_large_straight([1,2,4,4,5])}")

    print("\nThree of a Kind Tests")
    print("=" * 50)
    print(f"Three of a Kind? {CheckDice.check_three_of_kind([1,1,1,4,5])}")
    print(f"Three of a Kind? {CheckDice.check_three_of_kind([1,2,1,4,1])}")
    print(f"Three of a Kind? {CheckDice.check_three_of_kind([4,5,1,1,1])}")
    print(f"Three of a Kind? {CheckDice.check_three_of_kind([1,3,6,1,1])}")
    print(f"Three of a Kind? {CheckDice.check_three_of_kind([1,1,3,4,5])}")

    print("\nFour of a Kind Tests")
    print("=" * 50)
    print(f"Four of a Kind? {CheckDice.check_four_of_kind([1,2,2,2,2])}")
    print(f"Four of a Kind? {CheckDice.check_four_of_kind([3,2,3,3,3])}")
    print(f"Four of a Kind? {CheckDice.check_four_of_kind([4,4,4,4,5])}")
    print(f"Four of a Kind? {CheckDice.check_four_of_kind([1,1,3,4,5])}")

    print("\nFull House Tests")
    print("=" * 50)
    print(f"Full House? {CheckDice.check_full_house([1,1,3,4,5])}")
    print(f"Full House? {CheckDice.check_full_house([1,1,3,3,3])}")
    print(f"Full House? {CheckDice.check_full_house([5,4,4,5,4])}")
    print(f"Full House? {CheckDice.check_full_house([2,6,6,6,6])}")
    print(f"Full House? {CheckDice.check_full_house([2,2,2,2,6])}")

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