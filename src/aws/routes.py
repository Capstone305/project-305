from app import *

@app.route("/home", methods=["GET"])
def home():
    '''
    Displays the homepage.
    '''

    return render_template("../templates/index.html")

@app.route("/processing", methods=["GET"])
def processing():
    '''
    Displays the loading page.
    '''
    print("Loading...")
    return render_template("../templates/loading.html")

@app.route("/finished", methods=["GET"])
def finished():
    '''
    Displays the download page.
    '''

    return render_template("../templates/download.html")