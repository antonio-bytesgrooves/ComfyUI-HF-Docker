from flask import Flask, render_template, request
import subprocess


app = Flask(__name__)

result = ''

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        command = request.form['command']
        try:
            result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True)
        except subprocess.CalledProcessError as e:
            result = e.output

host="127.0.0.1"
port=7860
scheme = "https"

def start_server():
    app.run(host, port, debug=False)
    render_template('index.html', result=result)
    import webbrowser
    webbrowser.open(f"{scheme}://{host}:{port}")