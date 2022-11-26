class Chip():
    def __init__(self, location, color = None, outline = "black", width = 3):
        self.row = location[0]
        self.col = location[1]
        self.color = color
        self.outline = outline
        self.width = width

    def __str__(self):
        return f"Chip @ {(self.row, self.col)} that is {self.color}"

    def __repr__(self):
        if(self.color == None):
            return "-"
        return f"{self.color}"
    
    def getLocation(self):
        return self.location

    def getColor(self):
        return self.color

    def setLocation(self, location):
        self.location = location

    def setColor(self, color):
        self.color = color
        
    def drawChip(self, app, canvas):
        if(self.color == 0):
            color = app.color0
        elif(self.color == 1):
            color = app.color1
        else:
            color = ""
        rowIncrement = app.boardHeight / app.rows
        colIncrement = app.boardWidth / app.cols
        margin = 5
        canvas.create_oval(app.marginWidthLeft + self.col * colIncrement + margin, 
                           app.marginHeightTop + self.row * rowIncrement + margin,
                           app.marginWidthLeft + (self.col + 1) * colIncrement - margin,
                           app.marginHeightTop + (self.row + 1) * rowIncrement - margin,
                           fill = color, outline = self.outline, width = self.width)
        
