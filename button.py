class Button:
    def __init__(self, xCenter, yCenter, xLen, yLen, text,
                 bgColor = "gray", outlineColor = "black", outlineWidth = 5):
        self.xCenter = xCenter
        self.yCenter = yCenter
        self.xLen = xLen
        self.yLen = yLen
        self.bgColor = bgColor
        self.outlineColor = outlineColor
        self.outlineWidth = outlineWidth
        self.text = text

    def drawRectangleButton(self, app, canvas):
        canvas.create_rectangle(self.xCenter - self.xLen / 2,
                                self.yCenter - self.yLen / 2,
                                self.xCenter + self.xLen / 2,
                                self.yCenter + self.yLen / 2,
                                fill = self.bgColor, outline = self.outlineColor,
                                width = self.outlineWidth)

        canvas.create_text(self.xCenter, self.yCenter, text = self.text,
                           font = "Arial 26 bold", anchor = "c")

    def isPressed():
        pass

    def updateColor(self, color):
        self.color = color

    def buttonPressed(self):
        pass

