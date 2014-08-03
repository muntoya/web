# -*- coding: utf-8 -*-
'''
Created on Jun 27, 2014

@author: yaoxing
'''

import time
import random


#===============================================================================
# time
#===============================================================================

def get_sys_name():
    return 'bia'

def get_sys_time():
    return time.asctime( time.localtime(time.time()) )

def get_dev_type():
    return 'yfs'

def get_start_time():
    return '0434334'

def get_up_time():
    return '2015/1/1/00:59'

def get_sys_version():
    return '10.2'



#===============================================================================
# warning
#===============================================================================

def get_total_unread():
    return random.randint(1, 30)

def get_error_count():
    return random.randint(1, 30)

def get_warning_count():
    return random.randint(1, 30)

def get_info_count():
    return random.randint(1, 30)

def get_trial_remain():
    return random.randint(1, 30)


#===============================================================================
# io
#===============================================================================
def get_iops(t):
    return (random.randint(1, 800),
            random.randint(1, 800),
            random.randint(1, 800),
            random.randint(1, 800))
    
def get_throughput(t):
    return (random.randint(1, 800),
            random.randint(1, 800),
            random.randint(1, 800),
            random.randint(1, 800))
    
    