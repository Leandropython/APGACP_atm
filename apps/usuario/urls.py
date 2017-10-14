from __future__ import absolute_import
from django.conf.urls import url

from apps.usuario.views import RegistroUsuario, ProfileList, ProfileCreate, ProfileUpdate, ProfileDelete, ProfileLists

urlpatterns = [
    url(r'^registrar', RegistroUsuario.as_view(), name = "registrar"),
    url(r'^profile/listar_profile$', ProfileList.as_view(), name = 'Profile_listar'),
    url(r'^profile/listar_profiles$', ProfileLists.as_view(), name = 'Profile_listar'),
    url(r'^profile/nueva_profile$', ProfileCreate.as_view(), name = 'Profile_nueva'),
    url(r'^profile/editar_profile/(?P<pk>\d+)$', ProfileUpdate.as_view(), name = 'Profile_editar'),
    url(r'^profile/eliminar_profile/(?P<pk>\d+)$', ProfileDelete.as_view(), name = 'Profile_eliminar'),

]
