from django.contrib import admin
from .models import SozlukContent

# Register your models here.


class SozlukAdmin(admin.ModelAdmin):
    list_display = ['de','tr']
    list_display_links = ['de','tr']
    list_filter = ['de','tr']
    search_fields = ['de','tr']



admin.site.register(SozlukContent,SozlukAdmin)