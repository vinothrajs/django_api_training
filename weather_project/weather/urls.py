from django.urls import path
from .views import create_weather, search_weather,view_all_weather

urlpatterns = [
    path('create/', create_weather, name='create_weather'),
    path('view_all/', view_all_weather, name='view_all_weather'),
    path('search/', search_weather, name='search_weather'),
]