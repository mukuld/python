import os
import sys
import subprocess

#path = "/Users/dharmuku/Documents/Personal/src/python/"
file = open("merge_conflict.txt", "r")
for line in file:
    subprocess.run(["git", "add", line])
    #print(line)