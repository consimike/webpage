from flask import Flask, render_template,g,request
import os
from flask_sqlalchemy import SQLAlchemy
import sqlite3



app = Flask(__name__)

# db = SQLAlchemy()

# conn = sqlite3.connect('survey.db')
# print ("Opened database successfully")

# c = conn.cursor()

# c.execute(""" CREATE TABLE IF NOT EXISTS survey  (
#   id INTEGER PRIMARY KEY AUTOINCREMENT,
#   a1 TEXT,
#   a2 TEXT,
#   a3 TEXT,
#   a4 TEXT
# )""")

# print ("Table created successfully")


# conn.commit()




@app.route("/")
def build():
  return render_template('home.html')

@app.route('/video')
def video():
  return render_template('video.html')
# @app.route("/build", methods = ['POST', 'GET'])
# def build():
#   if request.method == 'POST':
#     try:
#       a1 = request.form['a1']
#       a2 = request.form['a2']
#       a3 = request.form['a3']
#       a4 = request.form['a4']

#       with sqlite3.connect('survey.db') as con:
#         c = con.cursor()
#         c.execute("INSERT INTO survey (a1,a2,a3,a4) VALUES (?,?,?,?)",(a1,a2,a3,a4))
#         con.commit()
#         msg = "Success"

#     except:
#       con.rollback()
#       msg = "error"

#     finally:
#       return render_template("home.html", msg = msg)
#       con.close()

# @app.route('/list')
# def list():
#    con = sqlite3.connect("survey.db")
#    con.row_factory = sqlite3.Row
   
#    cur = con.cursor()
#    cur.execute("select * from survey")
   
#    rows = cur.fetchall() 
#    return render_template("home.html",rows = rows)


if __name__ == "__main__":
  app.run(debug = True)