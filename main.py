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

"""
Globals to define base colors for use in the game. These can then be referenced
by the globals for the specific game being developed. These should not need to
change for any implementation.
"""
BLACK = (0,0,0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GRAY = (220,220,220)
GREEN = (0, 255, 0)
LAWN_GREEN = (124,252,0)
DARK_GREEN = (0,100,0)
OLIVE = (128,128,0)
"""
These are game sepcific globals. Adjust to meet your needs:
    TILE_SIZE: size of a tile in pixes. Assumes a square.
    TILE_MARGIN: size in pixes of a margin, if margins are wanted.
    WINDOW_WITH: size of window width, in tiles.
    WINDOW_HEIGHT: size of window height, in tiles.-
    NUMBER_OF_TEAMS: number of teams that will be created. To be further developed.
    PLAYERS_PER_TEAM: number of players to generate per team.
    PLAYABLE_TILE: color of tile that character can move on.
    RETREAT_TILE: color of tile to use for out of bounds.
"""
TILE_SIZE = 40
TILE_MARGIN = 0
WINDOW_WIDTH = 14 
WINDOW_HEIGHT = 10
NUMBER_OF_TEAMS = 2
PLAYERS_PER_TEAM = 2
PLAYABLE_TILE = LAWN_GREEN
RETREAT_TILE = OLIVE
TEAMS = [{ "color": RED, "startingLoc": 1},
     { "color": BLUE, "startingLoc": 11}]


def get_next_team_player(move_team, teams):
    """
    Finds the next active team and player able to make a move
    """
    ## does current team have more moves?
    check_current_team = teams[move_team].get_next_player()
    while check_current_team == -1:
        ## does other team have moves?
        if move_team == NUMBER_OF_TEAMS - 1:
            move_team = 0
        else:
            move_team = move_team + 1
        check_current_team = teams[move_team].get_next_player()
    ### 
    return move_team
        
def main():
    random.seed()
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH * (TILE_SIZE + TILE_MARGIN), WINDOW_HEIGHT * (TILE_SIZE + TILE_MARGIN)))
    clock = pygame.time.Clock()
    screen.fill(BLACK)
    game_board = GameField.GameField(WINDOW_HEIGHT, WINDOW_WIDTH, TILE_SIZE, TILE_MARGIN,
                            PLAYABLE_TILE, RETREAT_TILE, pygame, screen)
    game_board.draw()
    teams = []
    for team in TEAMS:
        teams.append(Team.Team(team['startingLoc'], PLAYERS_PER_TEAM, team['color'], game_board, pygame, screen))
    running = True
    move_team = 0
    teams[move_team].get_next_player()
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
                        teams[move_team].move_current_player(1, 0)
                    case pygame.K_UP:
                        teams[move_team].move_current_player(-1, 0)
                    case pygame.K_LEFT:
                        teams[move_team].move_current_player(0, -1)
                    case pygame.K_RIGHT:
                        teams[move_team].move_current_player(0, 1)
                    case pygame.K_SPACE:
                        #end turn, next player
                        teams[move_team].end_player_turn()
                        move_team = get_next_team_player(move_team, teams)
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__": 
    main() 
