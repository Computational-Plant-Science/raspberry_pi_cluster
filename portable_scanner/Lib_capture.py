"""
Version: 1.0
Capture images using usb cameras
Author: suxing liu
Author-email: suxingliu@gmail.com

USAGE

python capture.py

"""


import subprocess, os
import sys
import argparse
import numpy as np 
import pathlib
import os
import glob

from datetime import datetime


# generate foloder to store the output results
def mkdir(path):
    # import module
    import os
 
    # remove space at the beginning
    path=path.strip()
    # remove slash at the end
    path=path.rstrip("\\")
 
    # path exist?   # True  # False
    isExists=os.path.exists(path)
 
    # process
    if not isExists:
        # construct the path and folder
        #print path + ' folder constructed!'
        # make dir
        os.makedirs(path)
        return True
    else:
        # if exists, return 
        #print path+' path exists!'
        #shutil.rmtree(path)
        #os.makedirs(path)
        return False
        



# execute script inside program
def execute_script(cmd_line):
    
    try:
        #print(cmd_line)
        #os.system(cmd_line)

        process = subprocess.getoutput(cmd_line)
        
        print(process)
        
        #process = subprocess.Popen(cmd_line, shell = True, stdout = subprocess.PIPE)
        #process.wait()
        #print (process.communicate())
        
    except OSError:
        
        print("Failed ...!\n")




# execute pipeline scripts in order
def image_capture_pipeline(file_path):
    
  
    print("Writing images to folder '{}'...\n".format(file_path))
    
    file_path_full = file_path + '/'

    # python3 skeleton_graph.py -p ~/example/pt_cloud/tiny/ -m1 tiny_skeleton.ply
    #skeleton_analysis = "python3 skeleton_graph.py -p " + file_path_full + " -m1 " + model_skeleton_name
    
    camera_IC_list = ["i2cset -y 10 0x24 0x24 0x02", "i2cset -y 10 0x24 0x24 0x12",
                        "i2cset -y 10 0x24 0x24 0x22", "i2cset -y 10 0x24 0x24 0x32"]
    
    
    for image_id, set_cam_ID in enumerate(camera_IC_list):
        
        img_name =  "{:%Y-%m-%d-%H-%M-%S}".format(datetime.now())
        
        img_file = file_path + img_name + "_{:02d}".format(image_id) + ".jpg"
        
        
        # libcamera-still -t 5000 -n -o test.jpg --width 4656 --height 3496
        capture_cmd = set_cam_ID + " && " + "libcamera-still -t 2000 -n -o " + img_file + " --width 4656 --height 3496"
        
        print(capture_cmd)
        
        execute_script(capture_cmd)
        
    
    resume_cmd = "i2cset -y 10 0x24 0x24 0x00"
    
    execute_script(resume_cmd)
        
    #execute_script
    ####################################################################


    '''
    filename = folder_name + '_quaternion.xlsx'
    batch_cmd = " /home/suxing/example/quaternion/B73_result/values/" 
    execute_script(batch_cmd)
    
    filename = folder_name + '_his.png' 
    batch_cmd = "cp " + file_path_full + filename + " /home/suxing/example/quaternion/B73_result/histogram/" 
    execute_script(batch_cmd)
    
    filename = folder_name + '_quaternion_4D.html'
    batch_cmd = "cp " + file_path_full + filename + " /home/suxing/example/quaternion/B73_result/scatterplot/" 
    execute_script(batch_cmd)
    '''
    

    
    
   
    
if __name__ == '__main__':
    
    # construct the argument and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-p", "--path", required = False, help = "path to individual folders")
    args = vars(ap.parse_args())
    
   
    #parameter sets
    # path to individual folders
    current_path = args["path"]
    
    if (args['path']):
        save_path = args['path']
    else:
         # save folder construction
        #mkpath = os.path.dirname(abs_path) +'/marker_detection'
        #mkdir(mkpath)
        #marker_save_path = mkpath + '/'
        
        current_path = os.getcwd() 
        
        mkpath = current_path + '/images'
        mkdir(mkpath)
        save_path = mkpath + '/'
        
    image_capture_pipeline(save_path)



    
    '''
    ###########################################################
    #parallel processing module
    
    # get cpu number for parallel processing
    agents = psutil.cpu_count() - 2 
    #agents = multiprocessing.cpu_count() 
    #agents = 8
    
    print("Using {0} cores to perfrom parallel processing... \n".format(int(agents)))
    
    # Create a pool of processes. By default, one is created for each CPU in the machine.
    # extract the bouding box for each image in file list
    with closing(Pool(processes = agents)) as pool:
        result = pool.map(skeleton_analysis_pipeline, subfolders)
        pool.terminate()
    '''
