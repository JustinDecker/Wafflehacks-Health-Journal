import os
import pygame

from pathlib import Path

pygame.init()

SCREEN_HEIGHT = 864
SCREEN_WIDTH = 1536
WIN = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
pygame.display.set_caption("main menu screen")
cozyfont = pygame.font.Font('resource\CooperFiveOpti-Black.otf',  36)

WHITE = (255,255,255)
FPS = 60

background_image = pygame.image.load("resource\\background.png") #load an image as a surface

text_bg = pygame.image.load("resource\\text_background.png").convert_alpha() #load an image, convert alpha preserves transparency


button_analyze = pygame.image.load("resource\\button_analyze.png").convert_alpha() #load an image, convert alpha preserves transparency
button_analyze_xy = (130,630)
button_analyze_rect = button_analyze.get_rect(topleft = button_analyze_xy)

button_quit = pygame.image.load("resource\\button_back.png").convert_alpha() #load an image, convert alpha preserves transparency
button_quit_xy = (1070,630)
button_quit_rect = button_analyze.get_rect(topleft = button_quit_xy)



def draw_image(image, xy):
    WIN.blit(image, xy) #Screen.blit(image, (x,y))


def draw_bg(color):
    WIN.fill(color) #fill the window with color, color is a tuple variable (R,G,B)


def draw_rect(color, rectangle):
    #pygame.draw.rect(surface, color, pygame.Rect(30, 30, 60, 60))
    pygame.draw.rect(WIN, color, rectangle, 70 , 15)
    pygame.draw.rect(WIN, color, rectangle, 2 , 3)
    

def draw_line():
    #pygame.draw.rect(surface, color, pygame.Rect(30, 30, 60, 60))
    pygame.draw.line(WIN, (0,0,0), (0,0), (600,100), 6)


def display_health_screen():
    clock = pygame.time.Clock()
    run = True

    while run: #main loop that runs every frame
        clock.tick(FPS) #controls the update speed of the program
        for event in pygame.event.get(): #Checks all pygame events every frame
            if event.type == pygame.QUIT: #If the user quits the program
                run = False #Stop running
            if event.type == pygame.QUIT or ( event.type == pygame.KEYDOWN and event.key == pygame.K_1): #If the player clicks X button, or presses keyboard 1 (the 1 key)
                pygame.quit() #quit
                exit() #terminate
            # if event.type == pygame.MOUSEBUTTONDOWN: #If the user clicked 
            #     if(button_analyze_rect.collidepoint(event.pos)): #and the position of the click collides with the x_y for the button
            #         return ("analyze")


        draw_image(background_image, (0,0))
        pygame.display.flip()#This updates the screen to show all changes     
        
    pygame.quit()

if __name__ == "__main__":
    display_health_screen()