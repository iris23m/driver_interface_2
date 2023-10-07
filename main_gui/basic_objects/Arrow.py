import math as m
import pygame
class arrow:
    def __init__(self, master, a_direction, a_location, a_grid_width, a_grid_height, scale):
        self.master = master
        self.direction = a_direction
        self.location = a_location
        self.gridwidth = a_grid_width
        self.gridheight = a_grid_height
        self.scale = scale
        self.previouslyOn = False
        self.flashOn = False
        self.get_coords()
        
    def get_coords(self):
        'works out the coords in the grid space to put the arrow'
        self.arrow_y = self.gridheight/2
        self.arrowshape1 = self.gridwidth *0.15*self.scale
        self.arrowshape3 = self.gridheight *0.07*self.scale
        #self.arrowshape2 = m.sqrt((self.arrowhead1**2)+(self.arrowhead3**2))
        self.arrow_width = self.gridheight *0.2*self.scale
        
        self.arrowheady1 = self.arrow_y + (self.arrow_width/2)
        self.arrowheady2 = self.arrow_y + self.arrow_width + self.arrowshape3
        self.arrowheady3 = self.arrow_y - self.arrowshape3
        if self.direction == 'left':
            self.arrow_x1 = self.gridwidth * 0.3#0.1
            self.arrow_x2 = self.gridwidth * (0.1+(0.4*self.scale))
            #self.arrowside = tk.FIRST
            self.arrowheadx1 = self.arrow_x1 - self.arrowshape1
            self.arrowheadx2 = self.arrow_x1
            self.arrowheadx3 = self.arrow_x1
            

        elif self.direction == 'right':
            self.arrow_x1 =  self.gridwidth*(0.9-(0.4*self.scale))
            self.arrow_x2 = self.gridwidth*0.7#0.9
            #self.arrowside = tk.LAST
            self.arrowheadx1 = self.arrow_x2 + self.arrowshape1
            self.arrowheadx2 = self.arrow_x2
            self.arrowheadx3 = self.arrow_x2
    
        self.draw_arrow((127, 127, 127))

    def draw_arrow(self, colour):
        'Function to draw the arrow shape, need to give the colour but it takes the coords from the object'
        #self.location.create_line(self.arrow_x1, self.arrow_y, self.arrow_x2, self.arrow_y, 
                              #    width = self.arrow_width, fill = colour, arrow=self.arrowside, 
                                #  arrowshape=[self.arrowhead1,self.arrowhead2,self.arrowhead3])
        pygame.draw.polygon(self.location, colour, [[self.arrowheadx1,self.arrowheady1],
                                                    [self.arrowheadx2, self.arrowheady2], 
                                                    [self.arrowheadx3, self.arrowheady3]])
        pygame.draw.rect(self.location, colour, pygame.Rect(self.arrow_x1,self.arrow_y, 
                                                            (self.arrow_x2-self.arrow_x1),self.arrow_width))
   
    def flash_arrow(self): 
        'starts the indicator flashing, automatically stops when the status variable gets set to False'
        if self.flashOn:
            self.colour = (25, 25, 25)
        else:
            self.colour = (0, 255, 0)
        self.draw_arrow(self.colour)
        self.flashOn = not self.flashOn
        if not self.isOn:
            pygame.time.set_timer(self.flash_arrow(), 0)
            self.previouslyOn = False

    
  #  def flash_arrow_off(self):
   #     'Part of the flashing function- the two functions feedback to each other'
        
    #    self.draw_arrow(self.colour)
     #   if self.isOn:
      #      self.master.after(500, self.flash_arrow_on)
       #     self.previouslyOn = True
        #else:
         #   self.previouslyOn = False

    def update_arrow(self, isOn):
        if self.direction == 'left':
            my_event = pygame.USEREVENT + 1
        elif self.direction =='right':
            my_event = pygame.USEREVENT + 2
        self.isOn = isOn
        
        if self.isOn and self.previouslyOn == False:
            self.previouslyOn = True
            #self.flash_arrow()
            
            pygame.time.set_timer(my_event, 500)