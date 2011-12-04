from flask import Flask, request, redirect, url_for, render_template, session

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


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
    return redirect(url_for('index'))

@app.route('/config', methods=['GET', 'POST'])
def config():
    if request.method == 'POST':
        # session['username'] = request.form['username']
        redirect(url_for('config'))
    return render_template('config.html')
    
@app.route('/logout')
def logout():
    # remove the username from the session if its there
    session.pop('username', None)
    return redirect(url_for('index'))