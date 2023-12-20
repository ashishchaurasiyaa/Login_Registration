# user/urls.py
from django.urls import path
from .views import login, register, index, custom_logout

app_name = 'user'  # Set the app namespace

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('index/', index, name='index'),
    path('logout/', custom_logout, name='logout'),
]
