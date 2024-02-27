from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from flask_bcrypt import Bcrypt
import os

# Set the environment variable
os.environ['DB_URI'] = 'mysql+pymysql://root:Gangara4@localhost/social_media'

# Create the Flask application instance
app = Flask(__name__)
app.config.from_object(Config)

load_dotenv()  # Corrected missing parentheses

# Secret key
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')  # Using getenv instead of get

# db configurations
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URI')  # Using getenv instead of get
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize extensions
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from app.routes.root import *
from app.routes.user import *
from app.models.user import *
