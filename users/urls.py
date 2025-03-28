from django.urls import path
from . import views

urlpatterns = [
    # User create
    path('register/',views.register, name='register'),
]