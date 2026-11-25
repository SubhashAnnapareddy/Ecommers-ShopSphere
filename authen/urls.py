from django.urls import path
from .views import *

urlpatterns = [
    path('',login_,name='login_'),
    path('register/',register,name='register'),
    path('logout_/',logout_,name='logout_'),
    path('profile/',profile,name='profile'),
    path('forget_pasw/',forget_pasw,name='forget_pasw'),
    path('updateprofile/',updateprofile,name='updateprofile'),
    path('reset_pasw/',reset_pasw,name='reset_pasw')
]
