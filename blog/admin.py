from django.contrib import admin
from .models import Blog


class BlogAdmin(admin.ModelAdmin):
    readonly_fields = ['created_date', 'updated_date',]

admin.site.register(Blog, BlogAdmin)