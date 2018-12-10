from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView, \
    PasswordResetCompleteView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView
from django.urls import path, reverse_lazy

from .views import register

app_name = 'users'
urlpatterns = [
    path('register',
         register,
         name='register'),

    path('login',
         LoginView.as_view(template_name='users/login.html'),
         name='login'),
    path('logout',
         LogoutView.as_view(template_name='users/logout.html'),
         name='logout'),

    path('change-password',
         PasswordChangeView.as_view(template_name='users/password_change.html'),
         name='password_change'),
    path('change-password/done/',
         PasswordChangeDoneView.as_view(template_name='users/password_change_done.html'),
         name='password_change_done'),

    path('reset-password/',
         PasswordResetView.as_view(
             template_name='users/request_reset.html',
             email_template_name='users/password_reset_email.html',
             success_url=reverse_lazy('users:password_reset_done')
         ),
         name='password_reset'),
    path('reset-password/done/',
         PasswordResetDoneView.as_view(template_name='users/request_reset_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(
             template_name='users/reset_confirm.html',
             success_url=reverse_lazy('users:password_reset_complete')
         ),
         name='password_reset_confirm'),
    path('reset/done/',
         PasswordResetCompleteView.as_view(template_name='users/reset_done.html'),
         name='password_reset_complete'),
]
