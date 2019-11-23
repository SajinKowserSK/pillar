# Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)

import boto3
import json
from flask import jsonify

aws_access_key_id = 'AKIAJ5DU42PGNQXHXJGA'
aws_secret_access_key = 'PZldHluM3ZPBKSoltMMiLsqN/C2XxZ/HisCPyJY6'
region = 'us-east-1'

rekog_client = boto3.client(service_name='rekognition',
                            region_name=region,
                            aws_access_key_id=aws_access_key_id,
                            aws_secret_access_key=aws_secret_access_key)

def detect_faces(photo, bucket):

    response = rekog_client.detect_faces(
        Image={'S3Object': {'Bucket': 'shaman-faces', 'Name': photo}}, Attributes=['ALL'])

    print('Detected faces for ' + photo)
    for faceDetail in response['FaceDetails']:
        print('The detected face is between ' + str(faceDetail['AgeRange']['Low'])
              + ' and ' + str(faceDetail['AgeRange']['High']) + ' years old')
        print('Here are the other attributes:')
        print(json.dumps(faceDetail, indent=4, sort_keys=True))
    return len(response['FaceDetails'])


def compare_faces(sourceFile, targetFile):

    imageSource = open(sourceFile, 'rb')
    imageTarget = open(targetFile, 'rb')

    response = rekog_client.compare_faces(SimilarityThreshold=80,
                                          SourceImage={
                                              'Bytes': imageSource.read()},
                                          TargetImage={'Bytes': imageTarget.read()})

    for faceMatch in response['FaceMatches']:
        position = faceMatch['Face']['BoundingBox']
        similarity = str(faceMatch['Similarity'])
        print('The face at ' +
              str(position['Left']) + ' ' +
              str(position['Top']) +
              ' matches with ' + similarity + '% confidence')

    imageSource.close()
    imageTarget.close()
    res = {'match': len(response['FaceMatches'])}
    return jsonify(res)
