#Copyright 2020 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-custom-labels-developer-guide/blob/master/LICENSE-SAMPLECODE.)

import boto3
import time


def stop_model(model_arn):

    client=boto3.client('rekognition')

    print('Stopping model:' + model_arn)

    #Stop the model
    try:
        response=client.stop_project_version(ProjectVersionArn=model_arn)
        status=response['Status']
        print ('Status: ' + status)
    except Exception as e:  
        print(e)  

    print('Model has successfully been terminated.')
    
def stop_mmb_model():
    
    model_arn='arn:aws:rekognition:us-east-2:418857082272:project/pedestrian_detection_v2/version/pedestrian_detection_v2.2023-04-20T11.00.54/1682013654262'
    stop_model(model_arn)

if __name__ == "__main__":
    stop_mmb_model() 