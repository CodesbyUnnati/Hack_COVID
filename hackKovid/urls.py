from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('store/', views.store, name='store'),
    path('guidelines/', views.guide, name='guide'),
]
