from django.urls import path
from .views import user_login, index
from django.contrib.auth.views import LogoutView, PasswordChangeView, PasswordChangeDoneView

urlpatterns = [
    path('', index, name='index'),
    path('login/', user_login, name='login'),
    path('logout/', LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('password-change/', PasswordChangeView.as_view(template_name='users/password_change_form.html'), name='password-change'),
    path('password-change/done/', PasswordChangeDoneView.as_view(template_name='users/password_change_done.html'), name='password_change_done'),
]