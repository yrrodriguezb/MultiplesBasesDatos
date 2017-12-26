# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.contrib import admin
from .models import BaseDatos

class BaseDatosAdmin(admin.ModelAdmin):
    fields = ['BDNombre', 'BDDescripcion', ]
    list_display = ('id', 'BDNombre', 'BDDescripcion', )
    ordering = ('BDNombre',  )


admin.site.register(BaseDatos, BaseDatosAdmin)
