import socket
import socky
import threading

def serverInitVariables(app):
    app.SERVER = socket.gethostbyname(socket.gethostname())
    app.PORT = 50010
    app.ADDR = (app.SERVER, app.PORT)
    app.FORMAT = "utf-8"
    app.connections = []

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected")
    connected = True
    while connected:
        msg = conn.recv(1024).decode(app.FORMAT)
        print(f"[{addr}] {msg}")
        if(len(app.connections) >= 2):
            print("Here")
            index = app.connections.index(conn)
            print(index)
            print(app.connections)
            app.connections[1 - index].send(msg.encode(app.FORMAT))
        else:
            conn.send("msg received".encode(app.FORMAT))
            conn.send("msg not relayed".encode(app.FORMAT))
    conn.close()

def serverStarted(app):
    app.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    app.server.bind(app.ADDR)
    app.server.listen()
    print(f"[LISTENING] Server is listening on {app.SERVER}")
    while True:
        conn, addr = app.server.accept()
        app.connections.append(conn)
        thread = threading.Thread(target = handle_client, args = (conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")
    
def main(app):
    serverInitVariables(app)
    serverStarted(app)
    
app = socky.socky()
main(app)