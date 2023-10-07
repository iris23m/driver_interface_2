
from main_gui.basic_objects.numberDisplay import number_display
import pygame

class attach_speed():
    def __init__(self, master, grid_coord, grid, window_width, window_height):
        self.master = master
        self.grid_coord = grid_coord
        self.grid = grid
        self.window_width = window_width
        self.window_height = window_height
        self.getcoords()
    
    def getcoords(self):
        boxwidth = (self.window_width/self.grid.numberColumns)*self.grid.completeSpans[self.grid_coord[0]][self.grid_coord[1]][1]
        boxheight = (self.window_height/self.grid.numberRows)*self.grid.completeSpans[self.grid_coord[0]][self.grid_coord[1]][0]
        offset = boxwidth/ 10
        self.digit1Coords = [boxwidth*0.1, boxheight*0.1, boxwidth*0.2, boxheight*0.9]
        self.digit2Coords =  [boxwidth*0.3, boxheight*0.1, boxwidth*0.4, boxheight*0.9]
        self.digit3Coords =  [boxwidth*0.5, boxheight*0.1, boxwidth*0.6, boxheight*0.9]
        self.unitsCoords = [boxwidth*0.9, boxheight*0.5]
        self.draw_numbers()

    def draw_numbers(self):
        location = self.grid.canvaslist[self.grid_coord[0]][self.grid_coord[1]]
        self.digit1 = number_display(self.master, self.digit1Coords, location)
        self.digit2 = number_display(self.master, self.digit2Coords, location)
        self.digit3 = number_display(self.master, self.digit3Coords, location)
        unitsize = int(12 *(self.window_height/300))
        font = 'freesansbold.ttf' #+ str(unitsize)
        #self.units = location.create_text(self.unitsCoords[0], self.unitsCoords[1], text = 'km/h', fill = 'white', font = font)
        font = pygame.font.Font(font, unitsize)
        text = font.render('km/h', True, (255, 255, 255), (0,0,0))
        location.blit(text, [self.unitsCoords[0], self.unitsCoords[1]])

    def attach_values(self, number):
        digits = [int(n) for n in str(number)]
        try:
            self.digit1.get_colours(digits[-3])
        except:
            self.digit1.get_colours(0)
        
        try:
            self.digit2.get_colours(digits[-2])
        except:
            self.digit2.get_colours(0)
        
        self.digit3.get_colours(digits[-1])

        if len(digits) > 3:
            #this will cause horizontal lines to be displayed
            self.digit1.get_colours('error')
            self.digit2.get_colours('error')
            self.digit3.get_colours('error')

        self.digit1.draw_shape() 
        self.digit2.draw_shape()   
        self.digit3.draw_shape()
