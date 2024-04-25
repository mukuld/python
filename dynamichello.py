# Program to return a customized greeting to the user
# Programmer: Mukul Dharwadkar
# Date: 20 May 2020
# Python version: 3.7

import json
import sys

def call_name():
    #print("A response to user")

    resp = {
        "statusCode": 200,
        "headers": {
            "Allow-Control-Allow-Origin": "*",
        },
        "body": "Nandini Dharwadkar"
    }

    return resp
num = json.dumps(call_name())
name = json.loads(num)
print(name['body'])