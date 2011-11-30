from flask import Flask, render_template

from Termline import app

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/recent')
def recent():
    return render_template('recent.html')

@app.route('/')
def index():
    return render_template('generator.html')