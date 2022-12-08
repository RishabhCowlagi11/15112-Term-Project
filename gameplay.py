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
                # print((dr, dc), "testing inDirect()....", GamePlay.inDirection(app, board, row, col, dr, dc, player))
                # if(GamePlay.isOnBoardRowCol(app, row + dr, col + dc)):
                #     print("player: ", player)
                #     print((dr, dc), "testing board()....", str(board[row + dr][col + dc])) #.getColor() == 1 - player)
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
        # print("testing squareIsOpen().....", GamePlay.squareIsOpen(app, board, row, col))
        # print("testing inLine()......", GamePlay.inLine(app, board, row, col, player))
        if(GamePlay.squareIsOpen(app, board, row, col) and 
           GamePlay.inLine(app, board, row, col, player)):
            return True
        return False

    @staticmethod
    def flipPieces(app, boardObject, row, col, player):
        board = boardObject.getBoard()
        app.flipPieces = []

        drow = [-1, 0, 1]
        dcol = [-1, 0, 1]

        for dr in drow:
            for dc in dcol:
                # print(f"inDirection({(dr, dc)}):", GamePlay.inDirection(app, board, row, col, dr, dc, player))
                if(GamePlay.inDirection(app, board, row, col, dr, dc, player)):
                    newRow, newCol = row + dr, col + dc
                    while(board[newRow][newCol].getColor() == 1 - player):
                        app.flipPieces.append((newRow, newCol))
                        # boardObject.tempUpdateGameBoard(app, newRow, newCol, player)
                        # boardObject.animateFlip(app, newRow, newCol, player)
                        newRow += dr
                        newCol += dc

    @staticmethod
    def flipPieces2(app, boardObject, row, col, player):
        board = boardObject.getBoard()

        drow = [-1, 0, 1]
        dcol = [-1, 0, 1]

        for dr in drow:
            for dc in dcol:
                # print(f"inDirection({(dr, dc)}):", GamePlay.inDirection(app, board, row, col, dr, dc, player))
                if(GamePlay.inDirection(app, board, row, col, dr, dc, player)):
                    newRow, newCol = row + dr, col + dc
                    while(board[newRow][newCol].getColor() == 1 - player):
                        boardObject.tempUpdateGameBoard(app, newRow, newCol, player)
                        newRow += dr
                        newCol += dc