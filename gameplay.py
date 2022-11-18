class GamePlay:
    @staticmethod
    def isOnBoardXY(app, x, y):
        if(x > app.margin and y > app.margin and 
        x < app.width - app.margin and y < app.height - app.margin):
            return True
        return False

    @staticmethod
    def isOnBoardRowCol(app, row, col):
        if(0 <= row < app.rows and 0 <= col < app.cols):
            return True
        return False
    
    @staticmethod
    def inDirection(app, board, row, col, drow, dcol, player):
        # Prevents Checking Same Square
        if((drow, dcol) == (0, 0)):
            return False

        # Checks Intro Condition for Entering Loop
        newRow, newCol = row + drow, col + dcol
        if(not GamePlay.isOnBoardRowCol(app, newRow, newCol)):
            return False

        # Loops in Direction while new Square is of Opposite Color
        # Return False if Loops outside of Board
        while(board[newRow][newCol].getColor() == 1 - player):
            if(GamePlay.isOnBoardRowCol(app, newRow + drow, newCol + dcol)):
                newRow += drow
                newCol += dcol
            else:
                return False

        # If the Square that Breaks out of Loop is None return False else True
        if(board[newRow][newCol].getColor() == None):
            return False
        return True

    @staticmethod
    def inLine(app, board, row, col, player):
        drow = [-1, 0, 1]
        dcol = [-1, 0, 1]
        for dr in drow:
            for dc in dcol:
                if(GamePlay.inDirection(app, board, row, col, dr, dc, player) and
                   board[row + dr][col + dc].getColor() == 1 - player):
                    return True
        return False

    @staticmethod
    def squareIsOpen(app, board, row, col):
        if(board[row][col].getColor() == None):
            return True
        return False

    @staticmethod
    def legalSquare(app, board, row, col, player):
        if(GamePlay.squareIsOpen(app, board, row, col) and 
           GamePlay.inLine(app, board, row, col, player)):
            return True
        return False

    @staticmethod
    def flipPieces(app, board, row, col, player):
        drow = [-1, 0, 1]
        dcol = [-1, 0, 1]
        for dr in drow:
            for dc in dcol:
                if(GamePlay.inDirection(app, row, col, dr, dc, player)):
                    newRow, newCol = row + dr, col + dc
                    while(board[newRow][newCol].getColor() == 1 - player):
                        # Fix Line Below
                        app.gameBoardObject.updateGameBoard(app, newRow, newCol, player)
                        newRow += dr
                        newCol += dc