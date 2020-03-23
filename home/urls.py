from django.urls import path

from . import views

urlpatterns = [
    path('', views.AboutMe, name='AboutMe'),
]