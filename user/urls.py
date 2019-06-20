from django.urls import path,include
from .views import *
urlpatterns = [
    
    path('register',registerView),
    path('login',loginView),
    path('addWord',wordCreate),
    path('getWord',getWordsView),
    path('updateWord/<int:id>',wordUpdate),
    path('deleteWord/<int:id>',wordDelete),
    
]