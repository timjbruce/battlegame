import random
from . import Character

class Team():
    def __init__(self, coord, number_of_players, active_color, game_field, pygame, screen):
        self.players = []
        self.active = True
        self.coord = coord
        self.current_player = -1
        self.number_of_players = number_of_players
        self.pygame = pygame
        self.screen = screen
        for i in range(0, self.number_of_players):
            row = random.randint(1, 20)
            if row > 9:
                col = 1 + coord
                while row > 9:
                    row = row - 10
            else:
                col = coord
            self.players.append(Character.Character(row, col, active_color, game_field, pygame, screen))
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
            while finding_player and self.current_player < self.number_of_players - 1:
                self.current_player = self.current_player + 1
                if self.players[self.current_player].get_active():
                    finding_player = False
            if finding_player:
                self.active = False
                print(f"team is no longer active")
        return self.current_player
    
    def get_active(self):
        return self.active
    
    def move_current_player(self, by_row, by_col, game_board):
        self.players[self.get_current_player()].move(by_row, by_col, game_board, self.pygame, self.screen)