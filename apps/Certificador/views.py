# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import

from django.shortcuts import render
from django.http import HttpResponse

def index_certificador(request):
    return render(request, 'certificacion/index.html')

# Create your views here.
