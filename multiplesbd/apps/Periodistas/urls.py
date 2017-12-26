from django.conf.urls import url

from .views import PeriodistasListView

app_name = 'Periodistas'

urlpatterns = [
    url(r'^$', PeriodistasListView.as_view(), name='periodistas-listar'),
]
