import pygame
class text_manager:
    def __init__(self, master, gridCoord, grid, window_width, window_height):
        self.master = master
        self.gridCoord = gridCoord
        self.grid = grid
        self.length = 0
        self.window_width = window_width
        self.window_height = window_height
        self.coords_size()

    def coords_size(self): #could include text here to have size that changes with text input- but would have to call this everytime text is created
        #for t in text:
         #   self.length += 1
        self.boxWidth = (self.window_width/self.grid.numberColumns)*self.grid.completeSpans[self.gridCoord[0]][self.gridCoord[1]][1]
        self.boxHeight = (self.window_height/self.grid.numberRows)*self.grid.completeSpans[self.gridCoord[0]][self.gridCoord[1]][0]
        self.y = self.boxHeight/2
        self.x = self.boxWidth/2
        #size = int((boxwidth/self.length)* 1)
        self.size = int(13*(self.boxHeight/40))
        self.font = 'freesansbold.ttf'  #+ ' bold'
        self.canvasObject = self.grid.canvaslist[self.gridCoord[0]][self.gridCoord[1]]

    def display_text(self, text, isBold=False, colour= 'white'):
        #self.canvasObject.create_rectangle(0,0,self.boxWidth, self.boxHeight, fill = 'black' )
        pygame.draw.rect(self.canvasObject, (0, 0, 0), pygame.Rect(0,0, self.boxWidth,self.boxHeight))
        if isBold:
            self.font = self.font #+ 'bold'
        #self.canvasObject.create_text(self.x, self.y, text=text, fill=colour, font=self.font)
        font = pygame.font.Font(self.font, self.size)
        text = font.render(text, True, (255, 255, 255), (0,0,0))
        self.canvasObject.blit(text, [self.x, self.y])

    