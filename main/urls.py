from django.urls import path
from . import views

urlpatterns = [
  path('my_data/', views.my_data),

  path('home/<str:lang>/', views.home_page),
  path('home/', views.home_page),

  path('portfolio/<str:lang>/', views.portfolio_page),
  path('portfolio/', views.portfolio_page),

  path('project/<int:project_id>/<str:lang>/', views.project_page),
  path('project/<int:project_id>/', views.project_page),

  path('history/<str:lang>/', views.education_experience),
  path('history/', views.education_experience),
]