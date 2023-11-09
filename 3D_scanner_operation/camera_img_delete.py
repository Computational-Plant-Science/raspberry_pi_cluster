"""
Version: 1.0
Transfer images from cluster pis to PiContrller, then upload to Cyverse

Author: suxing liu
Author-email: suxingliu@gmail.com

USAGE

python camera_img_delete.py -p /home/pi/code/cam/2018-12-10/ 

"""

import subprocess, os
import sys
import argparse

import multiprocessing
from multiprocessing import Pool
from contextlib import closing

from os.path import relpath

'''
def move_img(host_address):
    
    #cmd_line = "ssh pi@" + ''.join(host_adr) + ' exit'
    
    #cmd_line = "ls && ls -la"
    
    cmd_line = "scp " + host_address + folder_path + "*.jpg " + folder_path
    
    #cmd_line = "scp " + host_address + folder_path + "transfer.zip " + folder_path
    
    #scp 192.168.1.110:/home/pi/code/cam/*.jpg .
    
    print(cmd_line)

    
    try:
        #subprocess.call(cmd_line + [str(img_name)])
        os.system(cmd_line)
        print("Captured images were moved to PiController...\n")
    except OSError:
        print("Failed moving image!\n")
'''

#def upload_img(host_address):

def delete_img(host_address):
    
    host_add = host_address.replace(":", "")
    
    #delete_cmd = " sudo rm -rf " + folder_path + "*.jpg "
    
    delete_cmd = " sudo rm -rf " + folder_path
    
    cmd_line = "ssh pi@" + ''.join(host_add) + delete_cmd + " exit"

    print(cmd_line)

    try:
        #subprocess.call(cmd_line + [str(img_name)])
        os.system(cmd_line)
        print("Captured images were deleted...\n")
    except OSError:
        print("Failed moving image!\n")
    
    
def main(args):
    
    #pasre paramters 
    ap = argparse.ArgumentParser()
    ap.add_argument('-p', '--path', required = True, help = "image files path")
    #ap.add_argument('-a', '--action', required = True, type = int, help = '"1" is move files' + '"2" is delete files' + '"3" is upload files')
    args = vars(ap.parse_args())
    
    global folder_path
    
    folder_path = args['path']
    
    #PiController = "192.168.1.110,"
    
    host_list = []
    
    for i in range(101,110):
        a = ("192.168.1.%i:" %i)
        host_list.append(a)
    

    #delete_img(host_list[0])
    # get cpu number for parallel processing
    agents = multiprocessing.cpu_count()
    
    
    # perform delete images in parallel way
    with closing(Pool(processes = agents)) as pool:
        pool.map(delete_img, host_list)
        pool.terminate()
        
        delete_local = "sudo rm -rf " + folder_path

        try:
            #subprocess.call(cmd_line + [str(img_name)])
            os.system(delete_local)
        except OSError:
            print("Failed deleting image!\n")
    
    #delete local folder
    
    delete_cmd = " sudo rm -rf " + folder_path

    print(delete_cmd)

    try:
        #subprocess.call(cmd_line + [str(img_name)])
        os.system(delete_cmd)
        print("Captured images were deleted...\n")
    except OSError:
        print("Failed moving image!\n")
    
    
'''
    if args['action'] == 1:
        
        # perform move images in parallel way
        with closing(Pool(processes = agents)) as pool:
            pool.map(move_img, host_list)
            pool.map(delete_img, host_list)
            pool.terminate()
    
    elif args['action'] == 2:

        # perform delete images in parallel way
        with closing(Pool(processes = agents)) as pool:
            pool.map(delete_img, host_list)
            pool.terminate()
            
            delete_local = "sudo rm -rf " + folder_path

            try:
                #subprocess.call(cmd_line + [str(img_name)])
                os.system(delete_local)
            except OSError:
                print("Failed deleting image!\n")
    
    elif args['action'] == 3:
        
        cwd = os.getcwd()
        
        folder_name = os.path.basename(folder_path)
        
        #print(folder_name)
        
        #abs_path = os.path.abspath(img_name)
        
        #cmd_line = 'pyicmd --host data.cyverse.org --port 1247 --user lsx1980 --passwd lsx6327903 --zone iplant put /iplant/home/lsx1980/root-images '.split()        
        
        #cmd_line = "pyicmd --host data.cyverse.org --port 1247 --user lsx1980 --passwd lsx6327903 --zone iplant put /iplant/home/lsx1980/root-images " + img_name
        
        cmd_line = "pyicmd --host data.cyverse.org --port 1247 --user lsx1980 --passwd lsx6327903 --zone iplant put -R /iplant/home/lsx1980/root-images " + folder_name
        
        print(cmd_line)
        
        try:
            #subprocess.call(cmd_line + [str(img_name)])
            os.system(cmd_line)
            print("Captured images were uploaded to cyverse server...\n")
        except OSError:
            print("Failed upload image folder!\n")
        
    else:
        print("Invalid action choice!\n")
'''   
        
        

if __name__ == '__main__':
    
    sys.exit(main(sys.argv))
    
