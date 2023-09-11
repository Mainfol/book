from django.urls import path, include
from .views import *

urlpatterns = [
    path('register/', Register_page, name='register'),
    path('login/', Login_page, name='login')
]