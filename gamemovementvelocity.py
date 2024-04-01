import pygame
from pygame.constants import K_DOWN, K_LEFT, K_RIGHT, K_UP, KEYDOWN, QUIT
pygame.init()
 # colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

# snakevariables
snakex = 380
snakey = 280
snake_sizex = 20
snake_sizey = 20
velocity_x = 0
velocity_y = 0
snk_list = []
snakelenghth = 2
# gamespecific variables
FPS = 20
score = 0
clock = pygame.time.Clock()
screen_width = 800
screen_height = 600
game_window = pygame.display.set_mode((screen_width,screen_height))
game_title = pygame.display.set_caption("Snake") 
    

# score on screen
font = pygame.font.SysFont(None,55)
def text_screen(text ,color ,xc ,yc):
    screen_text = font.render(text, True, color)
    game_window.blit(screen_text,[xc,yc])
# increasing length snake fn
def plot_snake(game_window , color ,snk_list ,snake_sizex):
    for x ,y in snk_list :
        pygame.draw.rect(game_window,color,[x , y ,snake_sizex , snake_sizex])
#food variables
import random
foodx = random.randrange(40,screen_width-40,20)
foody = random.randrange(40,screen_height-40,20)
pygame.display.update




exitgame = False
gameover = False





# gameloop
while not exitgame:
    for event in pygame.event.get():
        if event.type == QUIT:
            exitgame = True
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                velocity_x = 20
                velocity_y = 0
            elif event.key == K_LEFT:
                velocity_x = -20
                velocity_y = 0
            elif event.key == K_UP:
                velocity_y = -20
                velocity_x = 0
            elif event.key == K_DOWN:
                velocity_y = 20
                velocity_x = 0
    if abs (snakex - foodx)<5 and abs (snakey - foody)<5:
        score += 1
        foodx = random.randrange(40,screen_width-40,20)
        foody = random.randrange(40,screen_height-40,20)   
        snakelenghth += 2
    
    head = []
    head.append(snakex)
    head.append(snakey)
    snk_list.append(head)
    if len(snk_list)>snakelenghth:
        del snk_list [0]

    snakex += velocity_x
    snakey += velocity_y
    clock.tick(FPS)
    game_window.fill(white)
    pygame.draw.rect(game_window, black,[snakex , snakey , snake_sizex , snake_sizey])
    plot_snake(game_window , black ,snk_list ,snake_sizex)
    pygame.draw.rect(game_window,red,[foodx , foody ,snake_sizex , snake_sizex])
    text_screen("Score: " + str(score*10),black,5,5)
    pygame.display.update()