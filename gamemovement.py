import pygame
from pygame.constants import K_DOWN, K_LEFT, K_RIGHT, K_UP, KEYDOWN, QUIT
pygame.init()

# colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
# snakevariables
snakex = 390
snakey = 290
snake_sizex = 15
snake_sizey = 15


# gamespecific variables
FPS = 40
clock = pygame.time.Clock()
screen_width = 800
screen_height = 600
game_window = pygame.display.set_mode((screen_width,screen_height))
game_title = pygame.display.set_caption("Snake") 
exitgame = False
gameover = False
pygame.display.update

while not exitgame:
    for event in pygame.event.get():
        if event.type == QUIT:
            exitgame = True
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                snakex += 10
            elif event.key == K_LEFT:
                snakex -= 10
            elif event.key == K_UP:
                snakey -= 10
            elif event.key == K_DOWN:
                snakey += 10

    clock.tick(FPS)
    game_window.fill(white)
    pygame.draw.rect(game_window, black,[snakex , snakey , snake_sizex , snake_sizey])

    pygame.display.update()




    