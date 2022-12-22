from django.contrib import admin
from .models import *




class WomenAdmin(admin.ModelAdmin):
    list_display: str = ('id', 'title', 'time_create', 'photo', 'is_published')
    list_display_links: str = ('id', 'title')
    search_fields: str = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {'slug': ('title',)}


class CategoryAdmin(admin.ModelAdmin):
    list_display: str = ('id', 'name')
    list_display_links: str = ('id', 'name')
    search_fields: str = ('name', )
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Women, WomenAdmin)
admin.site.register(Category, CategoryAdmin)