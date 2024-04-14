import sqlite3
import pandas as pd
from flask import Flask, render_template
app = Flask(__name__)

conn = sqlite3.connect("pokemon.db") 
cur = conn.cursor()
df = cur.execute("SELECT * FROM pokemon LIMIT 1").fetchall()

conn = sqlite3.connect("games.db") 
cur = conn.cursor()
df2 = cur.execute("SELECT * FROM games LIMIT 1").fetchall()

@app.route('/')
def home():
    items = df
    return render_template('welcome.html', items=items)

@app.route('/about/db1')
def about1():
    items = df
    return render_template('about1.html', items=items)

@app.route('/about/db2')
def about2():
    items = df2
    return render_template('about2.html', items=items)

@app.route('/classification')
def classification():
    items = df
    return render_template('about2.html', items=items)

@app.route('/regression')
def regression():
    items = df
    return render_template('about2.html', items=items)

if __name__ == '__main__':
    app.run(debug=True)