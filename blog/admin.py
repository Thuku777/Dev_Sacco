from django.contrib import admin
from .models import *
from django.contrib.auth import get_user_model

User = get_user_model()

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'status')
    list_filter = ('status', 'created', 'updated')
    search_fields = ('author__username', 'title')
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ('status',)
    date_hierarchy = ('created')


admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
