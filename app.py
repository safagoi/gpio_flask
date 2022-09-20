from flask import Flask, render_template
from gpiozero import LED

app = Flask(__name__)

red = LED(17)
red_status = 0

@app.route("/")
def main():
    return render_template("app.html")

@app.route("/on")
def on():
    global red_status

    if red_status == 0:
        print("LED is on")
        red.on()
        red_status = 1
        return ("", 200)
    
    return ("", 204)


@app.route("/off")
def off():
    global red_status

    if red_status == 1:
        print("LED is off")
        red.off()
        red_status = 0
        return ("", 200)

    return ("", 204)