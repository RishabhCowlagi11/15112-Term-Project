import socket
import socky
import time

def clientStartedVariables(app):
    app.PORT = 50010
    app.SERVER = socket.gethostbyname(socket.gethostname())
    app.ADDR = (app.SERVER, app.PORT)
    app.FORMAT = "utf-8"
    app.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def clientStarted(app):
    app.client.connect(app.ADDR)

def send(app, msg):
    message = msg.encode(app.FORMAT)
    app.client.send(message)
    print(app.client.recv(2048).decode(app.FORMAT))

app = socky.socky()
clientStartedVariables(app)
clientStarted(app)
while True:
    msg = input("Enter your message here: ")
    send(app, msg)


