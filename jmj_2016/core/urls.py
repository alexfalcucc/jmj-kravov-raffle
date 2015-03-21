# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import

from django.conf.urls import patterns, url

from .views import AboutContribView


urlpatterns = patterns('',
                       url(r'^about-contribuitions/$',
                           AboutContribView.as_view(),
                           name='about-contribuitions'),
                       )
