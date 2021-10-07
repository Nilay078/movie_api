from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.secret_key = 'sessionKey'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/movie_database'

db = SQLAlchemy(app)

import base.com.controller
