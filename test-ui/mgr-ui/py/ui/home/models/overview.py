# -*- coding: utf-8 -*-
'''
Created on Jun 6, 2014

@author: yaoxing
'''

from ui.cli import cli_system
from django.db import models
from ui.util.base_res import BaseTemplateRes

__all__ = ['SysInfo']

class SysInfoT(BaseTemplateRes):
    def __init__(self):
        self.dict = {}
        self.dict['sys_name'] = cli_system.get_sys_name()
        self.dict['sys_time'] = cli_system.get_sys_time()
        self.dict['dev_type'] = cli_system.get_dev_type()
        self.dict['start_time'] = cli_system.get_start_time()
        self.dict['up_time'] = cli_system.get_up_time()
        self.dict['sys_version'] = cli_system.get_sys_version()

