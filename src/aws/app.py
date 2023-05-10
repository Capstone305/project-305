from flask import Flask
app = Flask(__name__)

@app.route('/test')
def testing():
    return "Hello World!"

from routes import *

if __name__ == '__main__':
    print("Flask app is up and running.")
    app.run()