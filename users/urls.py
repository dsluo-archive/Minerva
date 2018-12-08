from django.urls import path

from .views import login, register

app_name = 'users'
urlpatterns = [
    path('login', login),
    path('register', register)
]
