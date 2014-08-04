from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from ui.util.decorator import http_except_dec
from models import overview, lun, pool, vserver
from ui.resource.models import initiator

#===============================================================================
# pages
#===============================================================================
@http_except_dec
def resource_page(request):
    dict_res = overview.StorageOverviewT().dict_res()
    return render_to_response('resource/resource.html', dict_res)

@http_except_dec
def lun_page(request):
    #FIXME: temp
    lun_res = lun.LunListT().dict_res()
    lundetail_res = lun.LunDetailT(1).dict_res()
    snapshot_res = lun.SnapshotListT(1).dict_res()
    
    res = {}
    res.update(lun_res)
    res.update(lundetail_res)
    res.update(snapshot_res)
    
    return render_to_response('resource/lun/lun.html', res)

@http_except_dec
def lunlist_page(request):
    lun_res = lun.LunListT().dict_res()
    return render_to_response('resource/lun/lun_list.html', lun_res)

@http_except_dec
def lundetail_page(request, lunid):
    lun_res = lun.LunDetailT(lunid).dict_res()
    return render_to_response('resource/lun/lun_detail.html', lun_res)

@http_except_dec
def snapshot_page(request, lunid):
    lun_res = lun.SnapshotListT(lunid).dict_res()
    return render_to_response('resource/lun/lun_snapshot.html', lun_res)

@http_except_dec
def pool_page(request):
    #FIXME:temp
    pool_res = pool.PoolListT().dict_res()
    pooldetail_res = pool.PoolDetailT(1).dict_res()
    poollun_res = pool.PoolLunListT(1).dict_res()
    pooldisk_res = pool.PoolDiskT(1).dict_res()
    
    res = {}
    res.update(pool_res)
    res.update(pooldetail_res)
    res.update(poollun_res)
    res.update(pooldisk_res)
    
    return render_to_response('resource/pool/storagePool.html', res)

@http_except_dec
def poollist_page(request):
    pool_res = pool.PoolListT()
    return render_to_response('resource/pool/pool_list.html', pool_res.dict_res())

@http_except_dec
def pooldetail_page(request, poolid):
    pool_res = pool.PoolDetailT(poolid).dict_res()
    return render_to_response('resource/pool/pool_detail.html', pool_res)

@http_except_dec
def poollun_page(request, poolid):
    poollun_res = pool.PoolLunListT(poolid).dict_res()
    return render_to_response('resource/pool/pool_lun.html', poollun_res)

@http_except_dec
def pooldisk_page(request, poolid):
    pooldisk_res = pool.PoolDiskT(poolid).dict_res()
    return render_to_response('resource/pool/pool_disk.html', pooldisk_res)

@http_except_dec
def initiator_page(request):
    #FIXME: temp
    initiator_res = initiator.InitiatorListT().dict_res()
    initiatordetail_res = initiator.InitiatorDetailT(1).dict_res()
    
    res = {}
    res.update(initiator_res)
    res.update(initiatordetail_res)
    
    return render_to_response('resource/initiator/initiator.html', res)

@http_except_dec
def initiatorlist_page(request):
    initiator_res = initiator.InitiatorListT().dict_res()
    return render_to_response('resource/initiator/initiator_list.html', initiator_res)

@http_except_dec
def initiatordetail_page(request, iid):
    initiator_res = initiator.InitiatorDetailT(iid).dict_res()
    return render_to_response('resource/initiator/initiator_detail.html', initiator_res)

@http_except_dec
def vserver_page(request):
    #FIXME:temp
    vserver_res = vserver.VServerListT().dict_res()
    vserverdetail_res = vserver.VServerDetailT(1).dict_res()
    
    res = {}
    res.update(vserver_res)
    res.update(vserverdetail_res)
    return render_to_response('resource/vserver/virtualServer.html', res)

@http_except_dec
def vserverlist_page(request):
    vserver_res = vserver.VServerListT()
    return render_to_response('resource/vserver/vserver_list.html', vserver_res.dict_res())

@http_except_dec
def vserverdetail_page(request, vid):
    vserver_res = vserver.VServerDetailT(vid)
    return render_to_response('resource/vserver/vserver_detail.html', vserver_res.dict_res())

#===============================================================================
# json
#===============================================================================

@http_except_dec
def resource_overview(requst):
    o = overview.StorageOverviewJ()
    return HttpResponse(o.json_res())
    
# lun --------------------------------------------------------------------------
@http_except_dec
def lun_list(request):
    l = lun.LunListJ()
    return HttpResponse(l.json_res())

@http_except_dec
def lun_detail(request, lunid):
    l = lun.LunDetailJ(int(lunid))
    return HttpResponse(l.json_res())

@http_except_dec
def lun_snapshot(request, lunid):
    s = lun.SnapshotListJ(int(lunid))
    return HttpResponse(s.json_res())

# pool -------------------------------------------------------------------------
@http_except_dec
def pool_list(request):
    p = pool.PoolListJ()
    return HttpResponse(p.json_res())

@http_except_dec
def pool_detail(request, poolid):
    p = pool.PoolDetailJ(int(poolid))
    return HttpResponse(p.json_res())

@http_except_dec
def pool_disk(requst, poolid):
    p = pool.PoolDiskJ(int(poolid))
    return HttpResponse(p.json_res())

# laucher ----------------------------------------------------------------------
@http_except_dec
def initiator_list(request):
    l = initiator.InitiatorListJ()
    return HttpResponse(l.json_res()) 

@http_except_dec
def initiator_detail(request, iid):
    l = initiator.InitiatorDetailJ(iid)
    return HttpResponse(l.json_res()) 

# vserver ----------------------------------------------------------------------
@http_except_dec
def vserver_list(request):
    v = vserver.VServerListJ()
    return HttpResponse(v.json_res()) 

@http_except_dec
def vserver_detail(request, vid):
    v = vserver.VServerDetailJ(vid)
    return HttpResponse(v.json_res()) 






