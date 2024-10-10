class program_loop:
    'main loop to keep updating everything- uses the window_update object that was first created in the window_setup object '
    def __init__(self, master, windowSetup, dataFetcher):
        self.master = master
        self.windowSetup = windowSetup
        self.dataFetcher = dataFetcher
        self.update()
 
    def update(self): 
        'updates the values and schedules the other update function to be called- the two functions pass between each other'
        
        self.dataFetcher.return_data()
        self.windowSetup.windowUpdater.general_update(self.dataFetcher.inputSpeed, self.dataFetcher.inputLeftIndicatorOn,
                                                       self.dataFetcher.inputRightIndicatorOn, self.dataFetcher.hazardsOn,
                                                         self.dataFetcher.updatingTextValues)
        
        #self.master.after(500, self.update2)
    def leftFlash(self):
        self.windowSetup.leftArrow.flash_arrow()
        
    def rightFlash(self):
        self.windowSetup.rightArrow.flash_arrow()
    
#    def update2(self):
 #       'updates the values and schedules the first function again'
  #      self.dataFetcher.return_data()
   #     self.windowSetup.windowUpdater.general_update(self.dataFetcher.inputSpeed, self.dataFetcher.inputLeftIndicatorOn,
    #                                                   self.dataFetcher.inputRightIndicatorOn, self.dataFetcher.hazardsOn,
     #                                                    self.dataFetcher.updatingTextValues, self.dataFetcher.driveMode)
      #  
       # self.master.after(500, self.update1)
    


    