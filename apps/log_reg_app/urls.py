from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^about$', views.about),
    url(r'^registration$', views.registration),
    url(r'^register$', views.register),
    url(r'^registered$', views.registered),
    url(r'^login$', views.login),
    url(r'^success$', views.success),
    url(r'^logout$', views.logout),
]