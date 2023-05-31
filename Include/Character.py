import os

BLUE = (0, 0, 255)
RED = (255, 0, 0)

class Character():
    game_field = None
    pygame = None
    screen = None

    def __init__(self, row, col, team_color, game_field, pygame, screen,
                character_class='FIGHTER'):
        self.row = -1
        self.col = -1
        self.character_class = character_class
        self.team_color = team_color
        self.active = True
        self.pos = None
        if self.game_field is None:
            self.game_field = game_field
        if self.pygame is None:
            self.pygame = pygame
        if self.screen is None:
            self.screen = screen
        self.load_assets()
        self.set_grid_position(row, col, True)
        self.draw()

    def set_grid_position(self, row, col, is_player_there):
        self.game_field.set_player_position(row, col, is_player_there)
        self.row = row
        self.col = col
        if is_player_there:
            self.draw()
        else:
            self.game_field.blit_background(row, col)

    def draw(self):
        self.pos = self.image_player.get_rect().move(self.col * 64, self.row * 64)
        self.screen.blit(self.image_player, self.pos)

    def move(self, by_row, by_col):
        if self.active:
            if self.row != -1 and self.col != -1:
                if self.game_field.is_valid(self.row + by_row, self.col + by_col): 
                    current_row = self.row
                    current_col = self.col
                    self.set_grid_position(self.row, self.col, False)
                    self.set_grid_position(self.row + by_row, self.col + by_col, True)
                    if by_row == -1:
                        self.pos.top = self.pos.top - 64
                    elif by_row == 1:
                        self.pos.top = self.pos.top + 64
                    elif by_col == -1:
                        self.pos.left = self.pos.left - 64
                    elif by_col == 1:
                        self.pos.left = self.pos.left + 64
                    self.game_field.blit_background(current_row, current_col)
            if self.col == 0 or self.col == self.game_field.get_window_width() - 1:
                self.active = False
        return self.row, self.col
    
    def get_active(self):
        return self.active
    
    def end_turn(self):
        print(f"do stuff for end of turn")

    def load_assets(self):
        if self.team_color == BLUE:
            self.image_player = self.pygame.image.load(os.path.join(os.getcwd(),'Assets/medievalUnit_01.png'))
        elif self.team_color == RED:
            self.image_player = self.pygame.image.load(os.path.join(os.getcwd(),'Assets/medievalUnit_07.png'))