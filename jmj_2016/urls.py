# coding: utf-8
from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'jmj_2016.core.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
)
