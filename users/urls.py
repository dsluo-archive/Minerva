from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView, \
    PasswordResetCompleteView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView
from django.urls import path

from .views import register

app_name = 'users'
urlpatterns = [
    path('register', register, name='register'),

    path('login', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout', LogoutView.as_view(template_name='users/logout.html'), name='logout'),

    path('change-password', PasswordChangeView.as_view(), name='password_change'),
    path('change-password/done/', PasswordChangeDoneView.as_view(), name='password_change_done'),

    path('reset-password/', PasswordResetView.as_view(), name='password_reset'),
    path('reset-password/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
