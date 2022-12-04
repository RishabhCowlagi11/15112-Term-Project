# Importing modules
from cmu_112_graphics import *
import copy, time, ast
import board as Board
import chip as Chip
from features import Button, Text
import gameplay as GamePlay
import person as Person
import draw as Draw

##################### APP STARTED #####################
def socketsClientAppStarted(app):
    # Include Server IP here
    app.SERVER = ""
    app.PORT = 50009
    app.ADDR = (app.SERVER, app.PORT)
    app.FORMAT = "utf-8"
    app.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        app.client.connect(app.ADDR)
    except ConnectionRefusedError:
        print("Begin by Running the Server")

def loginAppStarted(app):
    # Link: https://psdeals.net/id-store/game/1205152/othello-full-game
    app.mainImage = app.loadImage("othy.jpeg")

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
                                 text = "X", bgColor = "red")

    app.loginVerificationButtons = [app.submitLoginButton]

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

    app.signUpExitButton = Button(app.width / 10, app.height / 4.7,
                                  app.width / 20, app.height / 15,
                                  text = "X", bgColor = "red")

    app.signUpButtons = [app.submitSignUpButton]

def homeAppStarted(app):
    # Link: https://psdeals.net/id-store/game/1205152/othello-full-game
    app.mainImage = app.loadImage("othy.jpeg")

    app.verticalSpacing = app.height / 10 + 15

    # creates the buttons on the home page
    app.player2Button = Button(app.width / 2, app.height / 2, 
                                      app.width / 2, app.height / 10,
                                      text = "2 Player Othello!!!")
    app.player1Button = Button(app.width / 2, app.height / 2 + app.verticalSpacing,
                                      app.width / 2, app.height / 10,
                                      text = "1 Player Othello!!!")

    app.tournamentButton = Button(app.width / 2, app.height / 2 + 2 * app.verticalSpacing,
                                         app.width / 2, app.height / 10,
                                         text = "Tournament Othello!!!")

    app.homeBackButton = Button(app.width / 20, app.height / 30,
                                app.width / 12, app.height / 20,
                                text = "Back")

    app.homeButtons = [app.player2Button, app.player1Button, app.tournamentButton,
                       app.homeBackButton]

    app.fontSize = int(app.width / 30)

def confirmAppStarted(app):
    app.confirmButton = Button(app.width / 2, app.height - 13.5 * app.height / 36,
                               app.width / 5, app.height / 20, text = "Confirm")

    app.confirmExitButton = Button(13 * app.width / 36, 13.5 * app.height / 36,
                                   app.width / 15, app.height / 20, text = "X",
                                   bgColor = "white", fill = "red")

    app.confirmButtons = [app.confirmButton, app.confirmExitButton]

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

    app.selectionArrowButtons = [app.player1Left, app.player1Right, app.player2Left,
                                 app.player2Right]
    app.selectionButtons = [app.gameButton, app.selectionBackButton]

def gameAppStarted(app):
    app.colors = ["White", "Black", "Green", "Blue", "Cyan", "Yellow", "Magenta",
                  "Purple", "Dark Blue", "Orange", "Dark Green"]
    # declare the default board and chip colors
    app.baseColor = "gray"

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
    app.hoverRow = None
    app.hoverCol = None

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
    app.player1Name = "Player 1"
    app.player2Name = "Computer"

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

    app.lastPlayedRow = None
    app.lastPlayedCol = None

    app.flipPieces = []
    app.pieceFlip = False
    app.flipIncrements = 5
    app.dcol = 0

    app.miniMaxDepth = 2

    app.gameButtons = [app.helpButton]

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
    
    loginAppStarted(app)
    loginVerificationAppStarted(app)
    signUpAppStarted(app)
    confirmAppStarted(app)
    homeAppStarted(app)
    selectionAppStarted(app)
    gameAppStarted(app)
    helpAppStarted(app)
    
    # Boolean State Variables
    app.gameOver = False
    app.error = False
    app.miniMax = True

####################### BASIC IO #######################
# From 15112 Class Notes Strings: Basic IO
# Link: https://www.cs.cmu.edu/~112/notes/notes-strings.html#basicFileIO
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
        app.gameOver = True
    elif(app.gameBoardObject.noMoreMovesPlayer(app.playerTurn)):
        app.playerTurn = 1 - app.playerTurn
        app.gameBoardObject.updateLegalSquares(app, app.playerTurn)
    elif(app.pieceFlip):
        print("A")
        app.mode = "gameAnimation"
    print(app.computerTurn)
    if(app.playerTurn == 1 and app.miniMax and app.computerTurn):
        print("B")
        miniMax2(app, app.miniMaxDepth, app.miniMaxDepth, app.gameBoardObject,
                 app.gameBoardObject.getLegalSquares())
        app.computerTurn = False
        app.state, app.countColor0, app.countColor1 = getCounts(app, app.gameBoard)

def gameAnimation_timerFired(app):
    app.timerDelay = 100
    for row, col in app.flipPieces:
            app.gameBoard[row][col].setColor(None)
    print("D")
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
    app.slide1 = not app.slide1
##################### USER INPUTS ######################
def help_mousePressed(app, event):
    if(app.helpExitButton.isPressedCircle(event.x, event.y)):
        app.mode = "game"

def game_mousePressed(app, event):
    if(app.dcol + 2 <= app.boardWidth / app.cols and app.pieceFlip):
        return
    rowWidth = app.boardHeight / app.rows 
    colWidth = app.boardWidth / app.cols
    if(app.helpButton.isPressedCircle(event.x, event.y)):
        app.mode = "help"
    
    # If clicked square is on board, get its row and col
    if(isOnBoardXY(app, event.x, event.y)):
        clickedRow = int((event.y - app.marginHeightTop) / rowWidth)
        clickedCol = int((event.x - app.marginWidthLeft) / colWidth)
    else:
        return

    # Checks if square is legal, then places chip and changes turn
    if(isOnBoardXY(app, event.x, event.y) and
       GamePlay.GamePlay.legalSquare(app, app.gameBoard, clickedRow, clickedCol, app.playerTurn)):
        app.lastPlayedRow, app.lastPlayedCol = clickedRow, clickedCol
        app.gameBoardObject.updateGameBoard(app, clickedRow, clickedCol, app.playerTurn)
        print("C")
        app.pieceFlip = True

        app.state, app.countColor0, app.countColor1 = getCounts(app, app.gameBoard)
        
        app.playerTurn = 1 - app.playerTurn       
        updatePlayerOutline(app)
    else:
        app.error = True

def game_mouseMoved(app, event):
    if(isOnBoardXY(app, event.x, event.y)):
        rowWidth = app.boardHeight / app.rows 
        colWidth = app.boardWidth / app.cols
        app.hoverRow = int((event.y - app.marginHeightTop) / rowWidth)
        app.hoverCol = int((event.x - app.marginWidthLeft) / colWidth)
    else:
        app.hoverRow, app.hoverCol = None, None


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
    else:
        appStarted(app)

def selection_mousePressed(app, event):
    if(app.gameButton.isPressedRectangle(event.x, event.y)):
        app.mode = "game"
        app.timerDelay = 50
        colorFill0, colorFill1 = "black", "black"
        if(app.color0 == "Black" or app.color0.find("Dark") != -1):
            colorFill0 = "white"
        if(app.color1 == "Black" or app.color1.find("Dark") != -1):
            colorFill1 = "white"

        app.player1TurnButton = Text(app.width - app.marginWidthRight / 2, 
                                     app.height / 3,
                                     app.marginWidthRight / 1.2, app.height / 4,
                                     text = app.player1Name, bgColor = app.color0,
                                     fill = colorFill0)

        app.player2TurnButton = Text(app.width - app.marginWidthRight / 2, 
                                     app.height - app.height / 3,
                                     app.marginWidthRight / 1.2, app.height / 4,
                                     text = app.player2Name, bgColor = app.color1,
                                     fill = colorFill1)

        app.player1TurnButton.updateIsClicked(True)
        app.player1TurnButton.updateOutline()

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

def confirm_mousePressed(app, event):
    if(app.confirmButton.isPressedRectangle(event.x, event.y)):
        appStarted(app)
    elif(app.confirmExitButton.isPressedCircle(event.x, event.y)):
        app.mode = app.prevScreen

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

def home_mouseMoved(app, event):
    for button in app.homeButtons:
        if(button.isPressedRectangle(event.x, event.y)):
            button.updateColor("dark gray")
        else:
            button.updateColor("gray")

def clearTextBoxes(app):
    textBoxes = [app.userNameInput, app.passwordInput, app.signUpName, 
                 app.signUpUserName, app.signUpPassword]

    for text in textBoxes:
        text.clearText()

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
        # From 112 Class Notes: Strings
        # Link: https://www.cs.cmu.edu/~112/notes/notes-strings.html#basicFileIO
        users = ast.literal_eval(readFile("userAndPass.txt"))
        if(user in users and password == users[user]["password"]):
            if(app.playerCount == 2):
                app.mode = "selection"
                app.player2Name = user
            else:
                app.mode = "home"
                app.player1Name = user
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
    if(len(password) < 4):
        return False
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
        # REFERENCE: 112 Class Notes: Strings
        # Link: https://www.cs.cmu.edu/~112/notes/notes-strings.html#basicFileIO
        users = ast.literal_eval(readFile("userAndPass.txt"))
        if(user in users):
            app.signUpTakenUser = True
        elif(isValidPassword(app, password)):
            personAttributes = {
                "name": app.signUpName.getText(),
                "username": user,
                "password": password,
                "wins" : 0,
                "h2h" : {}
            }
            users[user] = personAttributes
            writeFile("userAndPass.txt", repr(users))
            if(app.playerCount == 2):
                app.mode = "selection"
                app.player2Name = user
            else:
                app.player1Name = user
                app.mode = "home"

            clearTextBoxes(app)
    else:
        makeTrueSignUp(app, -1)


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
        app.signUpExitButton.updateColor("magenta2")
    else:
        app.signUpExitButton.updateColor("red")

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
# REFERENCES
# https://en.wikipedia.org/wiki/minimax
# https://en.wikipedia.org/wiki/Alpha–beta_pruning
# https://www.youtube.com/watch?v=l-hh51ncgDI
# 112 Fundamentals of Game AI
# ^^ Link: https://www.cs.cmu.edu/~112/notes/student-tp-guides/GameAI.pdf
# TA Lecture on Game AI
# ^^ Link: https://docs.google.com/presentation/d/1GVwRIISX0RA4_jvgF90kZZUG_soZUS6P4FFutYwQ39M/edit#slide=id.g35f391192_00
def computerMakeMove(app, board, move):
    # time.sleep(0.7)
    board.updateGameBoard(app, move[0], move[1], 1)
    app.pieceFlip = True
    app.lastPlayedRow = move[0]
    app.lastPlayedCol = move[1]
    app.playerTurn = 0
    board.updateLegalSquares(app, app.playerTurn)
    updatePlayerOutline(app)

def miniMax2(app, depth, refDepth, board, legalSquares,
             alpha = -1000, beta = 1000, isComputerTurn = True):
    if(depth == 0 or board.isGameOver(app, int(isComputerTurn))):
        return getState(app, board.getBoard())

    # Computer wants to maximize game score
    if(isComputerTurn):
        boardScore = -1 * app.rows * app.cols - 1
        move = None
        for row, col in legalSquares:
            
            simulatedBoard = Board.Board(board.getRows(),
                                         board.getCols(),
                                         board = copy.deepcopy(board.getBoard()))

            simulatedBoard.updateGameBoard(app, row, col, int(isComputerTurn))
            simulatedBoard.updateLegalSquares(app, int(isComputerTurn))

            result = miniMax2(app, depth - 1, refDepth, simulatedBoard,
                              simulatedBoard.getLegalSquares(),
                              alpha, beta, not isComputerTurn)
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
                                         board.getCols(),
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

    if(move != None and depth == refDepth):
        computerMakeMove(app, board, move)

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

def oneHotEncoding(app, group, element, func, trueState, falseState):
    for i in group:
        if(i == element):
            func(i, trueState)
        else:
            func(i, falseState)

################## CHECKING FUNCTIONS ###################
def isOnBoardXY(app, x, y):
    if(x > app.marginWidthLeft and y > app.marginHeightTop and 
       x < app.width - app.marginWidthRight and y < app.height - app.marginHeightBottom):
        return True
    return False

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
    
    Draw.Confirm.drawConfirm(app, canvas)

def selection_redrawAll(app, canvas):
    Draw.Selection.drawSelectionPage(app, canvas)

def gameAnimation_redrawAll(app, canvas):
    Draw.Game.drawBoard(app, canvas)
    Draw.Game.drawLegalSquares(app, canvas)
    Draw.Game.drawChips(app, canvas)
    Draw.Game.drawScore(app, canvas)
    Draw.Game.drawGameButtons(app, canvas)
    Draw.Game.drawError(app, canvas)
    Draw.Animate.animateFlipPieces(app, canvas, app.playerTurn)
    if(app.gameOver):
        Draw.Game.drawGameOver(app, canvas)

def game_redrawAll(app, canvas):
    Draw.Game.drawBoard(app, canvas)
    Draw.Game.drawLegalSquares(app, canvas)
    Draw.Game.drawChips(app, canvas)
    Draw.Game.drawScore(app, canvas)
    Draw.Game.drawGameButtons(app, canvas)
    Draw.Game.drawError(app, canvas)
    if(app.gameOver):
        Draw.Game.drawGameOver(app, canvas)

def help_redrawAll(app, canvas):
    game_redrawAll(app, canvas)
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
