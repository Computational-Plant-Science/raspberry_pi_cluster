"""
Version: 1.0
Test raspberry pi cluster connection with master
Author: suxing liu
Author-email: suxingliu@gmail.com

USAGE

python cluster_update.py

"""

import subprocess, os
import sys
import multiprocessing
from multiprocessing import Pool
from contextlib import closing


def update_system(host_adr):
    
    update_cmd = " sudo apt-get update &" + " sudo apt-get upgrade &" + " sudo apt-get autoclean &"
    
    cmd_line = "ssh pi@" + ''.join(host_adr) + ''.join(update_cmd) + " exit"
    
    print(cmd_line)   
    
    #returned_value = subprocess.call(cmd_line, shell=True)
    
    try:
        #subprocess.call(cmd_line + [str(img_name)])
        os.system(cmd_line)
        print("Rapberry Pi host @{0} system was updated...\n".format(''.join(host_adr)))
    except OSError:
        print("Update failed ...!\n")
    

    

def main(args):
    '''
    
    PiController = "192.168.1.110,"
    
    pi01 = "192.168.1.101"
    pi02 = "192.168.1.102"
    pi03 = "192.168.1.103"
    pi04 = "192.168.1.104"
    pi05 = "192.168.1.105"
    pi06 = "192.168.1.106"
    pi07 = "192.168.1.107"
    pi08 = "192.168.1.108"
    pi09 = "192.168.1.109"
    '''
    
    host_list = []
    
    for i in range(101,110):
        a = ['192.168.1.%i' %i]
        host_list.append(a)
    
    #print host_list
    
    
    
    for i in range(0,9):
        
        update_system(host_list[i])
    '''
    
    # get cpu number for parallel processing
    agents = multiprocessing.cpu_count()
    
    # perfrom crop action based on bouding box results in parallel way
    with closing(Pool(processes = agents)) as pool:
        pool.map(test_connection, host_list)
        pool.terminate()
    '''
    
if __name__ == '__main__':
    
    sys.exit(main(sys.argv))
    
