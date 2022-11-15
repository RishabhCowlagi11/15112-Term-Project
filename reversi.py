from cmu_112_graphics import *
import numpy as np
import chip as Chip
import board as Board
import button as Button

def make2DList(rows, cols):
    L = [([None] * cols) for i in range(rows)]
    return L

############### APP STARTED ###############
def appStarted(app):
    app.baseColor = "gray"
    app.color0 = "white"
    app.color1 = "black"

    app.state = 0
    app.countColor0 = 2
    app.countColor1 = 2

    app.mode = "home"
    app.currentPage = "home"
    app.gameMode = "pvp"

    app.rows = 8
    app.cols = 8
    app.margin = 50
    app.board = make2DList(app.rows, app.cols)
    
    app.boardWidth = app.width - app.margin * 2
    app.boardHeight = app.height - app.margin * 2

    app.Chips = {}
    createChips(app)

    app.playerTurn = 0
    app.state = 0
    app.error = False

    app.legalSquares = set()
    updateLegalSquares(app)

def game_appStarted(app):
    pass

###################### CHECKING FUNCTIONS ######################
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
    while(app.Chips[(newRow, newCol)].getColor() == 1 - player):
        if(isOnBoardRowCol(app, newRow + drow, newCol + dcol)):
            newRow += drow
            newCol += dcol
        else:
            return False

    # If the Square that Breaks out of Loop is None return False else True
    if(app.Chips[(newRow, newCol)].getColor() == None):
        return False
    return True

def inLine(app, row, col, player):
    drow = [-1, 0, 1]
    dcol = [-1, 0, 1]
    for dr in drow:
        for dc in dcol:
            if(inDirection(app, row, col, dr, dc, player) and
               app.Chips[(row + dr, col + dc)].getColor() == 1 - player):
                return True
    return False

def squareIsOpen(app, row, col):
    if(app.Chips[(row, col)].getColor() == None):
        return True
    return False

def legalSquare(app, row, col, player):
    if(squareIsOpen(app, row, col) and inLine(app, row, col, player)):
        return True
    return False

####################### STATE FUNCTIONS #######################
def getCounts(app):
    state, countColor0, countColor1 = 0, 0, 0
    for i in range(app.rows):
        for j in range(app.cols):
            if(app.Chips[(i, j)].getColor() != None):
                if(app.Chips[(i, j)].getColor() == 0):
                    state -= 1
                    countColor0 += 1
                elif(app.Chips[(i, j)].getColor() == 1):
                    state += 1
                    countColor1 += 1

    return state, countColor0, countColor1

def updateLegalSquares(app):
    app.legalSquares = set()
    for i in range(app.rows):
        for j in range(app.cols):
            if(legalSquare(app, i, j, app.playerTurn)):
                app.legalSquares.add((i, j))

# References
# https://en.wikipedia.org/wiki/Minimax
def miniMax(app):
    for row, col in app.legalSquares:
        pass

######################### USER INPUTS #########################
# If r is pressed, then the game reverts back to its inital state
def game_keyPressed(app, event):
    if(event.key == "r"):
        appStarted(app)

# Makes the buttons gray when the mouse is on them
def home_mouseMoved(app, event):
    if(is2PlayerButtonPressed(app, event.x, event.y)):
        pass
    elif(is1PlayerButtonPressed(app, event.x, event.y)):
        pass
    
def home_mousePressed(app, event):
    if(is2PlayerButtonPressed(app, event.x, event.y)):
        app.mode = "game"
        app.gameMode = "2"
    elif(is1PlayerButtonPressed(app, event.x, event.y)):
        app.mode = "game"
        app.gameMode = "1"

def game_mousePressed(app, event):
    if(app.gameMode == "2"):
        # Gets the row and col of the board that the mouse was clicked in
        rowWidth = app.boardHeight / app.rows 
        colWidth = app.boardWidth / app.cols
        
        # Check if clicked square is on the board
        if(isOnBoardXY(app, event.x, event.y)):
            clickedRow = int((event.y - app.margin) / rowWidth)
            clickedCol = int((event.x - app.margin) / colWidth)

        # Checks if square is legal, then places chip and changes turn
        if(isOnBoardXY(app, event.x, event.y) and
        legalSquare(app, clickedRow, clickedCol, app.playerTurn)):
            app.Chips[(clickedRow, clickedCol)].setColor(app.playerTurn)
            flipPieces(app, clickedRow, clickedCol, app.playerTurn)
            app.state, app.countColor0, app.countColor1 = getCounts(app)
            app.playerTurn = 1 - app.playerTurn
            updateLegalSquares(app)
        else:
            app.error = True

def game_mouseReleased(app, event):
    app.error = False

####################### UPDATE GAME #######################
def flipPieces(app, row, col, player):
    drow = [-1, 0, 1]
    dcol = [-1, 0, 1]
    for dr in drow:
        for dc in dcol:
            if(inDirection(app, row, col, dr, dc, player)):
                newRow, newCol = row + dr, col + dc
                while(app.Chips[(newRow, newCol)].getColor() != player and 
                      app.Chips[(newRow, newCol)].getColor() != None):
                    app.Chips[(newRow, newCol)].setColor(player)
                    newRow += dr
                    newCol += dc

def createChips(app):
    for row in range(len(app.board)):
        for col in range(len(app.board[0])):
            if((row, col) == (app.rows // 2, app.cols // 2) or
               (row, col) == (app.rows // 2 - 1, app.cols // 2 - 1)):
               chip = Chip.Chip((row, col), 0)
            elif((row, col) == (app.rows // 2 - 1, app.cols // 2) or 
                 (row, col) == (app.rows // 2, app.cols // 2 - 1)):
                chip = Chip.Chip((row, col), 1)
            else:
                chip = Chip.Chip((row, col), None)
            app.board[row][col] = chip
            app.Chips[(row, col)] = chip

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
        drawChip(app, canvas, row, col, outline = "tan", width = 5)

def drawBoard(app, canvas):
    canvas.create_rectangle(0, 0, app.width, app.height, fill = app.baseColor)

    rowIncrement, colIncrement = getIncrements(app)
    for row in range(app.rows):
        for col in range(app.cols):
            canvas.create_rectangle(colIncrement * col + app.margin,
                                    rowIncrement * row + app.margin, 
                                    colIncrement * (col + 1) + app.margin, 
                                    rowIncrement * (row + 1) + app.margin,
                                    fill = "green", outline = "black")

def drawChip(app, canvas, row, col, color = "", outline = "", width = ""):
    if(color == 0):
        color = app.color0
    elif(color == 1):
        color = app.color1  
    rowIncrement, colIncrement = getIncrements(app)
    margin = 5
    canvas.create_oval(app.margin + col * colIncrement + margin, 
                       app.margin + row * rowIncrement + margin,
                       app.margin + (col + 1) * colIncrement - margin,
                       app.margin + (row + 1) * rowIncrement - margin,
                       fill = color, outline = outline, width = width)


def drawChips(app, canvas):
    for row in range(len(app.board)):
        for col in range(len(app.board[0])):
            chip = app.board[row][col]
            if(chip.getColor() is not None):
                drawChip(app, canvas, row, col, chip.getColor(), width = 0)

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
    drawChips(app, canvas)
    drawLegalSquares(app, canvas)
    drawScore(app, canvas)
    drawError(app, canvas)

def main():
    runApp(width = 600, height = 600)

# main()