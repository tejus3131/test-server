from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
Title = "TheHarshBlogs"


@app.route("/")
def hello_world():
    return render_template("index.html", title = Title)


@app.route("/blogs/<type>")
def blogs(type):
    return render_template("blogs.html", title = Title, blogs = type)


if __name__ == "__main__":
    app.run(debug=True)