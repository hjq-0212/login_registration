

from django.urls import path
from . import views

urlpatterns = [
    path('index/',views.index,name='index'),
    path('register/',views.register,name='register'),
    path('password/',views.password,name='password'),
    path('change_password/',views.change_password,name='change_password'),
]
