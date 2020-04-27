from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = '1234567'
socketio = SocketIO(app)


@app.route('/')
def sessions():
    return render_template('session.html')


def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')


@socketio.on('update')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('Received : ' + str(json))
    socketio.emit('response', json, callback=messageReceived)


if __name__ == '__main__':
    socketio.run(app, debug=True)
