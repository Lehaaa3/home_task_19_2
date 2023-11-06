from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import RegisterView, ProfilerView, activate, email_activated, restore_password

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfilerView.as_view(), name='profile'),
    path('activate/<str:uid>/', activate, name="activate"),
    path('email_activated', email_activated, name="email_activated"),
    path('restore_password', restore_password, name="restore_password"),
]