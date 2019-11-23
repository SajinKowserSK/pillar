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


def detect_faces(photo):

    imageSource = open(photo, 'rb')

    response = rekog_client.detect_faces(
        Image={'Bytes': imageSource.read()}, Attributes=['ALL'])

    data = response['FaceDetails'][0]
    res = {'AgeRange': data['AgeRange'],
           'Gender': data['Gender'], 'Emotion': [x['Type'] for x in data['Emotions'] if x['Confidence'] == max([x['Confidence'] for x in data['Emotions']])][0]}
    return res


def compare_faces(sourceFile, targetFile):

    imageSource = open(sourceFile, 'rb')
    imageTarget = open(targetFile, 'rb')

    response = rekog_client.compare_faces(SimilarityThreshold=70,
                                          SourceImage={
                                              'Bytes': imageSource.read()},
                                          TargetImage={'Bytes': imageTarget.read()})

    imageSource.close()
    imageTarget.close()
    return len(response['FaceMatches'])


def face_eval(sourceFile, targetFile):
    details = detect_faces(sourceFile)
    match = compare_faces(sourceFile, targetFile)
    res = {'match': match, 'details': details}
    return jsonify(res)
