"""
Version: 1.0
Capture pileline for all cameras controller by each pi cluster 
Author: suxing liu
Author-email: suxingliu@gmail.com

USAGE

python camera_cluster.py

"""

import subprocess, os
import sys


def main(args):
    
    PiController = "192.168.1.110,"
    
    host_list = []
    
    for i in range(101,110):
        a = ("192.168.1.%i," %i)
        host_list.append(a)
    
    str_host_list = ''.join(host_list)
    
    str_host_list = str_host_list.rstrip(',')
    
    cmd_line = "mpiexec -host " + PiController + str_host_list \
    + " python capture_sync.py -r 1 -s 1 -n 360"
    
    print(cmd_line)

    
    #cmd_line = "ls && ls -la"
    
    try:
        #subprocess.check_output(cmd_line)
        os.system(cmd_line)
        print("Image capture task finished successfully by camera cluster...\n")
    except OSError:
        print("Failed ...!\n")
    

if __name__ == '__main__':
    
    sys.exit(main(sys.argv))
    
