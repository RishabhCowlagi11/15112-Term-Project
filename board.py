import reversi

class Board:
    def __init__(self, rows, cols, boardColor = "green", bgColor = "gray"):
        self.rows = rows
        self.cols = cols
        self.bgColor = bgColor
        self.boardColor = boardColor
        self.board = [[None] * self.cols for i in range(self.rows)]

    def updateBoard(self, row, col, player):
        self.board[row][col] = player

    def displayBoard(self):
        print(self.board)

    def drawInitialBoard(self, app, canvas):
        canvas.create_rectangle(0, 0, app.width, app.height, fill = self.bgColor)

        rowIncrement, colIncrement = reversi.getIncrements(app)
        for row in range(self.rows):
            for col in range(self.cols):
                canvas.create_rectangle(colIncrement * col + app.margin,
                                        rowIncrement * row + app.margin, 
                                        colIncrement * (col + 1) + app.margin, 
                                        rowIncrement * (row + 1) + app.margin,
                                        fill = self.boardColor, outline = "black")


    