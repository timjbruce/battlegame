import pygame
import random
from Include import GameField
from Include import Team

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




def get_next_team_player(move_team, teams):
    print(f"current team {move_team}")
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
    game_board = GameField.GameField(WINDOW_HEIGHT, WINDOW_WIDTH, TILE_SIZE, TILE_MARGIN,
                            LAWN_GREEN, OLIVE)
    game_board.draw(pygame, screen)
    teams = []
    teams.append(Team.Team(1, PLAYERS_PER_TEAM, RED, game_board, pygame, screen))
    teams.append(Team.Team(11, PLAYERS_PER_TEAM, BLUE, game_board, pygame, screen))
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
                        teams[move_team].move_current_player(1, 0, game_board)
                    case pygame.K_UP:
                        teams[move_team].move_current_player(-1, 0, game_board)
                    case pygame.K_LEFT:
                        teams[move_team].move_current_player(0, -1, game_board)
                    case pygame.K_RIGHT:
                        teams[move_team].move_current_player(0, 1, game_board)
                    case pygame.K_SPACE:
                        #end turn, next player
                        move_team = get_next_team_player(move_team, teams)
                        print(f"starting values {move_team =} and {teams[move_team].get_current_player() =}")
                        print(f"player is active: {teams[move_team].get_current_player_object().get_active()}")
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__": 
    main() 
