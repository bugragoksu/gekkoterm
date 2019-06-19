from django.contrib import admin
from django.urls import path, include
from home.views import *

urlpatterns = [
    path('about/', about),
    path('', index),
    path('contact/', contact),
]
