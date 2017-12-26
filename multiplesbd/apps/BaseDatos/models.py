# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class BaseDatos(models.Model):
    BDNombre = models.CharField(max_length=255, verbose_name="Nombre")
    BDDescripcion = models.CharField(max_length=100, null=True, blank=True, verbose_name="Descripción")

    def __str__(self):
        return self.BDNombre
