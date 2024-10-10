class configuration:
    'key parameters to change the layout of the window'
    def __init__(self):
        self.setup()

    def setup(self):
        self.WINDOW_HEIGHT = 480
        self.WINDOW_WIDTH = 800
        self.ROWS = 10
        self.COLUMNS = 9
        #key needs to have a space between , and 2nd number to work
        #this is all the specially sized grid cells
        self.SPANS = {'[1, 2]':[4,5], 
         '[5, 0]':[1,2], '[6, 0]':[1,2],'[7, 0]':[1,2],'[8, 0]':[1,2],
         '[5, 5]':[1,2], '[6, 5]':[1,2], '[7, 5]':[1,2], '[8, 5]':[1,2]}

        


        