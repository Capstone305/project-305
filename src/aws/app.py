from flask import *
app = Flask(__name__, template_folder='../templates', static_folder='../static')

# Import all routes
from routes import *
