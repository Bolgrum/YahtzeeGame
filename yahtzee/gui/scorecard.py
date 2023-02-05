import pygame

# Global Classes
class Scorecard:
    def __init__(self, x_pos, y_pos, text, select, possible, done):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.text = text
        self.select = select
        self.possible = possible
        self.done = done

    def draw(self, screen, screen_colors: dict, font):
        pygame.draw.line(screen, screen_colors.get("black"), (self.x_pos, self.y_pos), (self.x_pos + 225, self.y_pos), 2)
        pygame.draw.line(screen, screen_colors.get("black"), (self.x_pos, self.y_pos + 30), (self.x_pos + 225, self.y_pos + 30), 2)
        
        if not self.done:
            if self.possible:
                text = font.render(self.text, True, (34, 140, 34))
            elif not self.possible:
                text = font.render(self.text, True, (255, 0, 0))
        else:
            text = font.render(self.text, True, (0, 0, 0))

        screen.blit(text, (self.x_pos + 5, self.y_pos + 10))

# Global Functions
def draw_scoreboard(screen, screen_colors, font) -> None:
    # Init Scorboard
    ones = Scorecard(0, 200, '1s', True, False, False)
    twos = Scorecard(0, 230, '2s', True, False, False)
    threes = Scorecard(0, 260, '3s', True, False, False)
    fours = Scorecard(0, 290, '4s', True, False, False)
    fives = Scorecard(0, 320, '5s', True, False, False)
    sixes = Scorecard(0, 350, '6s', True, False, False)
    upper_total_1 = Scorecard(0, 380, 'Upper Score', False, False, True)
    upper_bonus = Scorecard(0, 410, 'Bonus if >= 63', False, False, True)
    upper_total_2 = Scorecard(0, 440, 'Total Upper Score', False, False, True)
    three_kind = Scorecard(0, 470, '3 of a Kind', True, False, False)
    four_kind = Scorecard(0, 500, '4 of a Kind', True, False, False)
    full_house = Scorecard(0, 530, 'Full House', True, False, False)
    small_straight = Scorecard(0, 560, 'Small Straight', True, False, False)
    large_straight = Scorecard(0, 590, 'Large Straight', True, False, False)
    yahtzee = Scorecard(0, 620, 'YAHTZEE!', True, False, False)
    chance = Scorecard(0, 650, 'Chance', True, False, False)
    bonus = Scorecard(0, 680, 'Chance', True, False, False)
    lower_total_1 = Scorecard(0, 710, 'Upper Score', False, False, True)
    lower_total_2 = Scorecard(0, 740, 'Upper Total', False, False, True)
    grand_total = Scorecard(0, 770, 'Grand Total', False, False, True)
    
    # draw scorecard
    ones.draw(screen, screen_colors, font)
    twos.draw(screen, screen_colors, font)
    threes.draw(screen, screen_colors, font)
    fours.draw(screen, screen_colors, font)
    fives.draw(screen, screen_colors, font)
    sixes.draw(screen, screen_colors, font)
    upper_total_1.draw(screen, screen_colors, font)
    upper_bonus.draw(screen, screen_colors, font)
    upper_total_2.draw(screen, screen_colors, font)
    three_kind.draw(screen, screen_colors, font)
    four_kind.draw(screen, screen_colors, font)
    full_house.draw(screen, screen_colors, font)
    small_straight.draw(screen, screen_colors, font)
    large_straight.draw(screen, screen_colors, font)
    yahtzee.draw(screen, screen_colors, font)
    chance.draw(screen, screen_colors, font)
    bonus.draw(screen, screen_colors, font)
    lower_total_1.draw(screen, screen_colors, font)
    lower_total_2.draw(screen, screen_colors, font)
    grand_total.draw(screen, screen_colors, font)