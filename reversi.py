# Importing modules
from cmu_112_graphics import *
import copy, time, ast, random
import board as Board
import chip as Chip
from features import Button, Text, DrawBox
import gameplay as GamePlay
import draw as Draw
import numpy as np
import cv2
##################### APP STARTED #####################
def loginAppStarted(app):
    app.mainImage = app.loadImage("othy.jpeg")
    app.badNames = ["Player 1", "Player 2", "Computer"]

    app.loginButton = Button(app.width / 4, app.height / 2, 
                             app.width / 3, app.height / 10,
                             text = "LOGIN", textFont = "Arial 26 bold underline")

    app.signUpButton = Button(app.width - app.width / 4, app.height / 2,
                              app.width / 3, app.height / 10,
                              text = "SIGN UP", textFont = "Arial 26 bold underline")
    
    app.guestButton = Button(app.width / 2, app.height - app.height / 3,
                             app.width / 2, app.height / 10,
                             text = "Play as Guest",
                             textFont = "Arial 26 bold underline")

    app.loginBackButton = Button(app.width / 20, app.height / 30,
                                 app.width / 12, app.height / 20,
                                 text = "Back")

    app.loginButtons = [app.loginButton, app.signUpButton, app.guestButton,
                        app.loginBackButton]

def loginVerificationAppStarted(app):
    app.loginError = False
    app.userNameInput = Text(app.width - app.width / 3, app.height / 3,
                             app.width / 3, app.height / 10,
                             text = "")

    app.passwordInput = Text(app.width - app.width / 3, app.height / 2,
                             app.width / 3, app.height / 10,
                             text = "")

    app.submitLoginButton = Button(app.width / 2, app.height - app.height / 3,
                                   app.width / 2, app.height / 15, text = "Login!!")

    app.loginExitButton = Button(app.width / 10, app.height / 5,
                                 app.width / 20, app.height / 20,
                                 text = "X", bgColor = "white", fill = "red")

    app.loginVerificationButtons = [app.submitLoginButton]
    app.loginVerificationCircleButtons = [app.loginExitButton]

def signUpAppStarted(app):
    app.signUpTakenUser = False
    app.invalidPassword = False

    app.signUpName = Text(app.width - app.width / 3, app.height / 3,
                          app.width / 3, app.height / 12,
                          text = "")

    app.signUpUserName = Text(app.width - app.width / 3, app.height / 2,
                              app.width / 3, app.height / 12,
                              text = "")

    app.signUpPassword = Text(app.width - app.width / 3, app.height - app.height / 3,
                              app.width / 3, app.height / 12,
                              text = "")

    app.submitSignUpButton = Button(app.width / 2, app.height - app.height / 5.5,
                                    app.width / 2, app.height / 15, text = "Sign Up!!")

    app.signUpExitButton = Button(app.width / 10, app.height / 5,
                                  app.width / 20, app.height / 20,
                                  text = "X", bgColor = "white", fill = "red")

    app.signUpButtons = [app.submitSignUpButton]

def homeAppStarted(app):
    app.mainImage = app.loadImage("othy.jpeg")

    app.verticalSpacing = app.height / 10 + 15

    # creates the buttons on the home page
    app.player2Button = Button(app.width / 2, app.height / 2, 
                               app.width / 2, app.height / 10,
                               text = "2 Player Othello!!!")

    app.player1Button = Button(app.width / 2, app.height / 2 + app.verticalSpacing,
                               app.width / 2, app.height / 10,
                               text = "1 Player Othello!!!")

    app.profileButton = Button(app.width / 2, app.height / 2 + 2 * app.verticalSpacing,
                                  app.width / 2, app.height / 10,
                                  text = "Go To Profile!!!")

    app.homeBackButton = Button(app.width / 20, app.height / 30,
                                app.width / 12, app.height / 20,
                                text = "Back")

    app.homeButtons = [app.player2Button, app.player1Button, app.profileButton,
                       app.homeBackButton]

    app.fontSize = int(app.width / 30)

    app.drawErrorY = -1 * app.height / 12
    app.tellLogin = False
    app.flipDirection = False
    app.iteration1 = True

def confirmAppStarted(app):
    app.confirmButton = Button(app.width / 2, app.height - 13.5 * app.height / 36,
                               app.width / 5, app.height / 20, text = "Confirm")

    app.confirmExitButton = Button(13 * app.width / 36, 13.5 * app.height / 36,
                                   app.width / 15, app.height / 20, text = "X",
                                   bgColor = "white", fill = "red")

def selectionAppStarted(app):
    app.gameButton = Button(app.width - app.width / 10, app.height - app.height / 20,
                            app.width / 6, app.height / 20, text = "Go To Game",
                            textFont = "Arial 20")
    
    app.player1Left = Button(app.width / 2 - app.width / 8,
                             app.height / 2 - app.height / 6 + app.height / 10 + 20,
                             app.width / 20, app.height / 30,
                             direct = 1, text = "", outlineWidth = 1)

    app.player1Right = Button(app.width / 2 + app.width / 8,
                              app.height / 2 - app.height / 6 + app.height / 10 + 20,
                              app.width / 20, app.height / 30,
                              direct = -1, text = "", outlineWidth = 1)
    
    app.player2Left = Button(app.width / 2 - app.width / 8,
                             app.height / 2 + app.height / 5 + 20,
                             app.width / 20, app.height / 30,
                             direct = 1, text = "", outlineWidth = 1)

    app.player2Right = Button(app.width / 2 + app.width / 8,
                              app.height / 2 + app.height / 5 + 20,
                              app.width / 20, app.height / 30,
                              direct = -1, text = "", outlineWidth = 1)

    app.selectionBackButton = Button(app.width / 20, app.height / 30,
                                     app.width / 12, app.height / 20,
                                     text = "Back")


    app.easyButton = Button(app.width / 2 - app.width / 5,
                            app.height / 2 + app.height / 3,
                            app.width / 5, app.height / 15,
                            text = "Easy Mode")
    
    app.hardButton = Button(app.width / 2 + app.width / 5,
                            app.height / 2 + app.height / 3,
                            app.width / 5, app.height / 15,
                            text = "Hard Mode")

    app.selectionButtons = [app.gameButton, app.selectionBackButton,
                            app.easyButton, app.hardButton]

    app.selectionArrowButtons = [app.player1Left, app.player1Right, app.player2Left,
                                 app.player2Right]

def profileAppStarted(app):
    app.profileDraw = ""
    app.profileX = None
    app.profileY = None
    app.profileDrawing = False
    app.pixelSize = 5

    app.paletteIdx1 = 0
    app.paletteIdx2 = 1
    app.paletteIdx3 = 2

    img = cv2.imread("canvas.jpeg")
    scaledImg = cv2.resize(img, (app.width // 3, 2 * app.height // 5),
                                   interpolation = cv2.INTER_LINEAR)
    cv2.imwrite("default.jpg", scaledImg)

    app.image = Image.new("RGB", (app.width // 3, 2 * app.height // 5), (255, 255, 255))

    app.playerColorButton = DrawBox(app.width / 5, app.height / 3,
                                    app.width / 3, 2 * app.height / 5,
                                    text = "", bgColor = "")

    app.updateUserButton = Button(app.width / 5, 3 * app.height / 5 + app.height / 15,
                                  app.width / 4, app.height / 25,
                                  text = "Update Username")

    app.updatePassButton = Button(app.width / 5, 3 * app.height / 5 + 2 * app.height / 15,
                                  app.width / 4, app.height / 25,
                                  text = "Update Password")

    app.profileBackButton = Button(app.width / 20, app.height / 30,
                                   app.width / 12, app.height / 20,
                                   text = "Back")

    marginX = 45
    marginY = 30
    app.color1Button = Button(app.width / 5 - marginX, app.height / 3 - app.height / 5 - marginY,
                              app.width / 20, app.height / 20, text = "",
                              bgColor = app.colors[app.paletteIdx1], outlineWidth = 2)
        
    app.color2Button = Button(app.width / 5, app.height / 3 - app.height / 5 - marginY,
                              app.width / 20, app.height / 20, text = "",
                              bgColor = app.colors[app.paletteIdx2], outlineWidth = 2)
        
    app.color3Button = Button(app.width / 5 + marginX, app.height / 3 - app.height / 5 - marginY,
                              app.width / 20, app.height / 20, text = "",
                              bgColor = app.colors[app.paletteIdx3], outlineWidth = 2)

    app.colorLeft = Button(app.width / 5 - 2 * marginX, app.height / 3 - app.height / 5 - marginY,
                           app.width / 40, app.height / 40, text = "", direct = 1)
    
    app.colorRight = Button(app.width / 5 + 2 * marginX, app.height / 3 - app.height / 5 - marginY,
                            app.width / 40, app.height / 40, text = "", direct = -1)

    app.clearButton = Button(app.width / 5 + 3.5 * marginX, app.height / 3 - app.height / 5 - marginY,
                             app.height / 20, app.height / 20, text = "X",
                             outlineColor = "red", bgColor = "white", fill = "red")

    app.profileButtons = [app.updateUserButton, app.updatePassButton, app.profileBackButton]
    app.profileTriangleButtons = [app.colorLeft, app.colorRight]
    app.profileCircleButtons = [app.color1Button, app.color2Button, app.color3Button]

def updateUserAppStarted(app):
    app.updateUserInvalidPass = False
    app.newUserText = Text(app.width - app.width / 3, app.height / 3,
                                       app.width / 3, app.height / 10,
                                       text = "")

    app.userPasswordConfirm = Text(app.width - app.width / 3, app.height / 2,
                                    app.width / 3, app.height / 10,
                                    text = "")

    app.updateUserSubmitButton = Button(app.width / 2, app.height - app.height / 3,
                                        app.width / 2, app.height / 15, text = "Update Username!")

    app.updateUserExitButton = Button(app.width / 10, app.height / 5,
                                      app.width / 20, app.height / 20,
                                      text = "X", bgColor = "white", fill = "red")

def updatePassAppStarted(app):
    app.updatePassInvalidPass = False
    app.updatePassWrongPass = False
    app.passwordConfirmText = Text(app.width - app.width / 3, app.height / 3,
                                   app.width / 3, app.height / 10,
                                   text = "")

    app.newPassText = Text(app.width - app.width / 3, app.height / 2,
                           app.width / 3, app.height / 10,
                           text = "")

    app.updatePassSubmitButton = Button(app.width / 2, app.height - app.height / 3,
                                        app.width / 2, app.height / 15, text = "Update Password!")

    app.updatePassExitButton = Button(app.width / 10, app.height / 5,
                                      app.width / 20, app.height / 20,
                                      text = "X", bgColor = "white", fill = "red")

def gameAppStarted(app):
    app.colors = ["White", "Black", "Green", "Blue", "Cyan", "Yellow", "Magenta",
                  "Purple", "Orange", "Gold", "Lavender", "Maroon"]
    # declare the default board and chip colors
    app.baseColor = "gray"

    # app.gameBoardState = "2d"

    app.boardColorDark = "green"
    app.boardColorLight = "chartreuse4"
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
    app.marginWidthRight = app.width / 4
    app.marginWidth = app.marginWidthLeft + app.marginWidthRight

    app.marginHeightTop = app.height / 15
    app.marginHeightBottom = app.height / 24
    app.marginHeight = app.marginHeightTop + app.marginHeightBottom

    app.boardWidth = app.width - app.marginWidth
    app.boardHeight = app.height - app.marginHeight

    # Sets the number of players playing
    app.playerCount = 1
    app.player1Login = False
    app.player2Login = False
    app.player1Name = "Player 1"
    app.player2Name = "Computer"
    app.winner = None
    app.loser = None

    # player 0 make first move
    app.playerTurn = 0
    app.computerTurn = False

    # create the game board, place chips and get legal moves
    app.gameBoardObject = Board.Board(app.rows, app.cols)
    app.gameBoard = app.gameBoardObject.getBoard()
    placeChipsOnBoard(app)
    app.gameBoardObject.updateLegalSquares(app, app.playerTurn)

    app.helpButton = Button(app.width - app.width / 25, app.height / 20,
                            app.width / 8, app.height / 15,
                            text = "?", bgColor = "white", fill = "black",
                            textFont = f"Arial {app.fontSize} bold")

    app.placedRow = None
    app.placedCol = None
    app.lastPlayedRow = None
    app.lastPlayedCol = None
    app.hoverRow = None
    app.hoverCol = None
    app.legalSquareRowThick = None
    app.legalSquareColThick = None

    app.rx = 0
    app.ry = 0
    app.placeIncrements = 5
    app.rxIncrement = app.boardWidth / (app.placeIncrements * app.cols * 2)
    app.ryIncrement = app.boardHeight / (app.placeIncrements * app.rows * 2)

    app.flipPieces = []
    app.pieceFlip = False
    app.flipIncrements = 5
    app.dcol = 0

    app.miniMaxDepth = 1

    app.gameButtons = [app.helpButton]

def gameIsometricAppStarted(app):
    app.diff = app.boardWidth / 3
    app.diff2 = 50

    app.p1 = (app.marginWidthLeft + app.diff, app.marginHeightTop + app.diff2)
    app.p2 = (app.marginWidthLeft + app.boardWidth, app.marginHeightTop + app.diff)
    app.p3 = (app.marginWidthLeft + app.boardWidth - app.diff, app.marginHeightTop + app.boardHeight - app.diff2)
    app.p4 = (app.marginWidthLeft, app.marginHeightTop + app.boardHeight - app.diff)

    app.slope1_2 = (app.p1[1] - app.p2[1]) / (app.p1[0] - app.p2[0])
    app.slope1_4 = (app.p1[1] - app.p4[1]) / (app.p1[0] - app.p4[0])
    app.slope2_3 = (app.p2[1] - app.p3[1]) / (app.p2[0] - app.p3[0])
    app.slope3_4 = (app.p3[1] - app.p4[1]) / (app.p3[0] - app.p4[0])

    app.slope1Increment2 = (app.p2[0] - app.p1[0]) / app.cols
    app.slope2Increment2 = (app.p4[0] - app.p1[0]) / app.rows

def helpAppStarted(app):
    app.slide1 = True
    app.timerDelay = 1500
    app.helpExitButton = Button(app.width / 200 + app.width / 30,
                                app.height / 10 + app.height / 23,
                                app.width / 15, app.height / 15, text = "X",
                                fill = "red", bgColor = "white",
                                textFont = "Arial 36 bold")

    app.helpButtons = [app.helpExitButton]

def appStarted(app):
    # game starts at login screen 
    app.mode = "login"
    app.users = ast.literal_eval(readFile("userAndPass.txt"))

    homeAppStarted(app)
    gameAppStarted(app)
    loginAppStarted(app)
    loginVerificationAppStarted(app)
    profileAppStarted(app)
    updateUserAppStarted(app)
    updatePassAppStarted(app)
    signUpAppStarted(app)
    confirmAppStarted(app)
    selectionAppStarted(app)
    gameIsometricAppStarted(app)
    helpAppStarted(app)
    
    # Boolean State Variables
    app.gameOver = False
    app.error = False
    app.miniMax = True
    app.tie = False
    app.end = None

####################### BASIC IO #######################
def readFile(path):
    with open(path, "rt") as f:
        return f.read()

def writeFile(path, contents):
    with open(path, "wt") as f:
        f.write(contents)

##################### TIMER FIRED #####################
def game_timerFired(app):
    app.timerDelay = 50
    if(app.gameBoardObject.isGameOver(app, app.playerTurn)):
        gameEnding(app)
    elif(app.gameBoardObject.noMoreMovesPlayer(app.playerTurn)):
        app.playerTurn = 1 - app.playerTurn
        app.gameBoardObject.updateLegalSquares(app, app.playerTurn)
    elif(app.pieceFlip):
        app.mode = "gameAnimationPlace"
    if(app.playerTurn == 1 and app.miniMax and app.computerTurn):
        miniMax2(app, app.miniMaxDepth, app.miniMaxDepth, app.gameBoardObject,
                 app.gameBoardObject.getLegalSquares())
        app.computerTurn = False
    app.state, app.countColor0, app.countColor1 = getCounts(app, app.gameBoard)

def gameIsometric_timerFired(app):
    if(app.placedRow != None and app.placedCol != None):
        app.gameBoardObject.updateGameBoard(app, app.placedRow, 
                                            app.placedCol, 1 - app.playerTurn)
        app.lastPlayedRow = app.placedRow
        app.lastPlayedCol = app.placedCol
        app.placedRow, app.placedCol = None, None
    for row, col in app.flipPieces:
        app.gameBoard[row][col].setColor(1 - app.playerTurn)
    app.gameBoardObject.updateLegalSquares(app, app.playerTurn)
    app.flipPieces = []
    app.computerTurn = True
    game_timerFired(app)

def home_timerFired(app):
    app.timerDelay = 50
    if(app.tellLogin):
        if(app.drawErrorY < app.height / 25 and not app.flipDirection):
            app.drawErrorY += app.height / 50
        else:
            app.flipDirection = True
        if(app.drawErrorY > 0 and app.flipDirection and app.iteration1):
            time.sleep(1)
            app.drawErrorY -= app.height / 50
            app.iteration1 = False
        elif(app.drawErrorY > 0 and app.flipDirection):
            app.drawErrorY -= app.height / 50
        elif(app.flipDirection):
            app.drawError = -1 * app.height / 12
            app.tellLogin = False
            app.flipDirection = False
            app.iteration1 = True

def gameAnimationPlace_timerFired(app):
    app.timerDelay = 25
    rowIncrement = app.boardHeight / app.rows
    colIncrement = app.boardWidth / app.cols
    if(app.rx + 15 < colIncrement or app.ry + 15 < rowIncrement):
        app.rx += app.rxIncrement
        app.ry += app.ryIncrement
    else:
        app.gameBoardObject.updateGameBoard(app, app.placedRow, 
                                            app.placedCol, 1 - app.playerTurn)
        app.lastPlayedRow = app.placedRow
        app.lastPlayedCol = app.placedCol
        app.rx = 0
        app.ry = 0
        app.mode = "gameAnimationFlip"

def gameAnimationFlip_timerFired(app):
    app.timerDelay = 100
    for row, col in app.flipPieces:
            app.gameBoard[row][col].setColor(None)
    app.dcol += app.boardWidth / (app.cols * app.flipIncrements)
    if(app.dcol + 2 >= app.boardWidth / app.cols):
        for row, col in app.flipPieces:
            app.gameBoard[row][col].setColor(1 - app.playerTurn)
        app.gameBoardObject.updateLegalSquares(app, app.playerTurn)
        app.dcol = 0
        app.pieceFlip = False
        app.mode = "game"
        if(app.playerTurn == 1):
            app.computerTurn = True

def help_timerFired(app):
    app.timerDelay = 1500
    app.slide1 = not app.slide1
##################### USER INPUTS ######################
def help_mousePressed(app, event):
    if(app.helpExitButton.isPressedCircle(event.x, event.y)):
        app.mode = app.prevScreen

def game_mousePressed(app, event):
    if(app.dcol + 2 <= app.boardWidth / app.cols and app.pieceFlip):
        return
    rowWidth = app.boardHeight / app.rows 
    colWidth = app.boardWidth / app.cols
    if(app.helpButton.isPressedCircle(event.x, event.y)):
        app.mode = "help"
        app.prevScreen = "game"
    
    # If clicked square is on board, get its row and col
    if(isOnBoardXY2d(app, event.x, event.y)):
        clickedRow = int((event.y - app.marginHeightTop) / rowWidth)
        clickedCol = int((event.x - app.marginWidthLeft) / colWidth)
    else:
        return

    # Checks if square is legal, then places chip and changes turn
    if(isOnBoardXY2d(app, event.x, event.y) and
       GamePlay.GamePlay.legalSquare(app, app.gameBoard, clickedRow, clickedCol, app.playerTurn)):
        app.placedRow, app.placedCol = clickedRow, clickedCol
        app.pieceFlip = True

        # app.state, app.countColor0, app.countColor1 = getCounts(app, app.gameBoard)
        
        app.playerTurn = 1 - app.playerTurn       
        updatePlayerOutline(app)
    else:
        app.error = True

def game_mouseMoved(app, event):
    if(isOnBoardXY2d(app, event.x, event.y)):
        rowWidth = app.boardHeight / app.rows 
        colWidth = app.boardWidth / app.cols
        app.hoverRow = int((event.y - app.marginHeightTop) / rowWidth)
        app.hoverCol = int((event.x - app.marginWidthLeft) / colWidth)
        if((app.hoverRow, app.hoverCol) in app.gameBoardObject.getLegalSquares()):
            app.legalSquareRowThick = app.hoverRow
            app.legalSquareColThick = app.hoverCol
        else:
            app.legalSquareRowThick = None
            app.legalSquareColThick = None
    else:
        app.hoverRow = None
        app.hoverCol = None

def gameIsometric_mousePressed(app, event):
    if(app.helpButton.isPressedCircle(event.x, event.y)):
        app.mode = "help"
        app.prevScreen = "gameIsometric"
    if(not isOnBoardXYIsometric(app, event.x, event.y)):
        return

    clickedRow, clickedCol = getRowColIsometric(app, event.x, event.y)
    if(GamePlay.GamePlay.legalSquare(app, app.gameBoard, clickedRow, clickedCol, app.playerTurn)):
        app.lastPlayedRow, app.lastPlayedCol = clickedRow, clickedCol
        app.gameBoardObject.updateGameBoard(app, clickedRow, clickedCol, app.playerTurn)

        app.state, app.countColor0, app.countColor1 = getCounts(app, app.gameBoard)

        app.playerTurn = 1 - app.playerTurn
        updatePlayerOutline(app)
    else:
        app.error = True

def gameIsometric_mouseReleased(app, event):
    app.error = False

def gameIsometric_mouseMoved(app, event):
    if(isOnBoardXYIsometric(app, event.x, event.y)):
        app.hoverRow, app.hoverCol = getRowColIsometric(app, event.x, event.y)
        if((app.hoverRow, app.hoverCol) in app.gameBoardObject.getLegalSquares()):
            app.legalSquareRowThick = app.hoverRow
            app.legalSquareColThick = app.hoverCol
        else:
            app.legalSquareRowThick = None
            app.legalSquareColThick = None
    else:
        app.hoverRow = None
        app.hoverCol = None

def updatePlayerOutline(app):
    if(app.playerTurn == 1):
        app.player2TurnButton.updateIsClicked(True)
        app.player1TurnButton.updateIsClicked(False)
    else:
        app.player1TurnButton.updateIsClicked(True)
        app.player2TurnButton.updateIsClicked(False)  

    app.player1TurnButton.updateOutline()
    app.player2TurnButton.updateOutline()

def game_mouseReleased(app, event):
    app.error = False

def game_keyPressed(app, event):
    if(event.key == "r" and not app.gameOver):
        app.mode = "confirm"
        app.prevScreen = "game"
    elif(event.key == "i"):
        app.mode = "gameIsometric"
    elif(event.key == "r" and app.gameOver):
        appStarted(app)
    
def gameIsometric_keyPressed(app, event):
    if(event.key == "i"):
        app.mode = "game"
    elif(event.key == "r" and not app.gameOver):
        app.mode = "confirm"
        app.prevScreen = "gameIsometric"
    elif(event.key == "r"):
        appStarted(app)

def declarePlayerButtons(app):
    app.mode = "game"
    app.timerDelay = 50
    colorFill0, colorFill1 = "black", "black"
    if(app.color0 == "Black" or app.color0.find("Dark") != -1):
        colorFill0 = "white"
    if(app.color1 == "Black" or app.color1.find("Dark") != -1):
        colorFill1 = "white"
    
    app.badNames = ["Player 1", "Player 2", "Computer"]
    if(app.player1Name in app.badNames):
        app.player1TurnButton = Text(app.width - app.marginWidthRight / 2, 
                                    app.height / 3, app.marginWidthRight / 1.2, 
                                    app.height / 4, text = app.player1Name, 
                                    bgColor = app.color0, fill = colorFill0,
                                    textFont = "Arial 26 bold underline")
    else:
        imgName = app.users[app.player1Name]["pic"]
        img = app.loadImage(imgName)
        img2 = app.scaleImage(img, 15/24)
        app.player1TurnButton = Text(app.width - app.marginWidthRight / 2, 
                                    app.height / 3,app.marginWidthRight / 1.2, 
                                    app.height / 4, text = app.player1Name, 
                                    bgColor = app.color0, fill = colorFill0,
                                    image = img2, textFont = "Arial 26 bold underline")
    
    if(app.player2Name in app.badNames):
        app.player2TurnButton = Text(app.width - app.marginWidthRight / 2, 
                                        app.height - app.height / 3,
                                        app.marginWidthRight / 1.2, app.height / 4,
                                        text = app.player2Name, bgColor = app.color1,
                                        fill = colorFill1, textFont = "Arial 26 bold underline")
    else:
        imgName = app.users[app.player2Name]["pic"]
        img = app.loadImage(imgName)
        img2 = app.scaleImage(img, 15/24)
        app.player2TurnButton = Text(app.width - app.marginWidthRight / 2, 
                                    2 * app.height / 3, app.marginWidthRight / 1.2, 
                                    app.height / 4, text = app.player2Name, 
                                    bgColor = app.color1, fill = colorFill1,
                                    image = img2, textFont = "Arial 26 bold underline")

    app.player1TurnButton.updateIsClicked(True)
    app.player1TurnButton.updateOutline()

def selection_mousePressed(app, event):
    if(app.gameButton.isPressedRectangle(event.x, event.y)):
        declarePlayerButtons(app)
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
    elif(app.selectionBackButton.isPressedRectangle(event.x, event.y)):
        app.mode = "home"
    elif(app.easyButton.isPressedRectangle(event.x, event.y) and app.player2Name == "Computer"):
        app.miniMaxDepth = -1
        app.mode = "game"
        declarePlayerButtons(app)
    elif(app.hardButton.isPressedRectangle(event.x, event.y) and app.player2Name == "Computer"):
        app.miniMaxDepth = 3
        app.mode = "game"
        declarePlayerButtons(app)

def selection_mouseMoved(app, event):
    for button in app.selectionButtons:
        if(button.isPressedRectangle(event.x, event.y)):
            button.updateColor("dark gray")
        else:
            button.updateColor("gray")
    
    for arrow in app.selectionArrowButtons:
        if(arrow.isPressedTriangle(event.x, event.y)):
            arrow.updateColor("dark gray")
        else:
            arrow.updateColor("gray")

def confirm_mouseMoved(app, event):
    if(app.confirmButton.isPressedRectangle(event.x, event.y)):
        app.confirmButton.updateColor = "dark gray"
    else:
        app.confirmButton.updateColor = "gray"
    
    if(app.confirmExitButton.isPressedCircle(event.x, event.y)):
        app.confirmExitButton.updateColor = "gray75"
    else:
        app.confirmExitButton.updateColor = "white"

def confirm_mousePressed(app, event):
    app.badNames = ["Player 1", "Player 2", "Computer"]
    if(app.confirmButton.isPressedRectangle(event.x, event.y)):
        if(app.playerTurn == 0):
            if(app.player1Name not in app.badNames):
                loser = app.player1Name
            else:
                loser = None
            if(app.player2Name not in app.badNames):
                winner = app.player2Name
            else:
                winner = None
        else:
            if(app.player1Name not in app.badNames):
                winner = app.player1Name
            else:
                winner = None
            if(app.player2Name not in app.badNames):
                loser = app.player2Name
            else:
                loser = None

        if(loser != None):
            app.users[loser]["played"] += 1
        if(winner != None):
            app.users[winner]["played"] += 1
            app.users[winner]["wins"] += 1
        appStarted(app)
    elif(app.confirmExitButton.isPressedCircle(event.x, event.y)):
        app.mode = app.prevScreen

def profile_mousePressed(app, event):
    if(app.updateUserButton.isPressedRectangle(event.x, event.y)):
        app.mode = "updateUser"
    elif(app.updatePassButton.isPressedRectangle(event.x, event.y)):
        app.mode = "updatePass"
    elif(app.profileBackButton.isPressedRectangle(event.x, event.y)):
        name = app.users[app.player1Name]["pic"]
        updatedImg = cv2.cvtColor(np.array(app.img), cv2.COLOR_RGB2BGR)
        cv2.imwrite(name, updatedImg)
        writeFile("userAndPass.txt", repr(app.users))
        app.mode = "home"
    elif(app.color1Button.isPressedCircle(event.x, event.y)):
        app.playerColorButton.updateColor(app.colors[app.paletteIdx1])
    elif(app.color2Button.isPressedCircle(event.x, event.y)):
        app.playerColorButton.updateColor(app.colors[app.paletteIdx2])
    elif(app.color3Button.isPressedCircle(event.x, event.y)):
        app.playerColorButton.updateColor(app.colors[app.paletteIdx3])
    elif(app.colorLeft.isPressedTriangle(event.x, event.y)):
        app.paletteIdx1 += 1
        app.paletteIdx2 += 1
        app.paletteIdx3 += 1
        if(app.paletteIdx1 >= len(app.colors)):
            app.paletteIdx1 %= len(app.colors)
        elif(app.paletteIdx2 >= len(app.colors)):
            app.paletteIdx2 %= len(app.colors)
        elif(app.paletteIdx3 >= len(app.colors)):
            app.paletteIdx3 %= len(app.colors)
    elif(app.colorRight.isPressedTriangle(event.x, event.y)):
        app.paletteIdx1 -= 1
        app.paletteIdx2 -= 1
        app.paletteIdx3 -= 1
        if(app.paletteIdx1 < 0):
            app.paletteIdx1 %= len(app.colors)
        elif(app.paletteIdx2 < 0):
            app.paletteIdx2 %= len(app.colors)
        elif(app.paletteIdx3 < 0):
            app.paletteIdx3 %= len(app.colors)
    elif(app.clearButton.isPressedRectangle(event.x, event.y)):
        app.img = app.loadImage("default.jpg")
        
    
    app.color1Button.updateColor(app.colors[app.paletteIdx1])
    app.color2Button.updateColor(app.colors[app.paletteIdx2])
    app.color3Button.updateColor(app.colors[app.paletteIdx3])


def profile_mouseDragged(app, event):
    if(app.playerColorButton.isPressedRectangle(event.x, event.y)):
        app.timerDelay = 10
        app.drawingX = event.x
        app.drawingY = event.y
        app.playerColorButton.updateDrawing(app, event.x, event.y)

def profile_mouseMoved(app, event):
    sideLen = app.width / 2
    app.profileX = event.x
    app.profileY = event.y
    if(app.winsButton.isPressedArc(event.x, event.y)):
        app.winsButton.updateLens(sideLen + 40)
        app.lossButton.updateLens(sideLen)
        app.tieButton.updateLens(sideLen)
        app.profileDraw = "win"
    elif(app.lossButton.isPressedArc(event.x, event.y)):
        app.lossButton.updateLens(sideLen + 40)
        app.winsButton.updateLens(sideLen)
        app.tieButton.updateLens(sideLen)
        app.profileDraw = "loss"
    elif(app.tieButton.isPressedArc(event.x, event.y)):
        app.tieButton.updateLens(sideLen + 40)
        app.winsButton.updateLens(sideLen)
        app.lossButton.updateLens(sideLen)
        app.profileDraw = "tie"  
    else:
        app.lossButton.updateLens(sideLen)
        app.winsButton.updateLens(sideLen)
        app.tieButton.updateLens(sideLen)
        app.profileDraw = ""
    
    for button in app.profileButtons:
        if(button.isPressedRectangle(event.x, event.y)):
            button.updateColor("dark gray")
        else:
            button.updateColor("gray")
    
    if(app.clearButton.isPressedRectangle(event.x, event.y)):
        app.clearButton.updateColor("gray80")
    else:
        app.clearButton.updateColor("white")

    for button in app.profileTriangleButtons:
        if(button.isPressedTriangle(event.x, event.y)):
            button.updateColor("dark gray")
        else:
            button.updateColor("gray")
    
    for button in app.profileCircleButtons:
        if(button.isPressedCircle(event.x, event.y)):
            button.updateOutline("red")
        else:
            button.updateOutline("black")

def updateUser_mouseMoved(app, event):
    if(app.updateUserSubmitButton.isPressedRectangle(event.x, event.y)):
        app.updateUserSubmitButton.updateColor("dark gray")
    else:
        app.updateUserSubmitButton.updateColor("gray")

    if(app.updateUserExitButton.isPressedCircle(event.x, event.y)):
        app.updateUserExitButton.updateColor("gray75")
    else:
        app.updateUserExitButton.updateColor("white")

def updateUser_keyPressed(app, event):
    if(app.newUserText.getIsClicked()):
        action = getAction(event.key)
        if(isinstance(action, bool)):
            app.newUserText.updateIsClicked(action)
        else:
            app.newUserText.updateText(action)
    elif(app.userPasswordConfirm.getIsClicked()):
        action = getAction(event.key)
        if(isinstance(action, bool)):
            app.userPasswordConfirm.updateIsClicked(action)
        else:
            app.userPasswordConfirm.updateText(action)

def updateUser_mousePressed(app, event):
    if(app.newUserText.isPressedRectangle(event.x, event.y)):
        app.newUserText.updateIsClicked(True)
        app.userPasswordConfirm.updateIsClicked(False)
    elif(app.userPasswordConfirm.isPressedRectangle(event.x, event.y)):
        app.userPasswordConfirm.updateIsClicked(True)
        app.newUserText.updateIsClicked(False)
    elif(app.updateUserExitButton.isPressedCircle(event.x, event.y)):
        app.mode = "profile"
        clearTextBoxes(app)
    elif(app.updateUserSubmitButton.isPressedRectangle(event.x, event.y)):
        newUser = app.newUserText.getText()
        password = app.userPasswordConfirm.getText()
        if(password == app.users[app.player1Name]["password"]):
            app.users[newUser] = app.users[app.player1Name]
            del app.users[app.player1Name]
            app.player1Name = newUser
            writeFile("userAndPass.txt", repr(app.users))
            app.updateUserInvalidPass = False
            app.mode = "profile"
        else:
            app.updateUserInvalidPass = True

def updatePass_mouseMoved(app, event):
    if(app.updatePassSubmitButton.isPressedRectangle(event.x, event.y)):
        app.updatePassSubmitButton.updateColor("dark gray")
    else:
        app.updatePassSubmitButton.updateColor("gray")

    if(app.updatePassExitButton.isPressedCircle(event.x, event.y)):
        app.updatePassExitButton.updateColor("gray75")
    else:
        app.updatePassExitButton.updateColor("white")

def updatePass_keyPressed(app, event):
    if(app.passwordConfirmText.getIsClicked()):
        action = getAction(event.key)
        if(isinstance(action, bool)):
            app.passwordConfirmText.updateIsClicked(action)
        else:
            app.passwordConfirmText.updateText(action)
    elif(app.newPassText.getIsClicked()):
        action = getAction(event.key)
        if(isinstance(action, bool)):
            app.newPassText.updateIsClicked(action)
        else:
            app.newPassText.updateText(action)

def updatePass_mousePressed(app, event):
    if(app.passwordConfirmText.isPressedRectangle(event.x, event.y)):
        app.passwordConfirmText.updateIsClicked(True)
        app.newPassText.updateIsClicked(False)
    elif(app.newPassText.isPressedRectangle(event.x, event.y)):
        app.newPassText.updateIsClicked(True)
        app.passwordConfirmText.updateIsClicked(False)
    elif(app.loginExitButton.isPressedCircle(event.x, event.y)):
        app.mode = "profile"
        clearTextBoxes(app)
    elif(app.submitLoginButton.isPressedRectangle(event.x, event.y)):
        password = app.passwordConfirmText.getText()
        newPass = app.newPassText.getText()
        if(password == app.users[app.player1Name]["password"]):
            if(isValidPassword(app, newPass)):
                app.users[app.player1Name]["password"] = newPass
                writeFile("userAndPass.txt", repr(app.users))
                app.mode = "profile"
                app.updatePassInvalidPass = False
                app.updatePassWrongPass = False
            else:
                app.updatePassInvalidPass = True
        else:
            app.updatePassWrongPass = True

def home_keyPressed(app, event):
    if(event.key == "r"):
        app.mode = "confirm"
        app.prevScreen = "home"

def home_mousePressed(app, event):
    if(app.player2Button.isPressedRectangle(event.x, event.y)):
        app.playerCount = 2
        app.player2Name = "Player 2"
        app.mode = "login"
        app.miniMax = False
    elif(app.player1Button.isPressedRectangle(event.x, event.y)):
        app.mode = "selection"
        app.playerCount = 1
        app.miniMax = True
    elif(app.homeBackButton.isPressedRectangle(event.x, event.y)):
        app.mode = "login"
    elif(app.profileButton.isPressedRectangle(event.x, event.y)):
        if(app.player1Login):
            Draw.Profile.createStatsButtons(app)
            app.mode = "profile"
            name = app.users[app.player1Name]["pic"]
            app.img = app.loadImage(name)
        else:
            app.tellLogin = True

def home_mouseMoved(app, event):
    for button in app.homeButtons:
        if(button.isPressedRectangle(event.x, event.y)):
            button.updateColor("dark gray")
        else:
            button.updateColor("gray")

def clearTextBoxes(app):
    textBoxes = [app.userNameInput, app.passwordInput, app.signUpName, 
                 app.signUpUserName, app.signUpPassword, app.newUserText,
                 app.userPasswordConfirm, app.passwordConfirmText, app.newPassText]

    for text in textBoxes:
        text.clearText()

def loginVerify_mouseMoved(app, event):
    for button in app.loginVerificationButtons:
        if(button.isPressedRectangle(event.x, event.y)):
            button.updateColor("dark gray")
        else:
            button.updateColor("gray")

    for button in app.loginVerificationCircleButtons:
        if(button.isPressedCircle(event.x, event.y)):
            button.updateColor("gray64")
        else:
            button.updateColor("white")


def loginVerify_mousePressed(app, event):
    if(app.userNameInput.isPressedRectangle(event.x, event.y)):
        app.userNameInput.updateIsClicked(True)
        app.passwordInput.updateIsClicked(False)
    elif(app.passwordInput.isPressedRectangle(event.x, event.y)):
        app.passwordInput.updateIsClicked(True)
        app.userNameInput.updateIsClicked(False)
    elif(app.loginExitButton.isPressedCircle(event.x, event.y)):
        app.mode = "login"
        clearTextBoxes(app)
    elif(app.submitLoginButton.isPressedRectangle(event.x, event.y)):
        user = app.userNameInput.getText()
        password = app.passwordInput.getText()
        app.users = ast.literal_eval(readFile("userAndPass.txt"))
        if(user in app.users and password == app.users[user]["password"]):
            if(app.playerCount == 2):
                if(user == app.player1Name):
                    app.loginError = True
                else:
                    app.mode = "selection"
                    app.player2Name = user
                    app.player2Login = True
            else:
                app.mode = "home"
                app.player1Name = user
                app.player1Login = True
        else:
            app.loginError = True

        clearTextBoxes(app)
    else:
        app.userNameInput.updateIsClicked(False)
        app.passwordInput.updateIsClicked(False)


def getAction(event):
    if(len(event) == 1):
        return event
    elif(event == "Space"):
        return " "
    elif(event == "BackSpace"):
        return -1
    elif(event == "Return" or event == "Enter"):
        return False
    else:
        return ""

def loginVerify_keyPressed(app, event):
    if(app.userNameInput.getIsClicked()):
        action = getAction(event.key)
        if(isinstance(action, bool)):
            app.userNameInput.updateIsClicked(action)
        else:
            app.userNameInput.updateText(action)
    elif(app.passwordInput.getIsClicked()):
        action = getAction(event.key)
        if(isinstance(action, bool)):
            app.passwordInput.updateIsClicked(action)
        else:
            app.passwordInput.updateText(action)

def isValidPassword(app, password):
    app.num = False
    app.letter = False
    app.upper = False
    app.lower = False
    for letter in password:
        if(letter.isalpha()):
            app.letter = True
            if(letter.isupper()):
                app.upper = True
            elif(letter.islower()):
                app.lower = True
        elif(letter.isdigit()):
            app.num = True
    return app.num and app.letter and app.upper and app.lower

def makeTrueSignUp(app, element):
    app.signUpUserName.updateIsClicked(1 == element)
    app.signUpPassword.updateIsClicked(2 == element)
    app.signUpName.updateIsClicked(3 == element)
    
def signup_mousePressed(app, event):
    if(app.signUpUserName.isPressedRectangle(event.x, event.y)):
        makeTrueSignUp(app, 1)
    elif(app.signUpPassword.isPressedRectangle(event.x, event.y)):
        makeTrueSignUp(app, 2)
    elif(app.signUpName.isPressedRectangle(event.x, event.y)):
        makeTrueSignUp(app, 3)
    elif(app.signUpExitButton.isPressedCircle(event.x, event.y)):
        app.mode = "login"
        clearTextBoxes(app)
    elif(app.submitSignUpButton.isPressedRectangle(event.x, event.y)):
        user = app.signUpUserName.getText()
        password = app.signUpPassword.getText()
        if(not isValidPassword(app, password)):
            app.invalidPassword = True
        app.users = ast.literal_eval(readFile("userAndPass.txt"))
        if(user in app.users or user in ["Player 1", "Player 2", "Computer"]):
            app.signUpTakenUser = True
        elif(isValidPassword(app, password)):
            num = random.randint(0, 100000000000)
            img = cv2.imread("default.jpg")
            name = str(num) + ".jpg"
            cv2.imwrite(name, img)
            personAttributes = {
                "name": app.signUpName.getText(),
                "username": user,
                "password": password,
                "wins" : 0,
                "ties" : 0,
                "played" : 0,
                "history" : [],
                "h2h" : {},
                "pic" : name
            }
            app.users[user] = personAttributes
            writeFile("userAndPass.txt", repr(app.users))
            if(app.playerCount == 2):
                app.mode = "selection"
                app.player2Name = user
                app.player2Login = True
            else:
                app.player1Name = user
                app.mode = "home"
                app.player1Login = True

            clearTextBoxes(app)
    else:
        makeTrueSignUp(app, -1)

def game2_keyPressed(app, event):
    if(event.key == "r"):
        appStarted(app)

def signup_keyPressed(app, event):
    if(app.signUpUserName.getIsClicked()):
        action = getAction(event.key)
        if(isinstance(action, bool)):
            app.signUpUserName.updateIsClicked(action)
        else:
            app.signUpUserName.updateText(action)
    elif(app.signUpPassword.getIsClicked()):
        action = getAction(event.key)
        if(isinstance(action, bool)):
            app.signUpPassword.updateIsClicked(action)
        else:
            app.signUpPassword.updateText(action)
    elif(app.signUpName.getIsClicked()):
        action = getAction(event.key)
        if(isinstance(action, bool)):
            app.signUpName.updateIsClicked(action)
        else:
            app.signUpName.updateText(action)

def signup_mouseMoved(app, event):
    if(app.submitSignUpButton.isPressedRectangle(event.x, event.y)):
        app.submitSignUpButton.updateColor("dark gray")
    else:
        app.submitSignUpButton.updateColor("gray")
    
    if(app.signUpExitButton.isPressedCircle(event.x, event.y)):
        app.signUpExitButton.updateColor("gray64")
    else:
        app.signUpExitButton.updateColor("white")

def login_mousePressed(app, event):
    if(app.loginButton.isPressedRectangle(event.x, event.y)):
        app.mode = "loginVerify"
    elif(app.signUpButton.isPressedRectangle(event.x, event.y)):
        app.mode = "signup"
    elif(app.guestButton.isPressedRectangle(event.x, event.y)):
        if(app.playerCount == 2):
            app.mode = "selection"
        else:
            app.mode = "home"
    elif(app.loginBackButton.isPressedRectangle(event.x, event.y)):
        if(app.playerCount == 2):
            app.mode = "home"

def login_mouseMoved(app, event):
    for button in app.loginButtons:
        if(button.isPressedRectangle(event.x, event.y)):
            button.updateColor("dark gray")
        else:
            button.updateColor("gray")
##################### UPDATE GAME #######################
# MINIMAX
def computerMakeMove(app, board, move):
    if(app.mode == "game"):
        app.pieceFlip = True
    app.placedRow = move[0]
    app.placedCol = move[1]
    app.playerTurn = 0
    updatePlayerOutline(app)

def miniMax2(app, depth, refDepth, board, legalSquares,
             alpha = -1000, beta = 1000, isComputerTurn = True, minimize = False):
    moves = []
    if(depth == 0 or board.isGameOver(app, int(isComputerTurn))):
        return getState(app, board.getBoard())
    if(depth == -1):
        minimize = True
        depth = 1
        refDepth = 1

    # Computer wants to maximize game score
    if(isComputerTurn):
        boardScore = -1 * app.rows * app.cols - 1
        move = None
        for row, col in legalSquares:   
            simulatedBoard = Board.Board(board.getRows(),
                                         board.getCols(), flip = True,
                                         board = copy.deepcopy(board.getBoard()))

            simulatedBoard.updateGameBoard(app, row, col, int(isComputerTurn))
            simulatedBoard.updateLegalSquares(app, int(isComputerTurn))

            result = miniMax2(app, depth - 1, refDepth, simulatedBoard,
                              simulatedBoard.getLegalSquares(),
                              alpha, beta, not isComputerTurn)
            
            if(depth == refDepth):
                moves.append([result, (row, col)])

            if(result >= boardScore):
                boardScore = result
                move = (row, col)

            if(alpha <= result):
                alpha = result

            if(beta <= alpha):
                break
    else:
        boardScore = app.rows * app.cols + 1
        move = None

        for row, col in legalSquares:
            
            simulatedBoard = Board.Board(board.getRows(),
                                         board.getCols(), flip = True,
                                         board = copy.deepcopy(board.getBoard()))

            simulatedBoard.updateGameBoard(app, row, col, int(isComputerTurn))
            simulatedBoard.updateLegalSquares(app, int(isComputerTurn))

            result = miniMax2(app, depth - 1, refDepth, simulatedBoard,
                              simulatedBoard.getLegalSquares(), 
                              alpha, beta, not isComputerTurn)

            if(result <= boardScore):
                boardScore = result
                move = (row, col)

            if(beta >= result):
                beta = result
            
            if(beta <= alpha):
                break

    if(move != None and depth == refDepth and minimize):
        moves.sort()
        computerMakeMove(app, board, moves[0][1])
    elif(move != None and depth == refDepth):
        computerMakeMove(app, board, move)

    return boardScore

#################### STATE FUNCTIONS ####################
def print2dList(L):
    for i in L:
        print(i)

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

def oneHotEncoding(app, group, element, func, trueState, falseState):
    for i in group:
        if(i == element):
            func(i, trueState)
        else:
            func(i, falseState)

def gameEnding(app):
    app.gameOver = True
    if(app.countColor0 > app.countColor1 and app.player1Login):
        app.users[app.player1Name]["wins"] += 1
        app.users[app.player1Name]["played"] += 1
        if(app.player2Login):
            app.users[app.player2Name]["played"] += 1
    elif(app.countColor0 < app.countColor1 and app.player2Login):
        app.users[app.player2Name]["wins"] += 1
        app.users[app.player2Name]["played"] += 1
        if(app.player1Login):
            app.users[app.player1Name]["played"] += 1
    else:
        if(app.player1Login):
            app.users[app.player1Name]["ties"] += 1
            app.users[app.player1Name]["played"] += 1
        if(app.player2Login):
            app.users[app.player2Name]["ties"] += 1
            app.users[app.player2Name]["played"] += 1
    
    writeFile("userAndPass.txt", repr(app.users))
    if(app.mode == "game"):
        app.end = True
    else:
        app.end = False
    app.mode = "game2"

################## CHECKING AND GETTING FUNCTIONS ###################
def isOnBoardXY2d(app, x, y):
    if(x > app.marginWidthLeft and y > app.marginHeightTop and 
       x < app.width - app.marginWidthRight and y < app.height - app.marginHeightBottom):
        return True
    return False

def isOnBoardXYIsometric(app, x, y):
    if(x >= app.p1[0]):
        projY1 = app.slope1_2 * (x - app.p1[0]) + app.p1[1]
    else:
        projY1 = app.slope1_4 * (x - app.p1[0]) + app.p1[1]
    
    if(x >= app.p3[0]):
        projY2 = app.slope2_3 * (x - app.p3[0]) + app.p3[1]
    else:
        projY2 = app.slope3_4 * (x - app.p3[0]) + app.p3[1]
    
    if(y > projY1 and y < projY2):
        return True
    return False

def getRowColIsometric(app, x, y):
    row, col = None, None
    for c in range(1, app.cols + 1):
        point = (app.p1[0] + app.slope1Increment2 * c, app.p1[1] + app.slope1Increment2 * app.slope1_2 * c)
        projY = app.slope1_4 * (x - point[0]) + point[1]
        if(y <= projY):
            col = c - 1
            break

    for r in range(1, app.rows + 1):
        point = (app.p1[0] + app.slope2Increment2 * r, app.p1[1] + app.slope2Increment2 * app.slope1_4 * r)
        projX = (1 / app.slope1_2) * (y - point[1]) + point[0]
        if(x >= projX):
            row = r - 1
            break

    return row, col

######################## REDRAW ALL ########################
def signup_redrawAll(app, canvas):
    Draw.Login.drawLoginPage(app, canvas)
    Draw.SignUp.drawSignUp(app, canvas)
    if(app.signUpTakenUser):
        Draw.SignUp.drawUserTaken(app, canvas)
    if(app.invalidPassword):
        Draw.SignUp.drawInvalidPassword(app, canvas)

def loginVerify_redrawAll(app, canvas):
    Draw.Login.drawLoginPage(app, canvas)
    Draw.LoginVerification.drawLoginVerification(app, canvas)
    if(app.loginError):
        Draw.LoginVerification.drawLoginError(app, canvas)

def login_redrawAll(app, canvas):
    Draw.Login.drawLoginPage(app, canvas)

def home_redrawAll(app, canvas):
    Draw.Home.drawHomePage(app, canvas)

def confirm_redrawAll(app, canvas):
    if(app.prevScreen == "home"):
        home_redrawAll(app, canvas)
    elif(app.prevScreen == "game"):
        game_redrawAll(app, canvas)
    elif(app.prevScreen == "gameIsometric"):
        Draw.Game.drawIsometricBoard(app, canvas)
        Draw.Game.drawChipsIsometric(app, canvas)
        Draw.Game.drawScore(app, canvas)
        Draw.Game.drawGameButtons(app, canvas)
        Draw.Game.drawError(app, canvas)
        if(app.gameOver):
            Draw.Game.drawGameOver(app, canvas)
    
    Draw.Confirm.drawConfirm(app, canvas)

def selection_redrawAll(app, canvas):
    Draw.Selection.drawSelectionPage(app, canvas)

def gameAnimationPlace_redrawAll(app, canvas):
    Draw.Game.draw2dBoard(app, canvas)
    Draw.Game.drawLegalSquares(app, canvas)
    Draw.Game.drawChips2d(app, canvas)
    Draw.Game.drawScore(app, canvas)
    Draw.Game.drawGameButtons(app, canvas)
    Draw.Game.drawError(app, canvas)
    Draw.Animate.animatePlacePiece(app, canvas)
    if(app.gameOver):
        Draw.Game.drawGameOver(app, canvas)

def gameAnimationFlip_redrawAll(app, canvas):
    Draw.Game.draw2dBoard(app, canvas)
    Draw.Game.drawLegalSquares(app, canvas)
    Draw.Game.drawChips2d(app, canvas)
    Draw.Game.drawScore(app, canvas)
    Draw.Game.drawGameButtons(app, canvas)
    Draw.Game.drawError(app, canvas)
    Draw.Animate.animateFlipPieces(app, canvas, app.playerTurn)
    if(app.gameOver):
        Draw.Game.drawGameOver(app, canvas)

def game_redrawAll(app, canvas):
    Draw.Game.draw2dBoard(app, canvas)
    Draw.Game.drawLegalSquares(app, canvas)
    Draw.Game.drawChips2d(app, canvas)
    Draw.Game.drawScore(app, canvas)
    Draw.Game.drawGameButtons(app, canvas)
    Draw.Game.drawError(app, canvas)
    if(app.gameOver):
        Draw.Game.drawGameOver(app, canvas)

def gameIsometric_redrawAll(app, canvas):
    Draw.Game.drawIsometricBoard(app, canvas)
    Draw.Game.drawLegalSquares(app, canvas)
    Draw.Game.drawChipsIsometric(app, canvas)
    Draw.Game.drawScore(app, canvas)
    Draw.Game.drawGameButtons(app, canvas)
    Draw.Game.drawError(app, canvas)
    if(app.gameOver):
        Draw.Game.drawGameOver(app, canvas)

def game2_redrawAll(app, canvas):
    if(app.end):
        game_redrawAll(app, canvas)
    else:
        gameIsometric_redrawAll(app, canvas)

def profile_redrawAll(app, canvas):
    Draw.Profile.drawProfilePage(app, canvas)
    Draw.Profile.drawDrawing(app, canvas)
    Draw.Profile.drawButtons(app, canvas)
    Draw.Profile.drawStats(app, canvas)
    if(app.profileDraw != ""):
        Draw.Profile.drawStatsText(app, canvas, app.profileDraw, app.profileX, app.profileY)

def updateUser_redrawAll(app, canvas):
    profile_redrawAll(app, canvas)
    Draw.updateUser.drawUpdateUserPage(app, canvas)
    if(app.updateUserInvalidPass):
        Draw.updatePass.drawInvalidPassword(app, canvas)

def updatePass_redrawAll(app, canvas):
    profile_redrawAll(app, canvas)
    Draw.updatePass.drawUpdatePassPage(app, canvas)
    if(app.updatePassInvalidPass):
        Draw.updatePass.drawInvalidPassword(app, canvas)

    if(app.updatePassWrongPass):
        Draw.updatePass.drawIncorrectPassword(app, canvas)

def help_redrawAll(app, canvas):
    if(app.prevScreen == "game"):
        game_redrawAll(app, canvas)
    elif(app.prevScreen == "gameIsometric"):
        gameIsometric_redrawAll(app, canvas)
    Draw.Help.drawRulesPage(app, canvas)
    Draw.Help.drawMiniBoard(app, canvas)
    Draw.Help.drawHelpButtons(app, canvas)
    if(app.slide1):
        Draw.Help.drawRuleAnimation1(app, canvas)
    else:
        Draw.Help.drawRuleAnimation2(app, canvas)

def main():
    runApp(width = 1100, height = 800, title = "Othello")

main()
