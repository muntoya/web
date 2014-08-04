# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from ui.home.models import warning, io, storage, overview
from ui.util.decorator import http_except_dec

# Create your views here.

@http_except_dec
def home_page(request):
    dict_res = storage.StorageInfoT().dict_res()
    dict_res.update(overview.SysInfoT().dict_res())
    dict_res.update(warning.WarningInfoT().dict_res())
    
    return render_to_response('home/home.html', dict_res)

@http_except_dec
def baseinfo_page(request):
    ss = overview.SysInfoT()
    return render_to_response('home/baseinfo.html', ss.dict_res())


@http_except_dec
def warning_page(request):
    wi = warning.WarningInfoT()
    return render_to_response('home/warning.html', wi.dict_res())


@http_except_dec
def io_info(request):
    ii = io.IOInfoJ()
    return HttpResponse(ii.json_res())


@http_except_dec
def storage_info(request):
    ss = storage.StorageUsageJ()
    return HttpResponse(ss.json_res())


