# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Periodista(models.Model):
    PIdentificacion = models.CharField(max_length=20, verbose_name="No. de Identificación")
    PPrimerNombre = models.CharField(max_length=50, verbose_name="Primer Nombre")
    PSegundoNombre = models.CharField(max_length=50, null=True, blank=True, verbose_name="Segundo Nombre")
    PPrimerApellido = models.CharField(max_length=50, verbose_name="Primer Apellido")
    PSegundoApellido = models.CharField(max_length=50, null=True, blank=True, verbose_name="Segundo Apellido")
    PEmail = models.EmailField(verbose_name="Correo Electronico")
    PTelefono = models.CharField(max_length=255, null=True, blank=True, verbose_name="Telefono")
    PCelular = models.CharField(max_length=20, null=True, blank=True, verbose_name="Celular")
    PEmpresa = models.CharField(max_length=255, null=True, blank=True, verbose_name="Empresa")
    PFacebook = models.URLField(null=True, blank=True, verbose_name="Facebook")
    PTwitter = models.URLField(null=True, blank=True, verbose_name="Twitter")
    PCargo = models.CharField(max_length=150, null=True, blank=True, verbose_name="Cargo")
    POrganizacion = models.CharField(max_length=255, null=True, blank=True, verbose_name="Organización")

    class Meta:
        app_label = 'Periodistas'

    def __str__(self):
        return self.PPrimerNombre
