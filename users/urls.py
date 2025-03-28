from django.urls import path
from . import views
from django.contrib.auth import views as authentication_views

app_name = 'users'

urlpatterns = [
    # User create
    path('register/',views.register, name='register'),
    path('login/',authentication_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/',views.LogoutView, name='logout'),
    path('profile/',views.profile_page, name='profile'),
]