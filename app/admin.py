from django.contrib import admin
from .models import Site, User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['chat_id']
    fields = ('chat_id', 'is_admin')



@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    list_display = ['number', 'name']
    fields = ('number', 'logo_url', 'name', 'description', 'url')
