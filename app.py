from flask import Flask

app = Flask(__name__)

@app.route("/")
def btc_events():
    return "Welcome to BTC Events"