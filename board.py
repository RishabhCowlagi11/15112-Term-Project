import chip as Chip
import gameplay as GamePlay

class Board:
    def __init__(self, rows, cols, boardColorDark = "green", bgColor = "gray",
                 board = None, flip = False):
        self.rows = rows
        self.cols = cols
        self.bgColor = bgColor
        self.boardColorDark = boardColorDark
        self.chips = set()
        self.flip = flip
        if(board == None):
            self.board = [[None] * self.cols for i in range(self.rows)]
        else:
            self.board = board

    def getRows(self):
        return self.rows

    def getCols(self):
        return self.cols

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
        if(self.flip):
            GamePlay.GamePlay.flipPieces2(app, self, row, col, player)
        else:
            GamePlay.GamePlay.flipPieces(app, self, row, col, player)

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
                elif(row == app.hoverRow and col == app.hoverCol):
                    fill = "lime green"
                elif((row + col) % 2 == 1):
                    fill = app.boardColorDark
                else:
                    fill = app.boardColorLight                
                canvas.create_rectangle(colIncrement * col + app.marginWidthLeft,
                                        rowIncrement * row + app.marginHeightTop, 
                                        colIncrement * (col + 1) + app.marginWidthLeft, 
                                        rowIncrement * (row + 1) + app.marginHeightTop,
                                        fill = fill, outline = "black", width = 2)

    def drawIsometricBoard(self, app, canvas):
        canvas.create_rectangle(0, 0, app.width, app.height, fill = self.bgColor)
        for row in range(self.rows):
            for col in range(self.cols):
                if(row == app.lastPlayedRow and col == app.lastPlayedCol):
                    fill = "red"
                elif(row == app.hoverRow and col == app.hoverCol):
                    fill = "lime green"
                elif((row + col) % 2 == 1):
                    fill = app.boardColorDark
                else:
                    fill = app.boardColorLight
         
                p1 = (app.p1[0] + app.slope1Increment2 * col + app.slope2Increment2 * row, app.p1[1] + app.slope2Increment2 * row * app.slope1_4 + app.slope1Increment2 * app.slope1_2 * col)
                p2 = (p1[0] + app.slope1Increment2, p1[1] + app.slope1Increment2 * app.slope1_2)
                p3 = (p2[0] + app.slope2Increment2, p2[1] + app.slope2Increment2 * app.slope1_4)
                p4 = (p1[0] + app.slope2Increment2, p1[1] + app.slope2Increment2 * app.slope1_4)
                canvas.create_polygon(p1, p2, p3, p4, outline = "black", width = 0, fill = fill)
                mid1_2 = ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)
                mid1_4 = ((p1[0] + p4[0]) / 2, (p1[1] + p4[1]) / 2)
                centerX = (((app.slope1_4 * mid1_2[0]) - mid1_2[1] + mid1_4[1] - 
                            (app.slope1_2 * mid1_4[0])) / (app.slope1_4 - app.slope1_2))
                centerY = app.slope1_4 * (centerX - mid1_2[0]) + mid1_2[1]
                canvas.create_text(centerX, centerY, text = str(row) + " " + str(col))
        
        canvas.create_line(app.p4, app.p3, app.p2, fill = "black", width = 15)
        canvas.create_rectangle(app.p2[0] - 5, app.p2[1] - 5, app.p2[0] + 10, app.p2[1] + 30,
                                outline = "", width = 0, fill = self.bgColor)
        canvas.create_rectangle(app.p4[0] - 5, app.p4[1] - 5, app.p4[0] + 3, app.p4[1] + 30,
                                outline = "", width = 0, fill = self.bgColor)
    
    def drawChips2d(self, app, canvas):
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                if(self.board[row][col].getColor() != None):
                    chip = self.board[row][col]
                    chip.drawChip2d(app, canvas)

    def drawChipsIsometric(self, app, canvas):
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                if(self.board[row][col].getColor() != None):
                    chip = self.board[row][col]
                    chip.drawChipIsometric(app, canvas)

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
                if(GamePlay.GamePlay.legalSquare(app, app.gameBoard, i, j, playerTurn)):
                    result.add((i, j))
        self.legalSquares = result

    def getLegalSquares(self):
        return self.legalSquares

    def drawLegalSquares(self, app, canvas):
        for row, col in self.legalSquares:
            if(row == app.legalSquareRowThick and col == app.legalSquareColThick):
                chip = Chip.Chip((row, col), outline = "tan2", width = 8)
            else:
                chip = Chip.Chip((row, col), outline = "tan", width = 5)
            if(app.mode == "gameIsometric"):
                chip.drawChipIsometric(app, canvas)
            else:
                chip.drawChip2d(app, canvas)

    def isGameOver(self, app, playerTurn):
        if(self.boardIsFull()):
            return True
        elif(self.noMoreMoves(app, playerTurn)):
            return True
        return False

    def boardIsFull(self):
        for i in self.board:
            for j in i:
                if(j.getColor() == None):
                    return False
        return True
    
    def noMoreMovesPlayer(self, player):
        if(len(self.legalSquares) == 0):
            return True
        return False

    def noMoreMoves(self, app, playerTurn):
        if(len(self.legalSquares) == 0):
            self.updateLegalSquares(app, 1 - playerTurn)
            
            if(len(self.legalSquares) == 0):
                return True
            self.updateLegalSquares(app, 1 - playerTurn)
        return False





    

    



    


    