from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('coin/', views.coin, name='coin'),
]
