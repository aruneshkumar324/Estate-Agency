from django.contrib import admin
from .models import Property
from django.utils.html import format_html


class PropertyAdmin(admin.ModelAdmin):

    def thumbnail(self, object):
        return format_html("<img src='{}' style='width:50px;height:50px;border-radius:50px;' />".format(object.photo.url))
    
    thumbnail.short_description = 'photo'

    readonly_fields = ('created_date', 'updated_date')
    list_display = ('id', 'thumbnail', 'title', 'price', 'status', 'property_type')

    list_display_links = ('id', 'thumbnail', 'title')

    search_fields = ('id', 'title', 'price', 'status', 'state', 'city', 'property_type')

    list_filter = ('status', 'property_type')


admin.site.register(Property, PropertyAdmin)

