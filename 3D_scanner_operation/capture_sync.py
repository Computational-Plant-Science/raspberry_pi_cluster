
"""
Version: 1.0
Capture images using usb cameras controller by raspberry pi clutsers
Author: suxing liu
Author-email: suxingliu@gmail.com

USAGE

python capture_sync.py -r 1 -s 1 -n 360

"""

import argparse
import subprocess, os
import sys

import common
import TIS
import cv2

from gi.repository import Tcam, Gst

from motor import Motor
import RPi.GPIO as GPIO

import time
from time import sleep
from datetime import date, datetime

import multiprocessing
from multiprocessing import Pool
from contextlib import closing

# generate foloder to store the output results
def mkdir(path):
 
    # remove space at the beginning
    path=path.strip()
    # remove slash at the end
    path=path.rstrip("\\")
 
    # path exist?   # True  # False
    isExists=os.path.exists(path)
 
    # process
    if not isExists:
        # construct the path and folder
        print(path + ' folder constructed!\n')
        # make dir
        os.makedirs(path)
        return True
    else:
        # if exists, return 
        print(path+' path exists!\n')
        return False


# list all cameras connecting to the motherboard 
def list_devices():
    
    #create a source element to retrieve a device list through it
    source = Gst.ElementFactory.make("tcambin")
    
    #retrieve all available serial numbers
    serials = source.get_device_serials()
    
    print("Available devices:")

    #output all device infos
    for single_serial in serials:

        # This returns someting like:
        # (True, name='DFK Z12GP031',
        # identifier='The Imaging Source Europe GmbH-11410533', connection_type='aravis')
        # The identifier is the name given by the backend
        # The connection_type identifies the backend that is used.
        #     Currently 'aravis', 'v4l2' and 'unknown' exist
        (return_value, model,
         identifier, connection_type) = source.get_device_info(single_serial)

        # return value would be False when a non-existant serial is used
        # since we are iterating get_device_serials this should not happen
        if return_value:
            
            print("Model: {} Serial: {} Type: {}".format(model,
                                                         single_serial,
                                                         connection_type))
    return serials


# capture and save images
def write_img(image, serial_no):
    
    #count the time for capture and write images
    start_time = time.time()
    
    error = 0
    
    if image is not None:
        
        #define image name
        img_name = save_path + str(serial_no) + '-' + "{:%Y-%m-%d-%H-%M-%S}.jpg".format(datetime.now())
        
        # check write image status 
        if cv2.imwrite(img_name, image) is True:
            print('Image capture finihed...\n')
        else:
            print('Image capture failed!\n')
    

    else:
        print("No image reveived\n")
        error =  1
    
    cost_time = time.time() - start_time

    #output cost time
    print("cost_time for capture images is {0} \n".format(cost_time))
            
    return cost_time, error

#control motor movement
def motor_move(m, step_angle):

    start_time = time.time()
    
    m.move_to(step_angle)
    
    print("Move to angle {0}...\n".format(step_angle))
    
    cost_time = time.time() - start_time
    
    print("cost_time for motor's movement is {0}...\n".format(cost_time))
    
    return cost_time
    
    
def capture_img(serials):
    
    #initialize camera object with serial number
    #cam = TIS.TIS(serial_no, 3872, 2764, 3, 1, True)
    #cam = TIS.TIS(serial_no, 3840, 2160, 4, 1, True)
    #cam = TIS.TIS(serial_no, 2560, 1440, 10, 1, True)
    
    #cam = TIS.TIS(serials[0], 3840, 2160, 4, 1, True)
    
    
    #print("Gain Auto : %s " % cam.Get_Property("Gain Auto").value)
    #print("Gain : %d" % cam.Get_Property("Gain").value)
    #print("Exposure : %d" % cam.Get_Property("Exposure").value)
    
    
    
    
    cam_list = []
    
    for idx, serial in enumerate(serials):
        
        parameter_set = [x.strip() for x in resoltuion.split(',')]
        
        #initialize camera class objects
        #cam_list.append(TIS.TIS(serial, 3872, 2764, 3, 1, True))
        
        cam_list.append(TIS.TIS(serial, int(parameter_set[0]), int(parameter_set[1]), int(parameter_set[2]), int(parameter_set[3]), True))
        
        #Start the pipeline
        cam_list[idx].Start_pipeline()
        
        # Check, whether gain auto is enabled. If so, disable it.
        # setup parameters
        if cam_list[idx].Get_Property("Gain Auto").value:
            
            cam_list[idx].Set_Property("Gain Auto",False)

            cam_list[idx].Set_Property("Exposure Auto",False)

            cam_list[idx].Set_Property("whitebalance-module-enabled", False)    

            cam_list[idx].Set_Property("Gain",100)
            
            cam_list[idx].Set_Property("Exposure", 66666)
            
            
            
        print("Gain Auto : %s \n" % cam_list[idx].Get_Property("Gain Auto").value)
        
        print("Exposure Auto : %s \n" % cam_list[idx].Get_Property("Exposure Auto").value)
        
        print("whitebalance-module-enabled : %s \n" % cam_list[idx].Get_Property("whitebalance-module-enabled").value)
        
        print("Gain : %s \n" % cam_list[idx].Get_Property("Gain").value)
        
        print("Exposure : %s \n" % cam_list[idx].Get_Property("Exposure").value)
        
        '''
        # Check, whether gain auto is enabled. If so, disable it.
        if cam_list[idx].Get_Property("Exposure Auto").value:
            cam_list[idx].Set_Property("Exposure Auto",False)
            #print("Gain Auto now : %s " % cam.Get_Property("Gain Auto").value)
            cam_list[idx].Set_Property("Exposure",333400)
        '''

    #enable pi poard signal output
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    
    #initialize motor 
    # initizlize the pin output on motherboard head
    m = Motor([18,22,24,26])
     
    #define motor rpm 
    m.rpm = 3
    
    #define motor current mode
    m.mode = 2

    #initialize step angle motor will move to
    step_angle = 0
    
    #define angle interval
    #offset = 2
    
    #warn up camera video stream 
    cv2.waitKey(10)
    
    #print("Read to capture image from buffer\n")
    
    #capture image pipeline, keep camera open and streaming  
    for index in range(1, image_number):

        print("capturing and writing image \n")
        
        step_angle+= offset
        
        #loop all cameras
        for idx, serial in enumerate(serials):
            
            #get image from buffer 
            image = cam_list[idx].Get_image()
            
            #save image
            (cost_time, error) = write_img(image, serial)

            #print("current image is {0}\n".format(idx))
        
        #wait the motor to move to next angle
        time.sleep(motor_move(m, step_angle))
    
    
    #close cameras after motor move to final step and cameras finished all images capturing 
    for idx, serial in enumerate(serials):
        cam_list[idx].Stop_pipeline()
        print('Camera {0} capture pipeline was stopped!\n'.format(serial))
    
    '''
    # move imaging arc back to original position
    ind = 1
    interval = -65
    angle = 0
      
    for ind in range(1, 6):
        angle+= interval
        m.move_to(angle)
        sleep(1)
        ind+= 1
        print("Move to angle {0} ...\n".format(angle))
    '''
    
'''
def move_img(host_address):
    
    cmd_line = "scp " + host_address + save_path + "*.jpg " + save_path

    try:
        #subprocess.call(cmd_line + [str(img_name)])
        os.system(cmd_line)
        print("Captured image was moved to server pi...\n")
    except OSError:
        print("Failed moving image!\n")
'''

def resolution_choose(resoltuion):
    switcher = {
        1: '3872, 2764, 3, 1,',
        2: '3840, 2160, 4, 1,',
        3: '2560, 1440, 10, 1,'
    }
    return switcher.get(resoltuion, "Invalid resolution choice")


def main(args):
    
    #pasre paramters 
    ap = argparse.ArgumentParser()
    ap.add_argument('-r', '--resolution', type = int, required = True, help = '"1" is 3872X2764, fps = 3' 
                    + '"2" is 3840X2160, fps = 4' + '"3" is 2560X1440, fps = 10')
    ap.add_argument("-s", "--step_angle", type = int, required = True, help = "step angle for every motor movement")
    ap.add_argument("-n", "--image_number", type = int, required = True, help="Motor move angle range")
    args = vars(ap.parse_args())
    
    # setting path to model file
    global resoltuion, offset, image_number, save_path
    
    resoltuion = resolution_choose(args["resolution"])
    offset = args['step_angle']
    image_number = args['image_number']
    
    # init gstreamer 
    Gst.init(sys.argv)
    
    if len(sys.argv) > 1:
        if "-h" in sys.argv[1] or "--help" in sys.argv[1]:
            print_help()
            return
    
    #retrieve a device list
    serials = list_devices()
    
    #setup saving path for captured images
    today = str(date.today())
    current_path = os.getcwd()
   
    
    # save folder construction
    mkpath = current_path +'/' + today
    mkdir(mkpath)
    save_path = mkpath + '/'
    
    print('')
   
    
    # capture all images from device list
    #for serial in serials:
       #capture_img(serial)

    capture_img(serials)
    
    

 
    
    


if __name__ == '__main__':
    
    import sys
    sys.exit(main(sys.argv))

