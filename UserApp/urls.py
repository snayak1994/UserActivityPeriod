from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^getdata$', views.getUserData, name='getUserData'),
]
