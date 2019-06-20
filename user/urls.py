from django.urls import path,include
from .views import *
urlpatterns = [
    
    path('register',registerView),
    path('login',loginView),
    path('addWords',addWordsView),
    
]