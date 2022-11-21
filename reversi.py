# Importing modules
from cmu_112_graphics import *
import copy, time
import board as Board
import chip as Chip
import button as Button
import gameplay as GamePlay

##################### APP STARTED #####################
def appStarted(app):
    # game starts at home screen 
    app.mode = "home"

    # declare the default board and chip colors
    app.baseColor = "gray"
    app.color0 = "White"
    app.color1 = "Black"

    # declare the starting number of each chip
    app.countColor0 = 2
    app.countColor1 = 2

    # declare default board size
    app.rows = 8
    app.cols = 8

    # declare board dimensions
    app.margin = 50
    app.boardWidth = app.width - app.margin * 2
    app.boardHeight = app.height - app.margin * 2

    # player 0 make first move
    app.playerTurn = 0

    # create the game board, place chips and get legal moves
    app.gameBoardObject = Board.Board(app.rows, app.cols)
    app.gameBoard = app.gameBoardObject.getBoard()
    placeChipsOnBoard(app)
    app.gameBoardObject.updateLegalSquares(app, app.playerTurn)

    app.lastPlayedRow = None
    app.lastPlayedCol = None
    
    app.timerDelay = 1000000000000000000

    # probably ignore
    app.pause = False
    app.gameOver = False
    app.error = False
    app.miniMax = True

##################### USER INPUTS ######################
def game_mousePressed(app, event):
    rowWidth = app.boardHeight / app.rows 
    colWidth = app.boardWidth / app.cols
    
    # If clicked square is on board, get its row and col
    if(isOnBoardXY(app, event.x, event.y)):
        clickedRow = int((event.y - app.margin) / rowWidth)
        clickedCol = int((event.x - app.margin) / colWidth)
    else:
        return

    # Checks if square is legal, then places chip and changes turn
    # print("Player: ", app.playerTurn)
    # input()
    # print("Testing isOnBoardXY().....", isOnBoardXY(app, event.x, event.y))
    # print("Testing legalSquare().....", GamePlay.GamePlay.legalSquare(app, app.gameBoard, clickedRow, clickedCol, app.playerTurn))
    if(isOnBoardXY(app, event.x, event.y) and
    GamePlay.GamePlay.legalSquare(app, app.gameBoard, clickedRow, clickedCol, app.playerTurn)):
        app.lastPlayedRow, app.lastPlayedCol = clickedRow, clickedCol
        app.gameBoardObject.updateGameBoard(app, clickedRow, clickedCol, app.playerTurn)
        # GamePlay.GamePlay.flipPieces(app, app.gameBoardObject, clickedRow, clickedCol, app.playerTurn)
        app.state, app.countColor0, app.countColor1 = getCounts(app, app.gameBoard)
        
        app.playerTurn = 1 - app.playerTurn          
    else:
        app.error = True

def game_mouseMoved(app, event):
    pass

def game_mouseReleased(app, event):
    app.error = False
    if(app.playerTurn == 1 and app.miniMax):
            depth = 1
            miniMax(app, depth, depth, app.gameBoard, app.gameBoardObject.getLegalSquares())

    if(len(app.gameBoardObject.getLegalSquares()) == 0):
        app.playerTurn = 1 - app.playerTurn
        app.gameBoardObject.updateLegalSquares(app, app.playerTurn)
        if(len(app.gameBoardObject.getLegalSquares()) == 0):
            app.gameOver = True
        


def game_keyPressed(app, event):
    if(event.key == "r"):
        appStarted(app)

def home_keyPressed(app, event):
    if(event.key == "r"):
        appStarted(app)

def home_mousePressed(app, event):
    if(is2PlayerButtonPressed(app, event.x, event.y)):
        app.mode = "game"
    elif(is1PlayerButtonPressed(app, event.x, event.y)):
        app.mode = "game"

def home_mouseMoved(app, event):
    pass

def home_mouseReleased(app, event):
    pass

##################### UPDATE GAME #######################
# References
# https://en.wikipedia.org/wiki/Minimax
def miniMax(app, depth, refDepth, board, legalSquares, isComputerTurn = True):
    boardScore = 0
    move = None

    # Base Case
    if(depth == 0):
        return getState(app, board)

    for i, j in legalSquares:
        # Creating new board instance to simulate the game
        # as to not directly change the gameBoard
        simulatedBoard = Board.Board(app.gameBoardObject.rows, 
                                     app.gameBoardObject.cols,
                                     board = copy.deepcopy(board))

        simulatedBoard.updateGameBoard(app, i, j, int(isComputerTurn))

        # Recursive call to get the game score of the remaining moves
        result = miniMax(app, depth - 1, depth, simulatedBoard.getBoard(),
                         simulatedBoard.getLegalSquares(), not isComputerTurn)

        # Computer wants to maximize game score
        # Player wants to minimize game score
        if(isComputerTurn and result >= boardScore):
            boardScore = result
            move = (i, j)
        elif(result <= boardScore):
            boardScore = result
            move = (i, j)
    
    if(move != None and depth == refDepth):
        # From https://stackoverflow.com/questions/15472707/make-python-program-wait
        # time.sleep(1)
        app.gameBoardObject.updateGameBoard(app, move[0], move[1], 1)
        app.lastPlayedRow = move[0]
        app.lastPlayedCol = move[1]
        app.playerTurn = 0
    
    return boardScore

#################### STATE FUNCTIONS ####################
def game_timerFired(app):
    pass

def getCounts(app, board):
    state, countColor0, countColor1 = 0, 0, 0
    for i in range(app.rows):
        for j in range(app.cols):
            if(board[i][j].getColor() != None):
                if(board[i][j].getColor() == 0):
                    state -= 1
                    countColor0 += 1
                elif(board[i][j].getColor() == 1):
                    state += 1
                    countColor1 += 1

    return state, countColor0, countColor1

def getState(app, board):
    return getCounts(app, board)[0]

def placeChipsOnBoard(app):
    for row in range(len(app.gameBoard)):
        for col in range(len(app.gameBoard[0])):
            if((row, col) == (app.rows // 2, app.cols // 2) or
               (row, col) == (app.rows // 2 - 1, app.cols // 2 - 1)):
               chip = Chip.Chip((row, col), 0)
            elif((row, col) == (app.rows // 2 - 1, app.cols // 2) or 
                 (row, col) == (app.rows // 2, app.cols // 2 - 1)):
                chip = Chip.Chip((row, col), 1)
            else:
                chip = Chip.Chip((row, col), None)
            app.gameBoardObject.updateBoardWithObject(row, col, chip)

################## CHECKING FUNCTIONS ###################
def is2PlayerButtonPressed(app, x, y):
    centerX = app.width / 2
    centerY = app.height / 2
    xLen = app.width / 2
    yLen = app.height / 10
    if(centerX - xLen <= x <= centerX + xLen and
       centerY - yLen <= y <= centerY + yLen):
       return True
    return False

def is1PlayerButtonPressed(app, x, y):
    centerX = app.width / 2
    xLen = app.width / 2
    yLen = app.height / 10
    centerY = app.height / 2 + yLen + 15
    if(centerX - xLen <= x <= centerX + xLen and
       centerY - yLen <= y <= centerY + yLen):
       return True
    return False

def isOnBoardXY(app, x, y):
    if(x > app.margin and y > app.margin and 
       x < app.width - app.margin and y < app.height - app.margin):
        return True
    return False

###################### DRAWING FUNCTIONS ######################
def drawError(app, canvas):
    if(app.error and not app.gameOver):
        canvas.create_rectangle(0, 0, app.width, app.height, fill = "red")

def getIncrements(app):
    rowIncrement = app.boardHeight / app.rows
    colIncrement = app.boardWidth / app.cols
    return rowIncrement, colIncrement

def drawHomePage(app, canvas):
    canvas.create_rectangle(0, 0, app.width, app.height, fill = "green")
    # Add reversi image
    centerX = app.width / 2
    centerY = app.height / 2
    xLen = app.width / 2
    yLen = app.height / 10
    buttonDiff = 15
    player2Button = Button.Button(centerX, centerY, xLen, yLen,
                                  text = "2 Player Reversi!!")
    player1Button = Button.Button(centerX, centerY + yLen + buttonDiff, xLen, yLen,
                                  text = "1 Player Reversi!!!")
                                  
    player2Button.drawRectangleButton(app, canvas)
    player1Button.drawRectangleButton(app, canvas)

def drawLegalSquares(app, canvas):
    app.gameBoardObject.drawLegalSquares(app, canvas)

def drawLastPlayed(app, canvas):
    if(app.lastPlayedRow == None or app.lastPlayedCol == None):
        return
    else:
        canvas.create_rectangle()

def drawBoard(app, canvas):
    app.gameBoardObject.drawBoard(app, canvas)
    app.gameBoardObject.drawChips(app, canvas)

def drawScore(app, canvas):
    widthCenter = app.width / 2
    heightCenter = app.height / 20
    widthMargin = app.width / 8
    heightMargin = app.height / 20
    text = f"{app.color0} : {app.countColor0}\t{app.color1} : {app.countColor1}"
    canvas.create_text(widthCenter, heightCenter, text = text,
                       font = "Arial 28", anchor = "c")

def drawGameOver(app, canvas):
    canvas.create_rectangle(0, app.height / 3, app.width, app.height - app.height / 3,
                            fill = "green", outline = "black", width = 5)
    if(app.countColor0 > app.countColor1):
        text = f"{app.color0} Wins!!!\nPress 'r' to play again"
    elif(app.countColor0 < app.countColor1):
        text = f"{app.color1} Wins!!!\nPress 'r' to play again"
    else:
        text = "Tie!!\nPress'r' to play again"
    canvas.create_text(app.width / 2, app.height / 2, text = text,
                       font = "Arial 28", anchor = "c")

def home_redrawAll(app, canvas):
    drawHomePage(app, canvas)

def game_redrawAll(app, canvas):
    drawBoard(app, canvas)
    drawScore(app, canvas)
    drawLegalSquares(app, canvas)
    drawError(app, canvas)
    if(app.gameOver):
        drawGameOver(app, canvas)

def main():
    runApp(width = 600, height = 600)

main()
