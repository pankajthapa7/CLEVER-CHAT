from flask import Flask, render_template, request
from flask_socketio import SocketIO, send
from chat_ai import get_response

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handleMessage(msg):
    print(f"User: {msg}")
    response = get_response(msg)
    print(f"Bot: {response}")
    send({'msg': response.text, 'user': 'Bot'}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app)
