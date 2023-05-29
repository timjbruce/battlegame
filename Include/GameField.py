from . import FieldObject

class GameField():
    grid = []
    pygame = None
    screen = None

    def __init__(self, window_height, window_width, tile_size, tile_margin, base_color, retreat_color, pygame, screen):
        self.window_height = window_height
        self.window_width = window_width
        self.base_color = base_color
        self.retreat_color = retreat_color
        self.tile_size = tile_size
        self.tile_margin = tile_margin
        if self.pygame is None:
            self.pygame = pygame
        if self.screen is None:
            self.screen = screen
        for row in range(self.window_height):     
            self.grid.append([])
            for col in range(self.window_width):
                if col == 0 or col == (self.window_width - 1):
                    tile = FieldObject.FieldObject(row, col, True, "Retreat")
                else:
                    tile = FieldObject.FieldObject(row, col, True, "Grounds")
                self.grid[row].append(tile)

    def draw(self):
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                if self.grid[row][col].name == "Retreat":
                    color = self.retreat_color
                else:
                    color = self.base_color
                self.draw_cell(row, col, color)

    def draw_cell(self, row, col, color):
        if self.grid[row][col].border:
            self.pygame.draw.rect(self.screen, color, [
                (self.tile_size + self.tile_margin) * col + self.tile_margin,
                (self.tile_size + self.tile_margin) * row + self.tile_margin,
                self.tile_size + self.tile_margin, self.tile_size + self.tile_margin])
        else:
            self.pygame.draw.rect(self.screen, color, [
                (self.tile_size + self.tile_margin) * col + self.tile_margin,
                (self.tile_size + self.tile_margin) * row + self.tile_margin,
                self.tile_size + self.tile_margin, self.tile_size + self.tile_margin])
    
    def get_tile_size(self):
        return self.tile_size

    def get_tile_margin(self):
        return self.tile_margin
    
    def get_window_height(self):
        return self.window_height
    
    def set_player_location(self, row, col, player_located, active_color):
        self.grid[row][col].set_player_location(player_located)
        if player_located:
            self.draw_cell(row, col, active_color)
        else:
            self.draw_cell(row, col, self.base_color)
    
    def get_window_width(self):
        return self.window_width
    
    def get_base_color(self):
        return self.base_color
    
    def is_spot_available(self, row, col):
        if self.grid[row][col].is_available():
            return True
        else:
            return False
        
    def is_valid(self, row, col):
        return (-1 < row < self.get_window_height()) and (-1 < col < self.get_window_width())