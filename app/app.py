from flask import Flask
import socket
import datetime
import os

app = Flask(__name__)

@app.route("/")
def home():
    return f"""
    <html>
    <head>
        <title>Private GKE-Demo</title>
    </head>
    <body style="font-family:Arial;text-align:center;margin-top:60px;">
        <h1> Private GKE-Demo</h1>
        <h2>Application Running Successfully!</h2>

        <p><b>Version:</b> 1.0</p>

        <p><b>Hostname:</b> {socket.gethostname()}</p>

        <p><b>Environment:</b> {os.getenv("ENV","Production")}</p>

        <p><b>Current Time:</b> {datetime.datetime.now()}</p>

    </body>
    </html>
    """

@app.route("/health")
def health():
    return {
        "status":"healthy"
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080)
