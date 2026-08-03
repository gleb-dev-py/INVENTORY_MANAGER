from . import views
from django.urls import path

urlpatterns = [
    path('', views.base_version, name='base'),
    path('test', views.dark_version, name='dark')
]
