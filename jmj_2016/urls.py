# coding: utf-8
from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^$', 'jmj_2016.core.views.home', name='home'),
                       url(r'', include(
                           'jmj_2016.core.urls', namespace='core')),
                       )
