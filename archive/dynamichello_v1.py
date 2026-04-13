# Program to return a customized greeting to the user
# Programmer: Mukul Dharwadkar
# Date: 20 May 2020
# Python version: 3.7

import json
import sys

def call_name():
    #print("A response to user")

    with open(sys.argv[1], "r") as file1:
        resp = json.load(file1)
    return resp
num = json.dumps(call_name())
name = json.loads(num)
print(f"My name is : {name['body']}")
print(name['headers'])