from flask import *
app = Flask(__name__, template_folder='../templates', static_folder='../static')

from routes import *
