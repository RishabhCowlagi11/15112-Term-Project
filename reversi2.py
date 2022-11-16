# Importing modules
from cmu_112_graphics import *
import board as Board
import chip as Chip
import button as Button

##################### APP STARTED #####################
def appStarted(app):
    app.mode = "game"

    app.baseColor = "gray"
    app.color0 = "white"
    app.color1 = "black"

    app.rows = 8
    app.cols = 8

    app.margin = 50
    app.boardWidth = app.width - app.margin * 2
    app.boardHeight = app.height - app.margin * 2

    app.playerTurn = 0

    app.gameBoardObject = Board.Board(app.rows, app.cols)
    app.gameBoard = app.gameBoardObject.getBoard()
    placeChipsOnBoard(app)

##################### USER INPUTS ######################
def game_mousePressed(app, event):
    player = Chip.Chip((6, 6), app.playerTurn)
    app.gameBoardObject.updateBoard(6, 6, player)
    app.playerTurn = 1 - app.playerTurn

def game_mouseMoved(app, event):
    pass

def game_mouseReleased(app, event):
    pass

def home_keyPressed(app, event):
    if(event.key == "r"):
        appStarted(app)

def home_mousePressed(app, event):
    print("ye", event.y)

def home_mouseMoved(app, event):
    pass

def home_mouseReleased(app, event):
    pass

#################### STATE FUNCTIONS ####################
def getCounts(app):
    pass

def updateLegalSquares(app):
    pass

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
            app.gameBoardObject.updateBoard(row, col, chip)
    app.gameBoardObject.displayBoard()      

################## CHECKING FUNCTIONS ###################
def isOnBoardXY(app, x, y):
    pass

def isOnBoardRowCol(app, row, col):
    pass

def is2PlayerButtonPressed(app, x, y):
    pass

def is1PlayerButtonPressed(app, x, y):
    pass

def inDirection(app, row, col, drow, dcol, player):
    pass

def inLine(app, row, col, player):
    pass

def squareIsOpen(app, row, col):
    pass

def legalSquare(app, row, col, player):
    pass

###################### DRAWING FUNCTIONS ######################
def drawError(app, canvas):
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
    pass

def drawBoard(app, canvas):
    app.gameBoardObject.drawBoard(app, canvas)
    app.gameBoardObject.drawChips(app, canvas)

def drawChip(app, canvas, row, col, color = "", outline = "", width = ""):
    pass

def drawChips(app, canvas):
    pass

def drawScore(app, canvas):
    pass

def home_redrawAll(app, canvas):
    pass

def game_redrawAll(app, canvas):
    drawBoard(app, canvas)

def main():
    runApp(width = 600, height = 600)

main()
