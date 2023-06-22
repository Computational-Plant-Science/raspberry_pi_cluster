"""
Version: 1.0
Imaging Unit manual operate
Author: Xiaomeng Shi
Author-email: vsimon2013@gmail.com

USAGE

python3 cluster_capture_syn.py -s 1 -n 360 

python cluster_capture_syn.py -s 1 -n 360 

"""
import time
from time import sleep
import RPi.GPIO as gpio 
from datetime import date, datetime

import argparse
import subprocess, os
import sys

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

################################
#Vertical motor movement

def VMotor_move(mm):
    start_time = time.time()
    #gpio.cleanup()
    VMotor = Stepper([11,9]) #Vertical motor

    ppr = 400  #pules per rev
    rpm = 180  #rev per min

    speed = rpm*ppr/60
    
    mm1= abs(mm)
    steps=mm1/8.000*ppr 
             
    if mm > 0: VMotor.step(steps, "cw", speed,ppr)
          
    if mm < 0: VMotor.step(steps, "ccw", speed,ppr)
      
    VMotor.cleanGPIO
    #print("Move to height {0}...\n".format(mm))
    
    cost_time = time.time() - start_time
    
    #print("cost_time for motor's movement is {0}...\n".format(cost_time))
    
    return cost_time

################################
#root picker
#root picker on relay1=gpio23
#LED on relay2=gpio18
#relay3=gpio15
#relay4=gpio14
'''
def root_picker(SoleOn):
      
    gpio.setmode(gpio.BCM)
    
    Sole_pin = 23
    #set gpio pins
    gpio.setup(Sole_pin, gpio.OUT)
    
    if SoleOn == True: 
        gpio.output(Sole_pin, False)
        print("Solenoid is on.")

    if SoleOn == False: 
        gpio.output(Sole_pin, True)
        print("Solenoid is off.")
        gpio.cleanup()


def Initial_motors():
    gpio.setmode(gpio.BCM)
    gpio.setup(16, gpio.IN, pull_up_down=gpio.PUD_UP)
    gpio.setup(24, gpio.IN, pull_up_down=gpio.PUD_UP)
    while gpio.input(24) == True: VMotor_move(-1)
    print("Motors were initialled")
    gpio.cleanup
'''

def start_img(offset, image_number):
    '''
    #cmd_line = "ssh pi@" + ''.join(host_adr) + ' python FTP_uploadtohost.py -name ' + ''.join(root_name) + ' -host ' + ''.join(FTPhost_name)
    #cmd_line = "mpiexec --host 192.168.0.101,192.168.0.102,192.168.0.103,192.168.0.104,192.168.0.105,192.168.0.106,192.168.0.107,192.168.0.108,192.168.0.109,192.168.0.110 -n 10 python code/cam/img_Triproc.py -r 1 -s " + ''.join(offset) + ' -n ' + ''.join(image_number) + ' -name ' + ''.join(root_name) + ' -host ' + ''.join(FTPhost_name)
    cmd_line = "mpiexec --host 192.168.0.101,\
                            192.168.0.102,\
                            192.168.0.103,\
                            192.168.0.104,\
                            192.168.0.105,\
                            192.168.0.106,\
                            192.168.0.107,\
                            192.168.0.108,\
                            192.168.0.109,\
                            192.168.0.110\
                             -n 10 python code/cam/img_only.py -r 1 -s " + str(offset) + ' -n ' + str(image_number) + ' -name ' + str(root_name) +  ' -time ' + str(timenow)
    print(cmd_line)   
    '''
    
    #returned_value = subprocess.call(cmd_line, shell=True)
    
    PiController = "192.168.0.110,"
    
    host_list = []
    
    #for i in range(101,110):
    for i in range(101,110):
        a = ("192.168.0.%i," %i)
        host_list.append(a)
    
    str_host_list = ''.join(host_list)
    
    str_host_list = str_host_list.rstrip(',')
    
    cmd_line = "mpiexec -host " + PiController + str_host_list \
    + " python img_capture_pi.py -r 1 -s " + str(offset) + " -n " + str(image_number)
    
    print(cmd_line)

    
    #cmd_line = "ls && ls -la"
    
    try:
        #subprocess.check_output(cmd_line)
        os.system(cmd_line)
        print("Image capture task finished successfully by camera cluster...\n")
    except OSError:
        print("Failed ...!\n")
    
    



def upload_img(root_name, FTPhost_name):
    
    cmd_line = "mpiexec --host 192.168.0.101,192.168.0.102,192.168.0.103,192.168.0.104,192.168.0.105 -n 5 python upload_img.py"  + ' -name ' + str(root_name) + ' -host ' + str(FTPhost_name) 
    print(cmd_line)   
    returned_value = subprocess.call(cmd_line, shell=True)
    cmd_line = "mpiexec --host 192.168.0.106,192.168.0.107,192.168.0.108,192.168.0.109,192.168.0.110 -n 5 python upload_img.py"  + ' -name ' + str(root_name) + ' -host ' + str(FTPhost_name) 
    print(cmd_line) 
    returned_value = subprocess.call(cmd_line, shell=True)



def main(args):


    #pasre paramters 
    ap = argparse.ArgumentParser()
    ap.add_argument("-s", "--step_angle", type = int, required = True, help = "step angle for every motor movement")
    ap.add_argument("-n", "--image_number", type = int, required = True, help="Motor move angle range")
    #ap.add_argument("-name", "--root_name", type = str, required = True, help="Root name")
    #ap.add_argument("-host", "--FTPhost_name", type = str, required = True, help="Host IP")
    args = vars(ap.parse_args())
    
    # setting path to model file
    global root_name, FTPhost_name, offset, image_number, root_name, FTPhost_name
    
    #resoltuion = resolution_choose(args["resolution"])
    offset = args['step_angle']
    image_number = args['image_number']
    #root_name = args['root_name']
    #FTPhost_name = args['FTPhost_name']

    #timenow = datetime.now()
    timenow = date.today()
    print(timenow)
    
    if offset > 0: print("Imaging direction: ======>>>>>>>")
    if offset < 0: print("Imaging direction: <<<<<<<======")
    
    global ppr, rpm, speed
    
    #Go to initial position of all motors
   
    start_img(offset, image_number)
    
    
    #upload_img(root_name, FTPhost_name)
    
    #wait the motor to move
    #VMotor_move(-335)

    
    
if __name__ == '__main__':
    
    sys.exit(main(sys.argv))
    

