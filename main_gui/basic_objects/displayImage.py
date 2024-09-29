import tkinter as tk
import pygame
#from PIL import Image, ImageTk 


class display_image:
    'creates an image from a file given, and calculates coords to place it centrally in a grid space '
    def __init__(self, master, imageLocation, gridCoord, grid, size, windowWidth, windowHeight):
        self.master = master
        self.imageLocation = imageLocation
        self.gridCoord = gridCoord
        self.grid = grid
        self.size = size
        self.numberColumns = grid.numberColumns
        self.numberRows = grid.numberRows
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight
        self.canvasObject = self.grid.canvaslist[gridCoord[0]][gridCoord[1]]
        self.get_image()
        self.get_coords()
        

    def get_image(self):
        'gets the image from file and saves it in the correct way'
        #unsizedImage = Image.open(self.imageLocation)
        #resizedImage = unsizedImage.resize((self.size[0],self.size[1]), Image.ANTIALIAS)
        #self.img = ImageTk.PhotoImage(resizedImage)
        unsizedImage = pygame.image.load(self.imageLocation) 
        self.img = pygame.transform.scale(unsizedImage, (self.size[0],self.size[1]))

    def get_coords(self):
        self.boxwidth = (self.windowWidth/self.grid.numberColumns)*self.grid.completeSpans[self.gridCoord[0]][self.gridCoord[1]][1]
        self.boxheight = (self.windowHeight/self.grid.numberRows)*self.grid.completeSpans[self.gridCoord[0]][self.gridCoord[1]][0]
        boxCentrex = self.boxwidth/2
        boxCentrey = self.boxheight/2
        self.x = boxCentrex - (self.size[0]/2)
        self.y = boxCentrey - (self.size[1]/2)
    

    def attach_image(self):
        'method to actually put the image on the correct canvas so it displays'
    #    self.canvasObject.create_image(self.x,self.y ,anchor=tk.NW, image = self.img)
        self.canvasObject.blit(self.img, (self.x,self.y))

    def refresh(self):
        pygame.draw.rect(self.canvasObject, (0, 0, 0), pygame.Rect(0,0, self.boxwidth,self.boxheight))
    
    

