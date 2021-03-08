from flask import Flask
import socket
app = Flask(__name__)


@app.route('/')
def hello():
    return f"""<br><h1> Hello World!<h1> <br/><h2> Hostname:  {socket.gethostname()}<h2>\n"""

@app.route('/test/')
def test():
    return "testing page.........."


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)
