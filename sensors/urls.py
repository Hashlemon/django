from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="sensors-home"),
    path('about/', views.about, name="sensors-about"),
    path('detail/<int:sensor_id>/', views.detail, name='sensors-details'),
    path('detail/', views.detail_index, name='sensors-detail'),
    path('pinout/', views.pinout, name='sensors-pinout'),
    path('wiget/', views.wiget, name='sensors-wiget'),

]
