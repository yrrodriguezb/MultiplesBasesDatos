from django.conf.urls import url

from .views import BaseDatosListView


app_name = 'Bases de Datos'

urlpatterns = [
    url(r'^$', BaseDatosListView.as_view(), name='basedatos-listar'),
]
