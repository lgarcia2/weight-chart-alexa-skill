#!/usr/local/bin/python

import os

path = "."

for root, directories, files in os.walk(path, topdown=False):
    for name in files:
        if 'serverless.yml' in name:
            file_path = os.path.join(root, name)
            with(file_obj = open(file_path,'r')):
                for line in fileObj.readlines():
                    if 'alexaSkill' in line and 'amzn1.ask.skill' in line
                        print("Don't commit the Alexa Skill Id in the serverless.yml file.")
                        print(file_path)
                        exit(1)
exit(0)
