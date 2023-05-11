from app import *
from aws_model_start import *
from aws_model_end import *

import string

@app.route("/", methods=["GET"])
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

    # import os
    # print(os.getcwd())

    # When the user presses the submit button:
    if request.method == 'POST':

        # Get the name of the file
        file_name = request.form.get("filename")
        print("The file uploaded is called: " + str(file_name))

        # Get the types of micromobiles to include in the data
        result_skateboard = request.form.get("skateboard-check")
        result_bicycle = request.form.get("bicycle-check")
        result_scooter = request.form.get("scooter-check")
        print("The selected micromobile types are:")
        print("Skateboards:\t" + str(result_skateboard))
        print("Bicycle:\t" + str(result_bicycle))
        print("Scooter:\t" + str(result_scooter))

        # Starts the AWS Rekognition model
        start_mmb_model()

    print("Form response recieved.")
    return render_template("loading.html")


@app.route("/finished", methods=["GET"])
def finished():
    '''
    Displays the download page.
    '''

    return render_template("../templates/download.html")