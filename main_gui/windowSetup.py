from main_gui.config_file import configuration
from main_gui.windowUpdate import window_update 
from main_gui.medium_objects.manageGrid import manage_grid
from main_gui.medium_objects.attachSpeed import attach_speed 
from main_gui.basic_objects.numberDisplay import number_display 
from main_gui.basic_objects.Arrow import arrow
from main_gui.basic_objects.textManager import text_manager
from main_gui.basic_objects.displayImage import display_image

import pygame
import os

class window_setup:
    
    'sets up the window, creates all the objects, creates the window updater from the windows_update class that can be used later'
    def __init__(self):
        pygame.display.init()

 #       #this is to set up pygame in the linux framebuffer
 #       # Based on "Python GUI in Linux frame buffer"
 #       # http://www.karoltomala.com/blog/?p=679
 #       disp_no = os.getenv("DISPLAY")
 #       if disp_no:
 #           print("I'm running under X display = {0}".format(disp_no))
 #       
 #       # Check which frame buffer drivers are available
 #       # Start with fbcon since directfb hangs with composite output
 #       drivers = ['fbcon', 'directfb', 'svgalib']
 #       found = False
 #       for driver in drivers:
 #          # Make sure that SDL_VIDEODRIVER is set
 #           if not os.getenv('SDL_VIDEODRIVER'):
 #               os.putenv('SDL_VIDEODRIVER', driver)
 #           try:
 #               pygame.display.init()
 #           except pygame.error:
 #               print('Driver: {0} failed.'.format(driver))
 #               continue
 #           found = True
 #           break


        pygame.init()
        config_values = configuration()#still need for grid!
        
        self.window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        #self.window = pygame.display.set_mode((200, 200))
        self.windowWidth = self.window.get_width()
        self.windowHeight = self.window.get_height()
        geo = str(config_values.WINDOW_WIDTH) + 'x' + str(config_values.WINDOW_HEIGHT)
#        self.window.geometry(geo) #not sure still need geo
        self.grid = manage_grid(self.window, config_values.ROWS, config_values.COLUMNS , config_values.SPANS,self.windowWidth,self.windowHeight )
        self.gridWidth = self.windowWidth/config_values.COLUMNS
        self.gridHeight = self.windowHeight/config_values.ROWS
        self.updatableTextObjectsList = []
        status = True
    
        
        self.create_left_arrow()
        self.create_right_arrow()
        self.create_speed()
        self.create_battDrain()
        self.create_solarPower()
        self.create_busVolts()
        self.create_bmuStatus()
        self.create_motorStatuses()
        self.create_ivtStatuses()
        self.create_mpptStatuses()
        self.create_driveMode()
        self.create_warning_lights()
        self.update_window()

    def create_left_arrow(self):
        leftArrowDirection = 'left'
        leftArrowCanvas = self.grid.canvaslist[0][0]
        self.leftArrow = arrow(self.window, leftArrowDirection, leftArrowCanvas, self.gridWidth, self.gridHeight,1.5)
     
    def create_right_arrow(self):
        rightArrowDirection = 'right'
        rightArrowCanvas = self.grid.canvaslist[0][6]
        self.rightArrow = arrow(self.window, rightArrowDirection, rightArrowCanvas, self.gridWidth, self.gridHeight,1.5)

    def create_speed(self):
        self.speedObject = attach_speed(self.window, [1,0], self.grid, self.windowWidth, self.windowHeight)
    
    def create_text_object(self, text, position, displayNow = True):
        textObject = text_manager(self.window, position, self.grid, self.windowWidth, self.windowHeight)
        if displayNow:
              textObject.display_text(text)
        else:
              self.updatableTextObjectsList.append(textObject)
        return textObject
          
    def create_battDrain(self):
        self.battDrainText = self.create_text_object('Batt. drain: ', [5, 0])
        self.battDrainUnitsText = self.create_text_object('kW', [5, 2])
        self.battDrainValueText = self.create_text_object(None, [5,1], False)

    def create_solarPower(self):
        self.solarPowerText = self.create_text_object('Solar power: ', [6, 0])
        self.solarPowerUnitsText = self.create_text_object('kW', [6, 2])
        self.solarPowerValueText = self.create_text_object(None, [6,1], False)

    def create_busVolts(self):
        self.busVoltsText = self.create_text_object('Bus volts: ', [7, 0])
        self.busVoltsUnitsText = self.create_text_object('kW', [7, 2])
        self.busVoltsValueText = self.create_text_object(None, [7,1], False) 

    def create_bmuStatus(self):
        self.bmuStatusText = self.create_text_object('BMU: ', [8, 0])
        self.bmuStatusValueText = self.create_text_object(None, [8, 1], False)

    def create_motorStatuses(self):
        self.LMotorStatusText = self.create_text_object('L Motor: ', [8, 3])
        self.LMotorStatusValueText = self.create_text_object(None, [8, 4], False)
    
        self.RMotorStatusText = self.create_text_object('R Motor: ', [9, 3])
        self.RMotorStatusValueText = self.create_text_object(None, [9, 4], False)

    def create_ivtStatuses(self):
        self.ivtFrontStatusText = self.create_text_object('IVT Front: ', [9, 0])
        self.ivtFrontStatusValueText = self.create_text_object(None, [9, 1], False)

        self.ivtRearStatusText = self.create_text_object('IVT Rear: ', [10, 0])
        self.ivtRearStatusValueText = self.create_text_object(None, [10, 1], False)

    def create_mpptStatuses(self):
            
        self.mppt1StatusText = self.create_text_object('MPPT1: ', [5, 3])
        self.mppt1StatusValueText = self.create_text_object(None, [5, 4], False)
    
        self.mppt2StatusText = self.create_text_object('MPPT2: ', [6, 3])
        self.mppt2StatusValueText = self.create_text_object(None, [6, 4], False)
    
        self.mppt3StatusText = self.create_text_object('MPPT3: ', [7, 3])
        self.mppt3StatusValueText = self.create_text_object(None, [7, 4], False)

    def create_driveMode(self):
        self.DdriveModeObject = text_manager(self.window, [11, 2], self.grid, self.windowWidth, self.windowHeight)
        self.NdriveModeObject = text_manager(self.window, [11, 3], self.grid, self.windowWidth, self.windowHeight)  
        self.RdriveModeObject = text_manager(self.window, [11, 4], self.grid, self.windowWidth, self.windowHeight)           

    def create_warning_lights(self):
        self.hazardLight = display_image(self.window, "hazard_light.png" , [0,3], self.grid, [25,25], self.windowWidth, self.windowHeight)

    def update_window(self):
        self.windowUpdater = window_update(self.window, self.speedObject, self.leftArrow, self.rightArrow,self.hazardLight, self.updatableTextObjectsList, self.DdriveModeObject, self.NdriveModeObject, self.RdriveModeObject)
