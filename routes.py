import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
  return render_template('home.html')

if __name__ = '__main__':
    app.run(debug=True, use_reloader=True)