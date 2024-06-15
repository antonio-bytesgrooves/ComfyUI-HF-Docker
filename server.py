from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Congratulations, it's a web app!"

def start_server():
    app.run(host="127.0.0.1", port=7860, debug=True)