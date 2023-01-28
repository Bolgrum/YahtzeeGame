import random

def generate_dice_roll() -> list:
    rolled_dice = list()
    
    for num in range(0, 5):
        random_dice_roll = random.randint(1, 6)
        rolled_dice.append(random_dice_roll)
    
    return rolled_dice