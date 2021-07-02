import os
from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
import random
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv('DATABASE_URL')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

@app.route("/")
def index():
    random_number = random.randint(1, 20)
    return render_template('index.html', random_number=random_number)

@app.route("/home")
def home():
    random_number = random.randint(1, 20)
    return render_template("home.html", random_number=random_number)

@app.route("/textos")
def textos():
    random_number = random.randint(1, 20)
    return render_template("textos.html", random_number=random_number)

@app.route("/gifs")
def gifs():
    random_number = random.randint(1, 20)
    return render_template("gifs.html", random_number=random_number)

@app.route("/music")
def music():
    return render_template("music.html")

@app.route("/videos")
def videos():
    return render_template("videos.html")

@app.route("/imagenes")
def imagenes():
    return render_template("imagenes.html")

@app.route("/autor")
def autor():
    return render_template("autor.html")



def main():
    db.create_all()

if __name__ == "__main__":
    with app.app_context():
        main()
    app.run(debug=True)