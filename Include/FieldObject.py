class FieldObject():
    
    def __init__(self, row, col, border, name):
        self.name = name
        self.column = row
        self.col = col
        self.border = border
        self.player_location = False

    def get_name(self):
        return self.name
    
    def set_player_location(self, value):
        self.player_location = value

    def is_available(self):
        return not self.player_location
        