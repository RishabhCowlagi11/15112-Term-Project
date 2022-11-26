class Button:
    def __init__(self, xCenter, yCenter, xLen, yLen, text, direct = 1,
                 bgColor = "gray", outlineColor = "black", outlineWidth = 5,
                 textFont = "Arial 26 bold"):
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

    def drawRectangleButton(self, app, canvas):
        canvas.create_rectangle(self.xCenter - self.xLen / 2,
                                self.yCenter - self.yLen / 2,
                                self.xCenter + self.xLen / 2,
                                self.yCenter + self.yLen / 2,
                                fill = self.bgColor, outline = self.outlineColor,
                                width = self.outlineWidth)

        canvas.create_text(self.xCenter, self.yCenter, text = self.text,
                           font = self.textFont, anchor = "c")

    def drawCircleButton(self, app, canvas):
        canvas.create_oval(self.xCenter - self.xLen / 2,
                                self.yCenter - self.yLen / 2,
                                self.xCenter + self.xLen / 2,
                                self.yCenter + self.yLen / 2,
                                fill = self.bgColor, outline = self.outlineColor,
                                width = self.outlineWidth)

        canvas.create_text(self.xCenter, self.yCenter, text = self.text,
                           font = self.textFont, anchor = "c")

    def drawTriangleButton(self, app, canvas):
        canvas.create_polygon((self.xCenter + self.direct * self.xLen / 2, 
                              self.yCenter - self.yLen / 2), 
                              (self.xCenter - self.direct * self.xLen / 2, 
                              self.yCenter),
                              (self.xCenter + self.direct * self.xLen / 2, 
                              self.yCenter + self.yLen / 2),
                              fill = self.bgColor, outline = self.outlineColor,
                              width = self.outlineWidth)

    def isPressedRectangle(self, eventX, eventY):
        if(self.xCenter - self.xLen / 2 <= eventX <= self.xCenter + self.xLen / 2 and
           self.yCenter - self.yLen / 2<= eventY <= self.yCenter + self.yLen / 2):
            return True
        return False

    def isPressedCircle(self, eventX, eventY):
        pass

    def isPressedTriangle(self, eventX, eventY):
        pt1 = (self.xCenter + self.direct * self.xLen / 2, self.yCenter - self.yLen / 2)
        pt2 = (self.xCenter - self.direct * self.xLen / 2, self.yCenter)
        pt3 = (self.xCenter + self.direct * self.xLen / 2, self.yCenter + self.yLen / 2)
        
        lineSlope1 = (pt1[1] - pt2[1]) / (pt1[0] - pt2[0])
        lineSlope3 = (pt2[1] - pt3[1]) / (pt2[0] - pt3[0])

        projLine1 = lineSlope1 * (eventX - pt1[0]) + pt1[1]
        projLine3 = lineSlope3 * (eventX - pt2[0]) + pt2[1]

        # print(projLine1, eventY)
        # print(projLine3, eventY)
        # print(pt1[0], eventX)
        # print("*******************")

        if(self.direct == 1):
            if(eventY >= projLine1 and eventY <= projLine3 and eventX <= pt1[0]):
                return True
            return False
        elif(self.direct == -1):
            if(eventY >= projLine1 and eventY <= projLine3 and eventX >= pt1[0]):
                return True
            return False