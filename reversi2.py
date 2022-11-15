# Importing modules
from cmu_112_graphics import *
import board as Board
import chip as Chip
import button as Button

##################### APP STARTED #####################
def appStarted(app):
    app.mode = "game"

    app.baseColor = "gray"

    app.rows = 8
    app.cols = 8

    app.margin = 50
    app.boardWidth = app.width - app.margin * 2
    app.boardHeight = app.height - app.margin * 2

    app.gameBoard = Board.Board(app.rows, app.cols)
    app.gameBoard2 = Board.Board(app.rows, app.cols, boardColor = "pink", bgColor = "orange")

##################### USER INPUTS ######################
def game_mousePressed(app, event):
    pass

def game_mouseMoved(app, event):
    pass

def game_mouseReleased(app, event):
    pass

def home_keyPressed(app, event):
    if(event.key == "r"):
        appStarted(app)

def home_mousePressed(app, event):
    pass

def home_mouseMoved(app, event):
    pass

def home_mouseReleased(app, event):
    pass

#################### STATE FUNCTIONS ####################
def getCounts(app):
    pass

def updateLegalSquares(app):
    pass

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
    pass

def getIncrements(app):
    rowIncrement = app.boardHeight / app.rows
    colIncrement = app.boardWidth / app.cols
    return rowIncrement, colIncrement

def drawHomePage(app, canvas):
    pass

def drawLegalSquares(app, canvas):
    pass

def drawBoard(app, canvas):
    app.gameBoard.drawInitialBoard(app, canvas)

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
