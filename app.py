from flask import Flask, render_template,g,request
import os
from flask_sqlalchemy import SQLAlchemy
import sqlite3



app = Flask(__name__)





@app.route("/")
def build():
  return render_template('home.html')

@app.route('/video')
def video():
  return render_template('video.html')

@app.route('/contact')
def contact():
  return render_template('contact.html')


if __name__ == "__main__":
  app.run(debug = True)