class FieldObject():
    
    def __init__(self, row, col, border, name, image):
        self.name = name
        self.column = row
        self.col = col
        self.border = border
        self.player_location = False
        self.rect = None
        self.player_location = False
        self.image = image

    def get_name(self):
        return self.name
    
    def set_rect(self, rect):
        self.rect = rect

    def set_player_location(self, is_player_there):
        self.player_location = is_player_there

    def is_available(self):
        return not self.player_location and (self.name == 'Grounds' or self.name == 'Retreat')
    
    def has_base_image(self):
        return not self.base_image == None
        