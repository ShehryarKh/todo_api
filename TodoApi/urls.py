from django.conf.urls import url
from django.contrib import admin
from .views import register
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    url(r'^register$', csrf_exempt(register), name='register' ),

]