from django.urls import path
from . import views


urlpatterns = [
    path('', views.blogs, name='blog'),
    path('blog_details/<int:id>/', views.blog_details, name='blog_details')
]