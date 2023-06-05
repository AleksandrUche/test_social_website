from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    # path('login/', views.user_login, name='login'),
    # url-адрес входа
    path("login/", auth_views.LoginView.as_view(), name="login"),
    # url-адрес выхода
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    # url-адреса смены пароля
    path("password-change/", auth_views.PasswordChangeView.as_view(), name="password_change"),
    path("password-change/done/", auth_views.PasswordChangeDoneView.as_view(), name="password_change_done"),
    # Панель
    path("", views.dashboard, name="dashboard"),
]
