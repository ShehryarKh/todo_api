from django.conf.urls import url
from django.contrib import admin
from .views import register,login, create
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    url(r'^register$', csrf_exempt(register), name='register' ),
    url(r'^login$', csrf_exempt(login), name='login' ),
    url(r'^create$', csrf_exempt(create), name='create')

]