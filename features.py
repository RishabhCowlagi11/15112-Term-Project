import time, math

class Button:
    def __init__(self, xCenter, yCenter, xLen, yLen, text, direct = 1,
                 bgColor = "gray", outlineColor = "black", outlineWidth = 5,
                 textFont = "Arial 26 bold", fill = "white"):
        self.xCenter = xCenter
        self.yCenter = yCenter
        self.xLen = xLen
        self.yLen = yLen
        self.bgColor = bgColor
        self.outlineColor = outlineColor
        self.outlineWidth = outlineWidth
        self.text = text
        self.textFont = textFont
        self.direct = direct
        self.fill = fill

    def drawRectangleButton(self, app, canvas):
        canvas.create_rectangle(self.xCenter - self.xLen / 2,
                                self.yCenter - self.yLen / 2,
                                self.xCenter + self.xLen / 2,
                                self.yCenter + self.yLen / 2,
                                fill = self.bgColor, outline = self.outlineColor,
                                width = self.outlineWidth)

        canvas.create_text(self.xCenter, self.yCenter, text = self.text,
                           font = self.textFont, anchor = "c", fill = self.fill)

    def drawCircleButton(self, app, canvas):
        canvas.create_oval(self.xCenter - self.yLen / 2,
                                self.yCenter - self.yLen / 2,
                                self.xCenter + self.yLen / 2,
                                self.yCenter + self.yLen / 2,
                                fill = self.bgColor, outline = self.outlineColor,
                                width = self.outlineWidth)

        canvas.create_text(self.xCenter, self.yCenter, text = self.text,
                           font = self.textFont, anchor = "c", fill = self.fill)

    def drawTriangleButton(self, app, canvas):
        canvas.create_polygon((self.xCenter + self.direct * self.xLen / 2, 
                              self.yCenter - self.yLen / 2), 
                              (self.xCenter - self.direct * self.xLen / 2, 
                              self.yCenter),
                              (self.xCenter + self.direct * self.xLen / 2, 
                              self.yCenter + self.yLen / 2),
                              fill = self.bgColor, outline = self.outlineColor,
                              width = self.outlineWidth)

    def updateColor(self, color):
        self.bgColor = color

    def isPressedRectangle(self, eventX, eventY):
        if(self.xCenter - self.xLen / 2 <= eventX <= self.xCenter + self.xLen / 2 and
           self.yCenter - self.yLen / 2 <= eventY <= self.yCenter + self.yLen / 2):
            return True
        return False

    @staticmethod
    def getDistance(x1, y1, x2, y2):
        return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    def isPressedCircle(self, eventX, eventY):
        radius = self.yLen / 2
        distance = Button.getDistance(self.xCenter, self.yCenter, eventX, eventY)
        if(distance <= radius):
            return True
        return False

    def isPressedTriangle(self, eventX, eventY):
        pt1 = (self.xCenter + self.direct * self.xLen / 2, self.yCenter - self.yLen / 2)
        pt2 = (self.xCenter - self.direct * self.xLen / 2, self.yCenter)
        pt3 = (self.xCenter + self.direct * self.xLen / 2, self.yCenter + self.yLen / 2)
        
        lineSlope1 = (pt1[1] - pt2[1]) / (pt1[0] - pt2[0])
        lineSlope3 = (pt2[1] - pt3[1]) / (pt2[0] - pt3[0])

        projLine1 = lineSlope1 * (eventX - pt1[0]) + pt1[1]
        projLine3 = lineSlope3 * (eventX - pt2[0]) + pt2[1]

        if(self.direct == 1):
            if(eventY >= projLine1 and eventY <= projLine3 and eventX <= pt1[0]):
                return True
            return False
        elif(self.direct == -1):
            if(eventY >= projLine1 and eventY <= projLine3 and eventX >= pt1[0]):
                return True
            return False

class Text(Button):
    def __init__(self, xCenter, yCenter, xLen, yLen, text = "", 
                 isClicked = False, bgColor = "white", outlineColor = "black", 
                 outlineWidth = 5, textFont = "Arial 26 bold", fill = "white"):
        super().__init__(xCenter, yCenter, xLen, yLen, text = "", bgColor = bgColor,
                         outlineColor = outlineColor, outlineWidth = outlineWidth, 
                         textFont = textFont, fill = fill)
        self.isClicked = isClicked
        self.text = text
    
    def drawText(self, app, canvas):
        canvas.create_text(self.xCenter - self.xLen / 2 + 10, self.yCenter,
                           text = self.text, font = self.textFont, fill = "black",
                           anchor = "w")
    
    def getText(self):
        return self.text

    # Figure out how to fill the textbox without overflow
    def updateText(self, letter):
        if(letter == -1):
            self.text = self.text[:-1]
        elif(len(self.text) <= 11):
            self.text += str(letter)

    def clearText(self):
        self.text = ""

    def getIsClicked(self):
        return self.isClicked

    def updateIsClicked(self, state):
        self.isClicked = state
    
    def updateOutline(self):
        if(self.isClicked):
            self.outlineColor = "red"
        else:
            self.outlineColor = "black"

    def drawCursor(self, app, canvas):
        if(self.isClicked):
            canvas.create_line(self.xCenter - self.xLen / 2 + 10,
                               self.yCenter - self.cursorLen / 2,
                               self.xCenter - self.xLen / 2 + 10,
                               self.yCenter + self.cursorLen / 2,
                               fill = "black", width = 5)