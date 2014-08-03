# -*- coding: utf-8 -*-
'''
Created on Jul 16, 2014

@author: yaoxing
'''


from ui.cli import cli_storage 
from ui.util.base_res import BaseJsonRes, BaseTemplateRes

class VServerListT(BaseTemplateRes):
    def __init__(self):
        self.dict = {}
        self.dict['vserver_list'] = []
        keys = ('name', 'ip', 'vgroup', 'id')
        vl = cli_storage.get_vserver_list()
        for v in vl:
            self.dict['vserver_list'].append(dict(zip(keys, v)))
            
class VServerDetailT(BaseTemplateRes):
    def __init__(self, vid):
        self.dict = {}
        keys = ('name', 'ip', 'vgroup', 'id')
        v = cli_storage.get_vserver_detail(vid)
        self.dict['vserver'] = dict(zip(keys, v))
            
class VServerListJ(BaseJsonRes):
    def __init__(self):
        self.json = {}
        self.json['vserver'] = []
        keys = ('name', 'ip', 'vgroup', 'id')
        vl = cli_storage.get_vserver_list()
        for v in vl:
            self.json['vserver'].append(dict(zip(keys, v)))
            
            
class VServerDetailJ(BaseJsonRes):
    def __init__(self, vid):
        self.json = {}
        keys = ('name', 'ip', 'vgroup', 'id')
        v = cli_storage.get_vserver_detail(vid)
        self.json = dict(zip(keys, v))




