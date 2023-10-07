class dataFetcher:
    'the idea is that this is where the CAN function will go'
    def __init__(self):
        self.counter = 0
        self.return_data()

    def return_data(self):
        self.counter += 1
        self.inputSpeed =self.counter%200
        self.inputLeftIndicatorOn = True
        self.inputRightIndicatorOn = False
        self.hazardsOn = True
        self.battDrain = '100'
        self.solarPower = '20'
        self.updatingTextValues= ['100', '20', '1', 'NO COMMS','NO COMMS','NO COMMS','NO COMMS','NO COMMS',
                                  'NO COMMS','NO COMMS','NO COMMS']
        self.driveMode = 'N'
        if self.counter > 10:
            self.driveMode = 'D'
    
        if self.counter > 20:
            self.driveMode = 'N'
        


