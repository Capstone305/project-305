from flask import Flask
app = Flask(__name__)

@app.route('/test')
def testing():
    return "Hello World!"

if __name__ == '__main__':
    print("test")
    app.run()