class configuration:
    'key parameters to change the layout of the window'
    def __init__(self):
        self.setup()

    def setup(self):
        self.WINDOW_HEIGHT = 480
        self.WINDOW_WIDTH = 800
        self.ROWS = 12
        self.COLUMNS = 8
        #key needs to have a space between , and 2nd number to work
        self.SPANS = {'[1, 0]':[4,6], '[0, 3]':[1,2], '[4, 0]':[1,2], 
         '[5, 0]':[1,2], '[6, 0]':[1,2],'[7, 0]':[1,2],'[8, 0]':[1,2],
         '[9, 0]':[1,2], '[10, 0]':[1,2], '[4, 4]':[1,2],'[5, 4]':[1,2], '[6, 4]':[1,2],
         '[7, 4]':[1,2], '[8, 4]':[1,2], '[9, 4]':[1,2], '[11, 3]':[1,2]}

        


        