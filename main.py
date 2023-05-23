import pygame
import random

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    K_a,
    K_b,
    K_c,
    K_d,
    K_SPACE,
    KEYDOWN,
    QUIT
)

BLACK = (0,0,0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GRAY = (220,220,220)
GREEN = (0, 255, 0)
LAWN_GREEN = (124,252,0)
DARK_GREEN = (0,100,0)
OLIVE = (128,128,0)
SIZE = 60
TILE_SIZE = 40
PIP_SIZE = 40                                
TILE_MARGIN = 4
WINDOW_WIDTH = 14 
WINDOW_HEIGHT = 10
NUMBER_OF_TEAMS = 2
PLAYERS_PER_TEAM = 2

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

class GameField():
    grid = []
    base_color = LAWN_GREEN

    def __init__(self):
        for row in range(WINDOW_HEIGHT):     
            self.grid.append([])
            for col in range(WINDOW_WIDTH):
                if col == 0 or col == (WINDOW_WIDTH - 1):
                    tile = FieldObject(row, col, True, "Retreat")
                else:
                    tile = FieldObject(row, col, True, "Grounds")
                self.grid[row].append(tile)

    def draw(self, pygame, screen):
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                if self.grid[row][col].name == "Retreat":
                    color = OLIVE
                else:
                    color = self.base_color
                if self.grid[row][col].border:
                    pygame.draw.rect(screen, color, [(TILE_SIZE + TILE_MARGIN) * col + TILE_MARGIN,
                                (TILE_SIZE + TILE_MARGIN) * row + TILE_MARGIN,
                                TILE_SIZE, TILE_SIZE])
                else:
                    pygame.draw.rect(screen, color, [(TILE_SIZE + TILE_MARGIN) * col + TILE_MARGIN,
                                (TILE_SIZE + TILE_MARGIN) * row + TILE_MARGIN,
                                TILE_SIZE + TILE_MARGIN, TILE_SIZE + TILE_MARGIN])

class Character():
    active_color = BLACK
    inactive_color = LAWN_GREEN

    def __init__(self, row, col, screen, character_class='FIGHTER'):
        self.row = -1
        self.col = -1
        self.character_class = ''
        self.active = True
        print(f"new character at {row}, {col}")
        self.set_position(row, col, screen)
        self.character_class = character_class

    def draw(self, color, screen):
        pygame.draw.rect(screen, color, [(TILE_SIZE + TILE_MARGIN) * self.col + TILE_MARGIN,
                        (TILE_SIZE + TILE_MARGIN) * self.row + TILE_MARGIN,
                        TILE_SIZE, PIP_SIZE])

    def set_position(self, row, col, screen):
        self.draw(self.inactive_color, screen)
        self.row = row
        self.col = col
        if not (self.row == -1 and self.col == -1):
            self.draw(self.active_color, screen)

    def move(self, by_row, by_col, screen):
        if self.active:
            if self.row != -1 and self.col != -1:
                if (-1 < self.row + by_row < WINDOW_HEIGHT) and (-1 < self.col + by_col < WINDOW_WIDTH):
                    self.set_position(self.row + by_row, self.col + by_col, screen)
                else:
                    print("player made invalid move")
            if self.col == 0 or self.col == WINDOW_WIDTH - 1:
                self.active = False
        return self.row, self.col
    
    def get_active(self):
        return self.active

class Team():

    def __init__(self, coord, screen):
        self.players = []
        self.active = True
        self.coord = coord
        self.current_player = -1
        for i in range(0, PLAYERS_PER_TEAM):
            row = random.randint(1, 20)
            if row > 9:
                col = 1 + coord
                while row > 9:
                    row = row - 10
            else:
                col = coord
            self.players.append(Character(row, col, screen))
            print(f"this team now has {len(self.players)} players")

    def get_player_count(self):
        return len(self.players)
    
    def get_first_player(self):
        for i in range(0, len(self.players)):
            if self.players[i].get_active():
                return i
        #no active players
        self.active = False
        return -1
    
    def get_current_player(self):
        return self.current_player
    
    def get_current_player_object(self):
        return self.players[self.current_player]

    def get_next_player(self):
        if self.current_player == self.get_player_count() - 1:
            self.current_player = -1
        else:
            finding_player = True
            while finding_player and self.current_player < PLAYERS_PER_TEAM:
                self.current_player = self.current_player + 1
                if self.players[self.current_player].get_active():
                    finding_player = False
            if finding_player:
                self.active = False
                print(f"team is no longer active")
        return self.current_player
    
    def get_active(self):
        return self.active
    
    def move_current_player(self, by_row, by_col, screen):
        self.players[self.get_current_player()].move(by_row, by_col, screen)


def get_next_team_player(move_team, teams):
    if teams[move_team].get_next_player() == -1:
        if move_team == NUMBER_OF_TEAMS - 1:
            move_team = 0
            teams[move_team].get_next_player()
        else:
            move_team = move_team + 1
            teams[move_team].get_next_player()
    return move_team
        

def main():
    random.seed()
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH * (TILE_SIZE + TILE_MARGIN), WINDOW_HEIGHT * (TILE_SIZE + TILE_MARGIN)))
    clock = pygame.time.Clock()
    screen.fill(BLACK)
    game_board = GameField()
    game_board.draw(pygame, screen)
    teams = []
    teams.append(Team(1, screen))
    teams.append(Team(11, screen))
    running = True
    move_team = 0
    teams[move_team].get_next_player()
    print(f"starting values {move_team =} and {teams[move_team].get_current_player() =}")
    while running:
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == KEYDOWN:
                match event.key:
                    case pygame.K_d:
                        print('')
                    case pygame.K_DOWN:
                        teams[move_team].move_current_player(1, 0, screen)
                    case pygame.K_UP:
                        teams[move_team].move_current_player(-1, 0, screen)
                    case pygame.K_LEFT:
                        teams[move_team].move_current_player(0, -1, screen)
                    case pygame.K_RIGHT:
                        teams[move_team].move_current_player(0, 1, screen)
                    case pygame.K_SPACE:
                        #end turn, next player
                        move_team = get_next_team_player(move_team, teams)
                        print(f"starting values {move_team =} and {teams[move_team].get_current_player() =}")
                        print(f"player is active: {teams[move_team].get_current_player_object().get_active()}")
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__": 
    main() 
