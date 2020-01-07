
"""
Version: 1.0
Capture images using usb cameras
Author: suxing liu
Author-email: suxingliu@gmail.com

USAGE

python capture.py

"""

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


def move_img(host_address):
    
    cmd_line = "scp " + host_address + save_path + "*.jpg " + save_path

    try:
        #subprocess.call(cmd_line + [str(img_name)])
        os.system(cmd_line)
        print("Captured image was moved to controller pi...\n")
    except OSError:
        print("Failed moving image!\n")



def capture_img(serial_no, save_path):
    
    #initialize camera object with serial number
    #cam = TIS.TIS(serial_no, 3872, 2764, 3, 1, True)
    cam = TIS.TIS(serial_no, 3840, 2160, 4, 1, True)
    #cam = TIS.TIS(serial_no, 2560, 1440, 10, 1, True)


    #Start the pipeline
    cam.Start_pipeline()
    
    cv2.waitKey(10)
    
    #capture image from buffer
    image = cam.Get_image()
    
    #save image
    if image is not None:
        
        error = 0
        
        img_name = "{:%Y-%m-%d-%H-%M-%S}.jpg".format(datetime.now())
        img_name = save_path + str(serial_no) + '-' + img_name
        
        #print('\n')
        
        if cv2.imwrite(img_name, image) is True:
            print('Image capture finished...\n')
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
        error = error + 1

    cam.Stop_pipeline()

    

def main(args):
    
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
    
    
    # capture all images from device list
    for serial in serials:
        capture_img(serial, save_path)
    
    
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
