from flask import Flask, request, render_template
app = Flask(__name__, template_folder='../templates', static_folder='../static')


@app.route("/")
def home():
    '''
    Displays the homepage.
    '''

    return render_template("index.html")


@app.route("/processing", methods=["GET", "POST"])
def form_response():
    '''
    Gets the video uploaded by the user.
    '''

    import os
    print(os.getcwd())

    if request.method == 'POST':
        # User has submitted form
        print("A post request has been submitted.")

    print("Form response recieved.")
    return render_template("loading.html")


@app.route("/finished", methods=["GET"])
def finished():
    '''
    Displays the download page.
    '''

    return render_template("../templates/download.html")


if __name__ == '__main__':
    print("Flask app is up and running.")
    app.run()
