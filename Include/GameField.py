import os
from . import FieldObject

class GameField():
    grid = []
    pygame = None
    screen = None

    def __init__(self, window_height, window_width, tile_size, tile_margin, retreat_color, pygame, screen):
        self.window_height = window_height
        self.window_width = window_width
        self.retreat_color = retreat_color
        self.tile_size = tile_size
        self.tile_margin = tile_margin
        if self.pygame is None:
            self.pygame = pygame
        self.load_assets()
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

    def load_assets(self):
        self.image = self.pygame.image.load(os.path.join(os.getcwd(),'Assets/medievalTile_57.png')).convert()

    def draw_background(self):
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                if self.grid[row][col].name == "Retreat":
                    color = self.retreat_color
                self.draw_background_cell(row, col, color)

    def draw_background_cell(self, row, col, color):
        if self.grid[row][col].border:
            rect = self.pygame.draw.rect(self.screen, color, [
                (self.tile_size + self.tile_margin) * col + self.tile_margin,
                (self.tile_size + self.tile_margin) * row + self.tile_margin,
                self.tile_size + self.tile_margin, self.tile_size + self.tile_margin])
        else:
            rect = self.pygame.draw.rect(self.screen, color, [
                (self.tile_size + self.tile_margin) * col + self.tile_margin,
                (self.tile_size + self.tile_margin) * row + self.tile_margin,
                self.tile_size + self.tile_margin, self.tile_size + self.tile_margin])
        self.grid[row][col].set_rect(rect)
        if self.grid[row][col].name == "Grounds":
            self.screen.blit(self.image, rect)

    def set_player_position(self, row, col, is_character_there):
        self.grid[row][col].set_player_location(is_character_there)

    def get_tile_size(self):
        return self.tile_size

    def get_tile_margin(self):
        return self.tile_margin
    
    def get_window_height(self):
        return self.window_height
    
    def get_window_width(self):
        return self.window_width
    
    def get_base_color(self):
        return self.base_color
    
    def is_valid(self, row, col):
        if (-1 < row < self.get_window_height()) and (-1 < col < self.get_window_width()):
            if self.grid[row][col].is_available():
                return True
            else:
                return False
        else:
            return False
        
    def get_rows(self):
        return self.window_height
    
    def blit_background(self, row, col):
        print(f"background blitting {row} {col} {self.grid[row][col].rect}")
        self.screen.blit(self.image, self.grid[row][col].rect)
