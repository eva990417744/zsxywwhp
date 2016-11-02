from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<id>\d+)/$', views.detailed, name='detailed'),
    url(r'^(?P<id>\d+)/(?P<flag>buff|debuff)/$', views.buffchange, name='buffchange'),
]
