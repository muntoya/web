# -*- coding: utf-8 -*-
'''
Created on Jul 15, 2014

@author: yaoxing
'''

from ui.cli import cli_storage 
from ui.util.base_res import BaseJsonRes, BaseTemplateRes


#===============================================================================
# template
#===============================================================================
class PoolListT(BaseTemplateRes):
    def __init__(self):
        self.dict = {}
        self.dict['pool_list'] = []
        
        pl = cli_storage.get_pool_list()
        keys = ['name', 'id', 'available', 'free', 'used', 'useratio', 'status']
        
        for p in pl:
            self.dict['pool_list'].append(dict(zip(keys, p)))
            
class PoolDetailT(BaseTemplateRes):
    def __init__(self, poolid):
        self.dict = {}
        keys = ['name', 'id', 'available', 'free', 'used', 'useratio', 'status']
        p = cli_storage.get_pool_detail(poolid)
        self.dict['pool_detail'] = dict(zip(keys, p))
        
class PoolLunListT(BaseTemplateRes):
    def __init__(self, poolid):
        self.dict = {}
        self.dict['pool_lun_list'] = []
        
        pl = cli_storage.get_pool_lun_list(poolid)
        keys = ['name', 'id', 'available', 'status']
        
        for p in pl:
            self.dict['pool_lun_list'].append(dict(zip(keys, p)))
            
class PoolDiskT(BaseTemplateRes):
    def __init__(self, poolid):
        self.dict = {}
        self.dict['pool_disk_list'] = []
        keys = ('wwn', 'slot', 'type', 'available', 'free', 'used', 'pool', 'throughput', 'iops', 'status')
        dl = cli_storage.get_pool_disk(poolid)
        for d in dl:
            self.dict['pool_disk_list'].append(dict(zip(keys, d)))

#===============================================================================
# json            
#===============================================================================
class PoolListJ(BaseJsonRes):
    def __init__(self):
        self.json = {}
        self.json['pool'] = []
        
        pl = cli_storage.get_pool_list()
        keys = ('name', 'id', 'available', 'free', 'used', 'useratio', 'status')
        
        for p in pl:
            self.json['pool'].append(dict(zip(keys, p)))

class PoolDetailJ(BaseJsonRes):
    def __init__(self, poolid):
        self.json = {}
        keys = ('name', 'id', 'available', 'free', 'used', 'useratio', 'status')
        p = cli_storage.get_pool_detail(poolid)
        self.json = dict(zip(keys, p))
        
class PoolDiskJ(BaseJsonRes):
    def __init__(self, poolid):
        self.json = {}
        self.json['disk'] = []
        keys = ('wwn', 'slot', 'type', 'available', 'free', 'used', 'pool', 'throughput', 'iops', 'status')
        dl = cli_storage.get_pool_disk(poolid)
        for d in dl:
            self.json['disk'].append(dict(zip(keys, d)))
    
    
    
    
    
    
    
    
    