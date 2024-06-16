from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
import subprocess
import os
import aiohttp
from aiohttp import web

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'default_secret_key')
socketio = SocketIO(app)


@web.middleware
async def cache_control(request: web.Request, handler):
    response: web.Response = await handler(request)
    if request.path.endswith('.js') or request.path.endswith('.css'):
        response.headers.setdefault('Cache-Control', 'no-cache')
    return response

def create_cors_middleware(allowed_origin: str):
    @web.middleware
    async def cors_middleware(request: web.Request, handler):
        if request.method == "OPTIONS":
            # Pre-flight request. Reply successfully:
            response = web.Response()
        else:
            response = await handler(request)

        response.headers['Access-Control-Allow-Origin'] = allowed_origin
        response.headers['Access-Control-Allow-Methods'] = 'POST, GET, DELETE, PUT, OPTIONS'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
        response.headers['Access-Control-Allow-Credentials'] = 'true'
        return response

    return cors_middleware

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

def __init__(self):
    middlewares = [cache_control]
    middlewares.append(create_cors_middleware(True))
    max_upload_size = round(args.max_upload_size * 1024 * 1024)
    self.app = web.Application(client_max_size=max_upload_size, middlewares=middlewares)
    self.sockets = dict()
    self.web_root = os.path.join(os.path.dirname(
    os.path.realpath(__file__)), "web")
    routes = web.RouteTableDef()
    self.routes = routes
    self.last_node_id = None
    self.client_id = None
    
    
if __name__ == '__server__':
   app.run()

# host="127.0.0.1"
# port=7860
# scheme = "https"

# def start_server():
#     app.run(host, port, debug=False)
    
#     import webbrowser
#     webbrowser.open(f"{scheme}://{host}:{port}")