
"""
Version: 1.0
Capture LED light switch
Author: Xiaomengshi, suxing liu
Author-email: suxingliu@gmail.com

USAGE

python cluster_led.py -s 1
python3 cluster_led.py -s 1


"""
from time import sleep
import RPi.GPIO as gpio 
#import exitHandler #uncomment this and line 58 if using exitHandler

##############################
import argparse
import subprocess, os
import sys


################################
#LED switch
#root picker on relay1=gpio23
#LED on relay2=gpio18
#relay3=gpio15
#relay4=gpio14

######################################


def LED_sw(LEDon):
    
                 
    gpio.setmode(gpio.BCM)
    #led = LED(18)
    LED_pin = 18
    #set gpio pins
    gpio.setup(LED_pin, gpio.OUT)
    
    if LEDon == True: 
        gpio.output(LED_pin, False)
        print("LED is on.")

    if LEDon == False: 
        gpio.output(LED_pin, True)
        print("LED is off.")
        gpio.cleanup()
        
      
def main(args):
    
     #pasre paramters 
    ap = argparse.ArgumentParser()
    ap.add_argument('-s', '--switch', type = int, required = True, help = '"1" is on' 
                    + '"0" is off')
    args = vars(ap.parse_args())
    
    bool_switch = args['switch']
    
    if bool_switch > 0:
        
        LED_sw(True)
        print("Turn on all LED lights...")
        
    else:
        LED_sw(False)
        print("Turn off all LED lights...")

if __name__ == '__main__':
    
    import sys
    sys.exit(main(sys.argv))


