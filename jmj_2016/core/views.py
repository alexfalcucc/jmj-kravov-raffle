# coding: utf-8
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import

from django.views.generic import TemplateView

from django.shortcuts import render


class AboutContribView(TemplateView):
    template_name = 'about-contrib/raffles.html'


class AboutWydView(TemplateView):
    template_name = 'about-wyd/history.html'


def home(request):
    return render(request, 'home.html')
