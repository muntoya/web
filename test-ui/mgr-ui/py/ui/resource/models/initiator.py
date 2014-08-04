# -*- coding: utf-8 -*-
'''
Created on Jul 16, 2014

@author: yaoxing
'''


from ui.cli import cli_storage 
from ui.util.base_res import BaseJsonRes, BaseTemplateRes


class InitiatorListT(BaseTemplateRes):
    def __init__(self):
        self.dict = {}
        self.dict['initiator_list'] = []
        keys = ('id', 'alias', 'hbatype', 'status')
        ll = cli_storage.get_initiator_list()
        for l in ll:
            self.dict['initiator_list'].append(dict(zip(keys, l)))
            
class InitiatorDetailT(BaseTemplateRes):
    def __init__(self, lid):
        self.dict = {}
        keys = ('id', 'alias', 'hbatype', 'status', 'chapcnt', 'chapstatus')
        l = cli_storage.get_initiator_detail(lid)
        self.dict['initiator'] = dict(zip(keys, l))
            
class InitiatorListJ(BaseJsonRes):
    def __init__(self):
        self.json = {}
        self.json['initiator'] = []
        keys = ('id', 'alias', 'hbatype', 'status')
        ll = cli_storage.get_initiator_list()
        for l in ll:
            self.json['initiator'].append(dict(zip(keys, l)))
        
class InitiatorDetailJ(BaseJsonRes):
    def __init__(self, lid):
        self.json = {}
        keys = ('id', 'alias', 'hbatype', 'status', 'chapcnt', 'chapstatus')
        l = cli_storage.get_initiator_detail(lid)
        self.json = dict(zip(keys, l))

