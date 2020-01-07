"""
Version: 1.0
Shutdown all cluster pi except PiController
Author: suxing liu
Author-email: suxingliu@gmail.com

USAGE

python cluster_shutdown.py

"""


import subprocess, os
import sys

def close_connection(host_adr):
    
    cmd_line = "ssh pi@" + ''.join(host_adr) + ' sudo shutdown -h now'
    
    print(cmd_line)   
    
    returned_value = subprocess.call(cmd_line, shell=True)
    
    if returned_value == 255:
        print("Rapberry Pi host @{0} was shutdown...\n".format(''.join(host_adr)))
    else:
        print("SSH shutdown failed ...!\n")
    

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
        
        close_connection(host_list[i])
    
    
    
if __name__ == '__main__':
    
    sys.exit(main(sys.argv))
    

