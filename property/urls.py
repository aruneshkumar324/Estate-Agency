from django.urls import path
from . import views


urlpatterns = [
    path('', views.property, name='property'),
    path('property_details/', views.property_details, name='property_details'),
]
