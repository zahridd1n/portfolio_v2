from django.urls import path
from . import views
urlpatterns = [
    path('price/', views.PriceList.as_view()),
    path("generate-video/", views.GenerateFromFileView.as_view(), name="generate-from-file"),
    # path('check-status/<int:video_id>/', views.VideoStatusView.as_view(), name='check-status'),
    path('register/', views.register),
    path('logi_in/', views.log_in),
    path('log_out/', views.log_out),
    path('profile/', views.user_profile, name='user_profile'),
    path('buy_price/<int:price_id>/', views.buy_price, name='buy_price'),
    path('my_purchases/', views.MyPurchasesView.as_view(), name='my_purchases'),
]
