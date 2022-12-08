from cmu_112_graphics import *
from features import Button

class Login:
    @staticmethod
    def drawLoginPage(app, canvas):
        canvas.create_rectangle(0, 0, app.width, app.height, fill = app.boardColorDark)

        croppedImg = app.mainImage.crop((0, 30, 720, 205))
        canvas.create_image(app.width / 2, app.height / 2 - 225, 
                            image = ImageTk.PhotoImage(croppedImg))

        if(app.playerCount == 2):
            canvas.create_text(app.width / 2, app.height / 2 - app.height / 8,
                               text = "Player 2 Login", font = "Arial 26 bold underline")

            app.loginBackButton.drawRectangleButton(app, canvas)
        
        app.loginButton.drawRectangleButton(app, canvas)
        app.signUpButton.drawRectangleButton(app, canvas)

        app.guestButton.drawRectangleButton(app, canvas)

class LoginVerification:
    def drawLoginVerification(app, canvas):
        canvas.create_rectangle(app.width / 15, app.height / 6, 
                                app.width - app.width / 15, app.height - app.height / 6,
                                fill = app.boardColorDark, outline = "black", width = 5)
        
        canvas.create_text(app.width / 2, app.height / 4.5, fill = "white",
                        text = "LOGIN", font = "Arial 26 bold underline")

        canvas.create_text(app.width / 3, app.height / 3, fill = "black",
                        text = "Username: ", font = "Arial 26 bold")

        canvas.create_text(app.width / 3, app.height / 2, fill = "black",
                        text = "Password: ", font = "Arial 26 bold")
        
        app.userNameInput.drawRectangleButton(app, canvas)
        app.userNameInput.updateOutline()
        app.userNameInput.drawText(app, canvas)

        app.passwordInput.drawRectangleButton(app, canvas)
        app.passwordInput.updateOutline()
        app.passwordInput.drawText(app, canvas)

        app.submitLoginButton.drawRectangleButton(app, canvas)
        app.loginExitButton.drawCircleButton(app, canvas)

    def drawLoginError(app, canvas):
        canvas.create_text(app.width / 2, app.height - app.height / 3.6,
                           text = "Either Username or Password is Invalid",
                           fill = "red", font = "Arial 20 bold", anchor = "c")

class SignUp:
    def drawSignUp(app, canvas):
        canvas.create_rectangle(app.width / 15, app.height / 6, 
                                app.width - app.width / 15, app.height - app.height / 10,
                                fill = app.boardColorDark, outline = "black", width = 5)
        
        canvas.create_text(app.width / 2, app.height / 4.3, fill = "white",
                        text = "SIGN UP", font = "Arial 26 bold underline")

        canvas.create_text(app.width / 3, app.height / 3, fill = "black",
                        text = "Player Name:", font = "Arial 26 bold")

        canvas.create_text(app.width / 3, app.height / 2, fill = "black",
                        text = "Username:", font = "Arial 26 bold")

        canvas.create_text(app.width / 3, app.height - app.height / 3, fill = "black",
                        text = "Password:", font = "Arial 26 bold")
        
        text = "Password Must Include:\n1 UpperCase Letter\n1 Lower Case Letter\n1 Number"
        canvas.create_text(app.width / 3, app.height - app.height / 3.6,
                        text = text, font = "Arial 14 bold", anchor = "c")
        
        app.signUpName.drawRectangleButton(app, canvas)
        app.signUpName.updateOutline()
        app.signUpName.drawText(app, canvas)

        app.signUpUserName.drawRectangleButton(app, canvas)
        app.signUpUserName.updateOutline()
        app.signUpUserName.drawText(app, canvas)

        app.signUpPassword.drawRectangleButton(app, canvas)
        app.signUpPassword.updateOutline()
        app.signUpPassword.drawText(app, canvas)

        app.submitSignUpButton.drawRectangleButton(app, canvas)
        app.signUpExitButton.drawCircleButton(app, canvas)

    def drawUserTaken(app, canvas):
        canvas.create_text(app.width - app.width / 3, app.height / 2 + app.height / 15,
                           text = "Username Already Taken", fill = "red", 
                           font = "Arial 18 bold", anchor = "c")

    def drawInvalidPassword(app, canvas):
        canvas.create_text(app.width - app.width / 3, app.height - app.height / 3 + app.height / 15,
                           text = "Invalid Password", fill = "red",
                           font = "Arial 20 bold", anchor = "c")


class Selection:
    def drawSelectionPage(app, canvas):
        canvas.create_rectangle(0, 0, app.width, app.height, fill = app.boardColorDark)
        
        canvas.create_text(app.width / 2, app.height / 12, text = "Color Selection",
                        fill = "black", font = "Arial 36 bold underline", anchor = "c")

        # Draw the selection for player 1
        centerX = app.width / 2
        centerY = app.height / 2 - app.height / 6
        marginX = app.width / 8
        marginY = app.height / 10
        canvas.create_rectangle(centerX - marginX, centerY - marginY,
                                centerX + marginX, centerY + marginY, 
                                fill = app.color0, outline = "black", width = 5)

        canvas.create_text(centerX, centerY + marginY + 20, text = app.player1Name,
                        font = "Arial 28 bold",  fill = "Black", anchor = "c")
        
        # Draw the selection for player 2
        centerY = app.height / 2 + app.height / 10
        canvas.create_rectangle(centerX - marginX, centerY - marginY,
                                centerX + marginX, centerY + marginY, 
                                fill = app.color1, outline = "black", width = 5)

        canvas.create_text(centerX, centerY + marginY + 20, text = app.player2Name,
                           font = "Arial 28 bold", fill = "black", anchor = "c")

        Selection.drawSelectionButtons(app, canvas)
    
    def drawSelectionButtons(app, canvas):
        app.gameButton.drawRectangleButton(app, canvas)

        app.player1Left.drawTriangleButton(app, canvas)
        app.player1Right.drawTriangleButton(app, canvas)

        app.player2Left.drawTriangleButton(app, canvas)
        app.player2Right.drawTriangleButton(app, canvas)

        app.selectionBackButton.drawRectangleButton(app, canvas)

        if(app.player2Name == "Computer"):
            app.easyButton.drawRectangleButton(app, canvas)
            app.hardButton.drawRectangleButton(app, canvas)

class Home:
    def drawHomePage(app, canvas):
        canvas.create_rectangle(0, 0, app.width, app.height, fill = app.boardColorDark)
        croppedImg = app.mainImage.crop((0, 30, 720, 205))
        canvas.create_image(app.width / 2, app.height / 2 - 225, 
                            image = ImageTk.PhotoImage(croppedImg))

        app.player2Button.drawRectangleButton(app, canvas)
        app.player1Button.drawRectangleButton(app, canvas)

        app.profileButton.drawRectangleButton(app, canvas)

        app.homeBackButton.drawRectangleButton(app, canvas)
        if(app.tellLogin):
            canvas.create_rectangle(app.width / 2 - app.width / 6, 
                                    app.drawErrorY - app.height / 30,
                                    app.width / 2 + app.width / 6,
                                    app.drawErrorY + app.height / 30, fill = "hot pink",
                                    outline = "black", width = 5)
            canvas.create_text(app.width / 2, app.drawErrorY, text = "Login To Use This Feature",
                               font = "Arial 26 bold", fill = "black")

class Confirm:
    def drawConfirm(app, canvas):
        canvas.create_rectangle(app.width / 3, app.height / 3,
                                app.width - app.width / 3, app.height - app.height / 3,
                                fill = app.boardColorDark, outline = "black", width = 5)
        text = "Are you sure you want to restart?\nIf you are in a game this will\n\
count as a loss."
        canvas.create_text(app.width / 2, app.height / 2, text = text,
                           font = "Arial 22 bold", fill = "black")

        app.confirmButton.drawRectangleButton(app, canvas)
        app.confirmExitButton.drawCircleButton(app, canvas)

class Help:
    def drawRulesPage(app, canvas):
        xCorner = app.width / 200
        yCorner = app.height / 10
        canvas.create_rectangle(xCorner, yCorner, 
                                app.width - 5, app.height - app.height / 10,
                                fill = app.boardColorDark, outline = "black", width = 5)

        canvas.create_text(app.width / 2, yCorner + app.height / 15, text = "Rules", 
                           fill = "black", font = f"Arial {app.fontSize} bold underline",
                           anchor = "c")

        text = "Othello is a game where 2 players take turns\nplacing a chips of \
different colors on the board.\nThe only legal square to place a \
chip are the\nsquares that will flip over at least one of your\nopponent's \
chips (if there are no squares that flip\nover one of your opponent's \
chips, you lose your\nturn). When ever you place down a chip, all\n\
of your opponent's chips that are between the chip\nyou just played \
and another one of your chips gets\nflipped. The goal of the game \
is to 'control' the most\nnumber of chips. The game ends when the board \
is\nfull or neither player has any legal moves."

        canvas.create_text(6 * app.width / 17, 10 * app.height / 21,
                           text = text, font = f"Arial {int(app.fontSize - app.fontSize / 5)}",
                           anchor = "c", fill = "black")

    def drawMiniBoard(app, canvas):
        squareSide = app.width / 15
        startX = 11 * app.width / 16
        startY = app.height / 4
        for i in range(4):
            for j in range(4):
                canvas.create_rectangle(startX + squareSide * i, startY + squareSide * j,
                                        startX + squareSide * (i + 1), startY + squareSide * (j + 1),
                                        fill = app.boardColorDark, outline = "black", width = 3)

    def drawRuleAnimation1(app, canvas):
        squareSide = app.width / 18
        startX = 11 * app.width / 16
        startY = app.height / 4
        canvas.create_oval(startX + squareSide * 3 + 42, startY + 7,
                           startX + squareSide * 4 + 42, startY + squareSide + 7,
                           fill = "white", outline = "black", width = 3)

        canvas.create_oval(startX + squareSide * 2 + 32, startY + squareSide + 20,
                           startX + squareSide * 3 + 32, startY + squareSide * 2 + 20,
                           fill = "black", outline = "black", width = 3)

        canvas.create_oval(startX + squareSide * 2 + 32, startY + squareSide * 2 + 30,
                           startX + squareSide * 3 + 32, startY + squareSide * 3 + 30,
                           fill = "black", outline = "black", width = 3)

        canvas.create_oval(startX + squareSide * 3 + 42, startY + squareSide * 2 + 30,
                           startX + squareSide * 4 + 42, startY + squareSide * 3 + 30,
                           fill = "white", outline = "black", width = 3)

    def drawRuleAnimation2(app, canvas):
        squareSide = app.width / 18
        startX = 11 * app.width / 16
        startY = app.height / 4
        canvas.create_oval(startX + squareSide * 3 + 42, startY + 7,
                           startX + squareSide * 4 + 42, startY + squareSide + 7,
                           fill = "white", outline = "black", width = 3)

        canvas.create_oval(startX + squareSide * 2 + 32, startY + squareSide + 20,
                           startX + squareSide * 3 + 32, startY + squareSide * 2 + 20,
                           fill = "white", outline = "black", width = 3)

        canvas.create_oval(startX + squareSide * 2 + 32, startY + squareSide * 2 + 30,
                           startX + squareSide * 3 + 32, startY + squareSide * 3 + 30,
                           fill = "white", outline = "black", width = 3)

        canvas.create_oval(startX + squareSide * 3 + 42, startY + squareSide * 2 + 30,
                           startX + squareSide * 4 + 42, startY + squareSide * 3 + 30,
                           fill = "white", outline = "black", width = 3)

        canvas.create_oval(startX + squareSide + 20, startY + squareSide * 2 + 30,
                           startX + squareSide * 2 + 20, startY + squareSide * 3 + 30,
                           fill = "white", outline = "black", width = 3)

    def drawHelpButtons(app, canvas):
        app.helpExitButton.drawCircleButton(app, canvas)

class Game:
    def drawLegalSquares(app, canvas):
        app.gameBoardObject.drawLegalSquares(app, canvas)

    def draw2dBoard(app, canvas):
        app.gameBoardObject.drawBoard(app, canvas)

    def drawIsometricBoard(app, canvas):
        app.gameBoardObject.drawIsometricBoard(app, canvas)

    def drawChips2d(app, canvas):
        app.gameBoardObject.drawChips2d(app, canvas)

    def drawChipsIsometric(app, canvas):
        app.gameBoardObject.drawChipsIsometric(app, canvas)
        
    def drawScore(app, canvas):
        widthCenter = app.boardWidth / 2 + app.marginWidthLeft
        heightCenter = app.height / 25
        text = f"{app.player1Name} : {app.countColor0}\t{app.player2Name} : {app.countColor1}"
        canvas.create_text(widthCenter, heightCenter, text = text,
                        font = f"Arial {app.fontSize} bold", anchor = "c",
                        fill = "black")

    def drawGameOver(app, canvas):
        canvas.create_rectangle(app.width / 3, app.height / 3, 
                                2 * app.width / 3, app.height - app.height / 3,
                                fill = "green", outline = "black", width = 10)
        
        if(app.countColor0 > app.countColor1):
            text = f"{app.player1Name} Wins!!!\nPress 'r' to play again"
        elif(app.countColor0 < app.countColor1):
            text = f"{app.player2Name} Wins!!!\nPress 'r' to play again"
        else:
            text = "Tie!!\nPress'r' to play again"
        canvas.create_text(app.width / 2, app.height / 2, text = text,
                        font = "Arial 28 bold", anchor = "c")

    def drawGameButtons(app, canvas):
        app.player1TurnButton.drawRectangleButton(app, canvas)
        app.player2TurnButton.drawRectangleButton(app, canvas)
        app.helpButton.drawCircleButton(app, canvas)
        text = "Press 'r' to Go Back to Start Screen\nPress 'i' to Toggle Isometric View"
        canvas.create_text(app.width - app.width / 8, app.height - app.height / 20,
                           text = text, fill = "black", font = "Arial 14 bold")

    def drawError(app, canvas):
        if(app.error and not app.gameOver):
            canvas.create_rectangle(0, 0, app.width, app.height, fill = "red")

class Profile:
    def drawProfilePage(app, canvas):
        canvas.create_rectangle(0, 0, app.width, app.height, fill = app.boardColorDark)

        canvas.create_text(app.width / 5, 3 * app.height / 5, text = app.player1Name,
                           font = f"Arial {app.fontSize} bold underline",
                           fill = "black")

    def drawButtons(app, canvas):
        app.playerColorButton.drawRectangleButton(app, canvas)
        app.updateUserButton.drawRectangleButton(app, canvas)
        app.updatePassButton.drawRectangleButton(app, canvas)
        app.profileBackButton.drawRectangleButton(app, canvas)
        
        app.color1Button.drawCircleButton(app, canvas)
        app.color2Button.drawCircleButton(app, canvas)
        app.color3Button.drawCircleButton(app, canvas)

        app.colorLeft.drawTriangleButton(app, canvas)
        app.colorRight.drawTriangleButton(app, canvas)

        app.clearButton.drawRectangleButton(app, canvas)
        
    def drawDrawing(app, canvas):
        app.playerColorButton.drawDrawing(app, canvas)

    def createStatsButtons(app):
        app.wins = app.users[app.player1Name]["wins"]
        app.ties = app.users[app.player1Name]["ties"]
        app.played = app.users[app.player1Name]["played"]
        app.winFill = "blue"
        app.lossFill = "orange"
        app.tieFill = "yellow"
        winAngle, lossAngle, tieAngle = 0, 0, 0
        if(app.played == 0):
            app.winFill = ""
            winAngle = 360
        elif(app.wins == app.played):
            app.winFill = "blue1"
            winAngle = 360
        elif(app.ties == app.played):
            app.tieFill = "yellow1"
            tieAngle = 360
        elif(app.wins == 0 and app.ties == 0):
            app.lossFill = "orange1"
            lossAngle = 360
        else:
            winAngle = 360 * app.wins / app.played
            tieAngle = 360 * app.ties / app.played
            lossAngle = 360 - winAngle - tieAngle
        pieCenterX = 5 * app.width / 7
        pieCenterY = app.height / 2
        sideLen = app.width / 2
    
        app.winsButton = Button(pieCenterX, pieCenterY, sideLen, sideLen,
                                text = "", start = 90, extent = winAngle,
                                bgColor = app.winFill)
        
        app.tieButton = Button(pieCenterX, pieCenterY, sideLen, sideLen,
                               text = "", start = 90 + winAngle, extent = tieAngle,
                               bgColor = app.tieFill)

        app.lossButton = Button(pieCenterX, pieCenterY, sideLen, sideLen,
                                text = "", start = 90 + winAngle + tieAngle, 
                                extent = lossAngle, bgColor = app.lossFill)

    def drawStats(app, canvas):
        canvas.create_text(5 * app.width / 7, app.height / 15,
                           text = "Statistics", font = f"Arial {app.fontSize} bold underline",
                           fill = "black")
        if(app.winFill == ""):
            app.winsButton.drawCircleButton(app, canvas)
        elif(app.winFill.find("1") != -1):
            app.winsButton.drawCircleButton(app, canvas)
        elif(app.tieFill.find("1") != -1):
            app.tieButton.drawCircleButton(app, canvas)
        elif(app.lossFill.find("1") != -1):
            app.lossButton.drawCircleButton(app, canvas)
        else:
            app.winsButton.drawArcButton(app, canvas)
            app.tieButton.drawArcButton(app, canvas)
            app.lossButton.drawArcButton(app, canvas)
    
    def drawStatsText(app, canvas, element, x, y):
        boxWidth = app.width / 6
        boxHeight = app.height / 20
        if(app.played == 0):
            text = "Play a Game to Get\nStats to Appear"
        elif(element == "win"):
            percent = round(app.wins / app.played * 100, 2)
            text = f"Wins: {app.wins} | Played: {app.played}\nWin Percentage: {percent}%"
        elif(element == "tie"):
            percent = round(app.ties / app.played * 100, 2)
            text = f"Ties: {app.ties} | Played: {app.played}\nTie Percentage: {percent}%"
        elif(element == "loss"):
            losses = app.played - app.ties - app.wins
            percent = round(losses / app.played * 100, 1)
            text = f"Losses: {losses} | Played: {app.played}\nLoss Percentage: {percent}%"
        
        if(x + boxWidth + 10 > app.width):
            canvas.create_rectangle(x - boxWidth - 10, y, x, y + boxHeight, fill = "white")
            canvas.create_text(x - 10, y, text = text, font = "Arial 16", 
                               fill = "black", anchor = "ne")
        else:
            canvas.create_rectangle(x + 10, y, x + boxWidth, y + boxHeight, fill = "white")
            canvas.create_text(x + 10, y, text = text, font = "Arial 16", 
                               fill = "black", anchor = "nw")

class updateUser:
    def drawUpdateUserPage(app, canvas):
        canvas.create_rectangle(app.width / 15, app.height / 6, 
                                app.width - app.width / 15, app.height - app.height / 6,
                                fill = app.boardColorDark, outline = "black", width = 5)
        
        canvas.create_text(app.width / 2, app.height / 4.5, fill = "white",
                        text = "Update Username", font = "Arial 26 bold underline")

        canvas.create_text(app.width / 3, app.height / 3, fill = "black",
                        text = "New Username: ", font = "Arial 26 bold")

        canvas.create_text(app.width / 3, app.height / 2, fill = "black",
                        text = "Confirm Password: ", font = "Arial 26 bold")
        
        app.newUserText.drawRectangleButton(app, canvas)
        app.newUserText.updateOutline()
        app.newUserText.drawText(app, canvas)

        app.userPasswordConfirm.drawRectangleButton(app, canvas)
        app.userPasswordConfirm.updateOutline()
        app.userPasswordConfirm.drawText(app, canvas)

        app.updateUserSubmitButton.drawRectangleButton(app, canvas)
        app.updateUserExitButton.drawCircleButton(app, canvas)

class updatePass:
    def drawUpdatePassPage(app, canvas):
        canvas.create_rectangle(app.width / 15, app.height / 6, 
                                app.width - app.width / 15, app.height - app.height / 6,
                                fill = app.boardColorDark, outline = "black", width = 5)
        
        canvas.create_text(app.width / 2, app.height / 4.5, fill = "white",
                        text = "Update Password", font = "Arial 26 bold underline")

        canvas.create_text(app.width / 3, app.height / 3, fill = "black",
                        text = "Old Password: ", font = "Arial 26 bold")

        canvas.create_text(app.width / 3, app.height / 2, fill = "black",
                        text = "New Password: ", font = "Arial 26 bold")
        
        app.passwordConfirmText.drawRectangleButton(app, canvas)
        app.passwordConfirmText.updateOutline()
        app.passwordConfirmText.drawText(app, canvas)

        text = "Password Must Include:\n1 UpperCase Letter\n1 Lower Case Letter\n1 Number"
        canvas.create_text(app.width / 3, 4 * app.height / 7,
                        text = text, font = "Arial 14 bold", anchor = "c")

        app.newPassText.drawRectangleButton(app, canvas)
        app.newPassText.updateOutline()
        app.newPassText.drawText(app, canvas)

        app.updatePassSubmitButton.drawRectangleButton(app, canvas)
        app.updatePassExitButton.drawCircleButton(app, canvas)
    
    def drawIncorrectPassword(app, canvas):
        canvas.create_text(app.width - app.width / 3, app.height / 3 + app.height / 15,
                           text = "Password Incorrect", fill = "red", 
                           font = "Arial 18 bold", anchor = "c")

    def drawInvalidPassword(app, canvas):
        canvas.create_text(app.width - app.width / 3, app.height / 2 + app.height / 15,
                           text = "Invalid Password", fill = "red",
                           font = "Arial 20 bold", anchor = "c")

class Animate:
    def animateFlipPieces(app, canvas, player):
        if(player == 0):
            fill = app.color0
        else:
            fill = app.color1

        for chipRow, chipCol in app.flipPieces:
            rowIncrement = app.boardHeight / app.rows
            colIncrement = app.boardWidth / app.cols
            margin = 5
            if(app.dcol >= 0.5 * colIncrement and player == 0):
                fill = app.color1
            elif(app.dcol >= 0.5 * colIncrement):
                fill = app.color0
            canvas.create_oval(app.marginWidthLeft + chipCol * colIncrement + margin + app.dcol, 
                               app.marginHeightTop + chipRow * rowIncrement + margin,
                               app.marginWidthLeft + (chipCol + 1) * colIncrement - margin - app.dcol,
                               app.marginHeightTop + (chipRow + 1) * rowIncrement - margin,
                               fill = fill, outline = "black", width = 5)

    def animatePlacePiece(app, canvas):
        if(app.playerTurn == 0):
            fill = app.color1
        else:
            fill = app.color0

        rowIncrement = app.boardHeight / app.rows
        colIncrement = app.boardWidth / app.cols

        xCenter = app.marginWidthLeft + (app.placedCol + 0.5) * colIncrement
        yCenter = app.marginHeightTop + (app.placedRow + 0.5) * rowIncrement
        canvas.create_oval(xCenter - app.rx / 2, yCenter - app.ry / 2,
                           xCenter + app.rx / 2, yCenter + app.ry / 2,
                           fill = fill, outline = "black", width = (5 / colIncrement) * app.rx)
