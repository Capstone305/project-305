from flask import *
app = Flask(__name__)

print("Print statements from Flask should work.")

@app.route('/test2')
def testing2():
    return "Hello World Again!"

@app.route("/submitform", methods=["GET", "POST"])
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
    return render_template("../../templates/loading.html")

if __name__ == '__main__':
    print("Flask app is up and running.")
    app.run()