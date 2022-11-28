from cmu_112_graphics import *

class Login:
    @staticmethod
    def drawLoginPage(app, canvas):
        canvas.create_rectangle(0, 0, app.width, app.height, fill = app.boardColor)

        croppedImg = app.mainImage.crop((0, 30, 720, 205))
        canvas.create_image(app.width / 2, app.height / 2 - 225, image = ImageTk.PhotoImage(croppedImg))

        if(app.playerCount == 2):
            canvas.create_text(app.width / 2, app.height / 2 - app.height / 8,
                               text = "Player 2 Login", font = "Arial 26 bold underline")
        
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

class Home:
    def drawHomePage(app, canvas):
        canvas.create_rectangle(0, 0, app.width, app.height, fill = "green")
        croppedImg = app.mainImage.crop((0, 30, 720, 205))
        canvas.create_image(app.width / 2, app.height / 2 - 225, image = ImageTk.PhotoImage(croppedImg))

        app.player2Button.drawRectangleButton(app, canvas)
        app.player1Button.drawRectangleButton(app, canvas)

        app.tournamentButton.drawRectangleButton(app, canvas)

class Game:
    def drawLegalSquares(app, canvas):
        app.gameBoardObject.drawLegalSquares(app, canvas)

    def drawBoard(app, canvas):
        app.gameBoardObject.drawBoard(app, canvas)
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

    def drawGameButton(app, canvas):
        app.player1TurnButton.drawRectangleButton(app, canvas)
        app.player2TurnButton.drawRectangleButton(app, canvas)

    def drawError(app, canvas):
        if(app.error and not app.gameOver):
            canvas.create_rectangle(0, 0, app.width, app.height, fill = "red")

