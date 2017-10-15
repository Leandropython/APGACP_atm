from __future__ import absolute_import
from django.conf.urls import url

from apps.usuario.views import RegistroUsuario, ProfileList, ProfileCreate, ProfileUpdate, ProfileDelete, GestorList, GestorCreate, GestorUpdate, GestorDelete, CertificadoresList, CertificadoresCreate, CertificadoresUpdate, CertificadoresDelete


urlpatterns = [
    url(r'^registrar', RegistroUsuario.as_view(), name = "registrar"),
    url(r'^profile/listar_profile$', ProfileList.as_view(), name = 'Profile_listar'),
    url(r'^profile/nueva_profile$', ProfileCreate.as_view(), name = 'Profile_nueva'),
    url(r'^profile/editar_profile/(?P<pk>\d+)$', ProfileUpdate.as_view(), name = 'Profile_editar'),
    url(r'^profile/eliminar_profile/(?P<pk>\d+)$', ProfileDelete.as_view(), name = 'Profile_eliminar'),
    url(r'^gestor/listar_gestor$', GestorList.as_view(), name = 'Gestor_listar'),
    url(r'^gestor/nueva_gestor$', GestorCreate.as_view(), name = 'Gestor_nueva'),
    url(r'^gestor/editar_gestor/(?P<pk>\d+)$', GestorUpdate.as_view(), name = 'Gestor_editar'),
    url(r'^gestor/eliminar_gestor/(?P<pk>\d+)$', GestorDelete.as_view(), name = 'Gestor_eliminar'),
    url(r'^gestor/listar_certificador$', CertificadoresList.as_view(), name = 'Certificador_listar'),
    url(r'^gestor/nueva_certificador$', CertificadoresCreate.as_view(), name = 'Certificador_nueva'),
    url(r'^gestor/editar_certificador/(?P<pk>\d+)$', CertificadoresUpdate.as_view(), name = 'Certificador_editar'),
    url(r'^gestor/eliminar_certificador/(?P<pk>\d+)$', CertificadoresDelete.as_view(), name = 'Certificador_eliminar'),


]
