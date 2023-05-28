# Battle Game

Work in progress

Python 3.11

## Classes

### FieldObject
This class represents a single space on a field.

#### __init__
row = integer: row the object is in for the GameField
col = integer: col the object is in for the GameField
border = boolean: include a border
name = string: name of the FieldObject

### GameField
This class represents the entirety of a game board. Each space is made up of a FieldObject.

#### __init__
window_height = integer: height of window using number of tiles
window_width = integer: width of window using number of tiles
tile_size
tile_margin
base_color
retreat_color


### Character
This class represents a character that can move around a GameField

### Team
This class represents a team of characters.