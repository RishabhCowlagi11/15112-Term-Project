import reversi as Reversi

class Chip():
    def __init__(self, location, color = None, outline = "", width = 0):
        self.row = location[0]
        self.col = location[1]
        self.color = color
        self.outline = outline
        self.width = width

    def __str__(self):
        return f"Chip @ {(self.location)} that is {self.color}"

    def __repr__(self):
        return f"{type(self)}"
    
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
        rowIncrement, colIncrement = Reversi.getIncrements(app)
        margin = 5
        canvas.create_oval(app.margin + self.col * colIncrement + margin, 
                           app.margin + self.row * rowIncrement + margin,
                           app.margin + (self.col + 1) * colIncrement - margin,
                           app.margin + (self.row + 1) * rowIncrement - margin,
                           fill = color, outline = self.outline, width = self.width)
        
