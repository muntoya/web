# -*- coding: utf-8 -*-
'''
Created on Jun 6, 2014

@author: yaoxing
'''

import json
from ui.cli import cli_system
from ui.util.base_res import BaseJsonRes

import time
TEST_TIMESTAMP = time.mktime(time.strptime('20000101 16:00:00', '%Y%m%d %X'))

class IOInfoJ(BaseJsonRes):
    fake_data_1 = []                    # 假数据列表1
    fake_data_2 = []                    # 假数据列表2,应该与1一样长
    fake_start_time = TEST_TIMESTAMP    # 第一个假数据的开始时间
    def __init__(self):
        while (len(IOInfoJ.fake_data_1) <=181):
            # 数据不足182的时候，要添加够182，
            t = time.strftime('%X', time.localtime(IOInfoJ.fake_start_time))
            a, b, c, d = cli_system.get_throughput(t)
            IOInfoJ.fake_data_1.append({'time': t, 'or': a, 'ow': b, 'ir': c, 'iw': d})
            a, b, c, d = cli_system.get_iops(t)
            IOInfoJ.fake_data_2.append({'time': t, 'or': a, 'ow': b, 'ir': c, 'iw': d})
            # 加20秒 (3600 / 180) 
            IOInfoJ.fake_start_time = IOInfoJ.fake_start_time + 20
            
            
        while (len(IOInfoJ.fake_data_1) > 181):
            # 最终的数据需要181条，删除最旧的。
            del IOInfoJ.fake_data_1[0]
            del IOInfoJ.fake_data_2[0]
           
        self.json = {'throughput':IOInfoJ.fake_data_1, 'iops':IOInfoJ.fake_data_2}
