import chip as Chip

class Board:
    def __init__(self, rows, cols, boardColor = "green", bgColor = "gray"):
        self.rows = rows
        self.cols = cols
        self.bgColor = bgColor
        self.boardColor = boardColor
        self.board = [[None] * self.cols for i in range(self.rows)]
        self.chips = set()

    def updateBoardWithObject(self, row, col, player):
        self.board[row][col] = player
        if(player.getColor() != None):
            self.chips.add(player)

    def updateGameBoard(self, row, col, player):
        chip = Chip.Chip((row, col), player)
        self.board[row][col] = chip

    def getBoard(self):
        return self.board

    def displayBoard(self):
        for i in self.board:
            print(i)

    def drawBoard(self, app, canvas):
        canvas.create_rectangle(0, 0, app.width, app.height, fill = self.bgColor)

        rowIncrement = app.boardHeight / app.rows
        colIncrement = app.boardWidth / app.cols
        for row in range(self.rows):
            for col in range(self.cols):
                canvas.create_rectangle(colIncrement * col + app.margin,
                                        rowIncrement * row + app.margin, 
                                        colIncrement * (col + 1) + app.margin, 
                                        rowIncrement * (row + 1) + app.margin,
                                        fill = self.boardColor, outline = "black")

    def drawChips(self, app, canvas):
        print("Running drawChips()...")
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                if(self.board[row][col].getColor() != None):
                    chip = self.board[row][col]
                    print("drawing", chip)
                    chip.drawChip(app, canvas)


    


    