from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('agents/', views.agents, name='agents'),
    path('agent_profile/<int:id>/', views.agent_profile, name='agent_profile')
]
