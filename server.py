from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
import subprocess

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'yhjstyjypty,b,=k5=k5p,b=per,]f[lge-ot=-4y=-5=g,=50,=perkg=4'  # Replace with your actual secret key
    socketio = SocketIO(app)

    @app.route('/')
    def index():
        return render_template('index.html')

    @socketio.on('execute_command')
    def handle_execute_command(data):
        command = data['command']

        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        for line in iter(process.stdout.readline, ''):
            emit('command_output', {'output': line.strip()})  # Emit each line of output

        process.stdout.close()
        process.wait()

    #return app, socketio

    @socketio.on('system_command')
    def handle_system_command(data):
        command = data["command"]

        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        for line in iter(process.stdout.readline, ''):
            emit('system_output', {'output': line.strip()})  # Emit each line of output

        process.stdout.close()
        process.wait()


    return app, socketio

app, socketio = create_app()

if __name__ == '__main__':
    socketio.run(app, host='127.0.0.1', port=7860, debug=True)


# host="127.0.0.1"
# port=7860
# scheme = "https"

# def start_server():
#     app.run(host, port, debug=False)
    
#     import webbrowser
#     webbrowser.open(f"{scheme}://{host}:{port}")