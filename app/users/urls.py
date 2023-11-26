""" URL patterns for the users app """

from django.urls import path, include
from . import views


app_name = 'users'
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('registration/', views.registration, name='registration'),
]