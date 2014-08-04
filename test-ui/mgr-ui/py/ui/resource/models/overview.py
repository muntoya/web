# -*- coding: utf-8 -*-
'''
Created on Jul 4, 2014

@author: yaoxing
'''

from ui.cli import cli_storage
from ui.util.base_res import BaseTemplateRes, BaseJsonRes


class StorageOverviewT(BaseTemplateRes):
    def __init__(self):
        self.dict = {}
        self.dict['lun_cnt'] = cli_storage.get_lun_cnt()
        self.dict['lun_available'] = cli_storage.get_lun_available()
        self.dict['snapshot_cnt'] = cli_storage.get_snapshot_cnt()
        self.dict['pool_cnt'] = cli_storage.get_pool_cnt()
        self.dict['pool_available'] = cli_storage.get_pool_available()
        
class StorageOverviewJ(BaseJsonRes):
    def __init__(self):
        self.json = {}
        self.json['pool'] = {'available': cli_storage.get_pool_available(), 
                             'used': cli_storage.get_pool_used()}
        self.json['lun'] = {'unmapped': cli_storage.get_lun_available(),
                            'mapped': cli_storage.get_lun_used()}
        