import chip as Chip
import gameplay as GamePlay

class Board:
    def __init__(self, rows, cols, boardColor = "green", bgColor = "gray",
                 board = None):
        self.rows = rows
        self.cols = cols
        self.bgColor = bgColor
        self.boardColor = boardColor
        self.chips = set()
        if(board == None):
            self.board = [[None] * self.cols for i in range(self.rows)]
        else:
            self.board = board

    def __str__(self):
        pass

    def updateBoardWithObject(self, row, col, player):
        self.board[row][col] = player
        if(player.getColor() != None):
            self.chips.add(player)

    def tempUpdateGameBoard(self, app, row, col, player):
        chip = Chip.Chip((row, col), player)
        self.board[row][col] = chip

    # Consider making this do all the things, but for now ignore
    def updateGameBoard(self, app, row, col, player):
        chip = Chip.Chip((row, col), player)
        self.board[row][col] = chip
        GamePlay.GamePlay.flipPieces(app, self, row, col, player)
        Board.updateLegalSquares(self, app, 1 - player)

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
                if(row == app.lastPlayedRow and col == app.lastPlayedCol):
                    fill = "red"
                else:
                    fill = self.boardColor
                canvas.create_rectangle(colIncrement * col + app.marginWidthLeft,
                                        rowIncrement * row + app.marginHeightTop, 
                                        colIncrement * (col + 1) + app.marginWidthLeft, 
                                        rowIncrement * (row + 1) + app.marginHeightTop,
                                        fill = fill, outline = "black", width = 2)

    def drawChips(self, app, canvas):
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                if(self.board[row][col].getColor() != None):
                    chip = self.board[row][col]
                    # print("drawing", chip)
                    chip.drawChip(app, canvas)

    def simulateLegalSquares(self, app, playerTurn):
        result = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if(GamePlay.GamePlay.legalSquare(app, board, i, j, playerTurn)):
                    result.add((i, j))
        return result


    def updateLegalSquares(self, app, playerTurn):
        result = set()
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if(GamePlay.GamePlay.legalSquare(app, self.board, i, j, playerTurn)):
                    result.add((i, j))
        self.legalSquares = result

    def getLegalSquares(self):
        return self.legalSquares

    def drawLegalSquares(self, app, canvas):
        for row, col in self.legalSquares:
            chip = Chip.Chip((row, col), outline = "tan", width = 5)
            chip.drawChip(app, canvas)

    def isGameOver(self, app):
        if(self.boardIsFull()):
            return True
        elif(self.noMoreMoves(app)):
            return True
        return False

    def boardIsFull(self):
        for i in self.board:
            for j in i:
                if(j == None):
                    return False
        return True

    def noMoreMoves(self):
        if(len(self.legalSquare) == 0):
            updateLegalSquares(self, app, 1 - playerTurn)
            
            if(len(self.legalSquares) == 0):
                return True
            updateLegalSquares(self, app, 1 - playerTurn)
        
        return False





    

    



    


    