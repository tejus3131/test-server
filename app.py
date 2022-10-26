from re import T
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/harsh")
def harsh_video():
    return render_template("harsh.html")

if __name__ == "__main__":
    app.run(debug=True)