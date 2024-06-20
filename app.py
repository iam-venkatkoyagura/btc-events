from flask import Flask, render_template
from database import get_data

app = Flask(__name__)

@app.route("/")
def btc_home():
    events = get_data()
    return render_template('home.html', events=events)

@app.route("/events")
def btc_events():
    return render_template('events.html')