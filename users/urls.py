from django.contrib.auth.views import LoginView
from django.urls import path
from users.apps import UsersConfig
from users.views import RegisterView, ProfileView, logout_view

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
]