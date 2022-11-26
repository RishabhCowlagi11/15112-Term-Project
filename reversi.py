# Importing modules
from cmu_112_graphics import *
import copy, time
import board as Board
import chip as Chip
import button as Button
import gameplay as GamePlay

##################### APP STARTED #####################
def homeAppStarted(app):
    app.img = app.loadImage("oth.png")
    app.img2 = app.loadImage("othy.jpeg")

    app.verticalSpacing = app.height / 10 + 15

    # creates the buttons on the home page
    app.player2Button = Button.Button(app.width / 2, app.height / 2, 
                                      app.width / 2, app.height / 10,
                                      text = "2 Player Othello!!!")
    app.player1Button = Button.Button(app.width / 2, app.height / 2 + app.verticalSpacing,
                                      app.width / 2, app.height / 10,
                                      text = "1 Player Othello!!!")

    app.tournamentButton = Button.Button(app.width / 2, app.height / 2 + 2 * app.verticalSpacing,
                                         app.width / 2, app.height / 10,
                                         text = "Tournament Othello!!!")

    app.fontSize = int(app.width / 30)


def selectionAppStarted(app):
    app.gameButton = Button.Button(app.width - app.width / 10, app.height - app.height / 20,
                               app.width / 6, app.height / 20, text = "Go To Game",
                               textFont = "Arial 20")
    
    app.player1Left = Button.Button(app.width / 2 - app.width / 10,
                                    app.height / 2 - app.height / 6 + app.height / 10 + 20,
                                    app.width / 20, app.height / 30,
                                    direct = 1, text = "", outlineWidth = 1)

    app.player1Right = Button.Button(app.width / 2 + app.width / 10,
                                    app.height / 2 - app.height / 6 + app.height / 10 + 20,
                                    app.width / 20, app.height / 30,
                                    direct = -1, text = "", outlineWidth = 1)
    
    app.player2Left = Button.Button(app.width / 2 - app.width / 10,
                                    app.height / 2 + app.height / 5 + 20,
                                    app.width / 20, app.height / 30,
                                    direct = 1, text = "", outlineWidth = 1)

    app.player2Right = Button.Button(app.width / 2 + app.width / 10,
                                    app.height / 2 + app.height / 5 + 20,
                                    app.width / 20, app.height / 30,
                                    direct = -1, text = "", outlineWidth = 1)

def gameAppStarted(app):
    app.colors = ["White", "Black", "Green", "Blue", "Cyan", "Yellow", "Magenta",
                  "Purple", "Dark Blue", "Orange", "Dark Green"]
    # declare the default board and chip colors
    app.baseColor = "gray"
    # app.boardColor = rgbString(0, 146, 106)
    app.boardColor = "green"
    app.colorIndex0 = 0
    app.colorIndex1 = 1
    app.color0 = app.colors[0]
    app.color1 = app.colors[1]

    # declare the starting number of each chip
    app.countColor0 = 2
    app.countColor1 = 2

    # declare default board size
    app.rows = 8
    app.cols = 8

    # declare board dimensions
    app.marginWidthLeft = app.width / 24
    app.marginWidthRight = app.width / 24
    app.marginWidth = app.marginWidthLeft + app.marginWidthRight

    app.marginHeightTop = app.height / 15
    app.marginHeightBottom = app.height / 24
    app.marginHeight = app.marginHeightTop + app.marginHeightBottom

    app.boardWidth = app.width - app.marginWidth
    app.boardHeight = app.height - app.marginHeight

    # player 0 make first move
    app.playerTurn = 0

    # create the game board, place chips and get legal moves
    app.gameBoardObject = Board.Board(app.rows, app.cols)
    app.gameBoard = app.gameBoardObject.getBoard()
    placeChipsOnBoard(app)
    app.gameBoardObject.updateLegalSquares(app, app.playerTurn)

    app.lastPlayedRow = None
    app.lastPlayedCol = None

def appStarted(app):
    # game starts at home screen 
    app.mode = "home"

    homeAppStarted(app)
    selectionAppStarted(app)
    gameAppStarted(app)
    
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
        clickedRow = int((event.y - app.marginHeightTop) / rowWidth)
        clickedCol = int((event.x - app.marginWidthLeft) / colWidth)
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

def game_mouseReleased(app, event):
    app.error = False
    if(app.playerTurn == 1 and app.miniMax):
            depth = 1
            miniMax(app, depth, depth, app.gameBoard, app.gameBoardObject.getLegalSquares())
            app.state, app.countColor0, app.countColor1 = getCounts(app, app.gameBoard)

    if(len(app.gameBoardObject.getLegalSquares()) == 0):
        app.playerTurn = 1 - app.playerTurn
        app.gameBoardObject.updateLegalSquares(app, app.playerTurn)
        if(len(app.gameBoardObject.getLegalSquares()) == 0):
            app.gameOver = True

def game_keyPressed(app, event):
    if(event.key == "r"):
        appStarted(app)

def selection_mousePressed(app, event):
    if(app.gameButton.isPressedRectangle(event.x, event.y)):
        app.mode = "game"
    elif(app.player1Left.isPressedTriangle(event.x, event.y)):
        app.colorIndex0 -= 1
        app.colorIndex0 %= len(app.colors)
        if(app.colors[app.colorIndex0] == app.color1):
            app.colorIndex0 -= 1
            app.colorIndex0 %= len(app.colors)
        app.color0 = app.colors[app.colorIndex0]
    elif(app.player1Right.isPressedTriangle(event.x, event.y)):
        app.colorIndex0 += 1
        app.colorIndex0 %= len(app.colors)
        if(app.colors[app.colorIndex0] == app.color1):
            app.colorIndex0 += 1
            app.colorIndex0 %= len(app.colors)
        app.color0 = app.colors[app.colorIndex0]
    elif(app.player2Left.isPressedTriangle(event.x, event.y)):
        app.colorIndex1 -= 1
        app.colorIndex1 %= len(app.colors)
        if(app.colors[app.colorIndex1] == app.color0):
            app.colorIndex1 -= 1
            app.colorIndex1 %= len(app.colors)
        app.color1 = app.colors[app.colorIndex1]
    elif(app.player2Right.isPressedTriangle(event.x, event.y)):
        app.colorIndex1 += 1
        app.colorIndex1 %= len(app.colors)
        if(app.colors[app.colorIndex1] == app.color0):
            app.colorIndex1 += 1
            app.colorIndex1 %= len(app.colors)
        app.color1 = app.colors[app.colorIndex1]

def home_keyPressed(app, event):
    if(event.key == "r"):
        appStarted(app)

def home_mousePressed(app, event):
    if(app.player2Button.isPressedRectangle(event.x, event.y)):
        app.mode = "selection"
        app.miniMax = False
    elif(app.player1Button.isPressedRectangle(event.x, event.y)):
        app.mode = "selection"
        app.miniMax = True


##################### UPDATE GAME #######################
# References
# https://en.wikipedia.org/wiki/Minimax
# TA Lecture on Game AI
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
        time.sleep(0.3)
        app.gameBoardObject.updateGameBoard(app, move[0], move[1], 1)
        app.lastPlayedRow = move[0]
        app.lastPlayedCol = move[1]
        app.playerTurn = 0
    
    return boardScore

#################### STATE FUNCTIONS ####################
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
def isOnBoardXY(app, x, y):
    if(x > app.marginWidthLeft and y > app.marginHeightTop and 
       x < app.width - app.marginWidthRight and y < app.height - app.marginHeightBottom):
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

def drawSelectionPage(app, canvas):
    canvas.create_rectangle(0, 0, app.width, app.height, fill = app.boardColor)
    
    canvas.create_text(app.width / 2, app.height / 20, text = "Color Selection",
                       fill = "black", font = "Arial 36 bold underline", anchor = "c")

    # Draw the selection for player 1
    centerX = app.width / 2
    centerY = app.height / 2 - app.height / 6
    marginX = app.width / 8
    marginY = app.height / 10
    canvas.create_rectangle(centerX - marginX, centerY - marginY,
                            centerX + marginX, centerY + marginY, 
                            fill = app.color0, outline = "black", width = 5)

    canvas.create_text(centerX, centerY + marginY + 20, text = "Player 1",
                       font = "Arial 28 bold",  fill = "Black", anchor = "c")
    
    # Draw the selection for player 2
    centerY = app.height / 2 + app.height / 10
    canvas.create_rectangle(centerX - marginX, centerY - marginY,
                            centerX + marginX, centerY + marginY, 
                            fill = app.color1, outline = "black", width = 5)

    canvas.create_text(centerX, centerY + marginY + 20, text = "Player 2",
                       font = "Arial 28 bold", fill = "black", anchor = "c")

    app.gameButton.drawRectangleButton(app, canvas)

    app.player1Left.drawTriangleButton(app, canvas)
    app.player1Right.drawTriangleButton(app, canvas)

    app.player2Left.drawTriangleButton(app, canvas)
    app.player2Right.drawTriangleButton(app, canvas)



def drawHomePage(app, canvas):
    canvas.create_rectangle(0, 0, app.width, app.height, fill = "green")
    croppedImg = app.img.crop((170, 35, 860, 250))
    croppedImg = app.img2.crop((0, 30, 720, 205))
    canvas.create_image(app.width / 2, app.height / 2 - 225, image = ImageTk.PhotoImage(croppedImg))                   
    
    app.player2Button.drawRectangleButton(app, canvas)
    app.player1Button.drawRectangleButton(app, canvas)

    app.tournamentButton.drawRectangleButton(app, canvas)

def drawLegalSquares(app, canvas):
    app.gameBoardObject.drawLegalSquares(app, canvas)

def drawBoard(app, canvas):
    app.gameBoardObject.drawBoard(app, canvas)
    app.gameBoardObject.drawChips(app, canvas)

def drawScore(app, canvas):
    widthCenter = app.width / 2
    heightCenter = app.height / 22
    text = f"{app.color0} : {app.countColor0}\t\t{app.color1} : {app.countColor1}"
    canvas.create_text(widthCenter, heightCenter, text = text,
                       font = f"Arial {app.fontSize}", anchor = "c")

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

def selection_redrawAll(app, canvas):
    drawSelectionPage(app, canvas)

def main():
    runApp(width = 800, height = 800, title = "Othello")

main()
