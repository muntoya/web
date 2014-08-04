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
        self.dict['device_list'] = []
        cl = cli_device.get_device_list()
        keys = ('ip', 'type', 'status', 'cpu', 'disk', 'in', 'out')
        
        for c in cl:
            self.dict['device_list'].append(dict(zip(keys, c)))


class DeviceDetailT(BaseTemplateRes):
    def __init__(self, did):
        self.dict = {}
        c = cli_device.get_device_detail(did)
        keys = ('starttime', 'status', 'heartbeat', 'core', 'frequency', 'cpuused', 'memory', 'memused', 'disk', 'diskused', 'in', 'out')
        self.dict['device_detail'] = dict(zip(keys, c))
        
         

