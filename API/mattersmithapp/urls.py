
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import url, include
from .views import *
urlpatterns = [
    url(r'^users/', Users.as_view(), name='registerUser'),
    url(r'^login/', login.as_view(), name='loginUser'),
    url(r'^search/', Search.as_view(), name='Search')
]
