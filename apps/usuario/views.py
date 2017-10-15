from __future__ import unicode_literals
from __future__ import absolute_import

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from apps.usuario.forms import RegistroForm, ProfileForm, GestorForm, CertificadoresForm
from apps.usuario.models import Profile, Gestores, Certificadores

class RegistroUsuario(CreateView):
    model=  User
    template_name = "usuario/registrar.html"
    form_class = RegistroForm
    success_url =reverse_lazy('administrador:index_administrador')

class ProfileList(ListView):
    model = Profile
    template_name = 'usuario/profile_list.html'

class ProfileLists(ListView):
    model = Profile
    queryset = Profile.objects.filter(perfil="Certificador")
    template_name = 'gestion/asignacion_ingresar.html'

class ProfileCreate(CreateView):
    model=Profile
    template_name = 'usuario/profile_form.html'
    form_class = ProfileForm
    second_form_class = RegistroForm
    success_url = reverse_lazy('usuario:Profile_listar')

    def get_context_data(self, **kwargs):
        context = super(ProfileCreate, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)
        if form.is_valid() and form2.is_valid():
            profile = form.save(commit=False)
            profile.user = form2.save()
            profile.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form, form2=form2))

class ProfileUpdate(UpdateView):

        model = Profile
        second_model = User
        template_name = 'usuario/profile_form.html'
        form_class = ProfileForm
        second_form_class = RegistroForm
        success_url =reverse_lazy('usuario:Profile_listar')


	def get_context_data(self, **kwargs):
	    context = super(ProfileUpdate, self).get_context_data(**kwargs)
	    pk = self.kwargs.get('pk', 0)
	    profile = self.model.objects.get(id=pk)
	    user = self.second_model.objects.get(id=profile.user_id)
	    if 'form' not in context:
	    	context['form'] = self.form_class()
	    if 'form2' not in context:
	    	context['form2'] = self.second_form_class(instance=user)
	    context['id'] = pk
	    return context

	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		id_profile = kwargs['pk']
		profile = self.model.objects.get(id=id_profile)
		user = self.second_model.objects.get(id=profile.user_id)
		form = self.form_class(request.POST, instance=profile)
		form2 = self.second_form_class(request.POST, instance=user)
		if form.is_valid() and form2.is_valid():
			form.save()
			form2.save()
			return HttpResponseRedirect(self.get_success_url())
		else:
			return HttpResponseRedirect(self.get_success_url())



class ProfileDelete(DeleteView):
    model = User
    template_name = 'usuario/profile_delete.html'
    success_url = reverse_lazy('usuario:Profile_listar')


class GestorList(ListView):
    model = Gestores
    template_name = 'usuario/gestor_list.html'

class GestorCreate(CreateView):
    model= Gestores
    template_name = 'usuario/gestor_form.html'
    form_class = GestorForm
    second_form_class = RegistroForm
    success_url = reverse_lazy('usuario:Gestor_listar')

    def get_context_data(self, **kwargs):
        context = super(GestorCreate, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)
        if form.is_valid() and form2.is_valid():
            gestor = form.save(commit=False)
            gestor.user = form2.save()
            gestor.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form, form2=form2))

class GestorUpdate(UpdateView):

        model = Gestores
        second_model = User
        template_name = 'usuario/gestor_form.html'
        form_class = GestorForm
        second_form_class = RegistroForm
        success_url =reverse_lazy('usuario:Gestor_listar')


	def get_context_data(self, **kwargs):
	    context = super(GestorUpdate, self).get_context_data(**kwargs)
	    pk = self.kwargs.get('pk', 0)
	    gestor = self.model.objects.get(id=pk)
	    user = self.second_model.objects.get(id=gestor.user_id)
	    if 'form' not in context:
	    	context['form'] = self.form_class()
	    if 'form2' not in context:
	    	context['form2'] = self.second_form_class(instance=user)
	    context['id'] = pk
	    return context

	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		id_gestor = kwargs['pk']
		gestor = self.model.objects.get(id=id_gestor)
		user = self.second_model.objects.get(id=gestor.user_id)
		form = self.form_class(request.POST, instance=gestor)
		form2 = self.second_form_class(request.POST, instance=user)
		if form.is_valid() and form2.is_valid():
			form.save()
			form2.save()
			return HttpResponseRedirect(self.get_success_url())
		else:
			return HttpResponseRedirect(self.get_success_url())


class GestorDelete(DeleteView):
    model = User
    template_name = 'usuario/gestor_delete.html'
    success_url = reverse_lazy('usuario:Gestor_listar')

class CertificadoresList(ListView):
    model = Certificadores
    template_name = 'usuario/certificador_list.html'

class CertificadoresCreate(CreateView):
    model= Certificadores
    template_name = 'usuario/certificador_form.html'
    form_class = CertificadoresForm
    second_form_class = RegistroForm
    success_url = reverse_lazy('usuario:Certificador_listar')

    def get_context_data(self, **kwargs):
        context = super(CertificadoresCreate, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)
        if form.is_valid() and form2.is_valid():
            certificador = form.save(commit=False)
            certificador.user = form2.save()
            certificador.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form, form2=form2))

class CertificadoresUpdate(UpdateView):

        model = Certificadores
        second_model = User
        template_name = 'usuario/certifador_form.html'
        form_class = CertificadoresForm
        second_form_class = RegistroForm
        success_url =reverse_lazy('usuario:Certificador_listar')


	def get_context_data(self, **kwargs):
	    context = super(CertificadoresUpdate, self).get_context_data(**kwargs)
	    pk = self.kwargs.get('pk', 0)
	    certificador = self.model.objects.get(id=pk)
	    user = self.second_model.objects.get(id=certificador.user_id)
	    if 'form' not in context:
	    	context['form'] = self.form_class()
	    if 'form2' not in context:
	    	context['form2'] = self.second_form_class(instance=user)
	    context['id'] = pk
	    return context

	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		id_certificador = kwargs['pk']
		certificador = self.model.objects.get(id=id_certificador)
		user = self.second_model.objects.get(id=certificador.user_id)
		form = self.form_class(request.POST, instance=certificador)
		form2 = self.second_form_class(request.POST, instance=user)
		if form.is_valid() and form2.is_valid():
			form.save()
			form2.save()
			return HttpResponseRedirect(self.get_success_url())
		else:
			return HttpResponseRedirect(self.get_success_url())


class CertificadoresDelete(DeleteView):
    model = User
    template_name = 'usuario/certificador_delete.html'
    success_url = reverse_lazy('usuario:Certificador_listar')
