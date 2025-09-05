from flask import Flask
import socket, os
app = Flask(__name__)
@app.route("/")
def index():
    return f"Hello from {socket.gethostname()} (pid {os.getpid()})\n"
if __name__=="__main__":
    app.run(host="0.0.0.0", port=8080)
