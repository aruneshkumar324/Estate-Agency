from django.contrib import admin
from .models import Inquiry


class InquiryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'user_id', 'car_id', 'car_title')

    list_display_links = ('id', 'name',)


admin.site.register(Inquiry, InquiryAdmin)