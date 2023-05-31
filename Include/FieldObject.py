class FieldObject():
    
    def __init__(self, row, col, border, name):
        self.name = name
        self.column = row
        self.col = col
        self.border = border
        self.player_location = False
        self.rect = None
        self.player_location = False

    def get_name(self):
        return self.name
    
    def set_rect(self, rect):
        self.rect = rect

    def set_player_location(self, is_player_there):
        self.player_location = is_player_there

    def is_available(self):
        return not self.player_location
        