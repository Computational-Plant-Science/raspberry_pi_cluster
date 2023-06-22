
"""
Version: 1.0
Capture images using usb cameras controller by raspberry pi clutsers
Author: Xiaomengshi, suxing liu
Author-email: suxingliu@gmail.com

USAGE


python snap_image_buffer.py -r 1 -s 1 -n 360 


"""
#import sys
#sys.path.append("../python-common")

from time import sleep
import RPi.GPIO as gpio 
#import exitHandler #uncomment this and line 58 if using exitHandler

##############################
import argparse
import subprocess, os
import sys

import common
import TIS
import cv2

from gi.repository import Tcam, Gst

import time
from time import sleep
from datetime import date, datetime

import shutil
###############################



class Stepper:
    #instantiate stepper 
    #pins = [stepPin, directionPin, enablePin]
    def __init__(self, pins):
        #setup pins
        self.pins = pins
        self.stepPin = self.pins[0]
        self.directionPin = self.pins[1]
        #self.enablePin = self.pins[2]
        
        #use the broadcom layout for the gpio
        gpio.setmode(gpio.BCM)
        
        #set gpio pins
        gpio.setup(self.stepPin, gpio.OUT)
        gpio.setup(self.directionPin, gpio.OUT)
        #gpio.setup(self.enablePin, gpio.OUT)
        
        #set enable to high (i.e. power is NOT going to the motor)
        #gpio.output(self.enablePin, True)
        

        #print("Stepper initialized (step=" + str(self.stepPin) + ", direction=" + str(self.directionPin) + ")")
    
        #print("Stepper initialized (step=" + str(self.stepPin) + ", direction=" + str(self.directionPin) + ", enable=" + str(self.enablePin) + ")")
    
    #clears GPIO settings
    def cleanGPIO(self):
        gpio.cleanup()
      
    #step the motor
    # steps = number of steps to take
    # dir = direction stepper will move
    # speed = defines the denominator in the waitTime equation: waitTime = 0.000001/speed. As "speed" is increased, the waitTime between steps is lowered
    # stayOn = defines whether or not stepper should stay "on" or not. If stepper will need to receive a new step command immediately, this should be set to "True." Otherwise, it should remain at "False."
    def step(self, steps, dir, speed, ppr):
        #set enable to low (i.e. power IS going to the motor)
        #gpio.output(self.enablePin, False)
        
        #set the output to true for left and false for right
        turnLeft = True
        if (dir == 'cw'):
            turnLeft = False;
        elif (dir != 'ccw'):
            print("STEPPER ERROR: no direction supplied")
            return False
        gpio.output(self.directionPin, turnLeft)


        
        waitTime = 1.000000/speed #waitTime controls speed
        

        stepCounter = 0
        while stepCounter < steps:
            #gracefully exit if ctr-c is pressed
            #exitHandler.exitPoint(True, cleanGPIO)

            #turning the gpio on and off tells the easy driver to take one step
            gpio.output(self.stepPin, True)
            sleep(waitTime/2)
            gpio.output(self.stepPin, False)
            sleep(waitTime/2)
            stepCounter += 1
            #print(stepCounter)
 
            #wait before taking the next step thus controlling rotation speed
           
        gpio.output(self.stepPin, True)
        #print("stepperDriver complete (turned " + dir + " " + str(steps) + " steps)")


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
        shutil.rmtree(path)
        os.makedirs(path)
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



################################
#Chamber motor movement

def CMotor_move(step_angle):
    start_time = time.time()
    #gpio.cleanup()
    CMotor = Stepper([2, 3]) #Chamber motor


    ppr = 6400  #pules per rev
    rpm = 10  #rev per min
    speed = rpm*ppr/60
    
    degree= abs(step_angle)
    steps=ppr*degree*31.415926/360 #steps for each degree interval
             
    if step_angle > 0: CMotor.step(steps, "cw", speed,ppr)
          
    if step_angle < 0: CMotor.step(steps, "ccw", speed,ppr)
      
    CMotor.cleanGPIO
    
    #print("Move to angle {0}...\n".format(step_angle))
    
    cost_time = time.time() - start_time
    
    #print("cost_time for motor's movement is {0}...\n".format(cost_time))
    
    return cost_time


# capture and save images
def write_img(image, serial_no, step_angle):
    
    #count the time for capture and write images
    start_time = time.time()
    
    error = 0
    
    if image is not None:
        
        #define image name
        #img_name = save_path + str(serial_no) + '-' + "{:%Y-%m-%d-%H-%M-%S}.jpg".format(datetime.now())
        
        img_name = save_path + str(serial_no) + '-' + "{0:03d}.jpg".format(step_angle)
        
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


def capture_img(serials):

    #check camera number and series nom shoudl be 1 
    if len(serials) > 1:
        print("More than 1 cameras was connected to one pi unit!")
    elif len(serials) > 0:
        single_serial = '"' + str(serials[0]) + '"'
        print("Camera series no was {}\n".format(single_serial))

    
    resolution_list = [x.strip() for x in resolution.split(',')]
    
    #initialize camera 
   
    Tis = TIS.TIS()
    
    #Tis.openDevice("39020464", 5472, 3648, "18/1", TIS.SinkFormats.BGRA, False)
    
    Tis.openDevice("39020464", int(resolution_list[0]), int(resolution_list[1]), str(resolution_list[2]), TIS.SinkFormats.BGRA, False)
       
    #print(type(Tis.serialnumber))
    #print(type(Tis.height))
    #print(type(Tis.width))
    #print(type(Tis.framerate))
    
    Tis.Start_pipeline()  # Start the pipeline so the camera streams
    
    # setup camera paramters
    Tis.Set_Property("Gain Auto",False)
    Tis.Set_Property("Gain",959)
    
    Tis.Set_Property("Exposure Auto",False)
    Tis.Set_Property("Exposure", 28949)
    
            
    #initialize step angle motor will move to
    step_angle = 0

    #warn up camera video stream 
    #cv2.waitKey(1)

    #capture image pipeline, keep camera open and streaming  
    for index in range(0, image_number):

        print("capturing and writing image \n")
        
        step_angle+= offset
        
        #loop all cameras
        if Tis.Snap_image(1) is True: 
            
            #get image from buffer 
            image = Tis.Get_image()
            
            #save image
            (cost_time, error) = write_img(image, str(serials[0]), step_angle)

            #print("current image is {0}\n".format(idx))
        
        #wait the motor to move to next angle
        #time.sleep(CMotor_move(step_angle))
        time.sleep(0.1)
    
    
    #close cameras after motor move to final step and cameras finished all images capturing 
    Tis.Stop_pipeline()
    print('Camera {0} capture pipeline was stopped!\n'.format(serials[0]))
    
        

def resolution_choose(resolution):
    switcher = {
        1: '5472, 3648, "18/1"',        #1: '3872, 2764, 3, 1,',
        2: '3840, 2160, "31/1"',
        3: '2736, 1824, "36/1"'
    }
    return switcher.get(resolution, "Invalid resolution choice")


def main(args):

    #pasre paramters 
    ap = argparse.ArgumentParser()
    ap.add_argument('-r', '--resolution', type = int, required = True, help = '"1" is 3872X2764, fps = 3' 
                    + '"2" is 3840X2160, fps = 4' + '"3" is 2560X1440, fps = 10')
    ap.add_argument("-s", "--step_angle", type = int, required = True, help = "step angle for every motor movement")
    ap.add_argument("-n", "--image_number", type = int, required = True, help="Motor move angle range")

    args = vars(ap.parse_args())
    
    # setting path to model file
    #global resoltuion, offset, image_number, root_name, hostname, save_path, today
    
    global resolution, offset, image_number, save_path
    
    global ppr, rpm, speed
    
    resolution = resolution_choose(args["resolution"])
    
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
    
    print(len(serials))
    #setup saving path for captured images
    today = str(date.today())
    current_path = os.getcwd()
    
    # save folder construction
    mkpath = current_path +'/' + today
    mkdir(mkpath)
    save_path = mkpath + '/'

    capture_img(serials)
    



if __name__ == '__main__':
    
    import sys
    sys.exit(main(sys.argv))
    


