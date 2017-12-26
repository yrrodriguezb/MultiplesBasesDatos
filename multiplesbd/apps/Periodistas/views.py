# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from .models import Periodista


class PeriodistasListView(ListView):
    model = Periodista
    template_name = 'Periodistas/PListar.html'
    context_object_name = "periodistas"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PeriodistasListView, self).dispatch( *args, **kwargs)
