from django.urls import path
from . import views

urlpatterns = [
  path('home/<str:lang>/', views.home_page),
  path('home/', views.home_page),

  path('my_data/', views.my_data),
  path('portfolio/', views.portfolio_page),
  path('project/<int:project_id>/', views.project_page),
  path('education_page/', views.education_page),
  path('experience_page/', views.experience_page),
]