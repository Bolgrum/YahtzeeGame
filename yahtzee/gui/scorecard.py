import pygame
from gui import button

class Scorecard:
    def __init__(self, colors: dict, font: dict):
        self.colors = colors
        self.font = font
        
        # Init Scorecard
        self.ones           = Scoreslot(0, 200, '1s', False, False)
        self.twos           = Scoreslot(0, 230, '2s', False, False)
        self.threes         = Scoreslot(0, 260, '3s', False, False)
        self.fours          = Scoreslot(0, 290, '4s', False, False)
        self.fives          = Scoreslot(0, 320, '5s', False, False)
        self.sixes          = Scoreslot(0, 350, '6s', False, False)
        self.upper_total_1  = Scoreslot(0, 380, 'Upper Score',False, True)
        self.upper_bonus    = Scoreslot(0, 410, 'Bonus if >= 63',False, True)
        self.upper_total_2  = Scoreslot(0, 440, 'Total Upper Score',False, True)
        self.three_kind     = Scoreslot(0, 470, '3 of a Kind', False, False)
        self.four_kind      = Scoreslot(0, 500, '4 of a Kind', False, False)
        self.full_house     = Scoreslot(0, 530, 'Full House', False, False)
        self.small_straight = Scoreslot(0, 560, 'Small Straight', False, False)
        self.large_straight = Scoreslot(0, 590, 'Large Straight', False, False)
        self.yahtzee        = Scoreslot(0, 620, 'YAHTZEE!', False, False)
        self.chance         = Scoreslot(0, 650, 'Chance', False, False)
        self.bonus          = Scoreslot(0, 680, 'Lower Bonus', False, False)
        self.lower_total_1  = Scoreslot(0, 710, 'Upper Score', False, True)
        self.lower_total_2  = Scoreslot(0, 740, 'Upper Total', False, True)
        self.grand_total    = Scoreslot(0, 770, 'Grand Total', False, True)
        
        self.OnesButton          = button.Button(self.colors.get("black"), 165, 200, 60, 30, "Ones")
        self.TwosButton          = button.Button(self.colors.get("black"), 165, 230, 60, 30, "Twos")
        self.ThreesButton        = button.Button(self.colors.get("black"), 165, 260, 60, 30, "Threes")
        self.FoursButton         = button.Button(self.colors.get("black"), 165, 290, 60, 30, "Fours")
        self.FivesButton         = button.Button(self.colors.get("black"), 165, 320, 60, 30, "Fives")
        self.SixesButton         = button.Button(self.colors.get("black"), 165, 350, 60, 30, "Sixes")
        self.ThreeKindButton     = button.Button(self.colors.get("black"), 165, 470, 60, 30, "3K")
        self.FourKindButton      = button.Button(self.colors.get("black"), 165, 500, 60, 30, "4k")
        self.FullHouseButton     = button.Button(self.colors.get("black"), 165, 530, 60, 30, "FH")
        self.SmallStraightButton = button.Button(self.colors.get("black"), 165, 560, 60, 30, "SS")        
        self.LargeStraightButton = button.Button(self.colors.get("black"), 165, 590, 60, 30, "LS")        
        self.YahtzeeButton       = button.Button(self.colors.get("black"), 165, 620, 60, 30, "Yahtzee")
        self.ChanceButton        = button.Button(self.colors.get("black"), 165, 650, 60, 30, "Chance") 
        
    def draw_scorecard(self, window, width: int, height: int):
        # draw verticle lines
        pygame.draw.rect(window, self.colors.get("white"), [0, 200, 225, height - 200])
        pygame.draw.line(window, self.colors.get("black"), (0, 200), (width, 200), 3)
        pygame.draw.line(window, self.colors.get("black"), (165, 200), (165, height), 3)
        pygame.draw.line(window, self.colors.get("black"), (225, 200), (225, height), 3)        
        
        # draw scorecard
        self.ones.draw(window, self.colors, self.font)
        self.twos.draw(window, self.colors, self.font)
        self.threes.draw(window, self.colors, self.font)
        self.fours.draw(window, self.colors, self.font)
        self.fives.draw(window, self.colors, self.font)
        self.sixes.draw(window, self.colors, self.font)
        self.upper_total_1.draw(window, self.colors, self.font)
        self.upper_bonus.draw(window, self.colors, self.font)
        self.upper_total_2.draw(window, self.colors, self.font)
        self.three_kind.draw(window, self.colors, self.font)
        self.four_kind.draw(window, self.colors, self.font)
        self.full_house.draw(window, self.colors, self.font)
        self.small_straight.draw(window, self.colors, self.font)
        self.large_straight.draw(window, self.colors, self.font)
        self.yahtzee.draw(window, self.colors, self.font)
        self.chance.draw(window, self.colors, self.font)
        self.bonus.draw(window, self.colors, self.font)
        self.lower_total_1.draw(window, self.colors, self.font)
        self.lower_total_2.draw(window, self.colors, self.font)
        self.grand_total.draw(window, self.colors, self.font)
        
        # draw scorecard buttons
        self.OnesButton.draw(window)
        self.TwosButton.draw(window)
        self.ThreesButton.draw(window)
        self.FoursButton.draw(window)
        self.FivesButton.draw(window)
        self.SixesButton.draw(window)
        self.ThreeKindButton.draw(window)
        self.FourKindButton.draw(window)
        self.FullHouseButton.draw(window)
        self.SmallStraightButton.draw(window)
        self.LargeStraightButton.draw(window)
        self.YahtzeeButton.draw(window)
        self.ChanceButton.draw(window)     
    
class Scoreslot:
    def __init__(self, x: int, y: int,text: str, possible: bool, done: bool) -> None:

        self.x_pos = x
        self.y_pos = y
        self.text = text
        self.possible = possible
        self.done = done
         
    def draw(self, window, colors: dict, font: dict):
        pygame.draw.line(window, colors.get('black'), (self.x_pos, self.y_pos), (self.x_pos + 225, self.y_pos), 2)
        pygame.draw.line(window, colors.get('black'), (self.x_pos, self.y_pos + 30), (self.x_pos + 225, self.y_pos + 30), 2)
        
        if not self.done:
            if self.possible:
                text = font.render(self.text, True, (34, 140, 34))
            elif not self.possible:
                text = font.render(self.text, True, (255, 0, 0))
        else:
            text = font.render(self.text, True, (0, 0, 0))
            
        window.blit(text, (self.x_pos + 5, self.y_pos + 10))        