# -*- coding: utf-8 -*-
'''
Created on Jul 2, 2014

@author: yaoxing
'''
import random

#===============================================================================
# pool
#===============================================================================
def get_pool_cnt():
    return random.randint(3, 20)

def get_pool_available():
    return 957.00

def get_pool_used():
    return round(random.random() * 957, 2)

def get_pool_list():
    '''
    return [(name, id, available, free, used, useratio, status)]
    '''
    ll = []
    for i in range(0, random.randint(3, 20)):
        item = ('lun' + str(i),
                i, 
                87.67,
                random.random() * 87.67,
                random.random() * 30.2,
                random.random() * 100,
                random.choice([0, 1]))
        ll.append(item)
    
    return ll

def get_pool_detail(poolid):
    '''
    return (name, id, available, free, used, useratio, status)
    '''
    return ('lun' + str(poolid),
            poolid, 
            87.67,
            random.random() * 87.67,
            random.random() * 30.2,
            random.random() * 100,
            random.choice([0, 1]))
    
def get_pool_disk(poolid):
    '''
    return [(wwn, slot, type, available, free, used, pool, throughput, iops, status)]
    '''
    dl = []
    for i in range(0, random.randint(3, 10)):
        item = (random.randint(3, 20),
                '3,4',
                random.choice([0, 1]),
                87.67,
                random.random() * 87.67,
                random.random() * 30.2,
                '1,5',
                random.random() * 600.0,
                random.random() * 600.0,
                random.choice([0, 1]))
        dl.append(item)
    return dl
    
def get_pool_lun_list(poolid):
    '''
    return [(name, id, available, status)]
    '''
    ll = []
    for i in range(0, random.randint(3, 10)):
        item = ('lun' + str(i),
                i, 
                random.random() * 87.67,
                random.choice([0, 1]))
        ll.append(item)
    
    return ll


#===============================================================================
# lun
#===============================================================================
def get_lun_cnt():
    return random.randint(3, 20)

def get_lun_available():
    return 87.67

def get_lun_used():
    return round(random.random() * 87.67, 2)

def get_lun_list():
    '''
    return [(name, id, available, free, dataspace, snapshotspace, status, mapped, socache)]
    '''
    ll = []
    for i in range(0, random.randint(3, 20)):
        item = ('lun' + str(i),
                i, 
                87.67,
                random.random() * 87.67,
                random.random() * 30.2,
                random.random() * 10.2,
                random.choice([0, 1]), 
                random.choice([0, 1]), 
                random.choice([0, 1]))
        ll.append(item)
    
    return ll

def get_lun_detail(lunid):
    '''
    return (name, id, capacity, dataspace, snapshotspace, status, mapped, socache, prestore, writeonrunning)
    '''
    return ('lun' + str(lunid),
            lunid,
            87.67,
            random.random() * 30.2,
            random.random() * 10.2,
            random.choice([0, 1]),
            random.choice([0, 1]),
            random.choice([0, 1]),
            random.choice([0, 1]),
            random.choice([0, 1]))

def get_lun_snapshot_list(lunid):
    '''
    return (name ,id, label, creation, accessed, lunid, lunname)
    '''
    sl = []
    for i in range(0, random.randint(3, 20)):
        item =  ('snapshot' + str(i),
                i,
                'bilibili' + str(lunid),
                '201407052301',
                random.choice([0, 1]),
                lunid,
                'lun' + str(lunid))
        sl.append(item)
    return sl
    
def get_snapshot_cnt():
    return random.randint(0, 30)


#===============================================================================
# launcher
#===============================================================================
def get_initiator_list():
    '''
    return [(id, alias, hbatype, status)]
    '''
    ll = []
    for i in range(0, random.randint(3, 20)):
        item = (i, 
                'initiator' + str(i),
                random.choice([0, 1]), 
                random.choice([0, 1]))
        ll.append(item)
    
    return ll

def get_initiator_detail(lid):
    '''
    return (id, alias, hbatype, status, chapcnt, chapstatus)
    '''

    return (lid, 
            'initiator' + str(lid),
            random.choice([0, 1]), 
            random.choice([0, 1]),
            random.randint(1, 44),
            random.choice([0, 1]))


#===============================================================================
# vserver
#===============================================================================
def get_vserver_list():
    '''
    return [(name, ip, vgroup, id)]
    '''
    ll = []
    for i in range(0, random.randint(3, 20)):
        item = ('vserver' + str(i),
                '192.168.' + str(random.randint(1, 255)) + '.' + str(random.randint(1, 255)),
                'baba' + str(random.randint(22, 44)), 
                i)
        ll.append(item)
    
    return ll
    
def get_vserver_detail(vid):
    '''
    return (name, ip, vgroup, id)
    '''
    return ('vserver' + str(vid),
            '192.168.' + str(random.randint(1, 255)) + '.' + str(random.randint(1, 255)),
            'baba' + str(random.randint(22, 44)), 
            vid)



