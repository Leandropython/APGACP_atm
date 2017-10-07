from __future__ import absolute_import
from django.conf.urls import url, include
from apps.Gestor.views import index_gestor, iniciativa_view, iniciativa_edit, iniciativa_list, iniciativalist, asignacion_view, asignacion_list, asignacion_edit, asignacion_delete, asignacionlist

urlpatterns = [
    url(r'^$', index_gestor, name ='index_gestor'),
    url(r'^nueva_iniciativa$', iniciativa_view, name = 'iniciativa_crear'),
    url(r'^listar_iniciativa', iniciativalist.as_view(), name = 'Iniciativa_listar'),
    url(r'^editar10/(?P<id_Iniciativa>\d+)/$', iniciativa_edit, name = 'Iniciativa_editar'),
    url(r'^nuevo_asignacion$', asignacion_view, name = 'Asignacion_crear'),
    url(r'^listar_asignacion', asignacionlist.as_view(), name = 'Asignacion_listar'),
    url(r'^editar15/(?P<id>\d+)/$', asignacion_edit, name = 'Asignacion_editar'),
    url(r'^eliminar15/(?P<id>\d+)/$', asignacion_delete, name = 'Asignacion_eliminar'),

]
