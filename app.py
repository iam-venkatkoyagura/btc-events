from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def btc_events():
    return render_template('home.html')