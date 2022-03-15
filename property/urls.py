from django.urls import path
from . import views


urlpatterns = [
    path('', views.property, name='property'),
    path('property_details/<int:id>/', views.property_details, name='property_details'),
    path('search/', views.search, name='search')
]
