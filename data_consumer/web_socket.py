from flask import Flask 
from flask_socketio import SocketIO, send
from mongodbreader import read_from_database

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins='*')

@socketio.on('message')
def handleMessage(rule):
    print("\n\n\n")
    print("HANDLE MESSAGE",rule)
    
    print("\n\n\n")
    if rule=="" or rule=="{{data}}":
        return
    else:
        print("RULE:",rule)
        print("CONDITION:",rule!="")
        tweet=read_from_database(rule)
        socketio.emit('message', tweet)


@socketio.on('connect')
def handleConnect():
    print("\n\n\n")
    print("Client connected")
    print("\n\n\n")

@socketio.on('disconnect')
def handleDisconnect():
    socketio.emit('disconnect', 'User has disconnected', broadcast=True)

if __name__ == "__main__":
    socketio.run(app)