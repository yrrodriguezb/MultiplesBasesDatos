# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Periodista


class PeriodistaModelAdmin(admin.ModelAdmin):

    using = 'periodistas_db'
    model = Periodista
    list_display = ('id', 'PIdentificacion', 'PPrimerNombre', 'PPrimerApellido',)
    ordering = ('PIdentificacion',  )

    def save_model(self, request, obj, form, change):
        obj.save(using=self.using)

    def delete_model(self, request, obj):
        obj.delete(using=self.using)

    def get_queryset(self, request):
        return super(PeriodistaModelAdmin, self).get_queryset(request).using(self.using)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        return super(PeriodistaModelAdmin, self).formfield_for_foreignkey(db_field, request, using=self.using, **kwargs)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        return super(PeriodistaModelAdmin, self).formfield_for_manytomany(db_field, request, using=self.using, **kwargs)


admin.site.register(Periodista, PeriodistaModelAdmin)
