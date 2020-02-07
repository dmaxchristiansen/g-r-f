from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^profile/(?P<number>\d+)$', views.profile),
    url(r'^update_prof_pic$', views.updateProfPic),
    url(r'^profile/(?P<number>\d+)$', views.profile),
    url(r'^new_project$', views.newProject),
    url(r'^create_new_project$', views.createNewProject),
    url(r'^projects$', views.projects),
    url(r'^project/(?P<number>\d+)$', views.project),
    url(r'^post_message/(?P<number>\d+)$', views.postMessage),
    url(r'^donate/(?P<number>\d+)$', views.donate),

]