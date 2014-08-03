# -*- coding: utf-8 -*-
'''
Created on Jun 6, 2014

@author: yaoxing
'''

from ui.cli import cli_system
from ui.util.base_res import BaseTemplateRes

__all__ = ['WarningInfo']


class WarningInfoT(BaseTemplateRes):
    def __init__(self):
        self.dict = {}
        self.dict['total_unread'] = cli_system.get_total_unread()
        self.dict['error_count'] = cli_system.get_error_count()
        self.dict['warning_count'] = cli_system.get_warning_count()
        self.dict['info_count'] = cli_system.get_info_count()
        self.dict['trial_remain'] = cli_system.get_trial_remain()
    