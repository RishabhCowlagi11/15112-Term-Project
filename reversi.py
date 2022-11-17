    # Importing modules
from cmu_112_graphics import *
import board as Board
import chip as Chip
import button as Button

##################### APP STARTED #####################
def appStarted(app):
    app.mode = "home"

    app.baseColor = "gray"
    app.color0 = "white"
    app.color1 = "black"

    app.countColor0 = 2
    app.countColor1 = 2

    app.rows = 8
    app.cols = 8

    app.margin = 50
    app.boardWidth = app.width - app.margin * 2
    app.boardHeight = app.height - app.margin * 2

    app.playerTurn = 0

    app.gameBoardObject = Board.Board(app.rows, app.cols)
    app.gameBoard = app.gameBoardObject.getBoard()
    placeChipsOnBoard(app)
    
    app.timerDelay = 1000000000000000000

    updateLegalSquares(app)

    app.pause = False
    app.error = False

##################### USER INPUTS ######################
def game_mousePressed(app, event):
    rowWidth = app.boardHeight / app.rows 
    colWidth = app.boardWidth / app.cols
    
    # If clicked square is on board, get its row and col
    if(isOnBoardXY(app, event.x, event.y)):
        clickedRow = int((event.y - app.margin) / rowWidth)
        clickedCol = int((event.x - app.margin) / colWidth)


    # Checks if square is legal, then places chip and changes turn
    if(isOnBoardXY(app, event.x, event.y) and
    legalSquare(app, clickedRow, clickedCol, app.playerTurn)):
        app.gameBoardObject.updateGameBoard(clickedRow, clickedCol, app.playerTurn) 
        flipPieces(app, clickedRow, clickedCol, app.playerTurn)
        app.state, app.countColor0, app.countColor1 = getCounts(app)
        updateLegalSquares(app)
        if(app.playerTurn == 0):
            print("RUNNING MINIMAX.....")
            miniMax(app, 2)
            app.playerTurn = 1 - app.playerTurn
        app.playerTurn = 1 - app.playerTurn
    else:
        app.error = True

def game_mouseMoved(app, event):
    pass

def game_mouseReleased(app, event):
    app.error = False

def game_keyPressed(app, event):
    if(event.key == "p"):
        app.pause = not app.pause

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
def flipPieces(app, row, col, player):
    drow = [-1, 0, 1]
    dcol = [-1, 0, 1]
    for dr in drow:
        for dc in dcol:
            if(inDirection(app, row, col, dr, dc, player)):
                newRow, newCol = row + dr, col + dc
                while(app.gameBoard[newRow][newCol].getColor() == 1 - player):
                    app.gameBoardObject.updateGameBoard(newRow, newCol, player)
                    newRow += dr
                    newCol += dc

def miniMaxHelper(app):
    pass

# References
# https://en.wikipedia.org/wiki/Minimax
def miniMax(app, depth, isComputerTurn = True):
    print(f"MINIMAX DEPTH is {depth}")
    if(depth == 0):
        print(f"RETURNING getState(app) = {getState(app)}")
        return getState(app)
    updateLegalSquares(app)
    for i, j in app.legalSquares:
        if(isComputerTurn):
            print(f"PLACING FOR COMPUTER AT {(i, j)}")
            app.gameBoardObject.updateGameBoard(i, j, 1)
            app.gameBoardObject.displayBoard()
            updateLegalSquares(app)
        else:
            print(f"PLACING FOR HUMAN AT {(i, j)}")
            app.gameBoardObject.updateGameBoard(i, j, 0)
            updateLegalSquares(app)
        x = miniMax(app, depth - 1, not isComputerTurn)
        print(f"RETURNING max of {getState(app)} and {x}")
        return max(getState(app), x)
    

#################### STATE FUNCTIONS ####################
def game_timerFired(app):
    pass

def getCounts(app):
    state, countColor0, countColor1 = 0, 0, 0
    for i in range(app.rows):
        for j in range(app.cols):
            if(app.gameBoard[i][j].getColor() != None):
                if(app.gameBoard[i][j].getColor() == 0):
                    state -= 1
                    countColor0 += 1
                elif(app.gameBoard[i][j].getColor() == 1):
                    state += 1
                    countColor1 += 1

    return state, countColor0, countColor1

def getState(app):
    return getCounts(app)[0]

def updateLegalSquares(app):
    app.legalSquares = set()
    for i in range(app.rows):
        for j in range(app.cols):
            if(legalSquare(app, i, j, app.playerTurn)):
                app.legalSquares.add((i, j))

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
    if(x > app.margin and y > app.margin and 
       x < app.width - app.margin and y < app.height - app.margin):
        return True
    return False

def isOnBoardRowCol(app, row, col):
    if(0 <= row < app.rows and 0 <= col < app.cols):
        return True
    return False

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

def inDirection(app, row, col, drow, dcol, player):
    # Prevents Checking Same Square
    if((drow, dcol) == (0, 0)):
        return False

    # Checks Intro Condition for Entering Loop
    newRow, newCol = row + drow, col + dcol
    if(not isOnBoardRowCol(app, newRow, newCol)):
        return False

    # Loops in Direction while new Square is of Opposite Color
    # Return False if Loops outside of Board
    while(app.gameBoard[newRow][newCol].getColor() == 1 - player):
        if(isOnBoardRowCol(app, newRow + drow, newCol + dcol)):
            newRow += drow
            newCol += dcol
        else:
            return False

    # If the Square that Breaks out of Loop is None return False else True
    if(app.gameBoard[newRow][newCol].getColor() == None):
        return False
    return True

def inLine(app, row, col, player):
    drow = [-1, 0, 1]
    dcol = [-1, 0, 1]
    for dr in drow:
        for dc in dcol:
            if(inDirection(app, row, col, dr, dc, player) and
               app.gameBoard[row + dr][col + dc].getColor() == 1 - player):
                return True
    return False

def squareIsOpen(app, row, col):
    if(app.gameBoard[row][col].getColor() == None):
        return True
    return False

def legalSquare(app, row, col, player):
    if(squareIsOpen(app, row, col) and inLine(app, row, col, player)):
        return True
    return False

###################### DRAWING FUNCTIONS ######################
def drawError(app, canvas):
    if(app.error):
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
    for row, col in app.legalSquares:
        chip = Chip.Chip((row, col), outline = "tan", width = 5)
        chip.drawChip(app, canvas)

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

def home_redrawAll(app, canvas):
    drawHomePage(app, canvas)

def game_redrawAll(app, canvas):
    drawBoard(app, canvas)
    drawScore(app, canvas)
    drawError(app, canvas)
    drawLegalSquares(app, canvas)

def main():
    runApp(width = 600, height = 600)

main()
