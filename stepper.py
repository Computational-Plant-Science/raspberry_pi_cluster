"""
Version: 1.0
Test step motor 
Author: suxing liu
Author-email: suxingliu@gmail.com

USAGE

python stepper.py

"""

from motor import Motor

from time import sleep
import RPi.GPIO as GPIO

 
if __name__ == "__main__":
    
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    
    m = Motor([18,22,24,26])
    m.rpm = 2
    m.mode = 2
    
    print "Pause in seconds: " + `m._T`
    
    #m.move_to(-10)
    
    #sleep(1)
    
    
    '''
    
    step_angle = 0
      
    offset = 10
    
    index = 1
    
    while (step_angle < 330):
        
        step_angle+= offset
        m.move_to(step_angle)
        sleep(1)
        print("Move to angle {0} ...\n".format(step_angle))
        print("Move to position {0} ...\n".format(index))
        index+=1
    
    '''
    ind = 1
    offset = -65
    step_angle = 0
      
    for ind in range(1, 6):
        step_angle+= offset
        m.move_to(step_angle)
        sleep(1)
        ind+= 1
        print("Move to angle {0} ...\n".format(step_angle))
    
    
    
    GPIO.cleanup()
