class Chip():
    def __init__(self, location, color = None, outline = "black", width = 5):
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
        
    def drawChip2d(self, app, canvas):
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
    
    def drawChipIsometric(self, app, canvas):
        drawIsometric = True
        if(self.color == 0):
            color0 = app.color0
            color1 = app.color1
        elif(self.outline.find("tan") != -1):
            drawIsometric = False
        else:
            color0 = app.color1
            color1 = app.color0

        point1 = (app.p1[0] + app.slope1Increment2 * self.col + app.slope2Increment2 * self.row, 
                app.p1[1] + app.slope2Increment2 * self.row * app.slope1_4 + app.slope1Increment2 * app.slope1_2 * self.col)
        point2 = (point1[0] + app.slope1Increment2, point1[1] + app.slope1Increment2 * app.slope1_2)
        point4 = (point1[0] + app.slope2Increment2, point1[1] + app.slope2Increment2 * app.slope1_4)
        mid1_2 = ((point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2)
        mid1_4 = ((point1[0] + point4[0]) / 2, (point1[1] + point4[1]) / 2)
        centerX = (((app.slope1_4 * mid1_2[0]) - mid1_2[1] + mid1_4[1] - 
                    (app.slope1_2 * mid1_4[0])) / (app.slope1_4 - app.slope1_2))
        centerY = app.slope1_4 * (centerX - mid1_2[0]) + mid1_2[1]
        xLen = point2[0] - point1[0]
        yLen = point4[1] - point1[1]
        chipHeight = 6
        reps = 300
        chipIncrement = chipHeight / reps

        if(drawIsometric):
            for i in range(reps):

                if(i * chipIncrement >= chipHeight - 2 * chipIncrement or i <= 10):
                    outline = "black"
                elif(i * chipIncrement >= 2 * chipHeight / 3):
                    outline = color0
                else:
                    outline = color1

                canvas.create_oval(centerX - xLen / 2, centerY - yLen / 2 - chipIncrement * i, 
                                   centerX + xLen / 2, centerY + yLen / 2 - chipIncrement * i,
                                   outline = outline, width = 0.5, fill = color0)
        else:
            canvas.create_oval(centerX - xLen / 2, centerY - yLen / 2, 
                               centerX + xLen / 2, centerY + yLen / 2,
                               outline = self.outline, width = 2, fill = "")
