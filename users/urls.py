from django.urls import path
from .views import user_login
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', user_login, name='login'),
    path('logout/', LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]