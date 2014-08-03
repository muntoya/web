# -*- coding: utf-8 -*-
'''
Created on Jun 27, 2014

@author: yaoxing
'''

from django.template import TemplateDoesNotExist
from django.http import Http404, HttpResponse, HttpResponseBadRequest
from exception import CLIException

def http_except_dec(func):
    def wrap_func(request, *args, **kwargs):

        # 检查用户 -----------------------------------------------------------------
        if False:
            res = HttpResponse(status=401)
            return res
        
        try:
            res = func(request, *args, **kwargs)
            return res
        except TemplateDoesNotExist:
            raise Http404()
        except CLIException:
            res = HttpResponse()
            return HttpResponseBadRequest(res)
        
    return wrap_func