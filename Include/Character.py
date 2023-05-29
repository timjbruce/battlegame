class Character():
    pygame = None
    screen = None
    game_field = None

    def __init__(self, row, col, active_color, game_field, pygame, screen, 
                character_class='FIGHTER'):
        self.row = -1
        self.col = -1
        self.character_class = character_class
        self.active_color = active_color
        self.active = True
        if self.pygame is None:
            self.pygame = pygame
        if self.screen is None:
            self.screen = screen
        if self.game_field is None:
            self.game_field = game_field
        self.set_position(row, col)

    def draw(self, color):
        self.pygame.draw.rect(self.screen, color, [
            (self.game_field.get_tile_size() + self.game_field.get_tile_margin()) * self.col + self.game_field.get_tile_margin(),
            (self.game_field.get_tile_size() + self.game_field.get_tile_margin()) * self.row + self.game_field.get_tile_margin(),
            self.game_field.get_tile_size(), self.game_field.get_tile_size()])

    def set_position(self, row, col):
        if self.game_field.is_spot_available(row, col):
            self.draw(self.game_field.get_base_color())
            self.game_field.set_player_location(self.row, self.col, False)
            self.row = row
            self.col = col
            if not (self.row == -1 and self.col == -1):
                self.draw(self.active_color)
                self.game_field.set_player_location(self.row, self.col, True)

    def move(self, by_row, by_col):
        if self.active:
            if self.row != -1 and self.col != -1:
                if (-1 < self.row + by_row < self.game_field.get_window_height()) and (-1 < self.col + by_col < self.game_field.get_window_width()):
                    self.set_position(self.row + by_row, self.col + by_col)
            if self.col == 0 or self.col == self.game_field.get_window_width() - 1:
                self.active = False
        return self.row, self.col
    
    def get_active(self):
        return self.active
    
    def end_turn(self):
        print(f"do stuff for end of turn")