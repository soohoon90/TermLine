from flask import Flask
from flaskext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///termline.db'
db = SQLAlchemy(app)

import Termline.models
import Termline.views_generate
import Termline.views_simple
