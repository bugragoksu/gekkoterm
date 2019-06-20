from django.contrib import admin
from .models import User

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ['username']
    list_display_links = ['username']
    list_filter = ['username','nameSurname']
    search_fields = ['username','nameSurname']



admin.site.register(User,UserAdmin)