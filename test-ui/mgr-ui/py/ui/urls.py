from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView
from django.core.urlresolvers import reverse

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

)

#===============================================================================
# home
#===============================================================================
urlpatterns += patterns('ui.home.views',
    url(r'^api/home/pages/$', 'home_page'),
    url(r'^api/home/pages/baseinfo/$', 'baseinfo_page'),
    url(r'^api/home/pages/warning/$', 'warning_page'),
        
    url(r'^api/home/io/$', 'io_info'),
    url(r'^api/home/storage/$', 'storage_info'),
)

#===============================================================================
# resource
#===============================================================================
urlpatterns += patterns('ui.resource.views',
    # pages --------------------------------------------------------------------
    url(r'^api/resource/pages/baseinfo/$', 'resource_page'),
    url(r'^api/resource/pages/lun/$', 'lun_page'),
    url(r'^api/resource/pages/lun/list/$', 'lunlist_page'),
    url(r'^api/resource/pages/lun/(?P<lunid>\d+)/detail/$', 'lundetail_page'),
    url(r'^api/resource/pages/lun/(?P<lunid>\d+)/snapshot/$', 'snapshot_page'),
    
    url(r'^api/resource/pages/pool/$', 'pool_page'),
    url(r'^api/resource/pages/pool/list/$', 'poollist_page'),
    url(r'^api/resource/pages/pool/(?P<poolid>\d+)/detail/$', 'pooldetail_page'),
    url(r'^api/resource/pages/pool/(?P<poolid>\d+)/lun/$', 'poollun_page'),
    url(r'^api/resource/pages/pool/(?P<poolid>\d+)/disk/$', 'pooldisk_page'),
    
    url(r'^api/resource/pages/initiator/$', 'initiator_page'),
    url(r'^api/resource/pages/initiator/list/$', 'initiatorlist_page'),
    url(r'^api/resource/pages/initiator/(?P<iid>\d+)/detail/$', 'initiatordetail_page'),
    
    url(r'^api/resource/pages/vserver/$', 'vserver_page'),
    url(r'^api/resource/pages/vserver/list/$', 'vserverlist_page'),
    url(r'^api/resource/pages/vserver/(?P<vid>\d+)/detail/$', 'vserverdetail_page'),
    
    # json ---------------------------------------------------------------------
    
    url(r'^api/resource/overview/$', 'resource_overview'),
    
    # lun ----------------------------------------------------------------------
    url(r'^api/resource/lun/$', 'lun_list'),
    url(r'^api/resource/lun/(?P<lunid>\d+)/detail/$', 'lun_detail'),
    url(r'^api/resource/lun/(?P<lunid>\d+)/snapshot/$', 'lun_snapshot'),
    
    # pool ---------------------------------------------------------------------
    url(r'^api/resource/pool/$', 'pool_list'),
    url(r'^api/resource/pool/(?P<poolid>\d+)/detail/$', 'pool_detail'),
    url(r'^api/resource/pool/(?P<poolid>\d+)/disk/$', 'pool_disk'),
    
    # launcher -----------------------------------------------------------------
    url(r'^api/resource/initiator/$', 'initiator_list'),
    url(r'^api/resource/initiator/(?P<iid>\d+)/detail/$', 'initiator_detail'),
    
    # vserver ------------------------------------------------------------------
    url(r'^api/resource/vserver/$', 'vserver_list'),
    url(r'^api/resource/vserver/(?P<vid>\d+)/detail/$', 'vserver_detail'),
)

#===============================================================================
# device
#===============================================================================
urlpatterns += patterns('ui.device.views',
    # pages --------------------------------------------------------------------
    url(r'^api/device/pages/baseinfo/$', 'device_page'),
    url(r'^api/device/pages/cluster/$', 'cluster_page'),
    url(r'^api/device/pages/manager/$', 'manager_page'),
    url(r'^api/device/pages/device/list/$', 'devicelist_page'),
    url(r'^api/device/pages/device/(?P<did>\d+)/detail/$', 'devicedetail_page')
    
)

urlpatterns += patterns('',
    url(r'^$', RedirectView.as_view(url=reverse('ui.home.views.home_page'))),
)

