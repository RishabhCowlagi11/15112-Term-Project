from cmu_112_graphics import *

class Login:
    @staticmethod
    def drawLoginPage(app, canvas):
        canvas.create_rectangle(0, 0, app.width, app.height, fill = app.boardColor)

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
                                fill = app.boardColor, outline = "black", width = 5)
        
        canvas.create_text(app.width / 2, app.height / 4.5, fill = "white",
                        text = "LOGIN", font = "Arial 26 bold underline")

        canvas.create_text(app.width / 3, app.height / 3, fill = "black",
                        text = "Username: ", font = "Arial 26 bold")

        canvas.create_text(app.width / 3, app.height / 2, fill = "black",
                        text = "Password: ", font = "Arial 26 bold")
        
        app.userNameInput.drawRectangleButton(app, canvas)
        # app.userNameInput.drawCursor(app, canvas)
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
                                fill = app.boardColor, outline = "black", width = 5)
        
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
        canvas.create_rectangle(0, 0, app.width, app.height, fill = app.boardColor)
        
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

        # if(app.player2Name == "Computer"):
        #     canvas.create_image(centerX, centerY,
        #                         image = ImageTk.PhotoImage(app.computer2))

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

class Home:
    def drawHomePage(app, canvas):
        canvas.create_rectangle(0, 0, app.width, app.height, fill = app.boardColor)
        croppedImg = app.mainImage.crop((0, 30, 720, 205))
        canvas.create_image(app.width / 2, app.height / 2 - 225, 
                            image = ImageTk.PhotoImage(croppedImg))

        app.player2Button.drawRectangleButton(app, canvas)
        app.player1Button.drawRectangleButton(app, canvas)

        app.tournamentButton.drawRectangleButton(app, canvas)

        app.homeBackButton.drawRectangleButton(app, canvas)

class Confirm:
    def drawConfirm(app, canvas):
        canvas.create_rectangle(app.width / 3, app.height / 3,
                                app.width - app.width / 3, app.height - app.height / 3,
                                fill = app.boardColor, outline = "black", width = 5)
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
                                fill = app.boardColor, outline = "black", width = 5)

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
                                        fill = app.boardColor, outline = "black", width = 3)

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

    def drawBoard(app, canvas):
        app.gameBoardObject.drawBoard(app, canvas)

    def drawChips(app, canvas):
        app.gameBoardObject.drawChips(app, canvas)
        
    def drawScore(app, canvas):
        widthCenter = app.boardWidth / 2 + app.marginWidthLeft
        heightCenter = app.height / 25
        text = f"{app.player1Name} : {app.countColor0}\t{app.player2Name} : {app.countColor1}"
        canvas.create_text(widthCenter, heightCenter, text = text,
                        font = f"Arial {app.fontSize} bold", anchor = "c",
                        fill = "black")

    def drawGameOver(app, canvas):
        canvas.create_rectangle(0, app.height / 3, app.width, app.height - app.height / 3,
                                fill = "green", outline = "black", width = 5)
        if(app.countColor0 > app.countColor1):
            text = f"{app.player1Name} Wins!!!\nPress 'r' to play again"
        elif(app.countColor0 < app.countColor1):
            text = f"{app.player2Name} Wins!!!\nPress 'r' to play again"
        else:
            text = "Tie!!\nPress'r' to play again"
        canvas.create_text(app.width / 2, app.height / 2, text = text,
                        font = "Arial 28", anchor = "c")

    def drawGameButtons(app, canvas):
        app.player1TurnButton.drawRectangleButton(app, canvas)
        app.player2TurnButton.drawRectangleButton(app, canvas)
        app.helpButton.drawCircleButton(app, canvas)

    def drawError(app, canvas):
        if(app.error and not app.gameOver):
            canvas.create_rectangle(0, 0, app.width, app.height, fill = "red")

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
