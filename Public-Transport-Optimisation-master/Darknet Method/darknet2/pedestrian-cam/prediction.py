import cv2
import time
import subprocess
import sys

        #      last = time.time()

        img = cv2.imread('hcl.JPG')

#ret, .read()

        # Convert to RGB
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2RGRAY);
        
        #        cv2.imwrite('cam.png', frame)
        
        cmd = "./darknet detector test cfg/coco.data cfg/yolo.2.0.cfg yolo.2.0.weights cam.png"# optional flag: -thresh .2"

        output = subprocess.check_output(cmd.split())

        output = output.decode("utf-8").split("\n")
        
        # Count the number of lines that contain "person"
        numPeople = len([i.split(":")[0] for i in output if i.split(":")[0] == 'person'])

        print(output[0])
        print("{} - {} people detected.".format(time.strftime("%d %b %Y %H:%M:%S", time.localtime()), numPeople))
