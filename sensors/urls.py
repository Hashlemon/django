from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="sensors-home"),
    path('about/', views.about, name="sensors-about"),
    path('<int:sensor_id>/', views.detail, name='detail')
    ]
