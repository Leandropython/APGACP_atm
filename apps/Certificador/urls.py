from __future__ import absolute_import
from django.conf.urls import url, include
from apps.Certificador.views import index_certificador

urlpatterns = [
    url(r'^$', index_certificador)
]
