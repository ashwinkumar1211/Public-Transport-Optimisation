#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Created on Sun Aug 26 06:34:35 2018
    
    @author: ashishputtaa
    """
import cv2
#import time
import subprocess
#img = cv2.imread('hcl.JPG')
# Convert to RGB
#img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cmd = "./darknet detect cfg/yolov3.cfg yolov3.weights ../Stop_Samples/11.jpg"# optional flag: -thresh .2
output = subprocess.check_output(cmd.split())
output = output.decode("utf-8").split("\n")

# Count the number of lines that contain "person"
numPeople = len([i.split(":")[0] for i in output if i.split(":")[0] == 'person'])
print(output[0])
print("{} - {} people detected.", numPeople)

