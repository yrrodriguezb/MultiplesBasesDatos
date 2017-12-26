# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.views.generic import FormView
from .models import BaseDatos
from .forms import BaseDatosForm


def index(request):
    return render(request, "index.html", {})


class BaseDatosListView(FormView):
    template_name = 'BaseDatos/BDListar.html'
    form_class = BaseDatosForm
    success_url = 'BaseDatos:basedatos-listar'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(BaseDatosListView, self).dispatch( *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            form = BaseDatosForm(request.POST)
            if form.is_valid():
                q = form.cleaned_data['BDNombre']
                return HttpResponseRedirect("/%s" % q)
        form = BaseDatosForm()
        return render(request, self.get_template_names(), { 'form': form })
