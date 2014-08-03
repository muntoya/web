# -*- coding: utf-8 -*-
'''
Created on Jun 27, 2014

@author: yaoxing
'''

import random



def get_cluster_info():
    '''
    return (sysname, iops, throughput, total, used, free, hit rate, read throughput, random read iops, cpu, memory) 
    ''' 
    return ('YeeStor',
            random.randint(30, 10000),
            random.randint(20, 400),
            random.random() * 50.0,
            random.random() * 50.0,
            random.random() * 50.0,
            random.random() * 100,
            random.randint(2, 200),
            random.randint(30, 10000),
            random.random() * 100,
            random.random() * 100)
    
    
def get_device_list():
    '''
    return [(ip, type, status, cpu, disk, in, out)]
    '''
    sl = []
    for i in range(0, random.randint(3, 20)):
        item =  ('192.168.' + str(random.randint(1, 255)) + '.' + str(random.randint(1, 255)),
                random.choice([0, 1]), 
                random.choice([0, 1]),
                random.randint(1, 100),
                random.randint(1, 100),
                random.random() * 10,
                random.random() * 10)
        sl.append(item)
        
    return sl
        

def get_device_detail(did):
    '''
    return (starttime, status, heartbeat, core, frequency, cpuused, memory, memused, disk, diskused, in, out)
    '''
    return ('2013-05-' + str(random.randint(1, 30)),
            random.choice([0, 1]), 
            '2013-05-' + str(random.randint(1, 30)),
            random.randint(1, 8),
            random.choice([1600, 2000, 2400]),
            random.randint(1, 100),
            random.random() * 24,
            random.random() * 24, 
            random.random() * 800,
            random.random() * 800,
            random.random() * 10,
            random.random() * 10)  
    
    
    
    
    
        

        