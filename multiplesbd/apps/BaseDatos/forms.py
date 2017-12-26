# -*- coding: utf-8 -*-

from django import forms
from .models import BaseDatos

queryset = BaseDatos.objects.all()
CHOICES_BASEDATOS = [(q.BDNombre, q.BDNombre) for q in queryset]

class BaseDatosForm(forms.ModelForm):

    class Meta:
        model = BaseDatos

        fields = [
            'BDNombre',
            'BDDescripcion'
        ]

        labels = {
            'BDNombre': 'Seleccione la base de datos:',
            'BDDescripcion': 'Descripción'
        }

        help_texts = {
            'BDNombre': 'Nombre de la base de datos',
        }

        widgets = {
            'BDNombre': forms.Select(choices=CHOICES_BASEDATOS),
            'BDDescripcion': forms.TextInput()
        }
