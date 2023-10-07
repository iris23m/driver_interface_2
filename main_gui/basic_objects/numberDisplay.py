import pygame
class number_display:
    def __init__(self,master, coords , canvasObject):
        self.x1 =coords[0]
        self.y1 =coords[1]
        self.x2 =coords[2]
        self.y2 =coords[3]
        self.colours = [(25, 25, 25) for i in range(7)]
        self.master = master
        self.width = int((self.y2 - self.y1)/15)
        self.canvasObject = canvasObject
        self.get_coords()
    
    def draw_line(self, linecoords, colour):
        pygame.draw.line(self.canvasObject, colour, (linecoords[0], linecoords[1]),(linecoords[2], linecoords[3]), self.width)
        #self.canvasObject.create_line(linecoords[0], linecoords[1], linecoords[2], linecoords[3], width = self.width, fill = colour)
 
    def get_coords(self):
        offset = (self.y2-self.y1)*0.05

        x1a = self.x1 + offset 
        x1b = self.x2 - offset 
        topHorizontal = [x1a, self.y1, x1b, self.y1]

        x2a = self.x1 + offset 
        x2b = self.x2 - offset 
        y2 = ((self.y2 - self.y1)/2) + self.y1
        middleHorizontal = [x2a, y2, x2b, y2]

        x3a = self.x1 + offset 
        x3b = self.x2 - offset 
        bottomHorizontal = [x3a, self.y2, x3b, self.y2]

        y4a = self.y1 + offset 
        y4b = ((self.y2-self.y1)/2) - offset + self.y1
        leftTopVertical = [self.x1, y4a, self.x1, y4b]

        y5a = ((self.y2-self.y1)/2) + offset +self.y1
        y5b = self.y2 - offset 
        leftBottomVertical = [self.x1, y5a, self.x1, y5b]

        y6a = self.y1 + offset 
        y6b = ((self.y2-self.y1)/2) - offset +self.y1
        rightTopVertical = [self.x2, y6a, self.x2, y6b]
        
        y7a = ((self.y2-self.y1)/2) + offset +self.y1
        y7b = self.y2 - offset 
        rightBottomVertical = [self.x2, y5a, self.x2, y5b]

        self.allLines = [topHorizontal, middleHorizontal, bottomHorizontal, leftTopVertical, 
                         leftBottomVertical, rightTopVertical, rightBottomVertical]
        self.draw_shape()

    def draw_shape(self):
        for i in range(7):
            self.draw_line(self.allLines[i], self.colours[i])

    def get_colours(self, number):
        off = (25, 25, 25) #grey
        on = (255, 255, 255) #white
        colours = [
            [on, off, on, on, on, on, on], 
            [off, off, off, off, off, on, on],
            [on, on, on, off, on, on, off],
            [on, on, on, off, off, on, on],
            [off, on, off, on, off, on, on],
            [on, on, on, on, off, off, on],
            [on, on, on, on, on, off, on],
            [on, off, off, off, off, on, on],
            [on, on, on, on, on, on, on],
            [on, on, on, on, off, on, on]]
        
        #in case of an input that isn't between 1 and 9
        try:
            self.colours = colours[number]
        except: self.colours = [off, on, off, off, off, off, off]