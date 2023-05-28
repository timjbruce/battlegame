class Character():
    pygame = None
    screen = None

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
        print(f"new character at {row}, {col}")
        self.set_position(row, col, game_field)

    def draw(self, color, game_field):
        self.pygame.draw.rect(self.screen, color, [
            (game_field.get_tile_size() + game_field.get_tile_margin()) * self.col + game_field.get_tile_margin(),
            (game_field.get_tile_size() + game_field.get_tile_margin()) * self.row + game_field.get_tile_margin(),
            game_field.get_tile_size(), game_field.get_tile_size()])

    def set_position(self, row, col, game_field):
        self.draw(game_field.get_base_color(), game_field)
        self.row = row
        self.col = col
        if not (self.row == -1 and self.col == -1):
            self.draw(self.active_color, game_field)

    def move(self, by_row, by_col, game_field, pygame, screen):
        if self.active:
            if self.row != -1 and self.col != -1:
                if (-1 < self.row + by_row < game_field.get_window_height()) and (-1 < self.col + by_col < game_field.get_window_width()):
                    self.set_position(self.row + by_row, self.col + by_col, game_field)
                else:
                    print("player made invalid move")
            if self.col == 0 or self.col == game_field.get_window_width() - 1:
                self.active = False
        return self.row, self.col
    
    def get_active(self):
        return self.active