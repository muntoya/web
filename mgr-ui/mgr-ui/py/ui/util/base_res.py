# -*- coding: utf-8 -*-
'''
Created on Jun 26, 2014

@author: yaoxing
'''

import json

class BaseJsonRes(object):
    def __init__(self):
        self.json = {}
        
    def json_res(self):
        return json.dumps(self.json, sort_keys=True, indent=4, separators=(',', ': '))
    
    
class BaseTemplateRes(object):
    '''
    classdocs
    '''
    def __init__(self):
        self.dict = {}
    
    def dict_res(self):
        return self.dict
        