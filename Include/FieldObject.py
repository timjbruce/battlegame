class FieldObject():
    name = ''
    col = -1
    row = -1
    border = True
    
    def __init__(self, row, col, border, name):
        self.name = name
        self.column = row
        self.col = col
        self.border = border

    def get_name(self):
        return self.name