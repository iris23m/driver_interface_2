from main_gui.windowSetup import window_setup 
from main_gui.programLoop import program_loop 
from main_gui.getData import dataFetcher
import pygame

windowSetup = window_setup()
dataFetcher = dataFetcher()
loop1 = program_loop(windowSetup.window, windowSetup, dataFetcher)
updateEvent = pygame.USEREVENT + 3
pygame.time.set_timer(updateEvent, 500)

while True:
    #windowSetup.window.update()
    #loop1.update()
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == updateEvent:
            loop1.update()
        
        if event.type == pygame.USEREVENT + 1:
            loop1.leftFlash()
        elif event.type == pygame.USEREVENT+2:
            loop1.rightFlash()

        if event.type == pygame.QUIT:
 
            # deactivates the pygame library
            pygame.quit()
 
            # quit the program.
            quit()
 


        