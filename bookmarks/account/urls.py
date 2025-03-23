from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    # old login path
    # path('login/', views.user_login, name='login'),

    # Login/Logout urls
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Dashboard
    path('', views.dashboard, name='dashboard'),
]