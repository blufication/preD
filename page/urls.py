from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('/', views.home, name='home'),
    path('/valid', views.valid(), name='valid'),
    path('/Diag', views.Diag(), name='Diag'),
]