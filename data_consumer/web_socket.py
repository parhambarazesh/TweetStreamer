from flask import Flask 
from flask_socketio import SocketIO, send
from mongodbreader import read_from_database

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins='*')

@socketio.on('message')
def handleMessage(rule):
    print("handling message, ",rule)
    if rule=="" or rule=="{{data}}":
        return
    else:
        tweet=read_from_database(rule)
        socketio.emit('message', tweet)


@socketio.on('connect')
def handleConnect():
    print("Client is connected")

@socketio.on('disconnect')
def handleDisconnect():
    socketio.emit('disconnect', 'User has disconnected', broadcast=True)

if __name__ == "__main__":
    socketio.run(app)