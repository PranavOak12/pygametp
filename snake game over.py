from ast import Pass, Return
from platform import python_branch
import pygame
from pygame.constants import K_DOWN, K_LEFT, K_RIGHT, K_UP, KEYDOWN, QUIT
pygame.init()
import random
import os
pygame.mixer.init()




# title and window
screen_width = 800
screen_height = 600
game_window = pygame.display.set_mode((screen_width,screen_height))
game_title = pygame.display.set_caption("Snake") 

# increasing length snake fn
def plot_snake(game_window , color ,snk_list ,snake_sizex):
    for x ,y in snk_list :
        pygame.draw.rect(game_window,color,[x , y ,snake_sizex , snake_sizex])
# score on screen
font = pygame.font.SysFont(None,55)
def text_screen(text ,color ,xc ,yc):
    screen_text = font.render(text, True, color)
    game_window.blit(screen_text,[xc,yc])
 # colors
white =(211,211,211)
red = (255, 0, 0)
black = (0, 0, 0)
bluee = (10,190,10)

bgimg = pygame.image.load("background.jpg")
bgimg = pygame.transform.scale(bgimg,(screen_width,screen_height)) .convert_alpha()


# welcome screen 
def welcome():
    exitgame = False
    while not exitgame:
        game_window.fill(white)
        text_screen('''SNAKES :) Press Enter To Continue''',black,75,255)
        pygame.display.update()
        for event in pygame.event.get():
                if event.type == QUIT:
                    exitgame = True
                if event.type == KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()




# gameloop
def gameloop():
    pygame.mixer.music.load('back.mp3')
    pygame.mixer.music.play(-1)
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
    if(not os.path.exists("highscore.txt")):
        with open("highscore.txt", "w") as f:
            f.write("0")
    with open("highscore.txt", "r") as f:
            hiscore = f.read()
    score = 0
    clock = pygame.time.Clock()
    exitgame = False
    gameover = False    
    #food variables
    foodx = random.randrange(40,screen_width-40,20)
    foody = random.randrange(40,screen_height-40,20)
    pygame.display.update
    while not exitgame:
        if gameover:
            with open("highscore.txt", "w") as f:
                f.write(str(hiscore)) 
            game_window.fill(red)
            text_screen("GAME OVER :Press Enter to continue",white,80,270)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == QUIT:
                    exitgame = True
                if event.type == KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()

        else:    
            for event in pygame.event.get():
                if event.type == QUIT:
                    exitgame = True
                if event.type == KEYDOWN:
                    if event.key == K_RIGHT and velocity_x != -20:
                        velocity_x = 20
                        velocity_y = 0
                    elif event.key == K_LEFT and velocity_x != 20:
                        velocity_x = -20
                        velocity_y = 0
                    elif event.key == K_UP and velocity_y != 20:
                        velocity_y = -20
                        velocity_x = 0
                    elif event.key == K_DOWN and velocity_y != -20:
                        velocity_y = 20
                        velocity_x = 0
            if abs (snakex - foodx)<5 and abs (snakey - foody)<5:
                beep = pygame.mixer.Sound('beep.mp3')
                beep.play()

                score += 10
                foodx = random.randrange(40,screen_width-40,20)
                foody = random.randrange(40,screen_height-40,20)   
                snakelenghth += 2
                if score  > int(hiscore):
                    hiscore = score

            head = []
            head.append(snakex)
            head.append(snakey)
            snk_list.append(head)
            if len(snk_list)>snakelenghth:
                del snk_list [0]
            
            pygame.draw.rect(game_window,red,[0,0,20,600])
            pygame.draw.rect(game_window,red,[0,0,800,20])
            pygame.draw.rect(game_window,red,[780,0,20,800])
            pygame.draw.rect(game_window,red,[0,580,800,20])
            
            pygame.draw.rect(game_window, black,[snakex , snakey , snake_sizex , snake_sizey])
            plot_snake(game_window , black ,snk_list ,snake_sizex)
            pygame.draw.rect(game_window,bluee,[foodx , foody ,snake_sizex , snake_sizex])
            text_screen("Score: " + str(score) + " Highscore: " + str(hiscore),black,5,5)
            pygame.display.update()
            game_window.fill(white)
            game_window.blit(bgimg ,(0,0))
            if head in snk_list[:-2]:
                gameover = True
                pygame.mixer.music.load('gameover.mp3')
                pygame.mixer.music.play()

            snakex += velocity_x
            snakey += velocity_y
            if snakex < 10 or snakex > 779 or snakey < 10 or snakey > 579:
                gameover = True
                pygame.mixer.music.load('gameover.mp3')
                pygame.mixer.music.play()

                
        clock.tick(FPS)
        
        

        
    pygame.quit
    quit()
# ............................................................................................................................

welcome()






