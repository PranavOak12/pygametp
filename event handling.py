import pygame
from pygame.constants import K_UP, KEYDOWN, QUIT
pygame.init()

game_window = pygame.display.set_mode((800, 600))
game_title = pygame.display.set_caption("My First Game :)") 
game_icon = 0

exitgame = False
gameover = False
highscore = 0

while not exitgame :
    for event in pygame.event.get():
        if event.type == QUIT:
                exitgame = True
        if event.type == KEYDOWN:
            if event.key == K_UP:
                print("upar gaya bird")
pygame.quit()
quit()

