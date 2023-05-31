import random
from . import Character

class Team():
    pygame = None
    screen = None

    def __init__(self, coord, number_of_players, team_color, game_field, pygame, screen):
        self.players = []
        self.active = True
        self.coord = coord
        self.current_player = -1
        if self.pygame == None:
            self.pygame = pygame
        if screen == None:
            self.screen = screen
        self.number_of_players = number_of_players
        for i in range(0, self.number_of_players):
            generating_start_location = True
            while generating_start_location:
                max = game_field.get_rows()
                row = random.randint(1, max * 2)
                if row > max:
                    col = 1 + coord
                    while row > max:
                        row = row - max
                else:
                    col = coord
                if game_field.is_valid(row, col):
                    print(f"checking {row =} {col =}")
                    generating_start_location = False
            self.players.append(Character.Character(row, col, team_color, game_field, pygame, screen))

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
            print(f"{finding_player =}")
            if finding_player:
                self.active = False
                self.current_player = -1
        return self.current_player
    
    def get_active(self):
        return self.active
    
    def move_current_player(self, by_row, by_col):
        self.players[self.current_player].move(by_row, by_col)

    def end_player_turn(self):
        self.players[self.current_player].end_turn()