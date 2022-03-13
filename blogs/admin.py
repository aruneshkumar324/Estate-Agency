from django.contrib import admin
from django.utils.html import format_html
from .models import Blog


class BlogAdmin(admin.ModelAdmin):

    def thumbnail(self, object):
        return format_html("<img src='{}' style='width:50px;height:50px;border-radius:25px;' />".format(object.photo.url))
    
    thumbnail.short_description = 'photo'

    readonly_fields = ['created_date', 'updated_date',]

    list_display = ('id','thumbnail', 'title', 'category', 'created_date', 'updated_date')

    list_display_links = ('id', 'title', 'thumbnail')

    search_fields = ('id', 'title', 'category')

    list_filter = ('category',)

admin.site.register(Blog, BlogAdmin)