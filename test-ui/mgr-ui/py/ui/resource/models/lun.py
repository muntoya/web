# -*- coding: utf-8 -*-
'''
Created on Jul 7, 2014

@author: yaoxing
'''

from ui.cli import cli_storage 
from ui.util.base_res import BaseJsonRes, BaseTemplateRes

#===============================================================================
# template
#===============================================================================
class LunListT(BaseTemplateRes):
    def __init__(self):
        self.dict = {}
        self.dict['lun_list'] = []
        ll = cli_storage.get_lun_list()
        keys = ('name', 'id', 'available', 'free', 'dataspace', 'snapshotspace', 'status', 'mapped', 'socache')
        
        for l in ll:
            self.dict['lun_list'].append(dict(zip(keys, l)))
            
class LunDetailT(BaseTemplateRes):
    def __init__(self, lunid):
        self.dict = {}
        keys = ('name', 'id', 'capacity', 'dataspace', 'snapshotspace', 'status', 
                'mapped', 'socache', 'prestore', 'writeonrunning')
        l = cli_storage.get_lun_detail(lunid)
        self.dict['lun_detail'] = dict(zip(keys, l))
        
class SnapshotListT(BaseTemplateRes):
    def __init__(self, lunid):
        self.dict = {}
        self.dict['snapshot_list'] = []
        keys = ('name' , 'id', 'label', 'creation', 'accessed', 'lunid', 'lunname')
        sl = cli_storage.get_lun_snapshot_list(lunid)
        for s in sl:
            self.dict['snapshot_list'].append(dict(zip(keys, s)))

#===============================================================================
# json
#===============================================================================
class LunListJ(BaseJsonRes):
    def __init__(self):
        self.json = {}
        self.json['lun'] = []
        ll = cli_storage.get_lun_list()
        keys = ('name', 'id', 'available', 'free', 'dataspace', 'snapshotspace', 'status', 'mapped', 'socache')
        
        for l in ll:
            self.json['lun'].append(dict(zip(keys, l)))
        
            
class LunDetailJ(BaseJsonRes):
    def __init__(self, lunid):
        self.json = {}
        keys = ('name', 'id', 'capacity', 'dataspace', 'snapshotspace', 'status', 
                'mapped', 'socache', 'prestore', 'writeonrunning')
        l = cli_storage.get_lun_detail(lunid)
        self.json = dict(zip(keys, l))
         
class SnapshotListJ(BaseJsonRes):
    def __init__(self, lunid):
        self.json = {}
        self.json['snapshot'] = []
        keys = ('name' , 'id', 'label', 'creation', 'accessed', 'lunid', 'lunname')
        sl = cli_storage.get_lun_snapshot_list(lunid)
        for s in sl:
            self.json['snapshot'].append(dict(zip(keys, s)))
        
        
        