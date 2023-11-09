"""
Version: 1.0
Test raspberry pi cluster connection with master
Author: suxing liu
Author-email: suxingliu@gmail.com

USAGE

python cluster_connection.py

"""

import subprocess, os
import sys
import multiprocessing
from multiprocessing import Pool
from contextlib import closing


def test_connection(host_adr):
    
    cmd_line = "ssh pi@" + ''.join(host_adr) + ' exit'
    
    print(cmd_line)   
    
    returned_value = subprocess.call(cmd_line, shell=True)
    
    if returned_value == 0:
        print("Rapberry Pi host @{0} was connected...\n".format(''.join(host_adr)))
    else:
        print("SSH connection failed ...!\n")
    

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
        
        test_connection(host_list[i])
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
    
