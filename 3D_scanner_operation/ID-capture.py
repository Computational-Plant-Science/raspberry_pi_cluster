
"""
Version: 1.0
Capture images using usb cameras
Author: suxing liu
Author-email: suxingliu@gmail.com

USAGE

python ID-capture.py -i 33810555

"""

import argparse

import TIS
import cv2

from gi.repository import Tcam, Gst

#from list_devices import select_camera
import common

import multiprocessing
from multiprocessing import Pool
from contextlib import closing

from datetime import datetime

from datetime import date

import time

import subprocess, os
import sys
import termios
import tty

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
        print path + ' folder constructed!'
        # make dir
        os.makedirs(path)
        return True
    else:
        # if exists, return 
        print path+' path exists!'
        return False


def getKey():
    
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    new = termios.tcgetattr(fd)
    new[3] = new[3] & ~termios.ICANON & ~termios.ECHO
    new[6][termios.VMIN] = 1
    new[6][termios.VTIME] = 0
    termios.tcsetattr(fd, termios.TCSANOW, new)
    key = None
    try:
        key = os.read(fd, 3)
    finally:
        termios.tcsetattr(fd, termios.TCSAFLUSH, old)
    return key


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

def write_img(image, serial_no):
    
    start_time = time.time()
    
    error = 0
    
    if image is not None:
    
        img_name = "{:%Y-%m-%d-%H-%M-%S}.jpg".format(datetime.now())
        img_name = save_path + str(serial_no) + '-' + img_name
        
        #print('\n')
        
        if cv2.imwrite(img_name, image) is True:
            print('Image capture finihed...\n')
            #key = "q"
            
        else:
            print('Image capture failed!\n')
    
        #abs_path = os.path.abspath(img_name)
        
        #cmd_line = 'pyicmd --host data.cyverse.org --port 1247 --user lsx1980 --passwd lsx6327903 --zone iplant put /iplant/home/lsx1980/root-images '.split()        
        '''
        cmd_line = "pyicmd --host data.cyverse.org --port 1247 --user lsx1980 --passwd lsx6327903 --zone iplant put /iplant/home/lsx1980/root-images " + img_name
        
        try:
            #subprocess.call(cmd_line + [str(img_name)])
            os.system(cmd_line)
            print("Captured image was uploaded to cyverse server...\n")
        except OSError:
            print("Failed upload image!\n")
        
        try:
            #subprocess.call(cmd_line + [str(img_name)])
            os.remove(img_name)
        except OSError:
            print("Failed delete image!\n")
        '''
    else:
        print("No image reveived\n")
        error =  1
    
    cost_time = time.time() - start_time

    print("cost_time {} \n".format(cost_time))
            
    return cost_time, error


def capture_img(serial_no):
    
    #initialize camera object with serial number
    #cam = TIS.TIS(serial_no, 3872, 2764, 3, 1, True)
    #cam = TIS.TIS(serial_no, 3840, 2160, 4, 1, True)
    #cam = TIS.TIS(serial_no, 2560, 1440, 10, 1, True)
    
    cam = TIS.TIS(serial_no, 3840, 2160, 4, 1, True)

    #Start the pipeline
    cam.Start_pipeline()
    
    cv2.waitKey(10)
    
    print("Read to capture image from buffer\n")

    '''
    print("Gain Auto : %s " % cam.Get_Property("Gain Auto").value)
    print("Gain : %d" % cam.Get_Property("Gain").value)
    print("Exposure : %d" % cam.Get_Property("Exposure").value)
    
    # Check, whether gain auto is enabled. If so, disable it.
    if cam.Get_Property("Gain Auto").value :
        cam.Set_Property("Gain Auto",False)
        print("Gain Auto now : %s " % cam.Get_Property("Gain Auto").value)

    cam.Set_Property("Gain",16)
    '''
    
    #key = str(getKey())
    '''
    key = "s"
    
    #index_img = 0
    
    while True:

        if key == "q":
            print('Stop capture pipeline!\n')
            cam.Stop_pipeline()
            break
            
        #elif key == "s":
        else:
            print("Start capturing and write image \n")
    
            image = cam.Get_image()

            (cost_time, error) = write_img(image, serial_no)
            
            time.sleep(2.00)
                
            #cam.Stop_pipeline()
    '''
    for index in range(0,5):
        
        print("Start capturing and write image \n")

        image = cam.Get_image()

        (cost_time, error) = write_img(image, serial_no)

        if error == 0:
            index+=1

        print("current image is {0}\n".format(index))

        time.sleep(1.00)
    
    cam.Stop_pipeline()
    
    

def move_img(host_address):
    
    cmd_line = "scp " + host_address + save_path + "*.jpg " + save_path

    try:
        #subprocess.call(cmd_line + [str(img_name)])
        os.system(cmd_line)
        print("Captured image was moved to server pi...\n")
    except OSError:
        print("Failed moving image!\n")

def main(args):
    
    ap = argparse.ArgumentParser()
    
    ap.add_argument('-i', '--ID', required = True, help = 'Camera ID')
    
    args = vars(ap.parse_args())
    
    # setting path to model file
    serials_ID = args["ID"]
    
    # init gstreamer
    Gst.init(sys.argv)
    
    if len(sys.argv) > 1:
        if "-h" in sys.argv[1] or "--help" in sys.argv[1]:
            print_help()
            return
            
    # we create a source element to retrieve a device list through it
    serials = list_devices()
    
    #serial_no = '12810399'
    
    today = str(date.today())
    
    #print(today)
    
    current_path = os.getcwd()
    
    #print(current_path)
    
    # save folder construction
    mkpath = current_path +'/' + today
    mkdir(mkpath)
    global save_path
    save_path = mkpath + '/'
    
    print('')
    print("Capturing images using avaliable devices...\n")

    capture_img(serials_ID)
    
    '''
    #move file to PiController
    host_list = ["192.168.1.138:","192.168.1.148:","192.168.1.108:","192.168.1.141:"]
   
    # get cpu number for parallel processing
    agents = multiprocessing.cpu_count()
    
    # perfrom crop action based on bouding box results in parallel way
    with closing(Pool(processes = agents)) as pool:
        pool.map(move_img, host_list)
        pool.terminate()
    '''
    
    
    

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
