# -*- coding: utf-8 -*-
'''
Created on Jun 6, 2014

@author: yaoxing
'''

from ui.cli import cli_storage
from ui.util.base_res import BaseJsonRes
from ui.util.base_res import BaseTemplateRes


class StorageUsageJ(BaseJsonRes):
    def __init__(self):
        self.json = {}
        self.json['pool'] = {'available': cli_storage.get_pool_available(), 
                             'used': cli_storage.get_pool_used()}
        self.json['lun'] = {'available': cli_storage.get_lun_available(),
                            'used': cli_storage.get_lun_used()}

class StorageInfoT(BaseTemplateRes):
    def __init__(self):
        self.dict = {}
        self.dict['pool_cnt'] = cli_storage.get_pool_cnt()
        self.dict['lun_cnt'] = cli_storage.get_lun_cnt()
        