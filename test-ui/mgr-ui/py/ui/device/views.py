from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from ui.util.decorator import http_except_dec
from ui.device.models import cluster
from ui.device.models import device
# Create your views here.

@http_except_dec
def device_page(request):
    #FIXME: temp
    c_res = cluster.DeviceListT().dict_res()
    return render_to_response('dev/dev.html', c_res)

@http_except_dec
def cluster_page(request):
    c_res = cluster.DeviceListT().dict_res()
    return render_to_response('dev/dev_cluster.html', c_res)

@http_except_dec
def manager_page(request):
    sl_res = device.DeviceListT().dict_res()
    s_res = device.DeviceDetailT(2).dict_res()

    res = {}
    res.update(sl_res)
    res.update(s_res)
    
    return render_to_response('dev/manager/deviceManager.html', res)

@http_except_dec
def devicelist_page(request):
    sl_res = device.DeviceListT().dict_res()
    return render_to_response('dev/manager/device_list.html', sl_res)

@http_except_dec
def devicedetail_page(request, did):
    s_res = device.DeviceDetailT(did).dict_res()
    return render_to_response('dev/manager/device_detail.html', s_res)
