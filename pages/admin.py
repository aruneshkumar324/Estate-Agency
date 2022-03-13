from django.contrib import admin
from .models import Agent
from django.utils.html import format_html


class AgentAdmin(admin.ModelAdmin):

    def thumbnail(self, object):
        return format_html("<img src='{}' style='width:50px;height:50px;border-radius:50px;' />".format(object.photo.url))
    
    thumbnail.short_description = 'photo'

    list_display = ('id', 'thumbnail', 'name', 'phone', 'email')
    list_display_links = ('id', 'thumbnail' ,'name')
    search_fields = ('id', 'name', 'phone', 'email')
    list_filter = ('name', 'email')


admin.site.register(Agent, AgentAdmin)