# Pygame lib for moving the snake 
# Time lib for neccessary initiation and game finishing
# Random lib for generating random position of food block
import pygame
import time
import random

# initiating the game
pygame.init()

# colors dictionary (probably i need a better color palette)
colors = {
    "DarkGreen": (19, 42, 19),
    "Mindaro": (236, 243, 158),
    "CarolinaBlue": (116, 179, 206),
    "Fulvous": (233, 138, 21),
    "Palatinate": '#59114D',
    "Ecru": "#C2B280",
}

# general display configs 
display_width = 1200
display_height = 800
display = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Basic Snake')

# syncing the clock 
clock = pygame.time.Clock()

# initializing snake 
snake_block = display_height / 40
snake_speed = display_width / 40

# Styles
font_style = pygame.font.SysFont("bahnschrift", int(snake_block)*2)
score_style = pygame.font.SysFont("comicsansms", int(snake_speed)*2)

# Score function
def Score(score):
    value = score_style.render("Score: " + str(score), True, colors["Mindaro"])
    display.blit(value, [display_width / 2.35, 10])

# Snake function
def Snake(snake_block, snakeBody):
    for x in snakeBody:
        pygame.draw.rect(display, colors["DarkGreen"], [x[0], x[1], snake_block, snake_block])

# Message function
def Message(msg, color):
    mesg = font_style.render(msg, True, color)
    display.blit(mesg, [display_width/3.75, display_height/2.5])

# the main game function
def gameLoop():
    game_over = False
    game_close = False 

    # setting coordinates
    x1 = display_width / 2
    y1 = display_height / 2
    x1_change = 0
    y1_change = 0

    snakeBody = []
    Length_of_snake = 1

    # initing the food
    food_x = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0 
    food_y = round(random.randrange(0, display_height - snake_block) / 10.0) * 10.0 

    # while loop 
    while not game_over:

        while game_close == True:
            # closing screen color
            display.fill(colors["Ecru"])
            Message("You Lost! Press Q or to play again press C", colors["Fulvous"]) 
            
            pygame.display.update()

            # commands of the closing screen
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        # commands for playing in the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -10
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = 10
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -10
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = 10
                    x1_change = 0

        # setting the borders for not letting the snake go out of them
        if x1 >= display_width or x1 < 0 or y1 >= display_height or y1 < 0:
            game_close = True
        
        # incrementing the coordinates and appending to the snake
        x1 += x1_change
        y1 += y1_change
        display.fill(colors["Ecru"])
        pygame.draw.rect(display,colors["Palatinate"], [food_x,food_y,snake_block,snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snakeBody.append(snake_Head)

        if len(snakeBody) > Length_of_snake:
            del snakeBody[0]

        for x in snakeBody[:-1]:
            if x == snake_Head:
                game_close = True
        
        Snake(snake_block, snakeBody)
        Score(Length_of_snake - 1)

        pygame.display.update()

        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0 
            food_y = round(random.randrange(0, display_height - snake_block) / 10.0) * 10.0 
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
    