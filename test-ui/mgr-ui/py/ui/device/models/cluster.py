# -*- coding: utf-8 -*-
'''
Created on Jul 31, 2014

@author: yaoxing
'''

from ui.cli import cli_device 
from ui.util.base_res import BaseJsonRes, BaseTemplateRes

#===============================================================================
# template
#===============================================================================
class DeviceListT(BaseTemplateRes):
    def __init__(self):
        self.dict = {}
        c = cli_device.get_cluster_info()
        keys = ('sysname', 'iops', 'throughput', 'total', 'used', 'free', 'hitrate', 'readtp', 'readiops', 'cpu', 'memory')
        self.dict['cluster'] = dict(zip(keys, c))
        
