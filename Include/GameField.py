from . import FieldObject

class GameField():
    grid = []

    def __init__(self, window_height, window_width, tile_size, tile_margin, base_color, retreat_color):
        self.window_height = window_height
        self.window_width = window_width
        self.base_color = base_color
        self.retreat_color = retreat_color
        self.tile_size = tile_size
        self.tile_margin = tile_margin
        for row in range(self.window_height):     
            self.grid.append([])
            for col in range(self.window_width):
                if col == 0 or col == (self.window_width - 1):
                    tile = FieldObject(row, col, True, "Retreat")
                else:
                    tile = FieldObject(row, col, True, "Grounds")
                self.grid[row].append(tile)

    def draw(self, pygame, screen):
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                if self.grid[row][col].name == "Retreat":
                    color = self.retreat_color
                else:
                    color = self.base_color
                if self.grid[row][col].border:
                    pygame.draw.rect(screen, color, [(self.tile_size + self.tile_margin) * col + self.tile_margin,
                                (self.tile_size + self.tile_margin) * row + self.tile_margin,
                                self.tile_size + self.tile_margin, self.tile_size + self.tile_margin])
                else:
                    pygame.draw.rect(screen, color, [(self.tile_size + self.tile_margin) * col + self.tile_margin,
                                (self.tile_size + self.tile_margin) * row + self.tile_margin,
                                self.tile_size + self.tile_margin, self.tile_size + self.tile_margin])
    
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