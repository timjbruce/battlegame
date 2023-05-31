import os
import random
from . import FieldObject

class GameField():
    grid = []
    pygame = None
    screen = None
    rocks = 5
    trees = 5

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
                    tile = FieldObject.FieldObject(row, col, True, "Retreat", self.water_image)
                else:
                    tree = random.randint(0, 100)
                    if tree <= self.trees:
                        tile = FieldObject.FieldObject(row, col, True, "Trees", self.trees_image)    
                    else:
                        rock = random.randint(0, 100)
                        if rock <= self.rocks:
                            tile = FieldObject.FieldObject(row, col, True, "Rocks", self.rocks_image)    
                        else:
                            tile = FieldObject.FieldObject(row, col, True, "Grounds", self.ground_image)
                self.grid[row].append(tile)

    def load_assets(self):
        self.water_image = self.pygame.image.load(os.path.join(os.getcwd(),'Assets/medievalTile_27.png')).convert()
        self.ground_image = self.pygame.image.load(os.path.join(os.getcwd(),'Assets/medievalTile_57.png')).convert()
        self.trees_image = self.pygame.image.load(os.path.join(os.getcwd(),'Assets/medievalTile_48.png')).convert()
        self.rocks_image = self.pygame.image.load(os.path.join(os.getcwd(),'Assets/medievalEnvironment_11.png')).convert()

    def draw_background(self):
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                self.draw_background_cell(row, col, self.retreat_color)

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
        self.blit_background(row, col)

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
        self.screen.blit(self.grid[row][col].image, self.grid[row][col].rect)
