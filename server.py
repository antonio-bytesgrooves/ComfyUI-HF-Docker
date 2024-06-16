from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
import subprocess
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'default_secret_key')
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('execute_command')
def handle_execute_command(data):
    command = data['command']
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    for line in iter(process.stdout.readline, ''):
        emit('command_output', {'output': line})
    
    process.stdout.close()
    process.wait()

if __name__ == '__server__':
   app.run()

# host="127.0.0.1"
# port=7860
# scheme = "https"

# def start_server():
#     app.run(host, port, debug=False)
    
#     import webbrowser
#     webbrowser.open(f"{scheme}://{host}:{port}")