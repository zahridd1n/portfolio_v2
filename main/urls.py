from django.urls import path
from . import views

urlpatterns = [
  path('home/', views.home_page),
  path('my_data/', views.my_data),
  path('portfolio/', views.portfolio_page),
  path('project/<int:project_id>/', views.project_page),
]