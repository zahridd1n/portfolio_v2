from django.urls import path
from . import views

urlpatterns = [
  path('home/', views.home_page),
  path('my_data/', views.my_data),
]