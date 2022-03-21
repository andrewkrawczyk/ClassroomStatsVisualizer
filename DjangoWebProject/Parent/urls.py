from datetime import datetime
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='parent-home'),
    path('contact/', views.contact, name='parent-contact'),
    path('about/', views.about, name='parent-about')
]