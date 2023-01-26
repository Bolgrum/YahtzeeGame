import random

def generate_dice_roll() -> list:
    random_die1 = random.randint(1,6)
    random_die2 = random.randint(1,6)
    random_die3 = random.randint(1,6)
    random_die4 = random.randint(1,6)
    random_die5 = random.randint(1,6)
    random_die6 = random.randint(1,6)
    
    rolled_dice = [random_die1, random_die2, random_die3, random_die4, random_die5, random_die6,]
    
    return rolled_dice
    