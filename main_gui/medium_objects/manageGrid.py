import pygame

class manage_grid():
    def __init__(self, master, numberRows, numberColumns, spans, width, height):
        self.master = master
        self.numberRows = numberRows
        self.numberColumns = numberColumns
        self.spans = spans
        self.width = width
        self.height = height
        self.canvaslist = [[] for i in range(numberRows)]
        self.completeSpans = [[] for i in range(numberRows)]
        self.create_grid()

    def create_grid(self):
        delete_grid = []
        for x in range(self.numberRows):
            for y in range(self.numberColumns):
                if [x,y] not in delete_grid:

                    columnSpan, rowSpan = self.manage_cell_merging(delete_grid, x, y)
                    self.create_canvas(x, y, columnSpan, rowSpan)

    def create_canvas(self, x, y, columnSpan, rowSpan):
        #x and y are the number along the column- so convert this to coords with window width etc.
        gridWidth = self.width/(self.numberColumns)
        gridHeight = self.height/(self.numberRows)
        xCoord = y*gridWidth
        yCoord = x*gridHeight
        canvas = self.master.subsurface(
            xCoord, yCoord, 
            columnSpan*gridWidth, rowSpan*gridHeight )
       
        self.canvaslist[x].append(canvas)

        self.completeSpans[x].append([rowSpan, columnSpan])

    def manage_cell_merging(self, delete_grid, x, y):
        try:
            columnSpan = self.spans[str([x,y])][1]
            rowSpan = self.spans[str([x,y])][0]
            for i in range(rowSpan):
                for j in range(columnSpan):
                    a = x+i
                    b = y+j
                    delete_grid.append([a,b])
        except:
            rowSpan = 1
            columnSpan = 1
        return columnSpan,rowSpan
