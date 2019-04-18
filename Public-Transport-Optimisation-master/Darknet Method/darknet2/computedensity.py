import cv2
import subprocess


def people_in_stop(loc):

    cmd = "./darknet detect cfg/yolov3.cfg yolov3.weights " + str(loc)
    print(cmd)
    output = subprocess.check_output(cmd.split())
    output = output.decode("utf-8").split("\n")
    
    # Count the number of lines that contain "person"
    numPeople = len([i.split(":")[0] for i in output if i.split(":")[0] == 'person'])
    
    return numPeople


route_weights = []

for i in range(10,15):

    loc = "../Stop_Samples/" + str(i) + ".jpg"
    print(loc)
    density = people_in_stop(loc)
        
    route_weights.append(density)
    
route_weights.append(sum(route_weights))
print(route_weights)
    