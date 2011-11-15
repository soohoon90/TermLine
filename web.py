import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for \
                abort, 
from werkzeug import secure_filename

# configuration
DATABASE = 'flaskr.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def index():
    return render_template('index.html')
 
@app.route('/hello')
def hello():
    return 'Hello World'

@app.route('/test/')
@app.route('/test/<name>')
def test(name=None):
    return render_template('test.html', name=name)

@app.route('/upload', methods=['GET','POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            print "saved"
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    # GET
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
